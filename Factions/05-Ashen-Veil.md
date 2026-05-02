---
faction_name: "The Ashen Veil"
alignment_bias: "Dark-III"
faction_tier: 4
headquarters: "The Hollow Conclave — a network of underground sanctuaries; the primary chamber is beneath a city that does not know it is sitting on one"
leadership: "The Pale Quorum — five Arch-Necromancers who govern by consensus; one of the five is a double agent"
status: "Draft"
---

# The Ashen Veil

## Overview
Necromancers, shadow priests, death-cultists, and undead-binders who have built an entire theological framework around the argument that death is not an ending — it is a resource. The Veil does not worship death. It disagrees with it. Their doctrine holds that the boundary between living and dead is an artificial constraint, and that the natural state of consciousness is continuity without terminus. They are correct that their rituals work. The question the world is asking is what the cost is, and the Veil considers that question provincial.

They are not cartoonish monsters. Their rank-and-file members are scholars, physicians who couldn't stop their patients from dying, parents who couldn't accept a child's death, soldiers who watched too many people disappear. The Veil offers something no other faction offers: the dead do not have to stay dead. This is not a small thing.

## Internal moral tension
The Veil's resurrection process is not free. It requires a life — not necessarily a human life, but a life with sufficient vital energy. In the early days, this was animals. Then it became criminals. Then it became people the Veil decided were expendable. The Arch-Necromancers have never made this explicit in doctrine; it is understood, not codified. The scholars at the lower ranks do not know where the energy comes from. Some of them have started to wonder.

A second tension: the dead the Veil raises are not entirely themselves. Something is different. The Veil calls it stabilisation drift and classifies it as a minor side effect. The raised are aware of the drift. Some of them consider it a form of ongoing theft.

## True agenda
Breach the threshold between life and death permanently — not just for individuals, but as a physical law of the world. If successful, death becomes optional. The Quorum knows this will destroy the ecological balance of the living world, because they have modelled it. They have decided the result is acceptable. The living world as it currently exists would end. Something else — something that does not die — would replace it.

## Alignment bias
Tier V–VII players have full access and are treated with genuine collegial respect — the Veil reads dark alignment not as wickedness but as a realistic understanding of how the world works. Tier IV players are recruited cautiously; the Veil believes Gray alignment is a transitional state and that everyone eventually chooses. Tier I–III players are considered philosophically confused and are monitored rather than trusted; the Veil genuinely doesn't understand why someone with power would choose limitation.

## Key NPCs

| NPC | Tier | Role | Note |
|-----|------|------|------|
| Arch-Necromancer Vorath | 5 | De facto Quorum leader; the one who finished the threshold model | Believes he is doing the right thing; the model is correct |
| Quorum Member Issara | 4 | The double agent inside the Quorum | See Spy Registry; her loyalty is to the Void Eternum |
| Scholar-Physician Dael | 3 | Mid-rank Veil member; beginning to ask about the energy source | Approaching disillusionment threshold |
| VEIL SPY — embedded in Verdant Circle | 4 | Spy; cover: ranger-initiate | Studying Circle ritual magic for threshold applications |

## Spy embedded here
**Incoming spy:** The Aureate Covenant has placed one agent in the Veil's lower scholarly ranks, documenting ritual methods for potential counter-measures.
- Cover identity: a necromantic scholar who "defected" from a smaller dark cult three years ago
- True loyalty: Aureate Covenant Inquisitorial Sub-Order
- Burn condition: Scholar-Physician Dael begins asking questions about the energy source and the Covenant agent provides a too-convenient redirect — which is itself suspicious. Player Perception rank 8+ reads the redirect as protective rather than curious.

## Faction defection mechanics
**Player defection triggers:**
- Player learns about stabilisation drift and exposes it publicly
- Player destroys a Veil threshold experiment at a critical story juncture
- Player's alignment rises to Tier III+ while holding Veil rank 3+

**Cost of leaving:** The Veil places a Marked designation on defectors — not a military threat, but something quieter. Raised dead begin appearing in the player's path, asking questions. The Veil wants to know what the player knows and who they've told. It is deeply unsettling and escalates if ignored.

**Reputation carry-over:** +12 trust with Aureate Covenant. +8 trust with Verdant Circle. −20 trust with Veil permanently.

**NPC defection — Scholar-Physician Dael:**
- Resentment threshold: 6 (tracks each time his questions about the energy source are deflected)
- Disillusionment threshold: 8 (tracks each raised subject he interviews whose drift has worsened)
- Tipping point: he performs a resurrection and recognises the energy signature — it is someone he knew
- Consequence: Dael does not fight the Veil. He begins documenting everything and looking for somewhere to send it. The player is the first person he trusts enough to approach.

## Faction rank ladder

| Rank | Title | Requirements |
|------|-------|-------------|
| 1 | Shade | Entry — alignment Tier IV or lower |
| 2 | Initiate of the Veil | Complete an introduction to Veil doctrine ritual |
| 3 | Scholar of Ash | Assist in a sanctioned resurrection; alignment Tier V or lower |
| 4 | Veil-Bound | Trust score 7+ with a Quorum member |
| 5 | Threshold Keeper | Completed major Veil arc; permitted in the Hollow Conclave's inner chamber |
| 6 | Pale Voice | Unlocks only if player assists with threshold model completion AND alignment is Tier VI–VII |

## Inter-faction relationships

| Faction | Relationship | Notes |
|---------|-------------|-------|
| Aureate Covenant | Active war | The Covenant considers the Veil an existential abomination; the Veil considers the Covenant philosophically obsolete |
| Verdant Circle | Active enemy | Veil corruption of soil and waterways is the Circle's primary environmental threat |
| Gray Compact | Transactional | The Compact sells information to the Veil at a significant risk premium |
| Iron Dominion | Active military conflict | The Dominion treats Veil operations in its territory as insurgency |
| Crimson Throne | Cold alliance | Both are dark-aligned; they do not cooperate, but they do not fight |
| Void Eternum | Unknown — and this is wrong | One Quorum member is a Void Eternum agent; the relationship is not what it appears |

## Dataview — all NPCs in this faction

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score, status
FROM "NPCs"
WHERE faction = "The Ashen Veil"
SORT npc_tier DESC, cunning DESC
```

---

*[[README|Back to Index]] · [[_System/Alignment-Spectrum]] · [[_System/Spy-Registry]]*
