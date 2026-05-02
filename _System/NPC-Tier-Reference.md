---
system_doc: true
doc_type: "Tier Reference"
version: "1.0"
---

# NPC Tier Reference

Five tiers. One template that scales. The tier you assign determines which sections of the template you fill — and how much writer time the NPC deserves.

---

## Tier overview

| Tier | Name | Time to fill | Used for |
|------|------|-------------|---------|
| 1 | Background | ~10 min | Crowd NPCs, shopkeepers, one-line guards |
| 2 | Supporting | ~30 min | Side quest contacts, recurring minor characters |
| 3 | Named | ~1–2 hrs | Mission-critical characters, faction members |
| 4 | Major | ~3–4 hrs | Key story characters, faction lieutenants, named antagonists |
| 5 | Legendary | ~6–8 hrs | Faction leaders, the antagonist, world-secret holders |

---

## Tier 1 — Background

**Fill:** Quick Profile only (function, first impression, signature line, basic lie response).

**What they do:** Exist in the world convincingly. Give the player a sense of a populated, living city. Occasionally deliver information or gate access. They are not story — they are texture.

**Lie response at Tier 1:** One visible behavioural change. No decision map, no memory log. If the player lies to a Tier 1 NPC and gets caught, something simple happens — the NPC refuses to serve them, calls for a guard, or gives them wrong directions.

**Promotion path:** A Tier 1 NPC can be promoted if a designer realises during writing or playtesting that the character has story potential. Promote by filling the next tier's sections. Do not retroactively invent backstory that contradicts established texture.

---

## Tier 2 — Supporting

**Fill:** Quick Profile + Layer 1 Identity + Main Attributes (no subs) + one goal + basic lie response.

**What they do:** Provide quests, information, or services that matter to the player across multiple scenes. The player will see them more than once and should feel continuity.

**Lie response at Tier 2:** Connects to their main attributes — a high Cunning NPC at Tier 2 responds differently than a low one, even without sub-attributes. The response is still simple but character-specific.

**Key distinction from Tier 1:** The player can form a rudimentary relationship with a Tier 2 NPC. They have a history and a want. That's enough.

---

## Tier 3 — Named

**Fill:** Everything in Tier 2 + Sub-Attributes + two goals (primary and secondary) + full Decision Map + Memory Log header.

**What they do:** Drive or complicate plot arcs. The player should remember their name. They have opinions about the player that shift based on player behaviour.

**Lie response at Tier 3:** Full Decision Map applies. Their sub-attributes produce specific, documented behaviour when they catch a lie. The memory log starts recording.

**Key distinction from Tier 2:** They have a decision map and sub-attributes. The same lie told to two Tier 3 NPCs produces different responses because their subs are different.

---

## Tier 4 — Major

**Fill:** Everything in Tier 3 + Hidden Agenda + Private Truth + Full Memory Log + Dialogue Hooks + Dataview Queries.

**What they do:** Carry significant story weight. The player invests emotionally in these characters. Their reveal moments (hidden agenda surfacing, debt deployed, trust broken or earned) are story events.

**Lie response at Tier 4:** The full system is live. The NPC has a decision map, a memory log, leverage they might hold, and a hidden agenda that may make the lie interesting rather than just threatening. Their response is the most dramatically rich in the game.

**Key distinction from Tier 3:** The hidden agenda means their *goals* are also partially hidden from the player. The player is interacting with someone who has a private programme running beneath every conversation.

---

## Tier 5 — Legendary

**Fill:** Everything in Tier 4 + Second Identity Layer + Cross-Faction Influence Map.

**What they do:** Anchor the main story. Their reveal recontextualises significant portions of what the player has experienced. They know things no one else knows. They are not who they appear to be — at any level.

**Lie response at Tier 5:** The most complex in the game. A Tier 5 NPC may not even register a player lie as relevant — they are operating at a scale where individual lies are tactical details, not moral events. Their response, when it comes, will be structural. A door closing. A faction shifting. A previously stable relationship reclassifying.

**Key distinction from Tier 4:** The second identity layer means they have *two* sets of goals, two alignment readings, two histories. One of those histories contradicts the other. Both are real.

**How many to build:** Most games have 2–4 Tier 5 NPCs in the main story. More than that and the weight of revelation collapses — every second person can't be secretly someone else. Fewer than 2 and the main story lacks structural surprise.

---

## Promotion checklist

Before promoting an NPC from one tier to the next:
- [ ] Is there a story reason for them to carry more weight?
- [ ] Has the new tier's required content been fully written (not placeheld)?
- [ ] Do the new sections contradict anything established at the lower tier? If so, resolve the contradiction explicitly.
- [ ] Has the Writer's Notes section been updated to reflect the promotion?
- [ ] Has the status field been updated from Draft to In Review?

---

## Dataview — roster by tier

```dataview
TABLE npc_name, faction, alignment_public, alignment_true, cunning, status
FROM "NPCs"
SORT npc_tier DESC, cunning DESC
```

---

*[[README|Back to Index]] · [[NPC-Intelligence-System]] · [[Attribute-Reference]]*
