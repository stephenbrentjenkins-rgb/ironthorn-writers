---
doc_type: "Writer Certification"
module: 3
title: "Writer Glossary — NPC System Vocabulary"
version: "1.0"
status: "Reference — no pass/fail"
prerequisite: "[[01-Writer-Primer]]"
---

# Writer Glossary
## NPC System Vocabulary

> [!info] How to use this document
> This is a reference document, not a lesson. Use it during NPC file construction and scene writing when you need to verify a term's exact meaning. Every term in this glossary has a specific technical definition in this system — do not use common language assumptions. If a term is not in this glossary, ask the lead writer before using it.

---

## A

**Active flag**
Any flag in an NPC's frontmatter that is currently set to true (for booleans) or has a value above neutral (for trust_score). Active flags drive mechanical consequences in future interactions. See also: *flag*, *memory log*.

**Alignment — public**
The alignment tier an NPC presents to the world. Their mask. The public persona expresses this alignment. It may or may not match their true alignment. Written as a tier label: Light-V, Light-III, Light-I, Gray, Dark-I, Dark-III, Dark-V.

**Alignment — true**
The alignment that actually drives the NPC's decisions. May differ from their public alignment. The gap between public and true alignment is the source of dramatic irony. Writers must know both before writing any scene.

**Alignment tier**
One of seven positions on the alignment spectrum. Numbered 1–7 in the frontmatter (alignment_tier field), labelled by name in prose:
- I: The Radiant (Light-V)
- II: The Steadfast (Light-III)
- III: The Watchful (Light-I)
- IV: The Unbound (Gray)
- V: The Shadowed (Dark-I)
- VI: The Corrupted (Dark-III)
- VII: The Void-Touched (Dark-V)

**Arc progression**
The movement of an NPC through their story trajectory — from their starting state toward their tipping point and defection, revelation, or collapse. Arc progression is driven entirely by mechanics (sub-attribute scores reaching thresholds, trust score changes, story events). Writers deliver the moment that mechanics have built. They do not invent arc progression through dialogue.

**Attribute — main**
One of five primary scores that define an NPC's fundamental nature: Cunning, Loyalty, Fear, Greed, Idealism. Each runs 1–10. Each has sub-attributes that express how the main plays out under pressure. See individual entries.

**Attribute — sub**
A more specific score within a main attribute that determines how that attribute expresses itself in behaviour. Example: Loyalty has sub-attributes Devotion and Resentment. A Loyalty score of 7 with Devotion 8 and Resentment 6 produces a very different NPC from a Loyalty score of 7 with Devotion 5 and Resentment 7.

---

## B

**Background (NPC)**
The specific history that shaped an NPC — where they came from, what they have done that they cannot undo, what formed the gap between their public persona and private truth. Background is not character. Character is what the NPC did with what happened to them.

**Baseline (tell)**
The surface tell in its active, normal state. The NPC's consistent behaviour when calm and uncompromised. The baseline is what makes deviation meaningful. Without an established baseline, a tell has no signal value. See also: *surface tell*, *deviation*.

**Broken (tone)**
The incorrect tone for this system. A broken NPC is collapsed, defined by suffering, performing damage, and unreachable by the player. Contrast with *tired*. See also: *tired*, *tone anchor*.

**Burn condition**
The specific event that exposes a spy NPC's true identity. Each spy in the Spy Registry has a precisely defined burn condition. Writers must not alter or approximate burn conditions — they are exact. See also: *Spy Registry*, *dual identity*.

---

## C

**Caught lie**
A Deception check that fails — the player's Deception skill roll does not exceed the NPC's Perception threshold, or the lie involves information the NPC can independently verify. Triggers: `liar_mark_active` sets, deep tell breaks surface, in-world response line plays, trust gains halved. Contrast with *successful lie*.

**Certification path**
The required sequence for new writers: Primer → Quiz (80% pass required) → Glossary review → first NPC submission using the Submission Form → lead writer review. No writer submits NPC content without completing this path.

**Cunning**
Main attribute. How this NPC processes advantage, information, and other people as pieces on a board. Sub-attributes: Ambition (how actively they pursue advantage), Patience (how long they hold leverage before deploying), Paranoia (how burned they have been; high = pre-emptive suspicion).

