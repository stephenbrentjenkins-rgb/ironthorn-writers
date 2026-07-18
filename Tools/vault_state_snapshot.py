"""
GameVault Vault State Snapshot Tool v1.0
=========================================
Walks the GameVault, parses YAML frontmatter from every markdown file in the
Story Engine scopes (and existing canonical scopes), and produces a single
JSON snapshot that web admin tools (Faction Influence Dashboard, NPC Priority
Inspector, etc.) can read.

USAGE:
  Double-click: vault_state_snapshot.bat
  Or run from command line: vault_state_snapshot.py [--out PATH]

WHAT IT DOES:
  1. Walks every relevant top-level folder in the GameVault
     (NPCs, Factions, World, WorldState, PhaseLayers, Questlines, DailyLife,
     StoryInstances, Instances)
  2. For each markdown file, parses YAML frontmatter (between leading --- lines)
  3. Aggregates everything into a single JSON document keyed by scope
  4. Writes the JSON to Tools/snapshots/latest.json (and also a timestamped
     copy to Tools/snapshots/<YYYY-MM-DD>_<HHMMSS>.json)

WHAT IT DOES NOT DO:
  - Does not modify any vault files
  - Does not validate frontmatter against templates (that's a separate tool)
  - Does not compute simulation state (that's the AFE)

OUTPUT SHAPE:
  {
    "snapshot_version": "1.0",
    "generated_at": "2026-05-02T14:30:00",
    "vault_root": "C:\\\\Users\\\\steph\\\\Desktop\\\\Game\\\\GameVault",
    "scopes": {
      "NPCs": [ { "path": "NPCs/Brother-Aldric.md", "frontmatter": {...} }, ... ],
      "Factions": [ ... ],
      "World": [ ... ],
      "WorldState": [ ... ],
      "PhaseLayers": [ ... ],
      "Questlines": [ ... ],
      "DailyLife": [ ... ],
      "StoryInstances": [ ... ],
      "Instances": [ ... ]
    },
    "errors": [ { "path": "...", "error": "..." }, ... ]
  }

DEPENDENCIES:
  Requires PyYAML. The Claude Desktop bundled Python typically does not have
  it preinstalled. If the import fails, the script falls back to a minimal
  internal YAML parser that handles the simple key:value, list, and nested
  dict shapes the GameVault uses. The fallback is good enough for the
  current frontmatter conventions but is not a general YAML parser.
"""

import os
import re
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# YAML loading: prefer PyYAML, fall back to a minimal parser that handles
# the GameVault's frontmatter shape.
# ---------------------------------------------------------------------------

try:
    import yaml  # type: ignore

    def parse_yaml(text: str) -> dict:
        result = yaml.safe_load(text)
        if not isinstance(result, dict):
            return {}
        return result

    YAML_BACKEND = "PyYAML"

except ImportError:

    def parse_yaml(text: str) -> dict:
        """
        Minimal frontmatter parser. Handles:
          - key: value (string, int, float, bool, null)
          - key: "quoted string"
          - key: 'quoted string'
          - key: [a, b, c]    (inline list)
          - key:               (nested dict or list, indented two spaces)
            sub_key: value
            sub_key: value
          - key:               (list of scalars or single-line objects)
            - item
            - item
        Does NOT handle multiline strings, anchors, aliases, complex nesting.
        Good enough for GameVault frontmatter; will quietly drop anything weird.
        """
        result: dict = {}
        lines = text.splitlines()
        i = 0
        n = len(lines)

        def coerce(raw: str):
            raw = raw.strip()
            if raw == "" or raw.lower() in ("null", "~"):
                return None
            if raw.lower() == "true":
                return True
            if raw.lower() == "false":
                return False
            # Quoted string
            if (raw.startswith('"') and raw.endswith('"')) or (
                raw.startswith("'") and raw.endswith("'")
            ):
                return raw[1:-1]
            # Inline list
            if raw.startswith("[") and raw.endswith("]"):
                inner = raw[1:-1].strip()
                if inner == "":
                    return []
                # Naive split on commas; OK for simple lists
                parts = [p.strip() for p in inner.split(",")]
                return [coerce(p) for p in parts]
            # Number?
            try:
                if "." in raw:
                    return float(raw)
                return int(raw)
            except ValueError:
                pass
            # Plain string
            return raw

        while i < n:
            line = lines[i]
            stripped = line.rstrip("\n")
            if stripped.strip() == "" or stripped.strip().startswith("#"):
                i += 1
                continue
            m = re.match(r"^([A-Za-z_][\w\-]*)\s*:\s*(.*)$", stripped)
            if not m:
                i += 1
                continue
            key = m.group(1)
            value_part = m.group(2)
            if value_part.strip() == "":
                # Could be nested dict or list
                # Look ahead at indented lines
                nested_lines = []
                j = i + 1
                while j < n:
                    next_line = lines[j]
                    if next_line.strip() == "":
                        j += 1
                        continue
                    if next_line.startswith("  ") or next_line.startswith("\t"):
                        nested_lines.append(next_line[2:] if next_line.startswith("  ") else next_line[1:])
                        j += 1
                    else:
                        break
                if not nested_lines:
                    result[key] = None
                elif nested_lines[0].lstrip().startswith("- "):
                    # List
                    items = []
                    for nl in nested_lines:
                        ns = nl.strip()
                        if ns.startswith("- "):
                            items.append(coerce(ns[2:]))
                    result[key] = items
                else:
                    # Nested dict
                    nested_text = "\n".join(nested_lines)
                    result[key] = parse_yaml(nested_text)
                i = j
            else:
                result[key] = coerce(value_part)
                i += 1
        return result

    YAML_BACKEND = "fallback"


