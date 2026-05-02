---
faction_name: "The Aureate Covenant"
alignment_bias: "Light-V"
faction_tier: 4
headquarters: "The Sanctum Absolute — a fortified cathedral city on the highest plateau in the known world"
leadership: "The Eternal Triune — three High Arbiters who vote on all doctrine; currently deadlocked"
status: "Draft"
---

# The Aureate Covenant

## Overview
The Aureate Covenant is the world's oldest organised force for light — paladins, clerics, holy scholars, and inquisitors bound by a centuries-old doctrine called the Immaculate Record. Publicly, they stand for eradication of corruption, restoration of sacred sites, and the protection of the innocent. They are revered across the light-aligned settlements, feared by dark-aligned factions, and welcomed without question in most neutral cities. Their golden sigil is the most recognised symbol of institutional authority in the world.

## Internal moral tension
The Covenant executes people in secret. Not criminals. Not proven dark-agents. People who witnessed the wrong thing, asked the wrong question, or hold memories that contradict official doctrine. The Inquisitorial Sub-Order — officially a relic-hunting division — runs these operations. Most rank-and-file Covenant members have no idea. Those who find out are given a choice: take the oath of silence, or become a case file themselves.

A second tension: the Covenant's wealth. It is staggering. It was built on century-old confiscations from dark-aligned families — wealth that was never returned to survivors. The doctrine says it was consecrated in the name of the light. The survivors say it was theft.

The Covenant is not evil. It genuinely believes in what it does. That is what makes it dangerous.

## True agenda
Restore the old world order under Covenant authority — not just the purging of darkness, but the centralisation of all spiritual, judicial, and eventually political power under the Triune's rule. The Immaculate Record is meant to become world law. Dissent from within is the only thing currently slowing this down.

## Alignment bias
Tier I–III players are welcomed, trusted, and eventually shown things that go deeper than the public face — deeper than is safe to know. Tier IV players are watched. The Covenant does not trust neutrality; it reads ambiguity as potential corruption. Tier V–VII players are marked on sight by Inquisitorial agents; the question is never whether to act against them, but when.

## Key NPCs

| NPC | Tier | Role | Note |
|-----|------|------|------|
| High Arbiter Serevahn | 5 | Triune leader — the public face | Rumoured to privately oppose the Sub-Order |
| Inquisitor-Commander Leth | 4 | Runs the Inquisitorial Sub-Order | Knows where all the bodies are — literally |
| Brother Aldric | 3 | Rank-and-file cleric; seed NPC | Loyal, devout, beginning to suspect something is wrong |
| Sister Maren Voss | 4 | Archivist; seed NPC | Knows more than she should; survival strategy still TBD |
| COVENANT SPY — embedded in Gray Compact | 4 | Spy; cover: information broker | See Spy Registry |

## Spy embedded here
**Incoming spy:** One agent from The Gray Compact is embedded in the Covenant's administrative layer, monitoring the Triune's internal communications.
- Cover identity: junior records clerk, unremarkable
- True loyalty: Gray Compact
- Burn condition: Player reaches Perception rank 9 AND has completed at least two Covenant internal quests, OR the Triune's deadlock breaks and the new majority calls for a full loyalty audit

## Faction defection mechanics
**Player defection triggers:**
- Player discovers the Sub-Order's execution programme (quest: *What the Archivist Knows*)
- Player's alignment drops below Tier IV while holding Covenant rank 3+
- Player sides against the Covenant in a major story junction

**Cost of leaving:** Rank titles stripped. Sanctum access revoked. Inquisitorial mark applied — Covenant NPCs treat player as a threat, not a neutral. Cannot be cleared without a major story event.

**Reputation carry-over:** +10 trust with Verdant Circle (shared distrust of Covenant overreach). +5 trust with Gray Compact. −15 trust with Iron Dominion (the Dominion values institutional stability).

**NPC defection — Brother Aldric:**
- Resentment threshold: 8 (tracks each time doctrine contradicts what he witnesses)
- Disillusionment threshold: 7 (tracks each lie the Covenant tells him directly)
- Tipping point: discovering that a person he personally vouched for was executed by the Sub-Order
- Consequence: Aldric does not simply leave. He takes the Archivist's sealed records with him — which reshapes the information economy of the entire main quest

## Faction rank ladder

| Rank | Title | Requirements |
|------|-------|-------------|
| 1 | Aspirant | Entry — alignment Tier I–III |
| 2 | Confirmed | 3 completed Covenant quests |
| 3 | Sworn Warden | Alignment check — must be Tier I–II |
| 4 | Arbiter's Voice | Trust score 8+ with a named Covenant NPC |
| 5 | Champion of the Record | Complete the main Covenant arc |
| 6 | Arbiter-Elect | Unlock only if all three Triune members trust the player — currently impossible due to deadlock |

## Inter-faction relationships

| Faction | Relationship | Notes |
|---------|-------------|-------|
| Verdant Circle | Tense alliance | Shared light alignment, conflicting methods; the Circle refuses Covenant authority over natural sites |
| Gray Compact | Cold tolerance | The Covenant uses the Compact's intelligence networks while publicly condemning them |
| Iron Dominion | Uneasy truce | Both want order; they disagree on who should run it |
| Ashen Veil | Active war | The Covenant considers the Veil an existential abomination |
| Crimson Throne | Declared enemies | Public executions of Throne agents have become doctrinal events |
| Void Eternum | Unknown | The Covenant has no doctrine for true nihilism — it does not fit their framework |

## Dataview — all NPCs in this faction

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score, status
FROM "NPCs"
WHERE faction = "The Aureate Covenant"
SORT npc_tier DESC, cunning DESC
```

---

*[[README|Back to Index]] · [[_System/Alignment-Spectrum]] · [[_System/Spy-Registry]]*