**Cunning filter**
Step 4 of the lie-catch decision map. Determines how the NPC's Cunning score and sub-attributes shape their response to a detected lie. Naive (1–3): blurts discomfort. Aware (4–6): logs quietly, dialogue shifts. Calculating (7–10): perfect composure, builds a case, deploys at optimal moment.

---

## D

**debt_flag_active**
A flag indicating the NPC holds something over the player — a stored lie, a witnessed act, a secret — and the player owes this NPC something they may not know about. Always activates `leverage_held` simultaneously. The NPC is waiting. See also: *leverage_held*, *flag*.

**Decision map**
The five-step logic every NPC runs when they detect a player lie. Written into every Tier 3+ NPC file. Steps: Survival check → Leverage check → Alignment filter → Cunning filter → Faction filter. Produces the NPC's specific in-world response.

**Deep tell**
The third tier of behavioural tells. Visible only to players at Perception rank 7+. The micro-signal that confirms the read — the tell that breaks surface under maximum pressure. When a lie is caught, the deep tell fires regardless of Perception, becoming visible to all players. Example: Aldric stops using the player's name. See also: *tell*, *surface tell*, *mid tell*.

**Defection**
When an NPC breaks their faction loyalty. Mechanically triggered when resentment reaches threshold AND a specific tipping-point event fires as defined in the NPC file. Writers deliver the defection moment — they do not trigger defection through dialogue without mechanical support. A defected NPC's tells all cease; a new baseline must be written for their post-defection state.

**Deployed (memory log status)**
The leverage has been used against the player. Creates a permanent disposition shift. Once deployed, the specific leverage entry is resolved — but the disposition shift remains. Contrast with *Leverage*, *Cleared*, *Watching*.

**Deviation (tell)**
When an NPC behaves contrary to their established surface tell baseline. The signal that something has changed in their internal state. Example: Aldric, who always asks how you are, does not ask. The deviation is the tell. See also: *baseline*, *surface tell*.

**Dialogue hook**
A scene seed in a Tier 4+ NPC file — not a full script, but enough for a writer to build the moment. Covers: first encounter, post-trust rise, post-Liar's Mark, debt deployment, Tier I player interaction, Tier VII player interaction.

**Disillusionment**
Sub-attribute of Idealism. How much the world has eroded the NPC's core belief. High disillusionment (7+) means they still say the right words, but the faith is hollow. At 8, the deep tell begins to fire without pressure trigger — suppression is failing. At the tipping point, they can no longer sustain the gap between what they believe and what they witness.

**Dual identity**
The second identity layer used exclusively by Tier 5 NPCs and spy NPCs. A complete separate identity beneath the first — different name, different faction, different history. The gap between the two identities is the character's core. See also: *second identity layer*, *burn condition*.

---

## F

**faction_alert_sent**
A flag indicating this NPC has passed intelligence about the player to their faction network. Cannot be cleared. All faction NPCs shift to "measured" dialogue quality. Higher-tier faction NPCs become aware of the player by name. Some quest branches become permanently unavailable. See also: *flag*.

**Faction filter**
Step 5 of the lie-catch decision map. Determines whether faction affiliation changes the NPC's response to a detected lie. Same faction: may warn quietly. Rival faction: reports to network, lie becomes intelligence. No faction relevance: handled personally.

**Fear**
Main attribute. What this NPC is afraid of, and what that fear does to their behaviour. Sub-attributes: Desperation (does fear make them act recklessly?), Suppression (how well they bury it).

**Flag**
A binary state (boolean) or scored value (trust_score, secrets_known) in an NPC's frontmatter that persists across interactions and drives future mechanical consequences. Flags are facts about the relationship — not emotions, not attitudes. The six flags: `liar_mark_active`, `debt_flag_active`, `leverage_held`, `faction_alert_sent`, `trust_score`, `secrets_known`. See individual entries.

**Frontmatter**
The YAML block at the top of every NPC file. Contains all scores, flags, and metadata that Dataview queries read. Flags live here and in the memory log. Writers do not edit frontmatter during scene writing — frontmatter is updated by the system when mechanics fire.

---

## G

**Goal — hidden agenda**
The NPC's deepest motivation. Never stated in dialogue without the player earning it through sustained investment. Drives 10% of decisions — but those are the decisions the player remembers. Must recontextualise all prior interactions when discovered. Written in the T4 Layer of the NPC file.