# ---------------------------------------------------------------------------
# Frontmatter extraction
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from a markdown file. Returns {} if none."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    yaml_block = m.group(1)
    try:
        return parse_yaml(yaml_block)
    except Exception as e:
        raise RuntimeError(f"YAML parse failed: {e}")


# ---------------------------------------------------------------------------
# Scope walker
# ---------------------------------------------------------------------------

# Folders to walk. Skip versions/, intake/, _Pending/, etc. — those aren't
# canonical state, they're workflow scaffolding.
SCOPES = [
    "NPCs",
    "Factions",
    "World",
    "WorldState",
    "PhaseLayers",
    "Questlines",
    "DailyLife",
    "StoryInstances",
    "Instances",
]

# Path components that, if present anywhere in a file's relative path, cause
# it to be skipped.
EXCLUDE_PATH_PARTS = {
    "Versions",
    "_Pending",
    "_Characters",
    "_Intake",
    ".git",
    ".obsidian",
    "Excalidraw",
}


def should_skip(rel_path: Path) -> bool:
    """True if any part of the relative path is an excluded directory name."""
    return any(part in EXCLUDE_PATH_PARTS for part in rel_path.parts)


def walk_scope(vault_root: Path, scope: str) -> tuple[list, list]:
    """Walk one scope folder. Returns (entries, errors)."""
    entries = []
    errors = []
    scope_path = vault_root / scope
    if not scope_path.exists():
        return entries, errors

    for path in scope_path.rglob("*.md"):
        rel = path.relative_to(vault_root)
        if should_skip(rel):
            continue
        # Skip _README.md files in scope roots — they're orientation docs,
        # not content with frontmatter we care about
        if path.name == "_README.md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = path.read_text(encoding="cp1252")
            except Exception as e:
                errors.append({"path": str(rel).replace("\\", "/"), "error": f"read failed: {e}"})
                continue
        except Exception as e:
            errors.append({"path": str(rel).replace("\\", "/"), "error": f"read failed: {e}"})
            continue

        try:
            frontmatter = extract_frontmatter(text)
        except Exception as e:
            errors.append({"path": str(rel).replace("\\", "/"), "error": str(e)})
            continue

        # Skip files with no frontmatter — they're prose-only docs that
        # don't represent a state row
        if not frontmatter:
            continue

        entries.append(
            {
                "path": str(rel).replace("\\", "/"),
                "frontmatter": frontmatter,
            }
        )

    # Stable sort by path for deterministic snapshots
    entries.sort(key=lambda e: e["path"])
    return entries, errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def find_vault_root(start: Path) -> Path:
    """
    Find the GameVault root by walking upward from `start` looking for a
    folder that contains both _System/ and _Templates/ and Tools/.
    """
    cur = start.resolve()
    while True:
        if (cur / "_System").is_dir() and (cur / "_Templates").is_dir() and (cur / "Tools").is_dir():
            return cur
        if cur.parent == cur:
            raise RuntimeError(f"Could not locate GameVault root by walking up from {start}")
        cur = cur.parent


def main(argv=None):
    parser = argparse.ArgumentParser(description="GameVault state snapshot")
    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Output path. Defaults to Tools/snapshots/latest.json next to the vault root.",
    )
    parser.add_argument(
        "--no-timestamped",
        action="store_true",
        help="Skip writing the timestamped archive copy.",
    )
    args = parser.parse_args(argv)

    script_dir = Path(__file__).resolve().parent
    vault_root = find_vault_root(script_dir)

    print(f"GameVault Vault State Snapshot v1.0")
    print(f"  vault root:   {vault_root}")
    print(f"  yaml backend: {YAML_BACKEND}")
    print()

    scopes_data = {}
    all_errors = []
    for scope in SCOPES:
        entries, errors = walk_scope(vault_root, scope)
        scopes_data[scope] = entries
        all_errors.extend(errors)
        print(f"  {scope:<16} {len(entries):>4} entries, {len(errors):>2} errors")

    snapshot = {
        "snapshot_version": "1.0",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "vault_root": str(vault_root),
        "yaml_backend": YAML_BACKEND,
        "scopes": scopes_data,
        "errors": all_errors,
    }

    snapshots_dir = vault_root / "Tools" / "snapshots"
    snapshots_dir.mkdir(exist_ok=True)

    out_path = Path(args.out) if args.out else snapshots_dir / "latest.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print()
    print(f"  wrote {out_path}")

    if not args.no_timestamped:
        ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        archive_path = snapshots_dir / f"{ts}.json"
        archive_path.write_text(
            json.dumps(snapshot, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"  wrote {archive_path}")

    if all_errors:
        print()
        print(f"  {len(all_errors)} parse errors. First few:")
        for err in all_errors[:5]:
            print(f"    {err['path']}: {err['error']}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
