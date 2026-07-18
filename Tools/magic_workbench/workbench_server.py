"""
Magic Workbench — Server
========================
A local Flask server providing an authoring suite for Ironthorn's
magic system. Several tools share the vault as their canonical data
store; SQLite is used only as an in-memory query cache rebuilt on
startup and on vault file changes.

Tools served (v1):
  /              — Workbench home / nav
  /practitioner  — Practitioner NPC Builder (read-write)
  /explorer      — Magic system reference (read-only; skeleton in v1)
  /aesthetics    — Tradition style guide (read-only; skeleton in v1)

Architecture:
  - Vault is canonical; SQLite is a cache.
  - All writes go to NPCs/_Pending/<slug>/ in the same shape the
    existing intake watcher expects.
  - Watchdog (when installed) rebuilds the cache on vault changes.
    If watchdog is not installed, a 60-second poll fallback runs.
  - Templates and static files live alongside this script.

Port: 7844 (Manager Board is 7843; Writer Board is 7842)
"""

import json
import os
import re
import sqlite3
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, redirect, render_template, request, url_for

# ─── PATHS ────────────────────────────────────────────────────────────────────

SCRIPT_DIR    = Path(__file__).resolve().parent
VAULT_ROOT    = Path(r"C:\Users\steph\Desktop\Game\GameVault")
NPCS_DIR      = VAULT_ROOT / "NPCs"
PENDING_DIR   = NPCS_DIR / "_Pending"
TEMPLATES_DIR = VAULT_ROOT / "_Templates"
SYSTEM_DIR    = VAULT_ROOT / "_System"
FACTIONS_DIR  = VAULT_ROOT / "Factions"
WORLD_DIR     = VAULT_ROOT / "World"

CACHE_DB      = SCRIPT_DIR / "workbench_cache.sqlite"

# ─── FLASK APP ────────────────────────────────────────────────────────────────

app = Flask(
    __name__,
    template_folder=str(SCRIPT_DIR / "templates"),
    static_folder=str(SCRIPT_DIR / "static"),
)
app.config["JSON_SORT_KEYS"] = False

# ─── MAGIC SYSTEM CONSTANTS ───────────────────────────────────────────────────
# These mirror what's locked in _System/Magic.md. If the doc changes,
# update these AND the doc together — they are the canonical enum source
# the validator uses.

TRADITIONS = [
    "Holy",
    "Unholy",
    "Nature-Plant",
    "Nature-Animal",
    "Elemental-Fire",
    "Elemental-Water",
    "Elemental-Air",
    "Elemental-Ice",
    "Mental",
    "Time",
]

FACTION_CREDENTIALS = [
    "Aureate Covenant",
    "Verdant Circle",
    "Crimson Throne",
    "Ashen Veil",
    "Gray Compact",
    "Iron Dominion",
    "Heretic-class",
    "Hedge / uncredentialled",
]

COST_CHANNELS = ["Physical", "Mental", "Faith"]

CORRUPTION_SURFACES = [
    "Physical",
    "Mental",
    "Moral",
    "Physical + Mental",
    "Physical + Moral",
    "Mental + Moral",
    "Physical + Mental + Moral",
]

VALID_TRADITION_CREDENTIAL = {
    "Holy": ["Aureate Covenant", "Heretic-class"],
    "Unholy": ["Crimson Throne", "Ashen Veil", "Hedge / uncredentialled"],
    "Nature-Plant": ["Verdant Circle", "Hedge / uncredentialled"],
    "Nature-Animal": ["Verdant Circle", "Hedge / uncredentialled"],
    "Elemental-Fire": ["Iron Dominion", "Gray Compact", "Hedge / uncredentialled"],
    "Elemental-Water": ["Iron Dominion", "Gray Compact", "Hedge / uncredentialled"],
    "Elemental-Air": ["Iron Dominion", "Gray Compact", "Hedge / uncredentialled"],
    "Elemental-Ice": ["Iron Dominion", "Gray Compact", "Hedge / uncredentialled"],
    "Mental": ["Gray Compact", "Hedge / uncredentialled"],
    "Time": ["Gray Compact"],
}

PREFERRED_CHANNEL = {
    "Holy": "Faith",
    "Unholy": "Faith",
    "Nature-Plant": "Physical",
    "Nature-Animal": "Physical",
    "Elemental-Fire": "Physical",
    "Elemental-Water": "Physical",
    "Elemental-Air": "Physical",
    "Elemental-Ice": "Physical",
    "Mental": "Mental",
    "Time": "Mental",
}

