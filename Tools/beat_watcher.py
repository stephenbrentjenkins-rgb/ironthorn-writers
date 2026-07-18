"""
Ironthorn Beat Intake Watcher v1.0
====================================
Watches Questlines/_Intake/ for new questline beat description drops.
Uses Claude Code CLI (already authenticated via Max subscription) to
extract beat structure from prose. Validates every reference against
the live vault — NPCs, districts, factions, phases, world flags — and
flags hallucinations before they reach the vault.

USAGE:
  Double-click: start_beat_watcher.bat

DROP FORMAT:
  Name the file after the beat slug (or close to it):
    hollows-compact-beat-03.md
    or
    Compact-Approaches-Player.md          (slug will be derived)

  Optional header:
    Writer: Jane Smith
    Email: jane@example.com
    Questline: hollows-compact
    Beat Index: 3
    Trigger Type: location_entry
    ---
    (prose below — describe what happens in the beat)

OUTPUTS (per submission):
  Questlines/_Pending/<beat-slug>/
    <beat-slug>.md                         (filled Beat template, ready for review)
    <beat-slug>_Submission-Intake.md       (writer-facing summary)
    <beat-slug>_Validation-Report.md       (reference checks: pass/fail/uncertain)
  Questlines/<questline-slug>/Notes/
    <beat-slug>_Origin-Prose.md            (writer's original prose preserved)
"""

import os
import sys
import time
import json
import re
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path

# ─── PATHS ────────────────────────────────────────────────────────────────────

VAULT_ROOT      = Path(r"C:\Users\steph\Desktop\Game\GameVault")
QUESTLINES_DIR  = VAULT_ROOT / "Questlines"
INTAKE_DIR      = QUESTLINES_DIR / "_Intake"
PENDING_DIR     = QUESTLINES_DIR / "_Pending"

# Reference sources for validation
NPCS_DIR        = VAULT_ROOT / "NPCs"
WORLD_DIR       = VAULT_ROOT / "World" / "Ironthorn"
FACTIONS_DIR    = VAULT_ROOT / "Factions"
PHASE_DIR       = VAULT_ROOT / "PhaseLayers"
WORLDSTATE_DIR  = VAULT_ROOT / "WorldState"

POLL_INTERVAL = 5  # seconds

EXCLUDED_FILENAMES = {
    "readme.md", "readme.txt", "readme",
    "instructions.md", "instructions.txt",
}

CLAUDE_PATHS = [
    r"C:\Users\steph\AppData\Roaming\npm\claude.cmd",
    r"C:\Users\steph\AppData\Roaming\npm\claude",
    r"C:\Program Files\nodejs\claude.cmd",
    r"C:\PROGRA~1\nodejs\claude.cmd",
]

