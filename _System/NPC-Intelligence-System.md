---
system_doc: true
doc_type: "NPC System"
version: "1.0"
---

# NPC Intelligence System

Every named NPC in this game is not a dialogue tree — they are a character with goals, history, and a private response to everything the player does. This document describes the architecture that makes that work.

---

## The four layers every NPC has

### 1. Identity layer
Two versions of who they are: **public persona** (the mask) and **private truth** (the engine). The gap between these two is where all interesting NPC behaviour lives.

### 2. Attribute layer
Five main attributes, each with sub-attributes that express how the main plays out under pressure. See [[Attribute-Reference]] for full details.

### 3. Goal layer
**Primary goal** (active, eventually discoverable), **Secondary goal** (complicates the primary), **Hidden agenda** (never stated in dialogue without player earning it). Every decision the NPC makes — including what they do when they catch a lie — flows from these three goals in priority order.

### 4. Memory layer
A persistent log of player interactions. Flags, leverage, trust score, and faction network alerts. Updated during play. Drives future dialogue branches.

---

## The lie-catch decision map

When an NPC detects a player lie, they run this logic in order:

**Step 1 — Survival check**
Does the lie threaten this NPC's survival or primary goal?
- YES → Assess threat level immediately. Do not react visibly. Begin indirect countermeasures.
- NO → Continue to Step 2.

**Step 2 — Leverage check**
Can this lie be used to further the NPC's own goals?
- YES → Log the lie silently. Set debt flag. Store as leverage. The player now owes this NPC something, even if they don't know it yet.
- NO → Continue to Step 3.

**Step 3 — Alignment filter**
How does the NPC's *true* alignment (not public) shape their instinct?
- True Light → Gentle confrontation. Offers the player a door to correct the lie. +1 alignment if player walks through.
- True Gray → Files silently. No reaction. Watches. Uses when useful.
- True Dark → Stores as ammunition. Deploys at the worst possible moment for the player — dramatically, not randomly.

**Step 4 — Cunning filter**
What does their Cunning score + subs produce?
- Cunning 1–3 (Naive) → Blurts discomfort or accepts the lie. May say "Something feels off."
- Cunning 4–6 (Aware) → Logs quietly. Dialogue shifts — shorter answers, less volunteered, more specific questions.
- Cunning 7–10 (Calculating) → Perfect composure. No tells. Builds a case. Deploys leverage at optimal moment.

**Step 5 — Faction filter**
Does faction affiliation change the response?
- Same faction as player → May warn quietly. Faction integrity matters more than punishment.
- Rival faction → Reports to faction leadership. Lie becomes an intelligence asset in the broader conflict.
- No faction relevance → Handled personally. No network escalation.

---

## The memory log

Every NPC maintains a private log of player interactions. Invisible to the player. Drives future dialogue branches and story triggers.

**Log entry fields:**
- Timestamp (in-world)
- What happened
- Flag set (Leverage / Deployed / Cleared / Watching)
- NPC's intent

**Leverage:** Stored, not yet used. The NPC is waiting.
**Deployed:** The leverage has been used against the player. Creates a permanent disposition shift.
**Cleared:** Resolved — player confessed, paid the debt, or the information became irrelevant.
**Watching:** Logged with no immediate flag. The NPC has noted it and is observing.

---

## Active flags

| Flag | What it means |
|------|--------------|
| `liar_mark_active` | Player failed a Deception check with this NPC. Mark persists. High-cunning NPCs share within faction network. |
| `debt_flag_active` | NPC holds leverage. Player owes something they may not know about yet. |
| `leverage_held` | NPC has something specific stored and ready to deploy. |
| `faction_alert_sent` | NPC has passed intelligence about the player to their faction network. |
| `trust_score` | 1–10. Drives dialogue branch selection, secret availability, and quest access. |

---

## NPC goals in practice

**Primary goal** drives 70% of decisions.
**Secondary goal** drives 20% — usually adds a complication or constraint.
**Hidden agenda** drives the remaining 10% — but those are the 10% the player will remember.

The hidden agenda is never the first thing an NPC acts from. It is always operating beneath the surface, shaping the edges of every interaction, until the player has earned enough trust (or caused enough damage) to bring it forward.

---

## The public persona / private truth gap

This gap is the source of the game's dramatic irony. The player interacts with the public persona. The private truth is running the actual decisions.

Some examples of what that gap looks like:
- A devoted priest whose faith collapsed nineteen years ago (Brother Aldric)
- A warm merchant who is running a counter-intelligence operation against a crime lord (Maren Voss)
- An honourable commander who is systematically dismantling a legitimate command structure (Commander Syla)

The gap is not always dark. Sometimes the private truth is more sympathetic than the public persona suggests. Sometimes the private truth is exactly what the player feared. The template does not dictate which — the designer does.

---

## NPC immunity

Certain NPCs cannot be deceived regardless of player Deception skill:
- Their `deception_immune` flag is set to true
- The in-world reason must be stated in their profile
- The immunity must feel earned — an oracle, a blind seer, a parent who simply knows
- These NPCs should be identifiable in-world as exceptional before the player tries to lie to them

---

*[[README|Back to Index]] · [[Alignment-Spectrum]] · [[Deception-Perception-Skills]] · [[Attribute-Reference]] · [[NPC-Tier-Reference]]*
