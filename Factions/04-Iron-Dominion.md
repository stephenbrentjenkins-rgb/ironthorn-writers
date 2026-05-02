---
faction_name: "The Iron Dominion"
alignment_bias: "Dark-I"
faction_tier: 4
headquarters: "The Forged City — a military-industrial capital built over a conquered settlement; the original city's name has been officially stricken"
leadership: "Lord-Marshal Caedric Vane — a tactician who rose through pure military merit and has never lost a campaign"
status: "Draft"
---

# The Iron Dominion

## Overview
Warlords, soldiers, strategists, engineers, and administrators who have built the most functionally effective military state in the known world. The Dominion does not hate people — it categorises them: useful, manageable, or in the way. It conquered six kingdoms in forty years not through cruelty but through overwhelming organisational competence. The roads the Dominion builds are excellent. The laws it enforces are consistent. The occupied cities run more efficiently than they did before. The people in them are not free, and the Dominion considers this a separate question from whether they are well-administered.

## Internal moral tension
The Dominion's expansion is funded by a conscription programme that takes one person from every household in occupied territory — not for combat, but for labour. Infrastructure construction, mining, fortification. Mortality rates are documented, filed, and treated as acceptable losses in the Dominion's internal reporting. The officers who process these reports have desk jobs. They have families. They attend civic events. The system is designed so that no single person feels responsible.

A second tension: Lord-Marshal Vane. He is genuinely moral by his own lights. He believes order prevents suffering. He believes the Dominion's expansion will eventually produce a unified world that is safer than the fractured one. He is not wrong that the fractured world causes suffering. He is wrong about what his solution costs. And somewhere beneath his certainty is a doubt he has not yet named.

## True agenda
Complete unification of the known world under Dominion administration. Not for personal power — Vane genuinely believes this is the only way to prevent the kind of internecine wars that have historically killed millions. The Dominion's long-term plan is to absorb every other faction into a governance structure where their functions continue but their independence ends. The Covenant becomes state clergy. The Compact becomes a regulated intelligence bureau. The Circle becomes a conservation district.

## Alignment bias
Tier IV–V players are the Dominion's preferred client — pragmatic, self-interested, and not asking inconvenient moral questions. Tier I–III players can operate within the Dominion but are flagged as potential destabilisers; their quests will frequently put them in contact with what the system actually does. Tier VI–VII players are useful to the Dominion as irregular assets but are never trusted with anything structural.

## Key NPCs

| NPC | Tier | Role | Note |
|-----|------|------|------|
| Lord-Marshal Caedric Vane | 5 | Faction leader | His hidden doubt is the crack in the entire structure |
| Commander Syla | 3 | Field commander; seed NPC | Competent, loyal, beginning to ask what she is loyal to |
| Prefect Ornen | 4 | Civilian administration chief | Manages the labour programme; has never visited a work site |
| DOMINION SPY — embedded in Verdant Circle | 4 | Spy; cover: military cartographer | Monitoring Circle territory for expansion routes |

## Spy embedded here
**Incoming spy:** The Verdant Circle has placed one agent in the Dominion's cartography division. The Gray Compact has placed one agent in the Dominion's procurement office.
- Circle agent cover: Survey officer, 2 years in post, clean record
- Circle agent burn condition: Commander Syla runs a supply audit that reveals the agent's survey maps show terrain features near protected Circle forest in more detail than any official survey would reach — implying access. Player Perception rank 7+ catches it during a routine debrief scene.
- Compact agent cover: Procurement officer, 4 years in post, strong performance reviews
- Compact agent burn condition: A Dominion internal investigation into contract pricing anomalies gets close enough that the agent is forced to sabotage it — which leaves a trace. Auditor Vesh (if still in the Compact) would catch it immediately. Player Perception rank 8+ catches it without Vesh.

## Faction defection mechanics
**Player defection triggers:**
- Player exposes the labour programme mortality figures to an outside faction
- Player sabotages a Dominion military operation from inside
- Player sides with an occupied settlement during a resistance event

**Cost of leaving:** Dominion military designation as a hostile actor. Active pursuit by Dominion field units in controlled territory. All Dominion NPCs shift to hostile. Cannot be undone except through a major story resolution.

**Reputation carry-over:** +15 trust with any faction the Dominion is currently threatening. +8 trust with Covenant (shared institutional respect, even in opposition). −10 trust with Gray Compact (destabilising clients are bad for business).

**NPC defection — Commander Syla:**
- Resentment threshold: 7 (tracks each order she follows that results in civilian harm)
- Disillusionment threshold: 8 (tracks each time Vane's justifications stop matching what she sees in the field)
- Tipping point: ordered to suppress a settlement revolt she considers legitimate
- Consequence: Syla takes two full Dominion military units with her — the faction's military capability measurably degrades, which affects every subsequent Dominion-adjacent quest

**NPC defection — Lord-Marshal Vane:**
- This is a Tier 5 defection and requires specific story conditions
- Tipping point: the player presents him with the mortality reports for the labour programme, annotated with names — not statistics, but individual people, their ages, their families
- Consequence: Vane does not defect to another faction. He suspends the expansion programme and calls for an internal review. The Dominion fractures between factions that follow him and factions that remove him. The resulting civil conflict is its own story arc.

## Faction rank ladder

| Rank | Title | Requirements |
|------|-------|-------------|
| 1 | Conscript-Adjacent | Entry — player accepts a Dominion contract |
| 2 | Registered Asset | Two completed Dominion operations, payment accepted |
| 3 | Auxiliary Officer | Trust score 6+ with Commander Syla or Prefect Ornen |
| 4 | Field Officer | Major military contribution; Vane has acknowledged the player by name |
| 5 | Strategic Advisor | Vane's trust score 8+; player has access to classified expansion plans |
| 6 | Voice of the Marshal | Unlocks only if player helps Vane survive a coup attempt from within the Dominion |

## Inter-faction relationships

| Faction | Relationship | Notes |
|---------|-------------|-------|
| Aureate Covenant | Uneasy truce | Both want order; the Covenant insists on spiritual primacy the Dominion will not concede |
| Verdant Circle | Hostile | Dominion expansion is actively threatening Circle-protected territory |
| Gray Compact | Stable client relationship | The Compact provides intelligence; the Dominion pays and doesn't ask how |
| Ashen Veil | Active military conflict | The Veil's operations in Dominion-controlled territory are treated as insurgency |
| Crimson Throne | Cold war | The Throne is the only faction the Dominion considers a peer threat |
| Void Eternum | Unknown | Dominion intelligence has no profile on them; this is unusual and disturbing to Vane |

## Dataview — all NPCs in this faction

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score, status
FROM "NPCs"
WHERE faction = "The Iron Dominion"
SORT npc_tier DESC, cunning DESC
```

---

*[[README|Back to Index]] · [[_System/Alignment-Spectrum]] · [[_System/Spy-Registry]]*
