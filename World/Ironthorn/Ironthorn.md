---
location_type: "City"
location_name: "Ironthorn"
region: "TBD"
controlling_faction: "Iron Dominion (garrison); no single faction controls the interior"
population: "Large — exact figures disputed; census has not been completed in eleven years"
access_tier: "Open — all districts accessible from the start except The Hollows"
status: "Draft"
---

# Ironthorn

## Overview
Ironthorn is a city that has learned to live with itself. It is large enough to contain factions that openly despise each other, old enough that its original purpose has been buried under three centuries of accumulation, and divided enough that no one faction has ever fully controlled it — though several have tried. The Iron Dominion garrison holds the Great Gate and patrols the main roads. Beyond that, the city governs itself in the way cities do: through money, habit, and the quiet understanding that some things are not asked about.

Visitors notice two things immediately. The first is the smell — coal smoke on the shadow side, something greener and older on the light side, and in the Ledger Row, nothing at all, as if commerce has no scent. The second is the light. The upper city has it. The lower city does not, not quite. The line between them is not a wall — it is a feeling, and it is somewhere in the middle of the city, and it moves slightly depending on who you ask.

Nobody official has ever explained the light. The city has stopped expecting them to.

## Design references
- **Structure:** Qeynos (EverQuest) — layered districts with distinct social function, faction guild presence, civic beauty over sub-city corruption. North/South division mapped to Upper/Lower Ironthorn.
- **Light-side tone:** Elwynn Forest (WoW) — cathedral light through old stone, warmth that feels earned, safety that has cracks in it if you look at the edges.
- **Shadow-side tone:** Duskwood (WoW) — not dramatic darkness, but tired darkness. The people here are pragmatic about what they live near. They have made their peace. The peace is uncomfortable.

## The divide
Ironthorn has no official Upper City or Lower City. The city's administrative documents refer only to districts. The residents use Upper and Lower constantly and have for generations. The divide is atmospheric first and architectural second — the streets on the shadow side are older, lower, built into a slight geographical depression that the upper city grew away from. This means the shadow side is also, technically, downstream of everything.

The line between sides runs roughly through the middle of Ledger Row, which is why the Gray Compact chose it as a home base. They sit exactly on the border and deal with both sides equally.

## Districts

| District | Side | Dominant faction | Primary function |
|----------|------|-----------------|-----------------|
| [[Sanctum-Ward]] | Upper | Aureate Covenant | Civic heart, main market, administration |
| [[Greenward]] | Upper | Verdant Circle | Parks, healing temples, old-growth grove |
| [[Ledger-Row]] | Divide | Gray Compact | Commerce, banking, information trade |
| [[Ashgate-Quarter]] | Lower | Ashen Veil (unofficial) | Old industry, ambient corruption |
| [[Wound-Market]] | Lower | Crimson Throne (indirect) | Black trade, pain-bonding contracts |
| [[The-Hollows]] | Beneath | Unknown | Sub-city; late-game access only |

## The Great Gate
The only official entry point to Ironthorn from the main road. Iron Dominion garrison — six soldiers at all times, commander on rotating eight-hour shifts. The garrison checks papers, collects a gate tax, and maintains a register of arriving visitors. The register is also sold to the Gray Compact on a weekly basis. This arrangement is not in any official document.

The garrison does not patrol the interior. They have an agreement with the city's districts: the Gate is theirs, everything past it is the city's problem. This agreement is enforced by the Dominion's continued need for Ironthorn's trade revenue and the city's continued need to not be garrisoned.

## The Hollows — access conditions
The Hollows are not accessible in the early game. Access requires one of the following:

- **Quest-driven:** Completion of the Gray Compact's missing-agent questline leads the player to a Hollows entrance beneath Ledger Row
- **Alignment-gated:** Tier VII players are approached by an unnamed contact who offers access without explanation
- **Perception-gated:** Perception rank 8+ causes the player to notice, in the Ashgate Quarter, that certain street-level grates are newer than the surrounding stonework — recent enough to have been installed to cover something, not to drain it
- **Faction-gated:** Reaching rank 4 in the Ashen Veil triggers a Hollows-related quest that opens one specific entrance beneath the Ashgate Quarter

Once accessed, the Hollows connect all districts beneath street level and contain content unavailable above ground.

## Faction presence summary

| Faction | Presence type | Location |
|---------|--------------|---------|
| Iron Dominion | Official garrison | Great Gate only |
| Aureate Covenant | Chapter house | Sanctum Ward |
| Gray Compact | Six unmarked offices | Ledger Row |
| Verdant Circle | Grove-keeper's station | Greenward |
| Ashen Veil | Unofficial; street-level influence | Ashgate Quarter |
| Crimson Throne | Indirect; runs the people who run it | Wound Market |
| Void Eternum | Unknown | Possibly the Hollows |

## Dataview — all NPCs in Ironthorn

```dataview
TABLE npc_name, npc_tier, faction, alignment_public, alignment_true, trust_score
FROM "NPCs"
WHERE location = "Ironthorn"
SORT npc_tier DESC
```

---

*[[../../README|Back to Index]] · [[_System/Alignment-Spectrum]] · [[_System/Spy-Registry]]*
