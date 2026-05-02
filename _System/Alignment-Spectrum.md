---
system_doc: true
doc_type: "Alignment System"
version: "2.0"
---

# Alignment Spectrum

The alignment spectrum is the engine of the NPC reaction system. Every NPC reads the player's current tier and responds accordingly — through dialogue, quest availability, pricing, secrets, and body language.

---

## The 7 tiers

| Tier | Name | Alignment | Description |
|------|------|-----------|-------------|
| I | The Radiant | Light-V | Selfless. Sacrifices for others without calculation. The world is better because you are in it, and you do not keep score. |
| II | The Steadfast | Light-III | Principled. Acts with consistent moral intention. Will not bend doctrine for convenience, but is not yet beyond understanding why others do. |
| III | The Watchful | Light-I | Cautiously good. Does the right thing when it costs something — but calculates the cost first. The last point where the world gives you the benefit of the doubt. |
| IV | The Unbound | Gray | No dominant alignment. Transactional, pragmatic, unreadable. Not without principles — but principles that serve no faction and answer to no doctrine. |
| V | The Shadowed | Dark-I | Morally compromised. Chooses self over others consistently. Not yet cruel — but the habit of self-interest has worn grooves that are getting harder to climb out of. |
| VI | The Corrupted | Dark-III | Feared. Causes harm deliberately and without significant guilt. Cruelty has become a tool, and the tool has become comfortable in the hand. |
| VII | The Void-Touched | Dark-V | Consumed. The darkness is no longer a choice — it is the condition. What remains is not evil so much as the absence of what was there before. |

---

## Design reference — mechanical precedents

These notes are for the designer. They explain why each tier behaves the way it does mechanically, grounded in how SWTOR and EverQuest handled equivalent alignment states.

**Tier I — The Radiant**
SWTOR Light V granted exclusive gear with a visible glow effect and unlocked the final light-side companion approval conversations. EverQuest's High Virtue path caused NPCs to offer aid unprompted — guards would step aside, priests would heal for free, certain quest items would be given rather than sold. This tier earns reverence, not just respect. NPCs do not treat the player as a customer; they treat them as something worth protecting.

**Tier II — The Steadfast**
SWTOR Light III opened companion dialogue lines where companions would share personal secrets — the relationship had moved from professional to trusted. EverQuest's Honorbound alignment gave faction bonuses with all lawful guilds and locked out certain rogue and shadowknight questlines permanently. This tier is trusted by institutions. They see the player as one of their own.

**Tier III — The Watchful**
SWTOR Light I was where most story choices landed by default for players making broadly good decisions without optimising for light points. EverQuest's Cautious Good band was the broadest alignment range — it covered most player characters who weren't actively trying to go dark. This tier is the last point where the world gives the player the benefit of the doubt. Beyond here, neutrality starts to look like a choice rather than a default.

**Tier IV — The Unbound**
SWTOR's Neutral path was harder to maintain than either extreme — choices that would move the player toward light or dark were more common than choices that held the centre. EverQuest's True Neutral was a rare deliberate choice that kept all faction options open at the cost of none trusting the player fully. This tier is the most flexible position and the loneliest one. Gray contacts are most comfortable here. Everyone else is watching.

**Tier V — The Shadowed**
SWTOR Dark I was where companion disapproval started compounding — companions would begin making comments about the player's choices rather than accepting them silently. EverQuest's Self-Serving alignment opened thief and mercenary questlines while costing temple access and triggering passive hostility from high-virtue NPCs. This tier is the point of no quiet return. Not because doors close, but because the player's reputation begins arriving before they do.

**Tier VI — The Corrupted**
SWTOR Dark III changed companion dialogue to deferential — companions stopped arguing and started complying. EverQuest's Darkbound path locked out all lawful faction quests permanently and opened necromancer and shadowknight content unavailable at any other alignment. Some EQ Darkbound NPCs would acknowledge the player with a lowered weapon rather than a greeting. This tier is where people stop trying to reach the player.

**Tier VII — The Void-Touched**
SWTOR Dark V gear was visually distinct — corrupted textures, cracked surfaces, wrong in a way that was hard to articulate. EverQuest's Consumed alignment was the rarest state: NPCs would flee on sight, but certain raid-tier enemies would not aggro, treating the player as a peer rather than prey. This tier closes more doors than it opens. But the ones it opens go somewhere no other tier reaches.

---

## How tiers shift

| Action | Point change |
|--------|-------------|
| Chose to lie (intent registered) | −1 |
| Lie succeeded | −2 |
| Lie caught by NPC | −4 |
| Chose truth when lie was available | +1 |
| Caught an NPC lying (Perception check) | +2 |
| Completed a selfless act with real cost | +3 to +5 |
| Caused deliberate harm to an innocent | −3 to −5 |
| Confessed a previous lie to the NPC | +3 |
| Used Manipulate dialogue option (Tier V+ only) | −3 |

---

## NPC reaction by tier

**Tier I — The Radiant:** Light NPCs revere. Gifts offered freely. Dark NPCs are uneasy. Prices drop without asking.

**Tier II — The Steadfast:** Light NPCs trust readily. Secrets shared. Dark NPCs are cautious but deal.

**Tier III — The Watchful:** Cooperative across the board. No deference, no suspicion. Most doors open.

**Tier IV — The Unbound:** Transactional. NPCs deal but don't trust. Gray zone contacts most comfortable here.

**Tier V — The Shadowed:** Civilians uncomfortable. Light NPCs step back. Dark NPCs become deferential.

**Tier VI — The Corrupted:** Light NPCs will not deal willingly. Dark NPCs offer service. Some quest lines close permanently.

**Tier VII — The Void-Touched:** Light NPCs flee. Dark NPCs kneel. Some doors open that cannot open any other way. Some close forever.

---

## The Gray path

Tier IV is a genuine playstyle, not a waiting room. A Gray player has access to both faction networks, can invest in both Deception and Perception (at 75% growth rate), and is watched by everyone because trusted by no one completely. The Gray path is the hardest to maintain. It is also the most flexible.

The Gray player's tension compounds over time: NPCs at alignment extremes (Tier I–II or Tier VI–VII) sense the ambiguity through extended interaction and apply pressure. Eventually, everyone asks the Gray player to choose. The game never forces the answer. But it makes the question louder.

---

## Skill interaction

- Deception grows faster at dark alignment. Perception grows faster at light alignment.
- Dark alignment grants a bonus modifier to Deception checks.
- Light alignment grants a bonus modifier to Perception checks.
- Modifiers scale with distance from Tier IV — the more extreme the alignment, the larger the modifier.
- Gray players (Tier IV) receive no alignment modifier to either skill. Both grow at 75% of their normal rate.

---

## Faction alignment bias — quick reference

| Faction | Comfortable tier range | Notes |
|---------|----------------------|-------|
| Aureate Covenant | I–III | Tier IV watched; Tier V–VII marked on sight |
| Verdant Circle | Any — if coherent | Hypocrisy flagged regardless of alignment |
| Gray Compact | IV | Principled players unpredictable; extreme dark players dangerous |
| Iron Dominion | IV–V | Tier I–III flagged as destabilisers |
| Ashen Veil | V–VII | Tier I–III considered philosophically confused |
| Crimson Throne | VI–VII | Tier V tested before trusted; Tier I–II suspect |
| Void Eternum | Any — if coherent | Reads consistency, not morality |

---

*[[README|Back to Index]] · [[Deception-Perception-Skills]] · [[NPC-Intelligence-System]] · [[Factions/01-Aureate-Covenant]]*
