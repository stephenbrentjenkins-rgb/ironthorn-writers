---
system_doc: true
doc_type: "Skill System"
version: "1.0"
---

# Deception & Perception Skills

Two skills that operate as a matched pair — one for lying, one for catching lies. Both live inside the alignment system and feed back into it.

---

## Deception

**What it does:** Determines the player's ability to lie convincingly. Controls which lie options appear in dialogue and the player's success probability against NPC perception thresholds.

**Alignment affinity:** Dark. Grows faster when alignment is dark. Dark alignment grants a check bonus.

**Skill ranks:** 1–10

| Rank | What unlocks |
|------|-------------|
| 1–2 | Basic misdirection options appear in dialogue |
| 3–4 | Deflect options available. Can attempt lies vs. low-threshold NPCs |
| 5–6 | Standard Lie options available against most NPCs |
| 7–8 | Hard lies vs. high-threshold NPCs become viable |
| 9 | Near-maximum deception. Only immune NPCs cannot be fooled |
| 10 | Maximum. Alignment dark bonus applies fully |

**Dialogue gate:** Lie options only appear in dialogue if the player's Deception rank meets the option's minimum. A player with Deception 4 will not see options marked "Deception 6+."

**Manipulate option:** Available only at Deception 9+ AND alignment Tier V–VII. No skill check — pure intimidation. Costs −3 alignment per use. Forces NPC compliance.

---

## Perception

**What it does:** Determines the player's ability to detect NPC lies. High Perception reveals hidden dialogue tags, surfaces secret NPC motivations, and can expose faction double-agents.

**Alignment affinity:** Light. Grows faster when alignment is light. Light alignment grants a check bonus.

**Skill ranks:** 1–10

| Rank | What unlocks |
|------|-------------|
| 1–2 | Occasional feeling that something is off. No specific information. |
| 3–4 | Player can attempt active Perception checks in suspicious conversations |
| 5–6 | Hidden NPC emotional states occasionally visible in dialogue tags |
| 7 | Passive mode activates — physical tells become readable without a check |
| 8 | Can detect most lies. Hidden NPC motivations surface in some conversations |
| 9 | Can expose faction double-agents with sufficient time and conversation |
| 10 | Maximum. Catches almost all lies. Some NPC secrets surface unbidden |

**Passive mode (Rank 7+):** The player begins seeing bracketed observations in NPC dialogue — *[Her hand moves to her pocket]*, *[He doesn't meet your eyes]*. These are physical tells that the NPC cannot suppress. They are information, not choices.

**Catching a lie:** When the player successfully catches an NPC lying, they gain +2 alignment toward light. The NPC's memory log is flagged.

---

## The skill check

When a player attempts a lie:

```
Success chance = base 50% + (Player Deception − NPC Perception Threshold) × 9%
+ Alignment modifier (dark = positive, light = negative for deception)

Capped: minimum 5%, maximum 95%
```

**Result — Success:** Lie believed. −2 alignment.
**Result — Failure:** Lie caught. −4 alignment. NPC Liar's Mark flag activates. NPC decision map triggers.

---

## The Liar's Mark

When a player fails a Deception check with an NPC:
- That NPC's `liar_mark_active` flag sets to true
- The NPC's decision map triggers (see [[NPC-Intelligence-System]])
- The mark persists for the rest of the game unless cleared
- High-cunning NPCs share the mark within their faction network (`faction_alert_sent` flag)

**Clearing the mark:** The player can return to the NPC and confess the lie. On confession: +3 alignment, mark clears, trust score increases, some previously-closed quest branches reopen.

---

## Gray path tension

A Gray player investing in both skills:
- Both grow at 75% of their normal rate
- No alignment bonus applies to either check
- Can maintain both pools simultaneously — useful for playing multiple factions
- Eventually tested: NPCs at alignment extremes (Tier I–II or Tier VI–VII) sense the ambiguity through extended interaction and apply pressure

The Gray deceiver — high Deception and Perception at Tier IV — is the hardest character to play and the one with the most story access, because they can read everyone and fool most. The cost is that no one fully trusts them, ever.

---

## Dialogue option structure

Every deception-adjacent dialogue option is tagged with:
- **Type:** Truth / Deflect / Lie / Manipulate
- **Minimum rank** (if gated)
- **Alignment tier requirement** (if gated)
- **Check difficulty** (shown or hidden, depending on player Perception rank)

Truth options are always available and always ungated. Choosing truth when a lie option was visible grants +1 alignment.

---

*[[README|Back to Index]] · [[Alignment-Spectrum]] · [[NPC-Intelligence-System]] · [[Attribute-Reference]]*
