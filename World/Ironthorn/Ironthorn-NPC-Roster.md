---
doc_type: "NPC Roster"
location: "Ironthorn"
version: "1.5"
npc_count_defined: 42
npc_count_filed: 6
status: "Active — populating"
---

# Ironthorn — NPC Roster

Master list of all NPCs defined for Ironthorn. Organised by district and tier. NPCs with a linked file have been fully built. NPCs without a link are defined and queued.

Priority flags: **Watch** = threshold approaching; **Anchor** = faction/story anchor; **Spy** = double agent; **Story** = major story thread; **BG** = background/texture.

---

## Live roster — Dataview

```dataview
TABLE npc_tier, faction, location, alignment_public, alignment_true, trust_score, status
FROM "NPCs"
WHERE location = "Ironthorn" OR contains(location, "Ironthorn")
SORT npc_tier DESC, faction ASC
```

---

## Watch flags

```dataview
TABLE npc_name, faction, loyalty_resentment, idealism_disillusionment, cunning_paranoia
FROM "NPCs"
WHERE contains(location, "Ironthorn")
WHERE loyalty_resentment >= 5 OR idealism_disillusionment >= 5 OR cunning_paranoia >= 6
SORT loyalty_resentment DESC
```

---

## Full defined roster — by district

### Sanctum Ward — Upper city · Aureate Covenant

| Tier | Name | Role | Flag | File |
|------|------|------|------|------|
| 4 | Inquisitor-Commander Leth | Runs Sub-Order; Chapter House | Anchor | — |
| 4 | Torven Ashcroft | Minor noble / Throne spy; penitent caseload | Spy | — |
| 4 | Nelle Davar | Records clerk / Compact spy; Office of the Record | Spy | — |
| 3 | Brother Aldric | Cleric; spiritual director | Watch | [[../NPCs/Brother-Aldric]] |
| 2 | Solta Byrne | Innkeeper, The Hearthstone | Anchor | — |
| 2 | Ser Orvane | Watch Commander, Ward Station | Story | — |
| 2 | Registrar Celn Avour | Office of the Record (senior) | Story | — |
| 2 | Mirren | Alchemist, Mirren's Compound | BG | — |
| 1 | Arnath | General vendor, Arnath's Provisions | BG | — |

---

### Greenward — Upper city · Verdant Circle

| Tier | Name | Role | Flag | File |
|------|------|------|------|------|
| 3 | Grove-Keeper Sennath | Circle's Ironthorn representative | Anchor | — |
| 3 | Verath of the Still Hand | Head cleric; alchemist | Anchor | — |
| 2 | Iravel | Commons Clerk, Office of the Commons | Story | — |
| 2 | Sellen | Trade broker, Sellen's Exchange | BG | — |
| 2 | Compact Students *(x2)* | Junior Compact operatives; scholar cover | Spy | — |
| 1 | Perris | Innkeeper, The Canopy Rest | BG | — |
| 1 | Warden Duss | Greenward Watch officer | BG | — |
| 1 | Renn | Repair, Renn's Workbench | BG | — |

---

### Ledger Row — The divide · Gray Compact

| Tier | Name | Role | Flag | File |
|------|------|------|------|------|
| 4 | Factor Renne Saul | Senior Compact broker; The Exchange | Anchor | — |
| 3 | Auditor Vesh | Compact internal affairs; Contract Hall | Watch | [[../NPCs/Auditor-Vesh]] |
| 3 | Treasurer Vasken Oull | Office of the Treasury | Story | — |
| 2 | Orvan Sel | Barkeep, The Neutral Table | Anchor | — |
| 2 | Officer Maret | Row Patrol lead | Story | — |
| 2 | Oswin Creel | Cartographer / Circle spy; Cartography House | Spy | — |
| 2 | Doss | Alchemist, The Meridian Compound | BG | — |
| 2 | Hallum | Repair, Hallum's Bench | BG | — |

---

