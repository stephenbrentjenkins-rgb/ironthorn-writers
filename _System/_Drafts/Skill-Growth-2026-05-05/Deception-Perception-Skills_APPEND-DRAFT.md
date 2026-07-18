---
system_doc: true
doc_type: "Skill System"
version: "1.1"
status: "Draft"
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

## Skill growth

How Deception and Perception ranks increase over play. The model is **percent-bar with exponentially scaling rank cost**: each rank shows a 0–100% bar, and the underlying point value of each percent grows with rank, so higher ranks take materially more play to fill even though the visual indicator is consistent.

This section closes the implementation gap left by the original v1.0 spec, which committed to "grows faster at dark/light alignment" but did not specify the unit of growth, the rate, or the anti-grind shape.

### The bar

Each rank between 1 and 10 has a hidden point requirement. The bar the player sees always reads 0–100% of the *current* rank's requirement.

| Rank transition | Points required (placeholder, tuning) |
|---|---|
| 1 → 2 | 10 |
| 2 → 3 | 25 |
| 3 → 4 | 55 |
| 4 → 5 | 100 |
| 5 → 6 | 165 |
| 6 → 7 | 255 |
| 7 → 8 | 380 |
| 8 → 9 | 555 |
| 9 → 10 | 800 |

Curve shape is exponential. Numbers are starting values and will be tuned during PoC playtest. Total points to max from rank 1: **2,345**.

### Growth events

Two events award progress: **sought-after success** and **failed-roll secondary check**.

**Sought-after success.** A check that resolved a registered intent. The dialogue system tracks an intent on every check the player initiates — *get past the guard*, *learn the password*, *talk down the price*, *catch the merchant lying about the manifest*. The check is sought-after if the post-check world state advanced that intent.

A successful Deception roll that landed the lie but produced no advance to the registered intent does not award. A successful Perception roll that caught a lie the player then ignored without registering a choice does not award. The check has to *do something*.

A sought-after success awards **+1 percentage point** of the current rank's bar.

**Failed-roll secondary check.** When a Deception or Perception check fails, a d100 fires. On a 1–10 result, the bar **loses 1 percentage point** of the current rank. On 11–100, the bar holds.

The failed-roll check is decoupled from the alignment system's failure consequences. Liar's Mark, alignment shifts, and NPC memory log writes still happen on the primary failure exactly as specified above. The secondary d100 only governs whether the player loses bar progress as well.

> **Pinned for future pass:** other systems may modify the failed-roll d100. The hook exists; the modifying system is not yet authored.

### Difficulty scaling

A sought-after success against a harder target awards more.

```
Award (in percentage points) =
    1 + max(0, NPC_perception_threshold − player_deception)    // for Deception
    1 + max(0, NPC_cunning − player_perception)                // for Perception
```

A Deception 4 player who lands a lie against a Perception-threshold-7 NPC and resolves the registered intent earns **4%** toward the next rank, not 1%. A Deception 8 player landing the same check against the same NPC earns the floor — **1%**.

This produces a natural curve where players are rewarded for reaching above their current weight, and where players coasting against trivial targets get the minimum. It also means rank growth slows organically as the player's skill matches the world's average difficulty.

### Anti-grind: diminishing returns

A player can repeatedly attempt checks against the same NPC, but progress diminishes within a single in-world day.

**Diminishing scope:** the same NPC + the same check type (Deception or Perception). Two different check types against the same NPC count separately. The same check type against two different NPCs counts separately.

**Diminishing curve (linear, placeholder):**

| Check N against (NPC, type) on this in-world day | Award multiplier |
|---|---|
| 1st | 100% |
| 2nd | 75% |
| 3rd | 50% |
| 4th | 25% |
| 5th and beyond | 0% |

Resets at the daily simulation tick (see [[Simulation-Tick]]).

The failed-roll d100 still fires on diminished checks — losing progress is not gated by the multiplier. A grinding player still experiences risk; they just stop earning reward.

### Alignment growth modifier

The "grows faster at dark/light alignment" rule from v1.0 is implemented by multiplying the awarded percent by an alignment-distance modifier:

