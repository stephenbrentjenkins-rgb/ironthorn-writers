---
doc_type: "Version Control Standard"
version: "1.0"
applies_to: "All vault documents, Python scripts, and game build assets"
---

# Version Control Standard

One standard. Applied everywhere. Automated so user error is not a factor.

---

## The rule

> Before editing any canonical file, version it first.

The automation script handles this. You do not need to remember the rule — you run the script and it does the work.

---

## File naming format

```
FileName_vMAJOR.MINOR_YYYY-MM-DD.ext
```

Examples:
```
Maren-Voss_v2.0_2026-04-30.md
ironthorn_blockout_v1.2_2026-04-30.py
03-Gray-Compact_v2.0_2026-05-15.md
Writer-Standards_v1.1_2026-04-30.md
```

**MAJOR** — increments when content fundamentally changes in scope or structure.
**MINOR** — increments for corrections, additions, and upgrades that don't change fundamental structure.

Version numbers are read from the file's frontmatter `version:` field. If no version field exists, the script defaults to `v1.0`.

---

## Where versions live

| Asset type | Canonical location | Versions folder |
|-----------|-------------------|-----------------|
| NPC files | `NPCs/NPC-Name.md` | `NPCs/_Characters/NPC-Name/Versions/` |
| System docs | `_System/Doc-Name.md` | `_System/Versions/` |
| Faction files | `Factions/XX-Name.md` | `Factions/Versions/` |
| World files | `World/Ironthorn/File.md` | `World/Ironthorn/Versions/` |
| Python scripts | `Content/Python/script.py` | `Content/Python/Versions/` |

---

## The automation script

**Location:** `GameVault/Tools/version_snapshot.py`

**Usage:**
```
python version_snapshot.py path\to\file.md
python version_snapshot.py path\to\script.py
```

**What it does:**
1. Reads the file's current version from frontmatter (or defaults to v1.0)
2. Determines the correct Versions/ folder for this file type
3. Copies the file to Versions/ with the correct naming format
4. Prints a confirmation

**What it does NOT do:**
- It does not edit the canonical file
- It does not increment the version number
- It does not move or delete anything

After running the script, edit the canonical file normally. When you are done, update the `version:` field in the frontmatter.

---

## MAJOR vs MINOR — when to increment

| Change type | Version change | Example |
|-------------|---------------|---------|
| Full rebuild of a section | MAJOR | NPC rebuilt to Writer-Standards: v1.0 → v2.0 |
| New content added | MINOR | New dialogue hook added: v1.0 → v1.1 |
| Correction or fix | MINOR | Faction name corrected: v1.0 → v1.1 |
| Tell system added | MINOR | v1.0 → v1.1 |
| Hidden agenda layer added | MAJOR | v1.0 → v2.0 |
| Python script rebuilt | MAJOR | v1.0 → v2.0 |
| Python script bug fix | MINOR | v1.0 → v1.1 |
| Faction file restructured | MAJOR | v1.0 → v2.0 |
| World file location added | MINOR | v1.0 → v1.1 |

---

## Frontmatter version fields

Every canonical file carries these fields:

```yaml
version: "1.0"
version_note: "Brief description of what changed in this version"
previous_version: "FileName_v1.0_2026-04-30.md"
```

`version_note` is required for MAJOR increments. Optional for MINOR.
`previous_version` is the filename of the snapshot taken before this edit.

---

*[[../README|Back to Index]] · [[Lead-Writer-Review-Workflow|Review Workflow]] · [[NPC-Return-Taxonomy|Return Taxonomy]]*
