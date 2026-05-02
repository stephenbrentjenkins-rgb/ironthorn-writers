# Game Design Vault

> Dark fantasy RPG system — NPC intelligence, alignment, deception, and faction design.
> Built for Obsidian with Dataview. Requires: **Dataview plugin** (live queries throughout).
> **Engine:** Unreal Engine 5.5

---

## How this vault is organised

| Folder | Contents |
|--------|----------|
| `_System/` | Rules, mechanics, and reference documents. The rulebook. |
| `_System/Versions/` | Snapshots of system documents before each edit. |
| `_System/Writer-Certification/` | Writer certification path — primer, quiz, glossary, submission form. |
| `_System/Writer-Certification/Records/` | Certification and submission records. |
| `_System/Writer-Certification/DevTools/` | Developer tooling documentation. |
| `_Templates/` | Master templates for NPCs, factions, and test scenarios. |
| `NPCs/` | Individual NPC files — one note per character. |
| `NPCs/_Characters/` | Per-NPC asset folders — versions, submissions, dialogue, notes. |
| `NPCs/_Pending/` | Writer submissions awaiting lead writer review. |
| `Factions/` | Faction profiles and inter-faction relationship maps. |
| `Factions/Versions/` | Snapshots of faction files before each edit. |
| `World/` | Cities, districts, regions, and location documents. |
| `World/Ironthorn/Versions/` | Snapshots of Ironthorn district files before each edit. |
| `Tools/` | Automation scripts — version snapshots, NPC approval, build utilities. |

---

## Start here — system documents

1. [[_System/Alignment-Spectrum]] — the 7-tier light/gray/dark system
2. [[_System/Deception-Perception-Skills]] — how lying and catching lies works
3. [[_System/NPC-Intelligence-System]] — decision maps, memory logs, goal architecture
4. [[_System/Attribute-Reference]] — main attributes and all sub-attributes explained
5. [[_System/NPC-Tier-Reference]] — when to use Tier 1 vs Tier 5
6. [[_System/Spy-Registry]] — all active double-agent operations; designer-only
7. [[_System/Writer-Standards]] — mandatory read before writing any NPC file or scene
8. [[_System/Lead-Writer-Review-Workflow]] — how submissions are reviewed and admitted
9. [[_System/NPC-Return-Taxonomy]] — standardised return codes for all submission failures
10. [[_System/Version-Control-Standard]] — versioning rules and automation tools

---

## Tools

Automation scripts that take user error out of the workflow.

| Tool | Usage | What it does |
|------|-------|-------------|
| `Tools/snapshot.bat` | Drag any file onto it | Snapshots the file to the correct Versions/ folder before editing |
| `Tools/approve_npc.bat NPC-Name` | Run from command line | Full approval workflow — snapshots existing file, moves submission to NPCs/, moves form to Submissions/ |
| `Content/Python/ironthorn_blockout.py` | Run in Unreal | Places all district volumes, ramps, roads, walls |
| `Content/Python/ironthorn_organise.py` | Run in Unreal | Organises actors into World Outliner folder hierarchy |
| `Content/Python/ironthorn_wireframe_colours.py` | Run in Unreal | Applies district wireframe colours |

---

## Developer tooling

> [!info] Two-layer developer connection — Obsidian ↔ Browser ↔ Unreal Engine 5.5

| Layer | Tool | Function |
|-------|------|---------|
| C — Obsidian | `gamevault-devtools.html` | Live NPC roster · submit NPC files · certify writers · export to Unreal |
| D — Unreal 5.5 | `NPCDevTools` module | Dockable editor panel · Ping Vault · Refresh Roster · Export JSON · VaultBridge HTTP sync |

---

## Writer certification path

> [!danger] Required before submitting any NPC content

| Step | Document | Status |
|------|---------|--------|
| 1 | [[_System/Writer-Certification/01-Writer-Primer]] — read in full | Required |
| 2 | [[_System/Writer-Certification/02-Writer-Quiz]] — 80% pass required | Required |
| 3 | [[_System/Writer-Certification/03-Writer-Glossary]] — reference; no pass/fail | Reference |
| 4 | [[_System/Writer-Certification/04-NPC-Submission-Form]] — one per NPC submitted | Required per NPC |

---

## Writer submission pipeline

| Step | Action |
|------|--------|
| 1 | Writer completes certification (Primer → Quiz → Glossary) |
| 2 | Writer builds NPC using NPC Template v3.0 |
| 3 | Writer completes Submission Form + Submission Intake document |
| 4 | Writer places all three files in `NPCs/_Pending/NPC-Name/` |
| 5 | Writer emails **stephenbrentjenkins@gmail.com** — subject: `[NPC SUBMISSION] NPC-Name — Writer Name — Date` |
| 6 | Lead writer reviews against 5 criteria — 5 business day window |
| 7 | **Approved** → run `approve_npc.bat NPC-Name` → Refresh Roster in Unreal |
| 8 | **Returned** → Return Notice placed in submission folder with return codes → writer revises and resubmits |

