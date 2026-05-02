---
system_doc: true
doc_type: "Connection Map"
version: "1.0"
---

> [!warning] This document is from a previous version of the world and is being rewritten.
> The faction names ("Gray Market", "Dawnward Order", "Iron Compact") and the city ("Ashford") referenced below are no longer canon. Current factions are listed in `Factions/`. The current city is Ironthorn. Do not use this document as reference until it has been rebuilt with current NPCs and locations.
>
> *Flagged: 2026-05-01*

---


# Cross-NPC Connection Map

Ashford is a small enough city that its key NPCs are aware of each other — directly or indirectly. This document maps those connections and flags where they create story opportunities or risks.

---

## Current NPC roster

| NPC | Faction | Tier | Location |
|-----|---------|------|---------|
| [[../NPCs/Maren-Voss\|Maren Voss]] | The Gray Market | 4 | Ashford Bazaar |
| [[../NPCs/Brother-Aldric\|Brother Aldric]] | The Dawnward Order | 4 | Sanctuary of Returning Light |
| [[../NPCs/Commander-Syla\|Commander Syla]] | The Iron Compact | 4 | Ashford Garrison |

---

## Known connections

### Maren Voss ↔ Commander Syla
**Type:** Indirect — structural
Syla controls the garrison and trade road security. Maren's smuggling operation depends on routes that Syla could shut down at any moment. Syla almost certainly knows something is moving through the eastern bazaar that shouldn't be. Whether she has chosen to act on it, or is holding it for a more useful moment, is undefined — **this is a story decision to make.**

**Story potential:** Syla could be the reason the debt never clears — if she is quietly tipping off Drael that his asset in the bazaar is being watched, keeping both parties dependent and manageable. Or she may be entirely unaware. Either version works. Choose before writing Syla's full intelligence log.

---

### Maren Voss ↔ Brother Aldric
**Type:** Community — she attends the sanctuary occasionally
Aldric ministers to the lower district. Maren's stall is in the bazaar, adjacent. She is not part of his congregation but she has donated to the sanctuary twice — practically, not spiritually. He has noticed her. He does not know what she is. She knows he is trustworthy and has considered approaching him — but approaching a priest with what she carries is a significant risk.

**Story potential:** If the player builds trust with both NPCs, Maren and Aldric could become aware of each other through the player as intermediary. They have complementary information — her evidence against Drael, his evidence against Bishop Voth. Whether those two threads connect is **a world design decision.** If they do, it opens a major cross-faction story arc.

---

### Brother Aldric ↔ Commander Syla
**Type:** Institutional — Order chaplain vs. Garrison command
The Dawnward Order provides chaplaincy to the garrison. Aldric occasionally ministers there. Syla tolerates the arrangement professionally. She has assessed him: not a threat, probably useful as a community intelligence asset if cultivated, not worth the effort of cultivating.

**Story potential:** Syla knows about the senior priests' investigation into shadow-touched sympathisers — it overlaps with garrison security concerns. She may know things about Bishop Voth's operation that Aldric does not. Whether she would share them, and at what price, is **undefined and open.**

---

## Faction tensions

| Faction pair | Relationship | Current tension |
|-------------|-------------|----------------|
| Gray Market ↔ Iron Compact | Tolerated coexistence | Garrison controls trade routes the Gray Market depends on |
| Dawnward Order ↔ Iron Compact | Institutional partnership | Garrison chaplaincy gives Order leverage; Syla resents the arrangement |
| Dawnward Order ↔ Gray Market | No formal relationship | Aldric knows smugglers use the sanctuary district as a waypoint and has chosen not to report it |

---

## Open story questions — flag for design team

- Does Syla know about Maren's evidence against Drael?
- Does Drael have an asset inside the garrison? If so, is it above or below Syla's level of awareness?
- Are the Greywood massacre (Aldric's thread) and the Ember Consortium (Maren's thread) connected at any level?
- What is Bishop Voth's relationship to the Iron Compact? Is he an ally of the Crown-loyal officers Syla is removing?
- Does the player's faction choice affect which of these connections become accessible?

---

## Dataview — all Ashford NPCs

```dataview
TABLE npc_name, npc_tier, faction, alignment_true, cunning, trust_score
FROM "NPCs"
WHERE location = "Ashford" OR contains(location, "Ashford")
SORT cunning DESC
```

---

*[[README|Back to Index]] · [[NPC-Intelligence-System]] · [[../NPCs/Maren-Voss|Maren Voss]] · [[../NPCs/Brother-Aldric|Brother Aldric]] · [[../NPCs/Commander-Syla|Commander Syla]]*
