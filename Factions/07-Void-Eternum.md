---
faction_name: "The Void Eternum"
alignment_bias: "Dark-V"
faction_tier: 4
headquarters: "Nowhere fixed — they exist in the spaces between other factions' awareness"
leadership: "The Unwritten — a collective of four individuals who erased their own identities as proof of commitment to the doctrine; they are referred to only by position"
status: "Draft"
---

# The Void Eternum

## Overview
The Void Eternum is not a faction in the conventional sense. It has no territory, no economy, no diplomatic relationships, and no interest in power over others. It is a philosophical collective whose members share a single conviction: existence was a mistake, and the correct response to a mistake is correction. They seek to unmake reality — not from hatred, not from pain, not from any comprehensible motivation that other factions can model. They have simply concluded that nothing should have ever been. They are working toward the end of everything, calmly and without urgency, because they do not believe time is ultimately real either.

They are, structurally, the most dangerous faction in the world — not because of their capabilities, but because their goal cannot be negotiated. You cannot offer the Void Eternum something they want more than the end of everything. There is nothing.

## Internal moral tension
The Eternum is not monolithic. This is the thing no other faction understands about them. Within the Unwritten's collective, there is a growing argument — conducted in the abstract, careful language of people who have erased their names — about *method*. One faction within the Eternum believes the unmaking should be total and immediate. Another believes it should be gradual, beginning with the structures that cause suffering, as a mercy before the end. A third believes the unmaking should be optional — that existence should simply become unsustainable, and each consciousness should choose for itself whether to continue.

The mercy faction is, paradoxically, the most dangerous to the player — because its members can pass as sympathetic. They are trying to end everything, but they are trying to end it kindly. This is the only moral argument inside the Eternum, and it is the crack in the foundation.

A second tension: one Unwritten member is not fully committed. They joined for reasons that made sense at a specific moment of their life. That moment has passed. They cannot leave because they erased their identity to join; there is no self left to leave with. They are continuing because they do not know what stopping looks like anymore.

## True agenda
The end of everything. No timeline, no negotiation, no sub-goals. The Eternum does not want to win the war. It wants the condition in which war is possible to stop existing.

They have placed agents in every faction — not to control those factions, but to observe the exact mechanisms by which existence perpetuates itself. The agents report. The Unwritten catalogue. They are building a map of everything that would need to stop for nothing to exist.

## Alignment bias
The Eternum does not read player alignment the way other factions do. They read *coherence* — not between light and dark, but between what the player believes and how they act. A player who is consistent is interesting. A player who is contradictory is a useful data point about how consciousness resists its own conclusions. Tier VII players are the most common recruits, but the Eternum has recruited Tier I players before, when the player's experience of the world has produced the right kind of despair.

The Eternum does not try to recruit. It allows itself to be found.

## Key NPCs

| NPC | Tier | Role | Note |
|-----|------|------|------|
| The First Unwritten | 5 | Collective leader; the architect of the doctrine | The one who is no longer fully committed; this has not yet shown |
| The Second Unwritten | 5 | The mercy faction's voice | The most accessible and therefore the most deceptive |
| Quorum Member Issara (Ashen Veil) | 4 | Deep-cover agent; embedded in the Veil's Pale Quorum | The Eternum's most successful long-term operation |
| The Cataloguer | 3 | Field observer; compiles existence-mechanism reports | Does not know the full plan; knows enough to be dangerous |

## Spy embedded here
The Eternum does not have incoming spies in the conventional sense. No faction has successfully placed an agent inside the Eternum because no faction has a reliable profile of who the Eternum's members are. The Eternum's operational security is not active concealment — it is the structural invisibility of people who are not trying to win anything.

However: the Gray Compact suspects the Eternum exists and has tasked one field agent with building a profile. That agent has been missing for four months. Their dossier is still open.

**Player Perception rank 10 only:** At maximum Perception, the player begins noticing a pattern in the Cataloguer's movements — certain locations, certain intervals, certain questions that appear in different contexts with different faces. This is the first traceable evidence of the Eternum's observation network.

## Faction defection mechanics
The Eternum cannot be joined through conventional faction mechanics. There is no rank ladder. There is no trust score pathway. A player can only access Eternum content through specific story conditions — usually through the Ashen Veil's Issara storyline, or through following the Cataloguer's trail far enough.

**Affiliation:** A player who reaches Eternum affiliation has not joined — they have been designated as interesting. The Unwritten are watching. This opens specific story branches and closes others permanently.

**Leaving Eternum observation:** The player cannot opt out once designated. However, they can become strategically less interesting — by acting incoherently, by making choices the Eternum's models cannot predict. This takes sustained effort and the player will not be told it is working.

**NPC — The First Unwritten:**
- The internal doubt is not tracked through resentment or disillusionment scores — those are systems built on the assumption of attachment
- The doubt surfaces through specific dialogue choices the player can make: not by arguing against the doctrine, but by asking questions the doctrine has no answer for
- Tipping point: the player asks what the First Unwritten was called before. Not who they are now — what they were *called*. The answer, if it comes, is the beginning of the most consequential conversation in the game.

## Inter-faction relationships

| Faction | Relationship | Notes |
|---------|-------------|-------|
| Aureate Covenant | Observed | The Covenant has no doctrine for nihilism; the Eternum finds this interesting |
| Verdant Circle | Observed | The Circle's attachment to continuity is, to the Eternum, the purest expression of the problem |
| Gray Compact | One missing agent | The Compact knows something is there; they do not know what |
| Iron Dominion | Observed | Vane's model of order is, to the Eternum, a particularly determined form of denial |
| Ashen Veil | Infiltrated | The Eternum has a Quorum member; the Veil's threshold project is of specific interest |
| Crimson Throne | Observed | Sevayne's fear of death is the most comprehensible thing the Eternum has encountered; they find it almost sympathetic |

## Dataview — all NPCs in this faction

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score, status
FROM "NPCs"
WHERE faction = "The Void Eternum"
SORT npc_tier DESC, cunning DESC
```

---

*[[README|Back to Index]] · [[_System/Alignment-Spectrum]] · [[_System/Spy-Registry]]*
