---
faction_name: "FACTION NAME"
alignment_bias: "Gray"
# Bias options: Light-V | Light-III | Light-I | Gray | Dark-I | Dark-III | Dark-V
faction_tier: 1
# 1 = Minor faction · 2 = Regional faction · 3 = Major faction · 4 = World-shaping faction
headquarters: "Location"
leadership: "NPC Name"
status: "Draft"
---

# Faction Name

## Overview
> REPLACE — one paragraph. What this faction is, what it wants, and how it operates publicly.

## True agenda
> REPLACE — what they actually want beneath the public mission.

## Alignment bias
> REPLACE — how this faction's alignment shapes how its NPCs react to the player. A Light-biased faction's NPCs are collectively more trusting of high-alignment players. A Dark-biased faction's NPCs are collectively more comfortable with low-alignment players.

## Key NPCs

| NPC | Tier | Role | Note |
|-----|------|------|------|
| REPLACE | — | — | — |

## Faction rank ladder

| Rank | Title | Requirements |
|------|-------|-------------|
| 1 | Initiate | Entry — no requirements |
| 2 | Pledged | 3 completed faction quests |
| 3 | Sworn | Alignment tier compatibility check |
| 4 | Warden | Trust score 7+ with a senior NPC |
| 5 | Champion | Major story contribution |
| 6 | Sovereign | Faction-specific unlock condition |

## Inter-faction relationships

| Faction | Relationship | Notes |
|---------|-------------|-------|
| REPLACE | REPLACE | REPLACE |

## Dataview — all NPCs in this faction

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score, status
FROM "NPCs"
WHERE faction = this.faction_name
SORT npc_tier DESC, cunning DESC
```

---

*[[../README|Back to Index]]*
