---
system_doc: true
doc_type: "Writer Standards"
version: "1.0"
applies_to: "All NPC files, all dialogue, all scene direction"
---

# Writer Standards

This document contains the non-negotiable rules every writer follows when building NPC files, writing dialogue, or scripting scenes in this world. These are not guidelines. They are the load-bearing walls of the story. Breaking them creates inconsistency that compounds across the game.

Read this document before opening any NPC file. Read it again before submitting any NPC file for review.

---

## Standard 1 — Tone anchor: tired, not broken

Every NPC in this world has been shaped by a world that does not fully deliver on what it promises. This is not a world of cartoons — there are no pure villains performing evil and no pure heroes performing goodness. Every character, at every alignment tier, is a person who made sense to themselves when they made their choices.

**The tone is tired. Not broken.**

This distinction governs everything:

| Tired | Broken |
|-------|--------|
| Still functioning | Collapsed |
| Carries the weight without showing it | Cannot hide the weight |
| Makes choices that cost something | Has stopped choosing |
| Has a horizon they still look toward | Has lost the horizon |
| Suppresses rather than performs | Performs rather than feels |

A broken NPC is a victim. A tired NPC is a person. The player can reach a tired NPC. They cannot reach a broken one.

**This applies at every alignment tier.** A Tier VII Void-Touched character is not melodramatically evil — they are exhausted by the same world the Tier I Radiant is exhausted by, but they came out the other side with different conclusions. A Tier I Radiant is not beatifically pure — they have simply paid the cost of their principles and are still paying it.

### Hard rules for writers — tone

1. **Never write an NPC as defined by their suffering.** Suffering is backstory, not character. Their character is what they did with what happened to them.

2. **Never write an NPC who monologues their inner state.** Aldric does not say "I am beginning to doubt the Covenant." He sets something down and asks you a question. The inner state is expressed through behaviour, not declaration.

3. **When in doubt, write the suppression, not the feeling.** What the NPC is hiding is almost always more interesting than what they show. High suppression scores mean almost nothing surfaces. Write what almost-nothing looks like.

4. **The most tired line is never the most dramatic line.** If a line reads as a speech, cut it to the bone. The line that lands is the one that sounds like something a real person would actually say in that moment, not something composed for impact.

5. **NPCs do not grow suddenly.** Arc progression is gradual and driven by mechanics (resentment scores, disillusionment scores, trust scores). A writer cannot accelerate an NPC's arc through dialogue alone. What dialogue can do is surface what the mechanics have already built.

---

## Standard 2 — Contextual behavioural tells

Every named NPC (Tier 2+) has at least one behavioural tell. A tell is a physical, vocal, or behavioural micro-signal that surfaces when the NPC is in a specific internal state. Tells are the game's primary tool for communicating subtext without stating it.

### What a tell is

A tell is **not** an emotion label. It is a **specific observable action** that the player (or a high-Perception player) can notice.

| Not a tell | A tell |
|-----------|--------|
| "He looks nervous" | "He stops using your name" |
| "She seems suspicious" | "She sets down whatever she is holding before she answers" |
| "He is hiding something" | "He asks you a question about something unrelated, then very carefully does not ask the follow-up" |
| "She is afraid" | "Her hands, which are usually still, move to straighten something that does not need straightening" |

A tell must be writable as stage direction. If you cannot write it as something a director could give to an actor, it is not specific enough.

### The three tell tiers

Every named NPC has tells at three visibility levels:

**Surface tell (Perception 0 — everyone sees it)**
The behavioural signature that is just part of how this NPC operates. Not a lie-catch signal — just how they are. It establishes the baseline so that deviation from it means something.

For Aldric: he asks how you are before you ask him anything. Always. This is surface behaviour. When he stops doing it, that is the deviation.

**Mid tell (Perception 5–6 — attentive players catch it)**
A detectable shift from baseline that indicates something is operating beneath the surface. Not proof of anything — a signal that something is different.

For Aldric: he straightens things that do not need straightening. Specifically objects nearest to him — books, candles, tools. He is not aware he does this. Players at Perception 5+ see it. Players below Perception 5 do not.

**Deep tell (Perception 7+ — only sharp players catch it)**
The micro-signal that confirms the read. This is the passive mode activation — the tell that, combined with context, tells a high-Perception player what is actually happening beneath the surface.

For Aldric: he stops using your name. He was using it before. He is not doing it consciously. Players at Perception 7+ catch the absence.

