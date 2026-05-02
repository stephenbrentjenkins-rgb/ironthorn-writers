---
doc_type: "Character Folder Index"
version: "1.0"
location: "NPCs/_Characters/"
---

# NPC Character Folders

Each named NPC in Ironthorn has a dedicated folder here. The folder is the full asset record for that character — not just the canonical file, but everything that has ever been written for them, submitted about them, or noted down during development.

The canonical NPC file (the one Obsidian queries and Unreal reads via the Dev Tools panel) lives in `NPCs/` directly. The character folder here is the working archive behind it.

---

## Folder structure — per NPC

```
_Characters/
  NPC-Name/
    Versions/       ← Timestamped snapshots of the canonical file on each revision
    Submissions/    ← Writer submission forms for this NPC (one per submission)
    Dialogue/       ← Dialogue scripts, scene files, line reads, approved exchanges
    Notes/          ← Designer notes, reference images, tone anchors, inspiration
```

---

## How the pipeline works

### New NPC submission (writer-built)

1. Writer completes the certification path: Primer → Quiz → Glossary
2. Writer builds the NPC file using the NPC Template v3.0
3. Writer completes the NPC Submission Form (one per NPC)
4. Writer places both files in `NPCs/_Pending/NPC-Name/` — the holding folder
5. Lead writer reviews against Writer-Standards v1.0
6. On approval:
   - Canonical file moves to `NPCs/NPC-Name.md`
   - Submission form moves to `_Characters/NPC-Name/Submissions/`
   - Character folder created if it doesn't exist
   - Refresh Roster in the Unreal Dev Tools panel pulls the new NPC in automatically
7. On rejection:
   - Submission form returned to writer with Lead Writer Review section completed
   - File stays in `_Pending/` until revised and resubmitted

### Revision / upgrade

1. Before editing a canonical file, copy the current version to `_Characters/NPC-Name/Versions/` with a date stamp
   - Example: `Maren-Voss_v1.0_2026-04-30.md`
2. Edit the canonical file in `NPCs/`
3. Complete a new Submission Form for the upgrade and place in `_Characters/NPC-Name/Submissions/`
4. Lead writer reviews the delta — tone, flag accuracy, tell consistency
5. On approval, the new version is live and Unreal pulls it on next Refresh Roster

### Dialogue submissions

- Approved dialogue scripts go in `_Characters/NPC-Name/Dialogue/`
- Name format: `NPC-Name_Scene-Name_v1.md`
- Dialogue files are not automatically pulled into Unreal — they feed the Dialogue system separately

---

## Current character folders

| NPC | Folder | Canonical file | Status |
|-----|--------|---------------|--------|
| Brother Aldric | `Brother-Aldric/` | `../Brother-Aldric.md` | ✓ Complete — Writer-Standards v1.0 |
| Maren Voss | `Maren-Voss/` | `../Maren-Voss.md` | ✓ Complete — Writer-Standards v1.0 |
| Auditor Vesh | `Auditor-Vesh/` | `../Auditor-Vesh.md` | ✓ Complete — Writer-Standards v1.0 |
| Scholar-Physician Dael | `Scholar-Physician-Dael/` | `../Scholar-Physician-Dael.md` | ✓ Complete — Writer-Standards v1.0 |
| Davan Ord | `Davan-Ord/` | `../Davan-Ord.md` | ✓ Complete — Writer-Standards v1.0 |
| Sevin | `Sevin/` | `../Sevin.md` | ✓ Complete — Writer-Standards v1.0 |
| Commander Syla | `Commander-Syla/` | `../Commander-Syla.md` | Seed build — needs Writer-Standards upgrade |

*Remaining 35 NPCs will have character folders created when their files are built or submitted.*

---

## Pending folder

Writer submissions that have not yet been reviewed live in:

```
NPCs/_Pending/
  NPC-Name/
    NPC-Name.md                    ← the submitted NPC file
    NPC-Submission-Form.md         ← completed submission form
```

Do not move files from `_Pending/` to `NPCs/` without lead writer sign-off.

---

*[[../../README|Back to Index]] · [[../../_System/Writer-Standards|Writer Standards]] · [[../../_System/Writer-Certification/04-NPC-Submission-Form|Submission Form]] · [[../../_System/Writer-Certification/01-Writer-Primer|Writer Primer]]*