**Goal — primary**
What the NPC is actively working toward right now. Drives 70% of decisions. Eventually discoverable through sustained player engagement.

**Goal — secondary**
Something the NPC also wants. Complicates the primary goal. Drives 20% of decisions. Visible to players at trust_score 6+.

**Goal tag**
A single word attached to each goal in the frontmatter for Dataview cross-referencing. Example: goal_primary_tag: "protection". Allows writers to find NPCs with shared or conflicting goal structures.

**Greed**
Main attribute. What the NPC wants, how much they want it, and what form that wanting takes. Sub-attributes: Appetite (how hungry), Restraint (how invisible they keep it), Envy (is their greed directional — fixated on what a specific person has?).

---

## H

**Hidden agenda**
See *Goal — hidden agenda*.

---

## I

**Idealism**
Main attribute. What principles the NPC holds, and how firm those principles are when tested. Sub-attributes: Conviction (how firm under pressure), Disillusionment (how much the world has eroded the belief).

**In-world response line**
The specific stage direction and dialogue fragment that plays when a lie is caught by this NPC. Written in the NPC file under Decision Map. Must be specific to this character — not generic. It is the moment the player knows the NPC knows.

---

## L

**Layer (NPC file)**
The structured sections of the NPC template, tiered by NPC complexity:
- T1: Quick Profile (all tiers)
- T2: Identity + Main Attributes (Tier 2+)
- T3: Sub-Attributes + Goals + Decision Map (Tier 3+)
- T4: Hidden Agenda + Memory Log + Dialogue Hooks (Tier 4+)
- T5: Second Identity + Cross-Faction Influence Map (Tier 5 only)

**Leverage**
Memory log status. The NPC has something stored and is not yet using it. They are waiting for optimal deployment timing. See also: *debt_flag_active*, *leverage_held*.

**leverage_held**
A flag indicating the NPC has decided what to do with what they know and is timing deployment. Always travels with `debt_flag_active`. Cannot exist without it. See also: *debt_flag_active*, *flag*.

**liar_mark_active**
A flag indicating the player failed a Deception check with this NPC. Permanent once set unless cleared through the confession mechanic. Halves all future trust gains with this NPC. High-Cunning NPCs (7+) share within faction network. See also: *flag*, *caught lie*.

**Loyalty**
Main attribute. Who the NPC is bound to, and how that binding holds under pressure. Sub-attributes: Devotion (how deep the loyalty runs), Resentment (the pressure building underneath). High Resentment + high Devotion = the powder keg.

---

## M

**Memory log**
The persistent record of player interactions with this NPC. Invisible to the player. Drives future dialogue branches and story triggers. Each entry: in-world timestamp, what happened, flag set, NPC intent. Status options: Leverage, Deployed, Cleared, Watching.

**Mid tell**
The second tier of behavioural tells. Visible to players at Perception rank 5–6. A detectable shift from baseline that indicates something is operating beneath the surface. Not proof — a signal. After `liar_mark_active` sets, the mid tell becomes permanently visible at Perception 4+ for that player. See also: *tell*, *surface tell*, *deep tell*.

---

## P

**Paranoia**
Sub-attribute of Cunning. How burned the NPC has been. High paranoia (7+) means they may strike first on a *suspected* lie — pre-emptive escalation. Low paranoia means they extend basic good faith until evidence compels otherwise.

**Patience**
Sub-attribute of Cunning. How long the NPC will sit on leverage before deploying it. High patience (7+) produces dangerous stillness — the NPC will hold for as long as it takes. Low patience means they act fast, sometimes too fast. Determines the timing of debt deployment.

**Perception threshold**
The NPC-specific difficulty rating for Deception checks against them. A player's Deception roll must exceed this threshold for a lie to succeed. Situationally modified — may drop in private settings or under intoxication; may rise in formal function or high-alert states.

**Private truth**
The full reality beneath the NPC's public persona. The lie they live every day. When you know the private truth, the public persona should feel like a costume. Written in T4 of the NPC file. Distinguished from *hidden agenda* — the private truth is the explanation; the hidden agenda is what they are actively doing about it.

**Public persona**
The mask. What the world sees. Two versions of every NPC exist: public persona and private truth. The gap between them is where interesting behaviour lives.

---

## R