# Canonical faction names for the `faction:` field — separate from credentials
# because an NPC may have credential A but currently work for faction B.
FACTIONS = [
    "Aureate Covenant",
    "Verdant Circle",
    "Crimson Throne",
    "Ashen Veil",
    "Gray Compact",
    "Iron Dominion",
    "Void Eternum",
    "Unaffiliated",
]

ALIGNMENT_TIERS = {
    1: ("Light-V", "The Radiant"),
    2: ("Light-III", "The Steadfast"),
    3: ("Light-I", "The Watchful"),
    4: ("Gray", "The Unbound"),
    5: ("Dark-I", "The Shadowed"),
    6: ("Dark-III", "The Corrupted"),
    7: ("Dark-V", "The Void-Touched"),
}

# ─── VAULT READER ─────────────────────────────────────────────────────────────

YAML_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser. Handles flat key:value structures only."""
    m = YAML_FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        if val == "true":
            val = True
        elif val == "false":
            val = False
        elif val == "":
            val = ""
        elif val == "[]":
            val = []
        else:
            try:
                if "." in val:
                    val = float(val)
                else:
                    val = int(val)
            except ValueError:
                pass
        fm[key] = val
    return fm


def read_vault_npcs():
    """Walk NPCs/ (excluding _Pending and _Characters) and return list of frontmatter dicts."""
    npcs = []
    if not NPCS_DIR.exists():
        return npcs
    for path in NPCS_DIR.rglob("*.md"):
        parts = path.parts
        if "_Pending" in parts or "_Characters" in parts or "Versions" in parts or "_Legacy" in parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if "npc_name" in fm:
                fm["__path"] = str(path)
                fm["__slug"] = path.stem.lower()
                npcs.append(fm)
        except Exception as e:
            print(f"[vault] failed to read {path}: {e}")
    return npcs


def read_vault_factions():
    """Walk Factions/ and return list of frontmatter dicts."""
    factions = []
    if not FACTIONS_DIR.exists():
        return factions
    for path in FACTIONS_DIR.rglob("*.md"):
        if "Versions" in path.parts or path.name.startswith("_"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if "faction_name" in fm:
                fm["__path"] = str(path)
                factions.append(fm)
        except Exception as e:
            print(f"[vault] failed to read faction {path}: {e}")
    return factions


# ─── SQLITE CACHE ─────────────────────────────────────────────────────────────


def init_cache():
    """Drop and rebuild the SQLite cache from vault content."""
    if CACHE_DB.exists():
        CACHE_DB.unlink()
    conn = sqlite3.connect(str(CACHE_DB))
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE npcs (
            slug TEXT PRIMARY KEY,
            npc_name TEXT,
            npc_tier INTEGER,
            faction TEXT,
            location TEXT,
            alignment_public TEXT,
            alignment_true TEXT,
            magical_practice INTEGER,
            tradition TEXT,
            faction_credential TEXT,
            cost_channel TEXT,
            corruption_level INTEGER,
            embraced INTEGER,
            path TEXT,
            raw_json TEXT
        )
        """
    )
    c.execute(
        """
        CREATE TABLE factions (
            faction_name TEXT PRIMARY KEY,
            alignment_bias TEXT,
            faction_tier INTEGER,
            path TEXT,
            raw_json TEXT
        )
        """
    )

    for npc in read_vault_npcs():
        c.execute(
            """
            INSERT OR REPLACE INTO npcs
            (slug, npc_name, npc_tier, faction, location, alignment_public,
             alignment_true, magical_practice, tradition, faction_credential,
             cost_channel, corruption_level, embraced, path, raw_json)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                npc.get("__slug", ""),
                npc.get("npc_name", ""),
                npc.get("npc_tier", 1) if isinstance(npc.get("npc_tier"), int) else 1,
                npc.get("faction", ""),
                npc.get("location", ""),
                npc.get("alignment_public", ""),
                npc.get("alignment_true", ""),
                1 if npc.get("magical_practice") else 0,
                npc.get("tradition", "") or "",
                npc.get("faction_credential", "") or "",
                npc.get("cost_channel", "") or "",
                npc.get("corruption_level", 0) if isinstance(npc.get("corruption_level"), int) else 0,
                1 if npc.get("embraced") else 0,
                npc.get("__path", ""),
                json.dumps({k: v for k, v in npc.items() if not k.startswith("__")}, default=str),
            ),
        )

    for fac in read_vault_factions():
        c.execute(
            """
            INSERT OR REPLACE INTO factions
            (faction_name, alignment_bias, faction_tier, path, raw_json)
            VALUES (?,?,?,?,?)
            """,
            (
                fac.get("faction_name", ""),
                fac.get("alignment_bias", "") or "",
                fac.get("faction_tier", 0) if isinstance(fac.get("faction_tier"), int) else 0,
                fac.get("__path", ""),
                json.dumps({k: v for k, v in fac.items() if not k.startswith("__")}, default=str),
            ),
        )

    conn.commit()
    conn.close()


def query_cache(sql, params=()):
    conn = sqlite3.connect(str(CACHE_DB))
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    rows = c.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ─── SLUG / FILENAME HELPERS ─────────────────────────────────────────────────


def slugify(name):
    """Convert 'Brother Aldric' → 'Brother-Aldric'. Matches the vault convention."""
    s = name.strip()
    s = re.sub(r"[^\w\s-]", "", s)        # drop punctuation
    s = re.sub(r"\s+", "-", s)            # spaces to hyphens
    s = re.sub(r"-+", "-", s)             # collapse runs
    return s.strip("-")


def existing_slugs():
    """Returns the set of slugs already present in the vault (live + pending),
    used to detect collisions before writing."""
    slugs = set()
    for path in NPCS_DIR.rglob("*.md"):
        if "Versions" in path.parts or "_Characters" in path.parts:
            continue
        slugs.add(path.stem)
    return slugs


# ─── VALIDATION ───────────────────────────────────────────────────────────────


def validate_submission(payload):
    """
    Walk the payload from the form and return (ok, errors, warnings).
    Errors block submission. Warnings allow submission but display to the writer.

    Mixed validation strategy:
      - Required fields missing → ERROR
      - Invalid (tradition, credential) combo → ERROR
      - Numeric out-of-range → ERROR
      - Slug collision with existing NPC → ERROR
      - Embraced flag set → WARNING (designer review required)
      - Non-preferred channel for tradition → WARNING
      - Embrace depth > 0 in PoC → WARNING
    """
    errors = []
    warnings = []

    # Required: npc_name, npc_role, faction
    if not payload.get("npc_name", "").strip():
        errors.append("NPC name is required.")
    if not payload.get("npc_role", "").strip():
        errors.append("NPC role is required.")
    if not payload.get("faction", "").strip():
        errors.append("Faction is required.")

    # Slug check
    if payload.get("npc_name", "").strip():
        slug = slugify(payload["npc_name"])
        if not slug:
            errors.append("NPC name does not produce a valid filename slug.")
        elif slug in existing_slugs():
            errors.append(f"An NPC with slug '{slug}' already exists. Choose a different name or rename the existing one first.")

    # Magic block — only required if magical_practice is true
    is_practitioner = payload.get("magical_practice") in (True, "true", "True", "on", 1, "1")
    if is_practitioner:
        tradition = payload.get("tradition", "").strip()
        credential = payload.get("faction_credential", "").strip()
        channel = payload.get("cost_channel", "").strip()

        if not tradition:
            errors.append("Practitioner requires a tradition.")
        elif tradition not in TRADITIONS:
            errors.append(f"Unknown tradition: {tradition}")

        if not credential:
            errors.append("Practitioner requires a faction credential.")
        elif credential not in FACTION_CREDENTIALS:
            errors.append(f"Unknown faction credential: {credential}")

        if not channel:
            errors.append("Practitioner requires a cost channel.")
        elif channel not in COST_CHANNELS:
            errors.append(f"Unknown cost channel: {channel}")

        # Combination validation
        if tradition in VALID_TRADITION_CREDENTIAL and credential:
            if credential not in VALID_TRADITION_CREDENTIAL[tradition]:
                errors.append(
                    f"Invalid combination: {tradition} cannot be credentialled through {credential}. "
                    f"Valid credentials for {tradition}: {', '.join(VALID_TRADITION_CREDENTIAL[tradition])}"
                )

        # Preferred channel warning
        if tradition in PREFERRED_CHANNEL and channel:
            preferred = PREFERRED_CHANNEL[tradition]
            if channel != preferred:
                warnings.append(
                    f"Non-preferred channel: {tradition} normally channels through {preferred}. "
                    f"You chose {channel}. This is allowed but corrupts faster. Justify in writer's notes."
                )

        # Corruption level bounds
        try:
            cl = int(payload.get("corruption_level", 0))
            if cl < 0 or cl > 10:
                errors.append("Corruption level must be between 0 and 10.")
        except (ValueError, TypeError):
            errors.append("Corruption level must be an integer.")

        # Embraced flag → designer review warning
        if payload.get("embraced") in (True, "true", "True", "on", 1, "1"):
            warnings.append(
                "Embraced NPCs require designer review at submission. Flag this in writer's notes "
                "and ensure the embrace ritual / private-act has been authored."
            )
            try:
                ed = int(payload.get("embrace_depth", 0))
                if ed < 1:
                    errors.append("Embraced NPCs must have embrace_depth >= 1.")
                if ed > 3:
                    warnings.append("Embrace depth above 3 is reserved for designer-authored NPCs in PoC.")
            except (ValueError, TypeError):
                errors.append("Embrace depth must be an integer.")

    # Drive bounds (1-10) — the five Drives plus perception threshold
    for attr in ["cunning", "loyalty", "fear", "greed", "idealism", "perception_threshold"]:
        try:
            v = int(payload.get(attr, 5))
            if v < 1 or v > 10:
                errors.append(f"{attr} must be between 1 and 10.")
        except (ValueError, TypeError):
            errors.append(f"{attr} must be an integer.")

    # Tier bounds (1-5)
    try:
        tier = int(payload.get("npc_tier", 2))
        if tier < 1 or tier > 5:
            errors.append("NPC tier must be between 1 and 5.")
    except (ValueError, TypeError):
        errors.append("NPC tier must be an integer.")

    return (len(errors) == 0, errors, warnings)


# ─── NPC FILE BUILDER ─────────────────────────────────────────────────────────


def build_npc_markdown(p):
    """
    Build the NPC Markdown file content from a validated payload dict.
    Matches v3.1 template shape. Quoted strings, blank lines between
    Drive groups, comments preserved where useful.

    Note: the five-stat behavioral system (Cunning/Loyalty/Fear/Greed/
    Idealism) is the Drives system per _System/Drives.md. Field names
    remain flat (cunning, loyalty, etc.) for backwards compatibility
    with existing Dataview queries and NPC files.
    """

    def s(key, default=""):
        """String getter — strips and returns empty string if missing."""
        v = p.get(key, default)
        return (str(v).strip() if v is not None else "")

    def i(key, default=5):
        """Int getter — coerces or returns default."""
        try:
            return int(p.get(key, default))
        except (ValueError, TypeError):
            return default

    def b(key):
        """Bool getter — handles form's string booleans."""
        v = p.get(key, False)
        return v in (True, "true", "True", "on", 1, "1")

    name = s("npc_name")
    slug = slugify(name)
    tier = i("npc_tier", 2)
    is_practitioner = b("magical_practice")

    # ─ Frontmatter ────────────────────────────────────────────────────
    lines = []
    lines.append("---")
    lines.append(f'npc_name: "{name}"')
    lines.append(f"npc_tier: {tier}")
    lines.append(f'npc_role: "{s("npc_role")}"')
    lines.append(f'faction: "{s("faction")}"')
    lines.append(f'location: "{s("location")}"')
    lines.append("")
    lines.append(f'alignment_public: "{s("alignment_public", "Gray")}"')
    lines.append(f'alignment_true: "{s("alignment_true", "Gray")}"')
    lines.append(f"alignment_tier: {i('alignment_tier', 4)}")
    lines.append("")
    lines.append(f"cunning: {i('cunning')}")
    lines.append(f"loyalty: {i('loyalty')}")
    lines.append(f"fear: {i('fear')}")
    lines.append(f"greed: {i('greed')}")
    lines.append(f"idealism: {i('idealism')}")
    lines.append("")
    lines.append(f"cunning_ambition: {i('cunning_ambition')}")
    lines.append(f"cunning_patience: {i('cunning_patience')}")
    lines.append(f"cunning_paranoia: {i('cunning_paranoia')}")
    lines.append("")
    lines.append(f"loyalty_devotion: {i('loyalty_devotion')}")
    lines.append(f"loyalty_resentment: {i('loyalty_resentment')}")
    lines.append("")
    lines.append(f"fear_desperation: {i('fear_desperation')}")
    lines.append(f"fear_suppression: {i('fear_suppression')}")
    lines.append("")
    lines.append(f"greed_appetite: {i('greed_appetite')}")
    lines.append(f"greed_restraint: {i('greed_restraint')}")
    lines.append(f"greed_envy: {i('greed_envy')}")
    lines.append("")
    lines.append(f"idealism_conviction: {i('idealism_conviction')}")
    lines.append(f"idealism_disillusionment: {i('idealism_disillusionment')}")
    lines.append("")
    lines.append(f"perception_threshold: {i('perception_threshold')}")
    lines.append("deception_immune: false")
    lines.append("")
    # Magic fields
    lines.append(f"magical_practice: {str(is_practitioner).lower()}")
    if is_practitioner:
        lines.append(f'tradition: "{s("tradition")}"')
        lines.append(f'faction_credential: "{s("faction_credential")}"')
        lines.append(f'cost_channel: "{s("cost_channel")}"')
        lines.append(f"corruption_level: {i('corruption_level', 0)}")
        surface = s("corruption_surface")
        if surface:
            lines.append(f'corruption_surface: "{surface}"')
        else:
            lines.append('corruption_surface: ""')
        lines.append(f"embraced: {str(b('embraced')).lower()}")
        lines.append(f"embrace_depth: {i('embrace_depth', 0)}")
    else:
        lines.append('tradition: ""')
        lines.append('faction_credential: ""')
        lines.append('cost_channel: ""')
        lines.append("corruption_level: 0")
        lines.append('corruption_surface: ""')
        lines.append("embraced: false")
        lines.append("embrace_depth: 0")
    lines.append("cosmology_reserved: false")
    lines.append("")
    lines.append('goal_primary_tag: ""')
    lines.append('goal_secondary_tag: ""')
    lines.append('goal_hidden_tag: ""')
    lines.append("")
    lines.append("liar_mark_active: false")
    lines.append("debt_flag_active: false")
    lines.append("trust_score: 5")
    lines.append("leverage_held: false")
    lines.append("secrets_known: []")
    lines.append("faction_alert_sent: false")
    lines.append("")
    lines.append("dual_identity: false")
    lines.append('true_faction: ""')
    lines.append("world_secret: false")
    lines.append("")
    lines.append('template_version: "3.1"')
    lines.append(f'submitted_by: "Magic Workbench"')
    lines.append(f'submitted_at: "{datetime.utcnow().isoformat()}Z"')
    lines.append('status: "Pending Review"')
    lines.append("---")
    lines.append("")

    # ─ Body ───────────────────────────────────────────────────────────
    lines.append(f"# {name}")
    lines.append("")
    lines.append("> [!info] Identity at a glance")
    lines.append(f"> **Tier:** {tier} · **Role:** {s('npc_role')} · **Faction:** {s('faction')}")
    lines.append(f"> **Location:** {s('location')}")
    lines.append(f"> **Alignment — public / true:** {s('alignment_public')} / {s('alignment_true')}")
    lines.append(f"> **Status:** Pending Review")
    lines.append("")
    lines.append("---")
    lines.append("")

    # T1 Quick Profile
    lines.append("## `[T1]` Quick Profile")
    lines.append("")
    lines.append(f"**Function in the world:** {s('function_in_world')}")
    lines.append("")
    lines.append(f"**First impression:** {s('first_impression')}")
    lines.append("")
    lines.append("**Signature line:**")
    sig = s("signature_line")
    if sig:
        lines.append(f"> *{sig}*")
    else:
        lines.append("> *To be authored.*")
    lines.append("")
    lines.append(f"**Basic lie response:** {s('basic_lie_response')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # T2 Layer 1 — Identity
    lines.append("## `[T2]` Layer 1 — Identity")
    lines.append("")
    lines.append("### Public persona")
    lines.append(s("public_persona") or "_To be authored._")
    lines.append("")
    lines.append("### Background")
    lines.append(s("background") or "_To be authored._")
    lines.append("")
    lines.append("### Voice & mannerisms")
    lines.append(s("voice_mannerisms") or "_To be authored._")
    lines.append("")
    lines.append("---")
    lines.append("")

    # T2 Layer 2 — Main Drives (full per-Drive interpretation pending review)
    lines.append("## `[T2]` Layer 2 — Main Drives")
    lines.append("")
    lines.append("> Scores filled in frontmatter. Per-Drive writer interpretation pending review.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # T2 Layer 2b — Magic (only if practitioner)
    if is_practitioner:
        lines.append("## `[T2]` Layer 2b — Magic")
        lines.append("")
        lines.append(f"**Practitioner:** true")
        lines.append(f"**Tradition:** {s('tradition')}")
        lines.append(f"**Faction credential:** {s('faction_credential')}")
        lines.append(f"**Cost channel:** {s('cost_channel')}")
        lines.append(f"**Corruption level:** {i('corruption_level', 0)} / 10")
        lines.append(f"**Corruption surface:** {s('corruption_surface') or '_(not yet surfaced)_'}")
        lines.append(f"**Embraced:** {b('embraced')}")
        if b("embraced"):
            lines.append(f"**Embrace depth:** {i('embrace_depth', 0)} / 10")
        lines.append("")
        lines.append("### Practice description")
        lines.append(s("practice_description") or "_To be authored._")
        lines.append("")
        lines.append("### Channelling style")
        lines.append(s("channelling_style") or "_To be authored._")
        lines.append("")
        lines.append("### Cost as it surfaces in this NPC")
        lines.append(s("cost_surfacing") or "_To be authored._")
        lines.append("")
        lines.append("### Corruption arc")
        lines.append(s("corruption_arc") or "_To be authored._")
        lines.append("")
        if b("embraced"):
            lines.append("> [!warning] Designer review required")
            lines.append("> This NPC is flagged as embraced. Confirm embrace ritual and embrace_depth before approval.")
            lines.append("")
        lines.append("---")
        lines.append("")

    # Writer's Notes
    lines.append("## Writer's Notes")
    lines.append("")
    notes = s("writers_notes")
    if notes:
        lines.append(notes)
    else:
        lines.append("_Submitted via Magic Workbench v0.2. Tier 3+ content (goals, decision map, hidden agenda) not authored in this submission — promote and complete in Obsidian._")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Submitted via Magic Workbench · Template v3.1*")
    lines.append("")

    return "\n".join(lines)


# ─── ROUTES ───────────────────────────────────────────────────────────────────


@app.route("/")
def home():
    npc_count = query_cache("SELECT COUNT(*) AS n FROM npcs")[0]["n"]
    practitioner_count = query_cache("SELECT COUNT(*) AS n FROM npcs WHERE magical_practice = 1")[0]["n"]
    faction_count = query_cache("SELECT COUNT(*) AS n FROM factions")[0]["n"]
    return render_template(
        "home.html",
        npc_count=npc_count,
        practitioner_count=practitioner_count,
        faction_count=faction_count,
        traditions=TRADITIONS,
    )


@app.route("/practitioner")
def practitioner_builder():
    return render_template(
        "practitioner.html",
        traditions=TRADITIONS,
        factions=FACTIONS,
        faction_credentials=FACTION_CREDENTIALS,
        cost_channels=COST_CHANNELS,
        corruption_surfaces=CORRUPTION_SURFACES,
    )


@app.route("/explorer")
def explorer():
    return render_template("explorer.html", placeholder=True, traditions=TRADITIONS)


@app.route("/aesthetics")
def aesthetics():
    return render_template("aesthetics.html", placeholder=True, traditions=TRADITIONS)


@app.route("/api/refresh", methods=["POST"])
def api_refresh():
    init_cache()
    return jsonify({"ok": True, "refreshed_at": datetime.utcnow().isoformat() + "Z"})


@app.route("/api/npcs")
def api_npcs():
    rows = query_cache("SELECT slug, npc_name, npc_tier, faction, magical_practice, tradition FROM npcs ORDER BY npc_name")
    return jsonify(rows)


@app.route("/api/factions")
def api_factions():
    rows = query_cache("SELECT faction_name, alignment_bias, faction_tier FROM factions ORDER BY faction_name")
    return jsonify(rows)


@app.route("/api/magic-constants")
def api_magic_constants():
    return jsonify(
        {
            "traditions": TRADITIONS,
            "faction_credentials": FACTION_CREDENTIALS,
            "cost_channels": COST_CHANNELS,
            "corruption_surfaces": CORRUPTION_SURFACES,
            "factions": FACTIONS,
            "alignment_tiers": {str(k): list(v) for k, v in ALIGNMENT_TIERS.items()},
            "valid_tradition_credential": VALID_TRADITION_CREDENTIAL,
            "preferred_channel": PREFERRED_CHANNEL,
        }
    )


@app.route("/api/practitioner/validate", methods=["POST"])
def api_validate():
    """Pre-flight validation. Returns errors and warnings without writing."""
    payload = request.get_json() or {}
    ok, errors, warnings = validate_submission(payload)
    return jsonify({"ok": ok, "errors": errors, "warnings": warnings})


@app.route("/api/practitioner/preview", methods=["POST"])
def api_preview():
    """Return the Markdown that would be written, without writing it.
    Used by the form's preview pane."""
    payload = request.get_json() or {}
    ok, errors, warnings = validate_submission(payload)
    if not ok:
        return jsonify({"ok": False, "errors": errors, "warnings": warnings, "markdown": ""})
    md = build_npc_markdown(payload)
    return jsonify({"ok": True, "errors": [], "warnings": warnings, "markdown": md})


@app.route("/api/practitioner/submit", methods=["POST"])
def api_submit():
    """Validate and write the NPC file to NPCs/_Pending/<slug>/<slug>.md."""
    payload = request.get_json() or {}
    ok, errors, warnings = validate_submission(payload)
    if not ok:
        return jsonify({"ok": False, "errors": errors, "warnings": warnings})

    name = payload.get("npc_name", "").strip()
    slug = slugify(name)
    md = build_npc_markdown(payload)

    # Ensure the pending dir exists
    target_dir = PENDING_DIR / slug
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / f"{slug}.md"

        # Don't overwrite — if pending already has this slug, fail loud
        if target_file.exists():
            return jsonify({
                "ok": False,
                "errors": [f"Pending file already exists: {target_file}. Resolve the existing pending submission before resubmitting."],
                "warnings": warnings,
            })

        target_file.write_text(md, encoding="utf-8")
    except Exception as e:
        return jsonify({"ok": False, "errors": [f"Write failed: {e}"], "warnings": warnings})

    # Rebuild cache so the new file shows up
    init_cache()

    return jsonify({
        "ok": True,
        "errors": [],
        "warnings": warnings,
        "slug": slug,
        "path": str(target_file),
        "relative_path": f"NPCs/_Pending/{slug}/{slug}.md",
    })


# ─── POLLING FALLBACK (watchdog optional) ────────────────────────────────────


def vault_poll_loop():
    """If watchdog isn't installed, poll for vault changes every 60s."""
    last_signature = None
    while True:
        try:
            md_files = list(NPCS_DIR.rglob("*.md")) + list(FACTIONS_DIR.rglob("*.md"))
            md_files = [f for f in md_files if "_Pending" not in f.parts and "_Characters" not in f.parts and "Versions" not in f.parts]
            mtimes = [f.stat().st_mtime for f in md_files]
            signature = (len(md_files), max(mtimes) if mtimes else 0)
            if signature != last_signature:
                if last_signature is not None:
                    print(f"[poll] vault changed; refreshing cache")
                init_cache()
                last_signature = signature
        except Exception as e:
            print(f"[poll] error: {e}")
        time.sleep(60)


# ─── ENTRY POINT ──────────────────────────────────────────────────────────────


def main():
    print()
    print("  Ironthorn Magic Workbench v0.3")
    print("  ==============================")
    print(f"  Vault: {VAULT_ROOT}")
    print(f"  Cache: {CACHE_DB}")
    print()
    print("  Building cache from vault ...")
    init_cache()
    npc_count = query_cache("SELECT COUNT(*) AS n FROM npcs")[0]["n"]
    fac_count = query_cache("SELECT COUNT(*) AS n FROM factions")[0]["n"]
    print(f"  Indexed: {npc_count} NPCs, {fac_count} factions")
    print()

    poller = threading.Thread(target=vault_poll_loop, daemon=True)
    poller.start()

    print("  Serving on http://localhost:7844")
    print("  Ctrl+C in this window stops the server.")
    print()
    app.run(host="127.0.0.1", port=7844, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
