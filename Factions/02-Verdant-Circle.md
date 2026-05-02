---
faction_name: "The Verdant Circle"
alignment_bias: "Light-III"
faction_tier: 3
headquarters: "The Root Court — a living structure grown over centuries inside the oldest forest in the world; no map accurately depicts it"
leadership: "The Eldest — a rotating title held by the Circle member with the longest unbroken connection to the forest; current Eldest is Thyss of the Long Root"
status: "Draft"
---

# The Verdant Circle

## Overview
Druids, rangers, beast-speakers, and nature mystics bound by a single principle: the living world comes first. The Circle predates every other faction and holds no allegiance to any of them — it existed before the war between light and dark, and it expects to exist long after. They do not recruit; they are found. A player cannot apply to join the Circle; the Circle decides whether the player belongs. Their territory is not marked on any political map, but everyone knows not to harvest old-growth without permission.

## Internal moral tension
The Circle practises a form of sacrifice that it does not advertise. When a region of the natural world is corrupted beyond recovery, the Circle performs what it calls a Severance — a ritual that kills everything in that zone, plant and animal alike, to prevent the corruption from spreading. Settlements inside a Severance zone are not warned in advance. The calculation is arithmetical: some lives for many lives. The Circle believes this is correct. The survivors do not.

A second tension lives in the Eldest's lineage. Thyss of the Long Root is carrying a secret that predates her title: the Root Court itself is slowly dying. The forest consciousness that gives the Circle its power is weakening — not from corruption, but from age. The Circle has known for thirty years. No one outside the inner three has been told.

## True agenda
Keep the natural world alive long enough to survive whatever the other factions do to each other. The Circle is not neutral out of indifference — it is neutral out of strategic patience. If a dark faction winning means the forest survives, the Circle will let the dark faction win. If a light faction's expansion destroys a watershed, the Circle will burn their granaries. The calculation is always ecological, never moral.

## Alignment bias
The Circle does not bias toward alignment the way other factions do. They bias toward *coherence* — a player who is consistently Tier I or consistently Tier VII is readable and therefore acceptable. A Gray player is also acceptable; ambiguity is natural. What the Circle cannot tolerate is a player who performs light alignment while doing dark things — they read the deception through the forest's memory, not through dialogue checks. Hypocrisy, here, has mechanical consequences.

## Key NPCs

| NPC | Tier | Role | Note |
|-----|------|------|------|
| Thyss of the Long Root | 5 | The Eldest; faction anchor | Carries the secret of the dying Root Court |
| Warden Coln | 3 | Enforcement arm; handles Severances | Morally worn down; approaching disillusionment threshold |
| Speaker Ilen | 3 | Outward-facing; handles faction diplomacy | The only Circle member with genuine relationships outside the forest |
| CIRCLE SPY — embedded in Iron Dominion | 4 | Spy; cover: military cartographer | Monitoring Dominion expansion toward protected forest boundaries |

## Spy embedded here
**Incoming spy:** The Ashen Veil has placed one agent inside the Circle's outer ring — a ranger whose corruption is slow and invisible, designed to study how the Circle's ritual magic works.
- Cover identity: ranger-initiate, joined three years ago, unremarkable record
- True loyalty: Ashen Veil
- Burn condition: Warden Coln performs a Severance in the region where the spy was supposedly raised — the spy's emotional reaction is the tell. Player Perception rank 7+ catches it passively.

## Faction defection mechanics
**Player defection triggers:**
- Player participates in or enables destruction of a natural site the Circle has marked
- Player exposes the Severance programme to an outside faction without Circle permission
- Player alignment becomes consistently Tier V+ while holding Circle rank 3+

**Cost of leaving:** The forest remembers. The player loses all forest-navigation bonuses, beast-speaking access, and the Root Court becomes physically inaccessible — the paths close. Some of these can be reopened through acts of ecological restoration (specific quests), but Circle rank cannot be recovered in the same playthrough.

**Reputation carry-over:** +8 trust with Verdant Circle enemies (being cast out signals that you threatened them). −10 trust with Covenant (they see it as proof the player was never truly aligned with the light).

**NPC defection — Warden Coln:**
- Resentment threshold: 7 (tracks each Severance he participates in)
- Disillusionment threshold: 8 (tracks each time the Eldest justifies ecological killing with ecological logic)
- Tipping point: ordered to Severance a settlement he has a personal connection to
- Consequence: Coln leaves and takes institutional knowledge of Circle ritual magic — which becomes a resource either for the player or for the Ashen Veil, depending on who reaches him first

## Faction rank ladder

| Rank | Title | Requirements |
|------|-------|-------------|
| 1 | Found | Entry — the Circle approached the player first |
| 2 | Rooted | Complete a forest-based quest without harming non-threatening wildlife |
| 3 | Warden | Pass the Coherence reading — no alignment hypocrisy flags |
| 4 | Voice of the Circle | Trusted by both Thyss and Speaker Ilen simultaneously |
| 5 | Bound | Completed the main Circle arc; carries a piece of the Root Court's memory |
| 6 | Keeper | Unlocks only if the dying Root Court secret is discovered and the player chooses to help conceal it |

## Inter-faction relationships

| Faction | Relationship | Notes |
|---------|-------------|-------|
| Aureate Covenant | Tense alliance | The Circle refuses to acknowledge Covenant spiritual authority over natural sites |
| Gray Compact | Tolerated | Compact agents sometimes carry Circle messages in exchange for access rights; arrangement is strictly transactional |
| Iron Dominion | Hostile | Dominion expansion is the Circle's primary territorial threat |
| Ashen Veil | Active enemy | The Veil's necromantic corruption of soil and waterways is the Circle's definition of an existential threat |
| Crimson Throne | Avoided | The Throne's cruelty is a secondary concern; the Circle doesn't fight what it doesn't have to |
| Void Eternum | Feared | The Eternum wants to unmake existence; the Circle considers this the only genuinely unacceptable position |

## Dataview — all NPCs in this faction

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score, status
FROM "NPCs"
WHERE faction = "The Verdant Circle"
SORT npc_tier DESC, cunning DESC
```

---

*[[README|Back to Index]] · [[_System/Alignment-Spectrum]] · [[_System/Spy-Registry]]*