**Resentment**
Sub-attribute of Loyalty. The pressure building underneath the NPC's stated loyalty. High resentment (7+) with high devotion = the powder keg. When resentment reaches 8, defection becomes mechanically possible regardless of devotion score. What stoked the resentment is the most important biographical question for any Watch-flagged NPC.

---

## S

**secrets_known**
A flag (array) containing specific things the player has revealed to this NPC. The NPC's private ledger of what they know about the player. High-Cunning NPCs cross-reference with faction network intelligence. At trust_score 8+, NPC may reference entries positively. At trust_score below 3, NPC may reference them as a warning.

**Second identity layer**
The T5 section of the NPC file. A complete second identity beneath the first — different name, different faction, a history that contradicts everything established. Used only for Tier 5 Legendary NPCs and spy NPCs with dual_identity set to true.

**Suppression**
Sub-attribute of Fear. How well the NPC buries their fear. High suppression (7+) means almost nothing surfaces under routine conditions — the NPC performs composure. At disillusionment 8, suppression begins to fail. The tells that exist beneath high suppression are small and specific; they require higher Perception to catch.

**Surface tell**
The first tier of behavioural tells. Visible to all players regardless of Perception (rank 0+). The NPC's baseline behaviour when calm and uncompromised. Its absence is the deviation — the signal that something has changed. See also: *tell*, *mid tell*, *deep tell*, *baseline*.

---

## T

**Tell**
A physical, vocal, or behavioural micro-signal that surfaces when an NPC is in a specific internal state. Not an emotion label — a specific observable action writable as stage direction. Three tiers: surface (Perception 0), mid (Perception 5–6), deep (Perception 7+). One tell per emotional state maximum. Consistent across all scenes.

**Tier (NPC)**
The complexity classification of an NPC. Determines which template layers are required:
- Tier 1: Background — Quick Profile only
- Tier 2: Supporting — adds Identity + Main Attributes
- Tier 3: Named — adds Sub-Attributes + Goals + Decision Map
- Tier 4: Major — adds Hidden Agenda + Memory Log + Dialogue Hooks
- Tier 5: Legendary — adds Second Identity + Cross-Faction Influence Map

**Tipping point**
The specific event defined in an NPC's file that triggers their arc's decisive moment — defection, revelation, or collapse. The tipping point must fire before the writer delivers the defection scene. It is not a dialogue moment; it is a world event. See also: *arc progression*, *defection*.

**Tired (tone)**
The correct tone for all NPCs in this system. A tired NPC is still functioning, still choosing, still looking toward a horizon. They carry weight without showing it — except in specific, consistent, learnable tells. Contrast with *broken*. See also: *tone anchor*.

**Tone anchor**
The single most important rule in this system: every NPC is tired, not broken. Applies at every alignment tier. See *tired*, *broken*.

**Trust score**
A numeric flag (1–10) tracking the accumulated relationship between player and this specific NPC. Not faction standing — individual. Drives dialogue branch selection, secret availability, quest access, and whether the NPC acts against faction interests for the player. Bidirectional — can rise and fall. After `liar_mark_active` sets, all gains are halved until cleared.

---

## V

**Voice (NPC)**
The specific pattern of speech, vocabulary, and silence that defines how an NPC communicates. Established in Layer 1 of the NPC file through voice fragments and mannerism notes. Does not change between writers. Constrained by the NPC's background — a forge master does not use an archivist's vocabulary. An NPC under pressure gets simpler, not more eloquent.

---

## W

**Watching**
Memory log status. The NPC has logged the interaction but taken no action yet. Not leverage — not yet. A low-level suspicion or noted discrepancy that has not crossed into active use. May escalate to Leverage if it compounds. Contrast with *Leverage*, *Deployed*, *Cleared*.

**Writer Standards**
The document at `_System/Writer-Standards.md` containing the five mandatory standards every writer follows. Non-negotiable. Read before opening any NPC file. Contains hard rules for tone, tells, cross-referencing, voice consistency, and what is never written.

---

*[[01-Writer-Primer|Back to Primer]] · [[02-Writer-Quiz|Back to Quiz]] · [[04-NPC-Submission-Form|Submission Form]] · [[../Writer-Standards|Writer Standards]] · [[../NPC-Intelligence-System|NPC Intelligence System]]*