### Ashgate Quarter — Lower city · Ashen Veil (unofficial)

| Tier | Name | Role | Flag | File |
|------|------|------|------|------|
| 3 | Scholar-Physician Dael | Veil mid-rank; Quarter clinician | Watch | [[../NPCs/Scholar-Physician-Dael]] |
| 2 | Davan Ord | Forge master; repair annex | Watch | [[../NPCs/Davan-Ord]] |
| 2 | Maren Voss | Merchant / relic smuggler | Story | [[../NPCs/Maren-Voss]] |
| 2 | Cress | Render yard owner; trade broker | Story | — |
| 2 | Works Director Havel | Office of Works | Story | — |
| 2 | Pell | Unlicensed alchemist; Pell's Back Room | BG | — |
| 1 | Mossa | Lodging house proprietor | BG | — |
| 1 | Watch Lead Brenk | Quarter Watch | BG | — |
| 1 | Grundt | General vendor, Grundt's Corner | BG | — |

---

### Wound Market — Lower city · Crimson Throne (indirect)

| Tier | Name | Role | Flag | File |
|------|------|------|------|------|
| 4 | Petrov Seld | Luxury supplier / Compact dead-drop contact | Spy | — |
| 3 | Sevin | Tolerance Director; lower-city power broker | Anchor | [[../NPCs/Sevin]] |
| 3 | The Collector | Throne local administrator; Overseer's Seat | Anchor | — |
| 3 | Arcanist Vorell | Blood-bound arcanist | Story | — |
| 2 | Sel Harrow | Proprietor, The Restless House | Story | — |
| 2 | Oversight Lead Penra | Market Oversight guard lead | BG | — |
| 2 | Essa | The Mender; repair operator | Story | — |
| 2 | Kess | Alchemist, The Bound Still | BG | — |

---

### The Hollows — Beneath the city · Unknown

| Tier | Name | Role | Flag | File |
|------|------|------|------|------|
| 3 | Rynn Ashav | Missing Compact field agent; last known location | Story | — |
| 2 | The Guttered | Alignment-gated Hollows guide | Story | — |

---

## Build priority queue

| Priority | NPC | Reason |
|---------|-----|--------|
| 1 | ~~Maren Voss~~ | ✓ Complete |
| 2 | ~~Auditor Vesh~~ | ✓ Complete |
| 3 | ~~Scholar-Physician Dael~~ | ✓ Complete |
| 4 | ~~Davan Ord~~ | ✓ Complete |
| 5 | ~~Sevin~~ | ✓ Complete |
| 6 | Factor Renne Saul | Compact anchor; primary Compact contact |
| 7 | Grove-Keeper Sennath | Circle anchor; Root Court thread begins here |
| 8 | Solta Byrne | Hearthstone anchor; upper-city intelligence source |
| 9 | Essa | Wildcard; unreadable alignment needs designed reason |
| 10 | Orvan Sel | Neutral Table anchor; cross-faction meeting point |
| 11 | Torven Ashcroft | Throne spy; Aldric burn condition prerequisite |
| 12 | Nelle Davar | Compact spy; Triune deadlock prerequisite |

---

## Build log

| Session | NPCs filed |
|---------|-----------|
| Session 5 | Maren Voss, Brother Aldric, Commander Syla (seed NPCs) |
| Session 11 | Brother Aldric rebuilt to Writer-Standards v1.0 |
| Session 14 | Maren Voss rebuilt; Auditor Vesh, Scholar-Physician Dael, Davan Ord built |
| Session 14 | Naming pass — all 7 unnamed NPCs named; Spy Registry v1.1 |
| Session 14 | Sevin built — Tolerance Director; highest information density NPC in lower city |

---

*[[Ironthorn|Back to Ironthorn]] · [[../../_System/Writer-Standards|Writer Standards]] · [[../../_System/NPC-Intelligence-System|NPC Intelligence System]] · [[../../_System/Spy-Registry|Spy Registry]]*
