---
system_doc: true
doc_type: "Skill System"
doc_name: "Skill Growth"
version: "1.0"
status: "Draft"
---

# Skill Growth

How player skills increase over play. This document defines the growth mechanic for Deception and Perception, the only two player skills in the canon today. The mechanic is designed to extend cleanly to additional skills if and when they're added post-PoC.

The parent system is `Deception-Perception-Skills.md` v1.0, which committed to the rank ladder, the dialogue-check formula, the Liar's Mark, the alignment affinities, and the Gray path penalty — but left "how does growth actually happen" implicit. This document closes that gap.

Read alongside `Alignment-Spectrum.md` (the source of the growth-rate modifier), `NPC-Intelligence-System.md` (the source of the registered-intent context that defines a sought-after check), and `Simulation-Tick.md` (the daily reset boundary for grind-prevention).

---

## Why a separate doc

Two reasons growth lives in its own file rather than appended to the parent skills doc:

1. **Growth is a mechanic, not a skill.** It applies the same way to Deception and to Perception, and will apply the same way to any future player skill. Putting it in the skills doc embeds a mechanic inside content; pulling it out lets the mechanic evolve independently from the skills it governs.

2. **Tuning will be heavy and ongoing.** The numbers in this document — rank cost curve, diminishing returns curve, alignment modifier table — will be revised throughout PoC playtest and again during the full build. Isolating tuning surfaces in one file keeps the core skills doc stable.

If a third or fourth player skill is authored later, that skill's doc will reference *this* doc's mechanic and only need to specify its own rank-unlock table.

---

## The bar model

Each rank, 1 through 10, is represented to the player as a 0–100% progress bar. The bar fills as the player makes successful, intent-resolving checks; it can lose progress on failed checks via a secondary d100; it advances to the next rank when it reaches 100%.

Beneath the visible bar, each rank has a **point requirement** that grows exponentially. Rank 2 fills quickly because it needs few points; rank 9 fills slowly because each percentage of the visible bar represents many more underlying points.

The player sees one consistent UI element across their entire progression. The mechanical curve is hidden by design: visible progression at high ranks should feel earned, not algorithmic.

### Rank cost curve

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

Total points to reach rank 10 from rank 1: **2,345**.

These are starting values. The shape is exponential. Tuning during PoC playtest will determine whether the curve rises faster or slower; the *shape* (each rank materially more expensive than the last) is the design commitment.

---

## Growth events

Two events change the bar: **sought-after success** and **failed-roll secondary check**.

### Sought-after success

A skill check that produced a registered-intent advance.

The dialogue system attaches an intent to every check the player initiates: *get past the guard*, *learn what the merchant is hiding*, *talk down the price*, *catch the priest in a lie about the gate registry*. Intents are registered when the player selects a check option. The check is **sought-after** if the post-resolution world state advanced the registered intent.

A successful Deception check that landed the lie but produced no advance against the registered intent does not award. This protects the mechanic against players gaming growth by lying for no reason, and it also prevents incidental success — landing a lie the engine considered low-stakes — from accidentally rewarding the player as much as a hard-fought win.

A successful Perception check that caught the NPC's lie but where the player took no in-world action with the information does not award either. Catching the lie is half the check; doing something with it is the other half.

Award on sought-after success: **+1 percentage point** of the current rank's bar, before difficulty scaling.

### Failed-roll secondary check

When a Deception or Perception primary check fails, a separate d100 fires after the primary failure resolves.

- **1–10 on the d100:** the bar **loses 1 percentage point** of the current rank.
- **11–100 on the d100:** the bar holds.

This secondary roll does not interact with Liar's Mark, alignment shifts, NPC memory writes, or any of the other primary-failure consequences. Those are governed by the parent doc and fire on every primary failure regardless of the secondary roll.