| Alignment tier | Deception growth × | Perception growth × |
|---|---|---|
| Tier I — Radiant | 0.50 | 1.50 |
| Tier II — Steadfast | 0.75 | 1.25 |
| Tier III — Watchful | 0.75 | 1.00 |
| Tier IV — Unbound (Gray) | 0.75 | 0.75 |
| Tier V — Shadowed | 1.00 | 0.75 |
| Tier VI — Corrupted | 1.25 | 0.75 |
| Tier VII — Void-Touched | 1.50 | 0.50 |

This produces canon's Gray penalty (75/75 at Tier IV) without making any other tier worse than 0.50× in its disfavored skill. Light players can still grow Deception, just slowly. Dark players can still grow Perception. Maxing both is hardest at Gray, easiest at the extremes — but the extremes only ever grow one of them efficiently.

> **Pinned for future pass:** the Gray 75% rate is computed against the post-modifier base. We may want to revisit whether Gray should instead be a flat post-multiplier penalty applied after difficulty scaling. Decide during tuning.

### What does not award growth

- Truth options chosen with no Deception check involved. (Truth grants alignment, not skill growth.)
- Catching a lie via Perception passive mode at rank 7+ when the player takes no action with the information. Passive observation without engagement is not a check.
- Manipulate uses. Manipulate has no check; it is a flat alignment cost and an unconditional NPC compliance. Skill growth requires a roll.
- Checks against `deception_immune` NPCs. The check does not run; no growth, no failed-roll d100.
- Checks initiated outside the dialogue system (scripted scene-level perception cues, ambient detection events). These flag information for the player but do not feed the skill bar.

### Starting state and PoC scope

For the PoC, all PCs begin at:
- Deception: rank 1, 0% bar
- Perception: rank 1, 0% bar

No background, class, or origin grants a starting bonus. Background-driven starting modifiers are post-PoC.

The PoC's demonstration thread (see [[PoC-Scope]]) must produce at least one beat where a player's check growth is visible to the player — bar advances, rank-up notification fires, dialogue options unlock. Suggested vehicle: the demonstration thread's Compact-Veil exposure beat carries a Tier 3+ Perception check that, when caught, both reveals the asset and visibly advances the player's Perception bar.

### Pinned items — to be resolved before v2.0

These are deferred design calls. They do not block the v1.1 spec.

- **Gray growth computation order.** Whether the 75% Gray rate applies before or after difficulty scaling. Affects whether a Gray player overcoming a high-difficulty target gets 0.75 × N% or N% × 0.75.
- **Alignment-cost interaction.** Whether *using* Deception (winning or losing a check) shifts alignment in addition to the existing per-check alignment effects. Currently: success = −2 alignment, failure = −4 alignment. Question: does sustained Deception use compound alignment shift, or is the per-check shift sufficient?
- **External system modifier on failed-roll d100.** Hook exists; the modifying system is not yet authored. When that system lands, this section gets updated to reference it.
- **Rank-cost curve final tuning.** Numbers above are placeholders. Tune during playtest.
- **Diminishing-returns curve shape.** Currently linear (100/75/50/25/0). Exponential (100/50/25/12/6) might feel more like "grinding doesn't work" and less like "you can squeeze five attempts out of a vendor." Tune during playtest.
- **Diminishing scope per session vs. per in-world day.** Currently per in-world day, resetting at the daily tick. Sessions and days may not align cleanly for players who play in long stretches; revisit.

---

## Changelog

- **1.1 (Draft, 2026-05-05)** — Skill growth model added. Percent-bar with exponential rank cost; growth events defined as sought-after success (+1pp) and failed-roll secondary d100; difficulty scaling on success; linear diminishing returns by (NPC, check type) per in-world day; alignment growth modifier table replacing the implicit "faster at dark/light" rule. Six pinned items declared for v2.0.
- **1.0** — Initial spec. Two skills, ten ranks each, alignment affinity, success formula, Liar's Mark, Gray path penalty, dialogue gating.

---

*[[README|Back to Index]] · [[Alignment-Spectrum]] · [[NPC-Intelligence-System]] · [[Attribute-Reference]] · [[Simulation-Tick]] · [[PoC-Scope]]*