**Lead writer review workflow:** [[_System/Lead-Writer-Review-Workflow]]
**Return taxonomy:** [[_System/NPC-Return-Taxonomy]]
**Version control standard:** [[_System/Version-Control-Standard]]

---

## World — locations

### Ironthorn
Primary city. Iron Dominion garrison at the Great Gate. Six districts plus the Hollows beneath.

**Full NPC roster:** [[World/Ironthorn/Ironthorn-NPC-Roster]] — 42 NPCs defined, all named

| District | Side | Faction | Key locations |
|----------|------|---------|--------------|
| [[World/Ironthorn/Sanctum-Ward]] | Upper | Aureate Covenant | The Hearthstone · Arnath's Provisions · Office of the Record |
| [[World/Ironthorn/Greenward]] | Upper | Verdant Circle | The Canopy Rest · Reagent Garden · Office of the Commons |
| [[World/Ironthorn/Ledger-Row]] | Divide | Gray Compact | The Neutral Table · The Exchange · Cartography House · Office of the Treasury |
| [[World/Ironthorn/Ashgate-Quarter]] | Lower | Ashen Veil (unofficial) | Ashgate Lodging · Full Forge · Office of Works |
| [[World/Ironthorn/Wound-Market]] | Lower | Crimson Throne (indirect) | The Restless House · Blood-Bound Arcanist · Office of Tolerance |
| [[World/Ironthorn/The-Hollows]] | Beneath | Unknown | The Dry Chamber · Access map · Void Eternum anchor |

---

## Live roster

```dataview
TABLE npc_name, npc_tier, faction, location, alignment_public, alignment_true, cunning, status
FROM "NPCs"
SORT npc_tier DESC, cunning DESC
```

---

## Active flags — all NPCs

```dataview
TABLE npc_name, faction, liar_mark_active, debt_flag_active, leverage_held, trust_score
FROM "NPCs"
WHERE liar_mark_active = true OR debt_flag_active = true OR leverage_held = true
```

---

## Warning watches

### Resentment approaching betrayal threshold (7+)
```dataview
TABLE npc_name, faction, loyalty, loyalty_devotion, loyalty_resentment
FROM "NPCs"
WHERE loyalty_resentment >= 7
SORT loyalty_resentment DESC
```

### Disillusionment approaching collapse (7+)
```dataview
TABLE npc_name, faction, idealism, idealism_conviction, idealism_disillusionment
FROM "NPCs"
WHERE idealism_disillusionment >= 7
SORT idealism_disillusionment DESC
```

### High paranoia — pre-emptive escalation risk (7+)
```dataview
TABLE npc_name, faction, cunning, cunning_paranoia, cunning_patience
FROM "NPCs"
WHERE cunning_paranoia >= 7
SORT cunning_paranoia DESC
```

---

## Faction overview

```dataview
TABLE faction_name, alignment_bias, faction_tier, leadership, status
FROM "Factions"
WHERE faction_name
SORT faction_tier DESC
```

---

## Build log

| Session | What was built |
|---------|---------------|
| Session 1 | Alignment spectrum, deception/perception skill system |
| Session 2 | NPC intelligence system — decision map, memory log, goal architecture |
| Session 3 | Attribute system — mains and subs |
| Session 4 | NPC template v3.0 — scaled Tier 1–5 |
| Session 5 | Seed NPCs — Maren Voss, Brother Aldric, Commander Syla |
| Session 6 | Full vault structure built and imported to Obsidian |
| Session 7 | All 7 factions built with internal tension, spy slots, and defection mechanics; Spy Registry added |
| Session 8 | Alignment-Spectrum updated to v2.0 |
| Session 9 | World folder created; Ironthorn city overview + 6 district files |
| Session 10 | All 6 Ironthorn district files fully populated |
| Session 11 | Writer-Standards added; Brother Aldric rebuilt; Ironthorn-NPC-Roster added (42 NPCs) |
| Session 12 | Writer Certification path built — Primer, Quiz, Glossary, Submission Form |
| Session 13 | DevTools browser panel + Unreal 5.5 NPCDevTools module — full pipeline live |
| Session 14 | NPCDevTools rebuilt as pure Slate module; vault connection confirmed end-to-end |
| Session 14 | 6 NPCs built to Writer-Standards v1.0; naming pass complete; Spy Registry v1.1 |
| Session 14 | Ironthorn city blockout in UE 5.5 — World Partition, 6 districts, roads, ramps, wireframe colours |
| Session 14 | Writer submission pipeline — _Characters/, _Pending/, Lead Writer Workflow, Return Taxonomy (27 codes), Return Notice template; Primer v1.1 |
| Session 14 | Version control standard + automation — version_snapshot.py, approve_npc.py, snapshot.bat, approve_npc.bat; Versions/ folders across all asset types |

---

*Vault version 2.1 · Template v3.0 · Engine: Unreal 5.5*