The secondary roll exists so failure has texture. Most failed checks are remembered by the world (Liar's Mark, alignment shift, NPC suspicion) but leave the player's skill development intact. Some — one in ten — also nick the player's progress, modeling the way a sharp failure can shake confidence.

> **Pinned for future pass:** Other systems may modify the failed-roll d100 — for example, a future Resolve or Composure stat that lets the player resist the bar loss. The hook exists. The modifying system is not yet authored.

---

## Difficulty scaling

A sought-after success against a harder target awards more.

```
Award (in percentage points) =
    1 + max(0, NPC_perception_threshold − player_deception)    // for Deception
    1 + max(0, NPC_cunning − player_perception)                // for Perception
```

A Deception 4 player who lands a lie against a Perception-threshold-7 NPC and resolves the registered intent earns **4 percentage points** toward the next rank. A Deception 8 player landing the same check against the same NPC earns the floor — **1 percentage point**. The harder the climb, the steeper the reward.

This scaling does the same work as the parent doc's success-chance formula, in the opposite direction: the success formula uses skill-vs-threshold margin to determine *whether* the check works; the growth formula uses the same margin to determine *how much it teaches you*.

Scaling produces three useful effects:

- Players are organically incentivized to attempt harder checks rather than coast.
- Late-game growth slows naturally as player skill matches the world's average difficulty, without needing an explicit late-game cap.
- A Tier 3+ NPC encounter feels heavier in growth as well as in narrative weight.

---

## Anti-grind: diminishing returns

A player can repeatedly attempt checks against the same NPC, but the bar award diminishes within a single in-world day.

**Diminishing scope.** The diminishing rule applies per (NPC, check type) per in-world day. Diminishing on Deception against Brother Aldric does not affect Perception against Aldric, and does not affect Deception against any other NPC. The two halves of the rule are deliberate: the player should be able to learn from a single difficult NPC across both check types in the same day, and the player should be able to practice the same check type against a varied roster.

**Diminishing curve (linear, placeholder):**

| Check N against (NPC, check type) on this in-world day | Award multiplier |
|---|---|
| 1st | 100% |
| 2nd | 75% |
| 3rd | 50% |
| 4th | 25% |
| 5th and beyond | 0% |

Reset boundary is the daily simulation tick (see `Simulation-Tick.md`). At the tick, all (NPC, check type) counters return to zero.

**Important:** the diminishing rule applies to *award*, not to *risk*. The failed-roll d100 fires on every primary failure regardless of how many times the player has attempted that (NPC, check type) today. A grinding player at zero award still risks losing bar progress. The system rewards engagement, not repetition, but it does not stop punishing failure.

> **Pinned for future pass:** Curve shape is currently linear. Exponential decay (100/50/25/12/6) might better model "grinding doesn't work" and less obviously cap at five attempts. Tune during playtest. Reset boundary is currently per in-world day; revisit if real-world session lengths produce reset patterns that feel arbitrary.

---

## Alignment growth modifier

The parent doc commits to "Deception grows faster at dark alignment" and "Perception grows faster at light alignment" without specifying a curve. This document supplies one.

After difficulty scaling, the awarded percent is multiplied by the alignment-distance modifier:

| Alignment tier | Deception growth × | Perception growth × |
|---|---|---|
| Tier I — Radiant | 0.50 | 1.50 |
| Tier II — Steadfast | 0.75 | 1.25 |
| Tier III — Watchful | 0.75 | 1.00 |
| Tier IV — Unbound (Gray) | 0.75 | 0.75 |
| Tier V — Shadowed | 1.00 | 0.75 |
| Tier VI — Corrupted | 1.25 | 0.75 |
| Tier VII — Void-Touched | 1.50 | 0.50 |

This table preserves the canon Gray penalty (75/75 at Tier IV from the parent doc) and produces a smooth growth curve as the player's alignment moves through tiers. The table is intentionally not symmetric across all values because the lore isn't symmetric: the most light-extreme character should still be able to grow some Deception, just slowly, because they're committed to a path that rarely lies; the most dark-extreme character should similarly be able to grow some Perception, just slowly.

The full multiplier — including the failed-roll d100, difficulty scaling, and diminishing returns — applies as:

```
award_pp =
    base_award_pp                 // 1 + difficulty bonus
    × alignment_modifier          // table above
    × diminishing_multiplier      // 1.00, 0.75, 0.50, 0.25, 0.00
```

> **Pinned for future pass:** Whether the alignment modifier should apply before or after difficulty scaling. Currently after, which means Gray players get the difficulty climb at full bonus and then take their 0.75× penalty; alternative is to apply alignment first, which would dampen Gray climbs equally regardless of difficulty. Tune during playtest.

---

## Cases that do not award growth

These situations look like growth events but produce no bar movement.

- **Truth options.** Choosing truth in dialogue grants alignment, not skill growth. There is no check on truth.
- **Passive Perception observation.** At rank 7+, the player sees physical tells in dialogue tags without rolling. Tells are information. If the player does nothing with the information — does not initiate a check, does not register an intent — there is no bar movement.
- **Manipulate uses.** Manipulate at Deception 9+ Tier V–VII has no check. It is a flat alignment cost and an unconditional NPC compliance. No roll, no growth.
- **Checks against `deception_immune` NPCs.** The check does not run. The dialogue surface should not even offer a Deception option against immune NPCs (the gate is enforced upstream).
- **Scripted scene-level perception cues.** Ambient detection events that flag information for the player without rolling against an NPC's threshold do not feed the skill bar.

---

## Starting state

For the Proof of Concept, all PCs begin at:

- Deception: rank 1, 0%
- Perception: rank 1, 0%

No background, class, origin, or character-creation choice grants a starting modifier. Background-driven starting bonuses are post-PoC and will be specified in a future PC sheet document.

---

## Demonstrating growth in the PoC

The PoC must surface growth visibly to the player. The mechanic, however well-tuned, fails its design purpose if the player can't tell it's working.

Three legibility surfaces support this:

- **The bar itself.** Visible in the dialogue UI when relevant; visible in the character sheet always. Animates on award.
- **Rank-up notification.** A first-class moment when the bar fills. Includes the unlock summary from the parent doc's rank-ladder tables.
- **Dialogue option unlocks.** New options become visible the next time the player enters a dialogue context that gates them. The player should encounter the unlock organically — not through a menu they have to consult.

The PoC demonstration thread (see `PoC-Scope.md`) is the natural vehicle. The Compact-Veil exposure beat carries at least one Tier 3+ Perception check; a player who catches the lie should experience all three legibility surfaces in succession (bar advance, possible rank-up, possible new dialogue option in the follow-up scene).

---

## Pinned items — to be resolved before v2.0

These design calls are deferred. They do not block the v1.0 spec or PoC implementation; they will need answers before the full game.

- **Gray growth computation order.** Whether the alignment modifier applies before or after difficulty scaling. Affects whether a Gray player's hard-target wins are dampened smoothly or proportionally.
- **Alignment-cost interaction with sustained skill use.** The parent doc has per-check alignment effects (success = −2, failure = −4). Open question: does sustained Deception use compound alignment shift beyond per-check, or is the per-check shift sufficient?
- **External-system modifier on the failed-roll d100.** Hook is reserved. The modifying system (likely a Resolve or Composure stat) is not yet authored.
- **Rank-cost curve final tuning.** Numbers are placeholders.
- **Diminishing-returns curve shape.** Currently linear; exponential is a strong alternative.
- **Diminishing-returns reset boundary.** Currently per in-world day. Sessions and days may not align well for all play patterns.
- **Background-driven starting modifiers.** Out of scope for PoC; in scope for full build.

---

## Changelog

- **1.0 (Draft, 2026-05-05)** — Initial spec. Percent-bar model with exponential rank cost. Two growth events: sought-after success (+1pp before scaling), failed-roll secondary d100 (10% chance −1pp). Difficulty scaling on success via skill-threshold margin. Linear diminishing returns by (NPC, check type) per in-world day. Alignment growth modifier table. Seven pinned items declared.

---

*[[../README|Back to Index]] · [[Deception-Perception-Skills]] · [[Alignment-Spectrum]] · [[NPC-Intelligence-System]] · [[Simulation-Tick]] · [[PoC-Scope]]*