### Hard rules for writers — tells

1. **One tell per emotional state, maximum.** Do not layer multiple tells for the same state. Pick the most specific one and write only that one. More tells dilute the signal.

2. **Tells must be consistent across all scenes featuring this NPC.** If Aldric straightens things when unsettled in scene 1, he straightens things when unsettled in scene 14. The player's ability to read him depends on consistency.

3. **The surface tell is always active.** It does not disappear when the NPC is calm — it IS their calm state. It is the baseline. Deviation from it is the signal.

4. **Never name a tell in standard dialogue.** A player at Perception 6 does not receive a pop-up saying "you notice Aldric seems nervous." They see the direction: *He sets down the candle. His hands move to the book. He sets down the book.* The interpretation is the player's.

5. **Perception-gated tells are shown as bracketed stage direction, not as dialogue.** The format is:
   > *[Perception 7+: He has not used your name in three exchanges. He was using it before.]*

6. **A tell that fires at the wrong moment breaks the NPC.** Do not write tells into scenes where the NPC would not actually be in that state. Aldric's straightening-tell fires when he is unsettled. It does not fire when he is performing official function (high suppression overrides the tell there). Know your NPC's suppression score before writing their tells into a scene.

---

## Standard 3 — Tell cross-referencing: lie system and NPC/PC interactions

Tells do not exist in isolation. They are part of an interconnected signal system across three layers:

### Layer 1 — Tell ↔ Lie system

When a player attempts a Deception check against an NPC, the NPC's tells are mechanically linked to the outcome:

**Failed lie (lie caught):**
- The NPC's deep tell fires immediately regardless of Perception — it breaks surface
- The in-world response line plays (written in the NPC file under Decision Map)
- The Liar's Mark flag activates in the NPC's memory log
- From this point forward, the NPC's mid tell is permanently visible to any player at Perception 4+ (the mark has lowered their guard threshold)

**Successful lie:**
- No tell fires
- The NPC's memory log notes the interaction with "Watching" status — no action yet
- If the player's Deception skill is lower than the NPC's perception threshold, the "Watching" status means the NPC has a low-level suspicion that does not cross into action unless it compounds

**Perception check (player catching NPC lie):**
- Player receives a description of the NPC's tell firing in real time
- Catching the lie grants +2 alignment toward light
- The player gains a choice: confront, bank it, or ignore it
- The NPC's memory log notes that the player noticed — future interactions from this NPC carry a "measured" quality regardless of surface behaviour

**Key writer rule:** The tell the player sees when catching an NPC lie should be the NPC's deep tell, not a new one invented for the moment. The deep tell is what breaks surface under maximum pressure.

### Layer 2 — Tell ↔ NPC/NPC interactions

NPCs in the same district notice each other's tells. This is not always stated — sometimes it is implied through dialogue that a second NPC picks up on something about the first.

**How to write it:**

When two NPCs interact in a scene, one NPC can register the other's tell if:
- Their Perception threshold is higher than the other NPC's suppression score
- They have a pre-existing relationship (colleague, rival, former ally) that gives them baseline familiarity

Example: Ser Orvane has a Perception threshold of 6. Aldric's suppression is 7. In most scenes, Orvane cannot read Aldric's internal state. But after eleven years of shared patrol routes, Orvane has learned Aldric's surface tell (asking how you are before you ask him). When Aldric does not do this, Orvane notices the absence — not through Perception, but through familiarity.

This is how to write NPC-NPC tell cross-reference:
> *Orvane hands him the report. Aldric takes it without asking how the night went. Orvane watches him walk back toward the Chapter House. He does not say anything.*

The tell fires in Aldric. Orvane notices through relationship, not skill. The scene carries more information than any dialogue could deliver.

**Hard rule:** An NPC can only register another NPC's tell through skill OR relationship, never through the writer's omniscience. If you are writing an NPC noticing something about another NPC, be clear about the mechanic — is it Perception, or is it a relationship-based baseline familiarity? Write it as the appropriate signal, not as implied shared awareness.

### Layer 3 — Tell ↔ PC interaction over time

Tells compound across the player's relationship with an NPC. The more interactions the player has had, the more context they have for what a tell means.

**Session 1:** Player sees Aldric straighten a book. No context. No meaning.

**Session 3:** Player has seen Aldric three times. He has not straightened anything when calm. Player at Perception 5+ begins to associate the straightening with a specific internal state.