def find_claude():
    for p in CLAUDE_PATHS:
        if Path(p).exists():
            return p
    result = subprocess.run(["where", "claude"], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip().split("\n")[0].strip()
    return None

# ─── REFERENCE LOADER ─────────────────────────────────────────────────────────
# Loads the live rosters at start-of-process so the AI prompt has them as
# ground truth and the validator can check the AI's output against them.

def slugify(s):
    """File-stem to slug: 'Factor-Renne-Saul' -> 'factor-renne-saul'."""
    return s.lower().strip()

def load_npc_slugs():
    """Canonical NPCs (live in NPCs/*.md)."""
    if not NPCS_DIR.exists():
        return []
    return sorted([slugify(p.stem) for p in NPCS_DIR.glob("*.md")])

def load_location_slugs():
    """Districts and named locations (World/Ironthorn/*.md)."""
    if not WORLD_DIR.exists():
        return []
    return sorted([slugify(p.stem) for p in WORLD_DIR.glob("*.md")])

def load_faction_slugs():
    """Factions (Factions/01-Aureate-Covenant.md -> aureate-covenant)."""
    if not FACTIONS_DIR.exists():
        return []
    out = []
    for p in FACTIONS_DIR.glob("*.md"):
        if p.stem.startswith("_"):
            continue
        # Strip leading "01-" prefix
        slug = re.sub(r'^\d+-', '', p.stem).lower()
        out.append(slug)
    return sorted(out)

def load_phase_slugs():
    """Phase definitions. Each yields phase_group:phase_slug pairs."""
    if not PHASE_DIR.exists():
        return []
    pairs = []
    for p in PHASE_DIR.glob("**/*.md"):
        if p.stem.startswith("_"):
            continue
        try:
            content = p.read_text(encoding="utf-8")
            slug_match = re.search(r'^phase_slug:\s*["\']?([\w\-]+)', content, re.MULTILINE)
            group_match = re.search(r'^phase_group:\s*["\']?([\w\-]+)', content, re.MULTILINE)
            if slug_match and group_match:
                pairs.append(f"{group_match.group(1)}:{slug_match.group(1)}")
        except Exception:
            pass
    return sorted(pairs)

def load_world_flag_slugs():
    """World flag definitions in WorldState/."""
    if not WORLDSTATE_DIR.exists():
        return []
    out = []
    for p in WORLDSTATE_DIR.glob("**/*.md"):
        if p.stem.startswith("_"):
            continue
        try:
            content = p.read_text(encoding="utf-8")
            m = re.search(r'^flag_slug:\s*["\']?([\w\-]+)', content, re.MULTILINE)
            if m:
                out.append(m.group(1))
        except Exception:
            pass
    return sorted(out)

def load_existing_beat_slugs():
    """Beats already in the vault (Questlines/<slug>/<slug>-beat-NN.md)."""
    out = []
    if not QUESTLINES_DIR.exists():
        return out
    for q_dir in QUESTLINES_DIR.iterdir():
        if not q_dir.is_dir() or q_dir.name.startswith("_"):
            continue
        for f in q_dir.glob("*-beat-*.md"):
            out.append(f.stem)
    return sorted(out)

# Cached at startup for AI context and validator
class VaultIndex:
    def __init__(self):
        self.npcs = load_npc_slugs()
        self.locations = load_location_slugs()
        self.factions = load_faction_slugs()
        self.phases = load_phase_slugs()
        self.world_flags = load_world_flag_slugs()
        self.beats = load_existing_beat_slugs()

    def summary(self):
        return (
            f"NPCs: {len(self.npcs)}, Locations: {len(self.locations)}, "
            f"Factions: {len(self.factions)}, Phases: {len(self.phases)}, "
            f"WorldFlags: {len(self.world_flags)}, Beats: {len(self.beats)}"
        )

# ─── INTAKE FILE PARSING ──────────────────────────────────────────────────────

def parse_intake_file(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    meta = {
        "writer": "", "email": "", "questline": "", "beat_index": "",
        "trigger_type": "", "trigger_target": "",
    }
    prose = content

    # Header detection — same shape as NPC watcher
    first_line = content.splitlines()[0] if content else ""
    if any(first_line.startswith(k) for k in
           ("Writer:", "Email:", "Questline:", "Beat Index:", "Trigger Type:", "Trigger Target:", "Name:")):
        parts = content.split("---", 1)
        if len(parts) == 2:
            header, prose = parts[0].strip(), parts[1].strip()
            for line in header.splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    k = key.strip().lower().replace(" ", "_")
                    if k in meta:
                        meta[k] = val.strip()

    return meta, prose.strip()

def derive_beat_slug(filename_stem, meta, ai_data):
    """
    Beat slug priority:
      1. AI-extracted beat_slug (preferred; AI knows the questline).
      2. Filename stem if it already matches the convention.
      3. Constructed from questline + beat_index.
    """
    if ai_data and ai_data.get("beat_slug"):
        return ai_data["beat_slug"]
    if re.match(r'^[\w\-]+-beat-\d+$', filename_stem):
        return filename_stem.lower()
    if meta.get("questline") and meta.get("beat_index"):
        try:
            n = int(meta["beat_index"])
            return f"{meta['questline']}-beat-{n:02d}"
        except ValueError:
            pass
    return filename_stem.lower()

# ─── CLAUDE CODE CALL ─────────────────────────────────────────────────────────

def call_claude_code(beat_intake_name, meta, prose, vault, claude_path):
    """
    AI prompt pulls in the live vault rosters so the model can pick correct
    slugs. Asked for strict JSON; we still validate after.
    """
    npc_list = ", ".join(vault.npcs) or "(none)"
    location_list = ", ".join(vault.locations) or "(none)"
    faction_list = ", ".join(vault.factions) or "(none)"
    phase_list = ", ".join(vault.phases) or "(none — no phases authored yet)"
    flag_list = ", ".join(vault.world_flags) or "(none — no world flags authored yet)"
    existing_beats = ", ".join(vault.beats) or "(none)"

    prompt = f"""You are a questline beat analyst for the Ironthorn dark fantasy RPG.
Read this beat description and extract structured beat data.

Intake filename: {beat_intake_name}
Writer: {meta.get('writer') or 'unknown'}
Questline hint: {meta.get('questline') or 'unknown'}
Beat index hint: {meta.get('beat_index') or 'unknown'}
Trigger type hint: {meta.get('trigger_type') or 'unknown'}

Beat description:
{prose}

LIVE VAULT REFERENCES — use these exact slugs only.

Canonical NPCs:
{npc_list}

Locations (districts):
{location_list}

Factions:
{faction_list}

Phases (format phase_group:phase_slug):
{phase_list}

World flags:
{flag_list}

Existing beat slugs (for prerequisites):
{existing_beats}

RULES.

1. Use only slugs from the lists above. If a beat references something
   that does NOT exist in the lists, set the field to null and add a
   note in `unresolved_references` explaining what was referenced and
   what should exist for the beat to work.

2. The beat MUST justify the scope of every effect it declares.
   - phase_activations are cohort-scoped — used when a player's view
     of the world changes, not the world itself.
   - world_writes are server-shared — used when the change is true
     for everyone.
   - npc_writes are proposed and queued for writer review.
   - If you cannot justify a scope, leave the field empty and add a
     note in `unresolved_references`.

3. Tone: tired, not broken. Cinematic theatricality is a tone failure.
   Reflect that in `tone_check`.

4. trigger_type MUST be one of:
     location_entry, npc_interaction, prior_beat_complete,
     world_flag, npc_threshold, manual

5. completion_condition MUST be one of:
     auto_on_dialogue_end, manual, condition

Respond ONLY with a JSON object. No markdown, no explanation.

Use this exact structure:
{{
  "beat_name": "Human-readable name",
  "beat_slug": "questline-slug-beat-NN",
  "questline_slug": "questline-slug",
  "beat_index": 1,
  "trigger_type": "location_entry",
  "trigger_target": "slug-from-lists-above-or-null",
  "prerequisites": ["beat-slug", ...],
  "phase_activations": ["phase-group:phase-slug", ...],
  "phase_deactivations": ["phase-group:phase-slug", ...],
  "world_writes": ["flag-slug:value", ...],
  "npc_writes": ["npc-slug:field:value", ...],
  "instance_entry": "instance-slug-or-empty-string",
  "completion_condition": "auto_on_dialogue_end",

  "what_happens": "1-3 paragraphs from the player's perspective",
  "trigger_narrative": "1 paragraph — the fictional cause",
  "body": "the actual content of the beat — dialogue with speaker labels, or environmental description",
  "player_choices": [
    {{"choice": "string", "effects": "string or null"}}
  ],
  "effects_justification": {{
    "phase_activations": "why cohort-scoped, per entry",
    "world_writes": "why server-shared, per entry",
    "npc_writes": "in-fiction event per entry",
    "instance_entry": "why private space needed or null"
  }},
  "completion_narrative": "how the beat ends",
  "downstream_beats": [
    {{"beat_slug": "next-beat-slug", "trigger": "what fires it"}}
  ],
  "tone_check": "1-2 lines on how the beat reflects tired-not-broken",

  "unresolved_references": [
    "free-text: what was referenced that does not exist in the vault"
  ],
  "writer_notes": "open questions, gaps, things that need decision"
}}
"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(prompt)
        prompt_file = f.name

    try:
        result = subprocess.run(
            [claude_path, "--print"],
            input=prompt, capture_output=True, text=True, timeout=180,
            encoding='utf-8'
        )
        output = (result.stdout or "").strip()
        if not output:
            raise ValueError(f"Claude returned empty output. stderr: {result.stderr[:500]}")

        output = re.sub(r'^```json\s*', '', output, flags=re.MULTILINE)
        output = re.sub(r'\s*```\s*$', '', output, flags=re.MULTILINE)
        match = re.search(r'\{[\s\S]*\}', output)
        if match:
            return json.loads(match.group(0))
        else:
            raise ValueError(f"No JSON found in output: {output[:500]}")
    finally:
        try:
            os.unlink(prompt_file)
        except Exception:
            pass

# ─── REFERENCE VALIDATOR ──────────────────────────────────────────────────────
# Even though the AI was given the rosters, validate every reference against
# the actual vault. Hallucinations slip through. This is the catch.

def validate_references(d, vault):
    """
    Returns a list of (severity, field, value, reason) tuples.
    Severity: ERROR (must fix), WARN (probably wrong), INFO (worth noting).
    """
    issues = []

    # trigger_type allowed values
    valid_triggers = {"location_entry", "npc_interaction", "prior_beat_complete",
                      "world_flag", "npc_threshold", "manual"}
    tt = d.get("trigger_type")
    if tt and tt not in valid_triggers:
        issues.append(("ERROR", "trigger_type", tt,
                       f"not in {sorted(valid_triggers)}"))

    valid_completion = {"auto_on_dialogue_end", "manual", "condition"}
    cc = d.get("completion_condition")
    if cc and cc not in valid_completion:
        issues.append(("ERROR", "completion_condition", cc,
                       f"not in {sorted(valid_completion)}"))

    # trigger_target — depends on trigger_type
    tgt = d.get("trigger_target")
    if tgt and tt:
        if tt == "location_entry" and tgt not in vault.locations:
            issues.append(("ERROR", "trigger_target", tgt,
                           "location not in vault"))
        elif tt == "npc_interaction" and tgt not in vault.npcs:
            issues.append(("ERROR", "trigger_target", tgt,
                           "NPC not in vault"))
        elif tt == "prior_beat_complete" and tgt not in vault.beats:
            issues.append(("WARN", "trigger_target", tgt,
                           "beat not in vault — may be valid if authored together"))
        elif tt == "world_flag" and tgt not in vault.world_flags:
            issues.append(("ERROR", "trigger_target", tgt,
                           "world flag not in vault"))
        elif tt == "npc_threshold" and tgt.split(":")[0] not in vault.npcs:
            issues.append(("ERROR", "trigger_target", tgt,
                           "NPC (before colon) not in vault"))

    # prerequisites
    for pre in d.get("prerequisites") or []:
        if pre not in vault.beats:
            issues.append(("WARN", "prerequisites", pre,
                           "beat not in vault — valid if authored together"))

    # phase_activations / deactivations
    for entry in (d.get("phase_activations") or []) + (d.get("phase_deactivations") or []):
        if entry == "":
            continue
        if ":" not in entry:
            issues.append(("ERROR", "phase_activations/deactivations", entry,
                           "missing colon — must be 'group:slug'"))
            continue
        # 'group:base' is valid (means 'exit group entirely')
        if entry.endswith(":base"):
            continue
        if entry not in vault.phases:
            issues.append(("ERROR", "phase_activations/deactivations", entry,
                           "phase not in vault"))

    # world_writes — flag-slug:value
    for entry in d.get("world_writes") or []:
        if ":" not in entry:
            issues.append(("ERROR", "world_writes", entry,
                           "missing colon — must be 'flag-slug:value'"))
            continue
        flag = entry.split(":", 1)[0]
        if flag not in vault.world_flags:
            issues.append(("ERROR", "world_writes", entry,
                           f"flag '{flag}' not in vault"))

    # npc_writes — npc-slug:field:value
    for entry in d.get("npc_writes") or []:
        parts = entry.split(":")
        if len(parts) < 3:
            issues.append(("ERROR", "npc_writes", entry,
                           "must be 'npc-slug:field:value'"))
            continue
        npc = parts[0]
        if npc not in vault.npcs:
            issues.append(("ERROR", "npc_writes", entry,
                           f"NPC '{npc}' not in vault"))

    # AI's own self-reported unresolved references
    for note in d.get("unresolved_references") or []:
        issues.append(("INFO", "ai_self_report", "—", note))

    return issues

# ─── OUTPUT BUILDERS ──────────────────────────────────────────────────────────

def build_beat_file(beat_slug, d, today):
    """Fill in the canonical Beat template with AI extraction."""
    beat_name = d.get("beat_name", beat_slug)
    questline_slug = d.get("questline_slug", "")
    beat_index = d.get("beat_index", 1)
    trigger_type = d.get("trigger_type", "manual")
    trigger_target = d.get("trigger_target") or ""
    prerequisites = d.get("prerequisites") or []
    phase_activations = d.get("phase_activations") or []
    phase_deactivations = d.get("phase_deactivations") or []
    world_writes = d.get("world_writes") or []
    npc_writes = d.get("npc_writes") or []
    instance_entry = d.get("instance_entry") or ""
    completion = d.get("completion_condition", "auto_on_dialogue_end")

    def yaml_list(items):
        if not items:
            return "[]"
        return "[" + ", ".join(f'"{x}"' for x in items) + "]"

    body = d.get("body", "REPLACE — write the body of the beat")
    choices = d.get("player_choices") or []
    if choices:
        choices_md = "\n".join(
            f"- **{c.get('choice', '?')}** — {c.get('effects') or '(narrative-only; no state change)'}"
            for c in choices
        )
    else:
        choices_md = "_(no player choices in this beat — narrative passes through)_"

    ej = d.get("effects_justification") or {}
    downstream = d.get("downstream_beats") or []
    if downstream:
        downstream_md = "\n".join(
            f"- **{b.get('beat_slug', '?')}** — fires when {b.get('trigger', 'TBD')}"
            for b in downstream
        )
    else:
        downstream_md = "_(none declared — beat is a leaf, or downstream beats not yet authored)_"

    return f"""---
beat_name: "{beat_name}"
beat_slug: "{beat_slug}"
questline_slug: "{questline_slug}"
beat_index: {beat_index}
trigger_type: "{trigger_type}"
trigger_target: "{trigger_target}"
prerequisites: {yaml_list(prerequisites)}
phase_activations: {yaml_list(phase_activations)}
phase_deactivations: {yaml_list(phase_deactivations)}
world_writes: {yaml_list(world_writes)}
npc_writes: {yaml_list(npc_writes)}
instance_entry: "{instance_entry}"
completion_condition: "{completion}"
template_version: "1.0"
status: "Draft"
intake_processed: "{today}"
---

# {beat_name}

> [!info] Beat at a glance
> **Slug:** `{beat_slug}` · **Questline:** `{questline_slug}` · **Index:** {beat_index}
> **Trigger:** `{trigger_type}` → `{trigger_target or '(unset)'}`
> **Status:** Draft

---

## What happens in this beat

{d.get("what_happens", "REPLACE — describe the beat from the player's perspective.")}

## Trigger

{d.get("trigger_narrative", "REPLACE — explain the fictional cause of this beat.")}

## Body

{body}

## Player choices

{choices_md}

## Effects — declared

This beat produces the following state changes (mirrors frontmatter):

**Phase activations:** {phase_activations or '(none)'}
**Phase deactivations:** {phase_deactivations or '(none)'}
**World writes:** {world_writes or '(none)'}
**NPC writes (proposed):** {npc_writes or '(none)'}
**Instance entry:** {instance_entry or '(none)'}

## Effects — justification

**Phase activations:** {ej.get('phase_activations') or 'REPLACE — justify cohort scope'}

**World writes:** {ej.get('world_writes') or 'REPLACE — justify server-shared scope'}

**NPC writes:** {ej.get('npc_writes') or 'REPLACE — state the in-fiction event causing each change'}

**Instance entry:** {ej.get('instance_entry') or '(no instance entry declared)'}

## Completion

{d.get("completion_narrative", "REPLACE — describe how the beat ends.")}

## Downstream beats

{downstream_md}

## Tone check

{d.get("tone_check", "REPLACE — one or two lines on tone.")}

## Unreal mapping

| YAML field | UStruct field | Type |
|---|---|---|
| beat_slug | BeatSlug | FName |
| questline_slug | QuestlineSlug | FName |
| beat_index | BeatIndex | int32 |
| trigger_type | TriggerType | ETriggerType |
| trigger_target | TriggerTarget | FName |
| prerequisites | Prerequisites | TArray<FName> |
| phase_activations | PhaseActivations | TArray<FString> |
| phase_deactivations | PhaseDeactivations | TArray<FString> |
| world_writes | WorldWrites | TArray<FString> |
| npc_writes | NpcWrites | TArray<FString> |
| instance_entry | InstanceEntry | FName |
| completion_condition | CompletionCondition | ECompletionCondition |

---

*[[../../README|Back to Index]] · [[../../_System/Story-Architecture]] · [[../../_System/Writer-Standards]]*
"""

def build_validation_report(beat_slug, issues, vault, today):
    if not issues:
        body = "**No issues found.** All references resolve against the live vault."
    else:
        errors = [i for i in issues if i[0] == "ERROR"]
        warns = [i for i in issues if i[0] == "WARN"]
        infos = [i for i in issues if i[0] == "INFO"]

        sections = []
        if errors:
            sections.append("### ERRORS — must resolve before approval\n\n" +
                "\n".join(f"- **{i[1]}**: `{i[2]}` — {i[3]}" for i in errors))
        if warns:
            sections.append("### Warnings — likely intentional but flag for review\n\n" +
                "\n".join(f"- **{i[1]}**: `{i[2]}` — {i[3]}" for i in warns))
        if infos:
            sections.append("### Info — AI self-reported unresolved references\n\n" +
                "\n".join(f"- {i[3]}" for i in infos))
        body = "\n\n".join(sections)

    return f"""---
doc_type: "Beat Validation Report"
beat_slug: "{beat_slug}"
date: "{today}"
issue_count: {len(issues)}
---

# Validation Report — {beat_slug}

Generated by Beat Intake Watcher on {today}.

Vault state at validation time: {vault.summary()}

---

{body}

---

## How to resolve

- **ERROR — slug not in vault:** the AI invented a slug that doesn't exist.
  Either correct the slug in the beat file (replace with a real one) or
  author the missing referent first (NPC, location, phase, flag) and
  re-run the watcher.

- **WARN — beat not in vault:** common for beats authored as a sequence.
  No action needed if the prerequisite beat is being authored alongside
  this one.

- **INFO — AI self-report:** the AI noticed something it couldn't resolve
  and surfaced it. Read these — they often catch design gaps.
"""

def build_intake_doc(beat_slug, meta, ai_data, issue_count, today):
    writer = meta.get("writer") or "FILL IN"
    questline = meta.get("questline") or ai_data.get("questline_slug") or "FILL IN"
    return f"""---
doc_type: "Beat Submission Intake"
beat_slug: "{beat_slug}"
writer: "{writer}"
date: "{today}"
---

# Beat Submission Intake — {beat_slug}

**Writer:** {writer}
**Email:** {meta.get('email') or 'FILL IN'}
**Questline:** {questline}
**Date:** {today}
**Validation issues:** {issue_count}

**Files included:**
- [x] Beat file (`{beat_slug}.md`) — pre-filled by intake watcher
- [x] Validation report (`{beat_slug}_Validation-Report.md`)
- [x] Origin prose (saved to `Questlines/{questline}/Notes/`)

**Next steps:**
1. Review the validation report — fix all ERRORS before submitting.
2. Review the beat file — replace any REPLACE markers, refine prose.
3. Open Manager Board → Beats tab → review and approve.
"""

def build_origin_prose(beat_slug, meta, prose, today):
    writer = meta.get("writer") or "Unknown"
    questline = meta.get("questline") or "unfiled"
    return f"""---
doc_type: "Beat Origin Prose"
beat_slug: "{beat_slug}"
writer: "{writer}"
questline: "{questline}"
date: "{today}"
---

# {beat_slug} — Origin Prose

*Written by {writer} / {today}*

---

{prose}

---

*Original prose submitted to Ironthorn Beat Intake Watcher on {today}. Preserved without modification.*
"""

# ─── PROCESS ONE FILE ─────────────────────────────────────────────────────────

def process_file(filepath, claude_path, vault):
    path = Path(filepath)
    intake_stem = path.stem
    today = date.today().strftime("%Y-%m-%d")

    print(f"\n{'='*60}")
    print(f"Processing: {path.name}")
    print(f"{'='*60}")

    meta, prose = parse_intake_file(filepath)
    if not prose or len(prose) < 30:
        print(f"  ERROR: Too little prose — skipping (got {len(prose)} chars)")
        return False

    print(f"  Prose: {len(prose)} characters")
    print(f"  Writer: {meta.get('writer') or 'not specified'}")
    print(f"  Questline hint: {meta.get('questline') or 'not specified'}")
    print(f"  Vault state: {vault.summary()}")

    print(f"  Calling Claude Code...")
    try:
        d = call_claude_code(intake_stem, meta, prose, vault, claude_path)
    except Exception as e:
        print(f"  ERROR (Claude call): {e}")
        import traceback
        traceback.print_exc()
        return False

    beat_slug = derive_beat_slug(intake_stem, meta, d)
    questline_slug = d.get("questline_slug") or meta.get("questline") or "unfiled"
    print(f"  Beat slug: {beat_slug}")
    print(f"  Questline: {questline_slug}")
    print(f"  Trigger: {d.get('trigger_type')} -> {d.get('trigger_target') or '(unset)'}")

    # Validate references
    issues = validate_references(d, vault)
    err_count = sum(1 for i in issues if i[0] == "ERROR")
    warn_count = sum(1 for i in issues if i[0] == "WARN")
    info_count = sum(1 for i in issues if i[0] == "INFO")
    print(f"  Validation: {err_count} errors, {warn_count} warnings, {info_count} info")
    if err_count:
        print(f"  >>> Beat has unresolved references. Review validation report.")

    # Build outputs
    pending_folder = PENDING_DIR / beat_slug
    pending_folder.mkdir(parents=True, exist_ok=True)

    (pending_folder / f"{beat_slug}.md").write_text(
        build_beat_file(beat_slug, d, today), encoding="utf-8")
    (pending_folder / f"{beat_slug}_Validation-Report.md").write_text(
        build_validation_report(beat_slug, issues, vault, today), encoding="utf-8")
    (pending_folder / f"{beat_slug}_Submission-Intake.md").write_text(
        build_intake_doc(beat_slug, meta, d, len(issues), today), encoding="utf-8")

    # Origin prose lives next to the questline, not in _Pending
    notes_folder = QUESTLINES_DIR / questline_slug / "Notes"
    notes_folder.mkdir(parents=True, exist_ok=True)
    (notes_folder / f"{beat_slug}_Origin-Prose.md").write_text(
        build_origin_prose(beat_slug, meta, prose, today), encoding="utf-8")

    print(f"  Output: {pending_folder}")
    print(f"  Origin: {notes_folder}")

    # Move processed intake file
    done_dir = INTAKE_DIR / "_Done"
    done_dir.mkdir(exist_ok=True)
    shutil.move(str(filepath), str(done_dir / path.name))
    print(f"  Moved intake to _Intake/_Done/")
    print(f"  DONE: {beat_slug}")
    return True

# ─── WATCHER LOOP ─────────────────────────────────────────────────────────────

def watch():
    claude_path = find_claude()
    if not claude_path:
        print("ERROR: Claude Code CLI not found.")
        print("Run: npm install -g @anthropic-ai/claude-code")
        input("Press Enter to exit...")
        return

    INTAKE_DIR.mkdir(parents=True, exist_ok=True)
    PENDING_DIR.mkdir(parents=True, exist_ok=True)

    vault = VaultIndex()

    print("=" * 60)
    print("  Ironthorn Beat Intake Watcher v1.0")
    print(f"  Claude: {claude_path}")
    print(f"  Watching: {INTAKE_DIR}")
    print(f"  Vault: {vault.summary()}")
    print(f"  Poll: every {POLL_INTERVAL}s")
    print("  Drop .md or .txt files describing a single beat")
    print("  Ctrl+C to stop")
    print("=" * 60)

    seen = set()
    while True:
        try:
            for fname in os.listdir(INTAKE_DIR):
                if fname.startswith(".") or fname.startswith("_"):
                    continue
                if fname.lower() in EXCLUDED_FILENAMES:
                    continue
                if not (fname.endswith(".md") or fname.endswith(".txt")):
                    continue
                fpath = INTAKE_DIR / fname
                if str(fpath) in seen:
                    continue
                time.sleep(1)
                if not fpath.exists():
                    continue
                seen.add(str(fpath))

                # Refresh vault index — new NPCs/phases may have been
                # approved between drops
                vault = VaultIndex()
                try:
                    process_file(fpath, claude_path, vault)
                except Exception as e:
                    print(f"  ERROR: {e}")
                    import traceback
                    traceback.print_exc()
            time.sleep(POLL_INTERVAL)
        except KeyboardInterrupt:
            print("\nWatcher stopped.")
            break

if __name__ == "__main__":
    watch()