**Session 6:** Player asks Aldric something that unsettles him. He straightens three things in eight seconds. Player at Perception 5+ now has enough context to know exactly what that means.

**How to write accumulated tell context:**

The NPC file's memory log tracks interactions. Dialogue scripts reference this: *[If trust score 6+: Aldric's straightening-tell has been visible in two prior interactions. The player has context. Do not re-introduce the tell as if it is new — write it as the player recognising something familiar.]*

**Hard rule for accumulated tells:** Never write a tell as if it is new information in a scene where the player has seen it before. After the second time, it is a pattern. After the third, it is a language. Write it accordingly.

---

## Standard 4 — NPC voice consistency

Every named NPC has a voice established in Layer 1 of their file. This voice does not change between writers.

### Hard rules for writers — voice

1. **Read the voice fragments in Layer 1 before writing any dialogue for that NPC.** Not after. Before.

2. **Write three lines of test dialogue in the NPC's voice before writing the scene.** Do not use the test lines in the scene. They are warm-up. They ensure you are in the character before you write the moment that matters.

3. **The NPC's vocabulary is constrained by their background.** Aldric uses full sentences and theological vocabulary that he deploys without flourish — it is working vocabulary, not performance. A forge master uses tactile, material language. An Archivist uses precise conditional phrasing. Match vocabulary to background.

4. **An NPC under pressure gets simpler, not more eloquent.** Stress reduces vocabulary. A panicking NPC uses shorter sentences. A cornered NPC uses fewer words. If an NPC is giving a speech under pressure, the writer has lost the character.

5. **Silence is dialogue.** A pause, a non-answer, a changed subject — these are as much the NPC's voice as any line. Write them explicitly in stage direction. Do not leave them for the director to infer.

---

## Standard 5 — What never gets written

Regardless of scene requirements, faction, alignment, or player state, these things are never written:

1. **An NPC who explains their own hidden agenda.** Hidden agendas surface through action, accumulation, and player discovery — never through the NPC articulating it. If the NPC is explaining their hidden agenda, they are not hiding it.

2. **An NPC whose sole purpose is to deliver exposition.** Every NPC who speaks exists as a person first. If they have to deliver a piece of world information, it is delivered in their voice, from their perspective, coloured by what they want the player to know and what they do not.

3. **An alignment jump without mechanical support.** An NPC cannot switch sides, betray their faction, or change their fundamental position without the underlying sub-attributes having reached their thresholds. The mechanics drive the arc. The writer delivers the moment — they do not invent it.

4. **A tell that contradicts the NPC's suppression score.** High suppression means the NPC's internal state does not surface without significant pressure. Do not write their deep tell firing in a low-stakes scene. Know the score. Write accordingly.

5. **An NPC who is wrong about themselves in a way the player cannot eventually discover.** If an NPC's self-image does not match their true alignment, there must be a discoverable path to that truth. Blind self-deception with no player access is a narrative dead end.

---

## Quick reference — tell visibility by Perception rank

| Perception rank | What the player can read |
|----------------|--------------------------|
| 0–4 | Surface tells only — the NPC's baseline behaviour |
| 5–6 | Mid tells — detectable shifts from baseline |
| 7–8 | Deep tells — micro-signals that confirm the read; passive mode activates |
| 9 | Faction double-agent detection becomes viable; hidden emotional states surface in dialogue tags |
| 10 | Maximum; catches almost all lies; some NPC secrets surface unbidden; Void Eternum observation pattern becomes visible |

---

## Quick reference — tell cross-system triggers

| Trigger | Tell result |
|---------|-------------|
| Lie caught by NPC | Deep tell breaks surface; Liar's Mark activates; threshold permanently lowered |
| Successful lie | No tell; "Watching" status logged |
| Player catches NPC lie (Perception check) | Deep tell fires in real time; player receives choice |
| Trust score reaches 7 | Mid tell becomes visible to Perception 4+ (relationship familiarity threshold) |
| Resentment reaches 8 | Surface tell begins to fire in low-stakes scenes (suppression weakening) |
| Disillusionment reaches 8 | Deep tell begins to fire without pressure trigger (suppression failing) |
| NPC defection | All tells cease — defected NPC operates with new baseline; new surface tell must be written |

---

*[[README|Back to Index]] · [[NPC-Intelligence-System]] · [[Deception-Perception-Skills]] · [[Alignment-Spectrum]] · [[Attribute-Reference]] · [[NPC-Tier-Reference]]*
