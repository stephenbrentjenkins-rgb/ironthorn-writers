---
doc_type: "Writer Certification"
module: 1
title: "Writer Primer — NPC System Fundamentals"
version: "1.1"
status: "Required reading — complete before Quiz"
prerequisite: "None"
next: "[[02-Writer-Quiz]]"
---

# Writer Primer
## NPC System Fundamentals

> [!danger] Mandatory
> This document must be read in full before you attempt the Writer Quiz. No exceptions. Writers who submit NPC files without completing certification will have their submissions returned.
>
> When you have finished this primer, proceed to [[02-Writer-Quiz]]. A passing score of 80% or above is required before you access the [[04-NPC-Submission-Form]].

---

## Why this system exists

Most games treat NPCs as dialogue trees — branching menus that give the player information and move on. This game does not do that.

Every named NPC in this world is a person with a private life, a private fear, a private goal, and a private record of everything the player has done in their presence. They remember. They wait. They use what they know at the moment that costs the player the most.

Your job as a writer is to make that feel real — not by writing more words, but by writing the right words in the right places. The system handles the mechanics. You handle the humanity.

This primer teaches you the six things you must understand before you write a single line of dialogue, and exactly what happens when you submit your work.

---

## Module 1 — The tone anchor

### The rule
The tone of every NPC in this world is: **tired, not broken.**

This is the most important sentence in this document. Read it again.

### What it means

A **tired** NPC is still functioning. They still make choices. They still have a horizon they look toward. They carry weight without showing it — except in specific, small, consistent ways that the player can learn to read. They are a person.

A **broken** NPC has collapsed. They are defined by their suffering. They perform their damage for the audience. The player cannot reach them because there is nothing left to reach. They are a victim, not a character.

This distinction is not about how much an NPC has suffered. It is about what they did with what happened to them.

### The table

| Tired | Broken |
|-------|--------|
| Still functioning | Collapsed |
| Carries weight without showing it | Cannot hide the weight |
| Makes choices that cost something | Has stopped choosing |
| Has a horizon they still look toward | Has lost the horizon |
| Suppresses rather than performs | Performs rather than feels |

### This applies at every alignment tier

A Tier VII (Void-Touched) NPC is not a cackling villain. They are exhausted by the same world every other NPC is exhausted by, and they came out the other side with different conclusions. Their darkness is not performed. It is the result of a long, specific, personal history that made sense to them at every step.

A Tier I (Radiant) NPC is not beatifically pure. They have paid the cost of their principles, repeatedly, and they are still paying. Their goodness is not effortless. It is chosen, over and over, against significant resistance.

### The five hard rules

1. Never write an NPC as defined by their suffering. Suffering is backstory. Character is what they did with it.

2. Never write an NPC who monologues their inner state. They do not say "I am beginning to doubt." They set something down and ask you a question.

3. When in doubt, write the suppression, not the feeling. What the NPC is hiding is almost always more interesting than what they show.

4. The most tired line is never the most dramatic line. If it reads like a speech, cut it to the bone.

5. NPCs do not grow suddenly. Arc progression is driven by mechanics — resentment scores, disillusionment scores, trust scores. A writer delivers the moment that the mechanics have built. They do not invent it.

---

## Module 2 — The flag system

### What flags are

Flags are the memory layer of the NPC. They are binary states — on or off — that live in the NPC's frontmatter and memory log. They do not represent emotion. They represent **facts about the relationship between the player and this NPC** that persist across every future interaction.

An NPC without flags is reacting to the current scene.

An NPC with flags is reacting to the current scene **plus everything that happened before.**

Flags are what make the system remember. Without them, every interaction resets. With them, a lie told in session 2 can reshape a conversation in session 9.

### The six flags

**`liar_mark_active` (Boolean — permanent once set)**
The player failed a Deception check with this NPC. The NPC caught the lie. This mark persists for the life of the playthrough. It cannot be cleared by apology or the passage of time — only by a specific in-world confession mechanic that costs the player alignment and trust simultaneously.

What it does:
- The NPC's mid tell becomes permanently visible at Perception 4+ for this player
- The NPC's deep tell breaks surface when the mark is set — all players see it regardless of Perception
- All future trust score gains with this NPC are halved until the mark is cleared
- NPCs with Cunning 7+ share the mark within their faction network

**`debt_flag_active` (Boolean — deployable)**
The NPC holds something over the player. A stored lie, a witnessed act, a secret the player let slip. The player owes this NPC something they do not yet know about. The NPC is waiting for the right moment.

What it does:
- Always activates `leverage_held` simultaneously — they travel together
- Debt flag and leverage held cannot exist independently
- Certain quest branches become unavailable until the debt is cleared or deployed
- If the player tries to defect from the NPC's faction while the debt flag is active, the NPC deploys immediately

**`leverage_held` (Boolean — paired with debt_flag)**
The NPC has made a decision to use what they have. Unlike the debt flag — which tracks the existence of an obligation — leverage held tracks that the NPC has planned a deployment. They know what they will do and they are timing it.

The distinction: debt is passive (the NPC knows something and is waiting). Leverage is active (the NPC has decided).

**`faction_alert_sent` (Boolean — cannot be cleared)**
This NPC has passed intelligence about the player to their faction network. Once sent, this cannot be recalled. All NPCs in the same faction shift to a "measured" quality in their dialogue. Higher-tier faction NPCs become aware of the player by name. Some quest branches become permanently unavailable.

**`trust_score` (Numeric 1–10 — bidirectional)**
The accumulated score of the player's relationship with this specific NPC. Not faction standing — individual trust. Controls what the NPC shares, what quests they offer, what secrets they reveal.

Score thresholds:
- 1–3: Guarded. Minimal dialogue. No quest access.
- 4–5: Neutral. Standard relationship.
- 6–7: NPC shares non-obvious information. Secondary goal becomes visible.
- 8–9: Hidden agenda begins to surface. Defection-path quests unlock.
- 10: NPC will act against their faction's interests for this player if circumstances warrant.

**`secrets_known` (Array — accumulates)**
A list of specific things the player has revealed to this NPC. Not the NPC's secrets — the player's. The NPC's private ledger of what they know about the player that the player may have forgotten they shared. Each entry can become a lever, a bond, or a liability.

### The critical rule for writers

**Flags are set by mechanics. Writers do not set flags through dialogue.**

You do not write a scene where an NPC decides to flag a player. You write the scene where the mechanic fires — the moment a lie is caught, the moment trust crests a threshold, the moment a faction alert was already inevitable. The flag has already been set by the time you write the scene. Your job is to write what that flag looks like on the surface.

---

## Module 3 — Behavioural tells

### What a tell is

A tell is a physical, vocal, or behavioural micro-signal that surfaces when an NPC is in a specific internal state. It is the game's primary tool for communicating subtext without stating it.

A tell is **not** an emotion label. It is a **specific observable action.**

| Not a tell | A tell |
|-----------|--------|
| He looks nervous | He stops using your name |
| She seems suspicious | She sets down whatever she is holding before answering |
| He is hiding something | He asks an unrelated question, then carefully does not ask the follow-up |
| She is afraid | Her hands, usually still, move to straighten something that needs no straightening |

A tell must be writable as stage direction. If you cannot give it to an actor, it is not specific enough.

### The three tell tiers

Every named NPC (Tier 2+) has tells at three visibility levels:

**Surface tell — Perception 0 (everyone sees this)**
The NPC's baseline behaviour. Not a signal of distress — just how they are. Establishes the standard so that deviation means something. When it stops, that is the tell firing as absence.

Example — Aldric: He asks how you are before you ask him anything. Every time. When he does not, something has already happened.

**Mid tell — Perception 5–6**
A detectable shift from baseline. Indicates something is operating beneath the surface. Not proof — a signal.

Example — Aldric: He straightens things that do not need straightening. Objects near his hands. He is not aware he does it.

**Deep tell — Perception 7+**
The micro-signal that confirms the read. The passive mode activation.

Example — Aldric: He stops using your name. He was using it before. He is not doing it consciously.

### The six hard rules

1. One tell per emotional state, maximum. More tells dilute the signal.

2. Tells must be consistent across all scenes. If the straightening fires in scene 1, it fires in scene 14. Consistency is what makes the system learnable.

3. The surface tell is always active. It is the baseline. Its absence is the signal.

4. Never name a tell in standard dialogue. The player sees stage direction, not a pop-up notification.

5. Perception-gated tells are bracketed stage direction:
   > *[Perception 7+: He has not used your name in three exchanges. He was using it before.]*

6. A tell that fires at the wrong moment breaks the NPC. Check the suppression score before writing any tell into a scene. High suppression means most tells are invisible under routine conditions.

### How tells connect to flags

When `liar_mark_active` is set:
- The deep tell breaks surface regardless of Perception — all players see it
- The mid tell becomes permanently visible at Perception 4+ for this player
- The NPC's in-world response line plays immediately

When the player catches an NPC's lie via Perception check:
- The NPC's deep tell fires in real time
- The player receives a choice: confront, bank it, or ignore it
- The NPC's memory log notes that the player noticed — future interactions carry a "measured" quality

---

## Module 4 — The decision map

### What it is

When an NPC detects a player lie, they do not simply react. They run a specific logic in order, shaped by their attributes, alignment, and faction. This logic is written into every Tier 3+ NPC file as the Decision Map.

### The five steps

**Step 1 — Survival check**
Does this lie threaten the NPC's survival or primary goal?
- Yes → Assess threat immediately. Do not react visibly. Begin indirect countermeasures.
- No → Continue to Step 2.

**Step 2 — Leverage check**
Can this lie be used to further the NPC's own goals?
- Yes → Log silently. Set `debt_flag_active`. Store as leverage. The player now owes this NPC something.
- No → Continue to Step 3.

**Step 3 — Alignment filter**
How does their **true** alignment (not public) shape the instinct?
- True Light → Gentle confrontation. Offers the player a door to correct the lie.
- True Gray → Files silently. No reaction. Watches. Uses when useful.
- True Dark → Stores as ammunition. Deploys at the worst possible moment.

**Step 4 — Cunning filter**
What do their Cunning sub-attributes produce?
- Cunning 1–3 (Naive) → May blurt discomfort. "Something feels off."
- Cunning 4–6 (Aware) → Logs quietly. Dialogue shifts — shorter, less volunteered.
- Cunning 7–10 (Calculating) → Perfect composure. Builds a case. Deploys at optimal moment.

**Step 5 — Faction filter**
Does faction affiliation change the response?
- Same faction as player → May warn quietly.
- Rival faction → Reports to network. Lie becomes an intelligence asset.
- No faction relevance → Handled personally.

### The in-world response line

Every NPC has one. It is the line that plays when a lie is caught — written as stage direction plus a dialogue fragment. It must be specific to this character, not generic. It is the moment the player knows the NPC knows.

---

## Module 5 — NPC voice consistency

### The rule

Every named NPC has a voice established in Layer 1 of their file. That voice does not change between writers. It does not change between sessions. It is the NPC.

### The five hard rules

1. Read the voice fragments in Layer 1 before writing any dialogue for that NPC. Not after. Before.

2. Write three lines of test dialogue in the NPC's voice before writing the scene. Do not use those lines in the scene. They are warm-up.

3. The NPC's vocabulary is constrained by their background. A cleric uses theological vocabulary without flourish — working vocabulary, not performance. A forge master uses tactile, material language. An archivist uses precise conditional phrasing.

4. An NPC under pressure gets simpler, not more eloquent. Stress reduces vocabulary. If they are giving a speech under pressure, the writer has lost the character.

5. Silence is dialogue. A pause, a non-answer, a changed subject — write these explicitly as stage direction.

---

## Module 6 — What is never written

Regardless of scene requirements, faction, alignment, or player state:

1. **An NPC who explains their own hidden agenda.** It surfaces through action and accumulation — never through the NPC stating it.

2. **An NPC whose sole purpose is to deliver exposition.** Every NPC who speaks is a person first. Information is delivered in their voice, from their perspective.

3. **An alignment jump without mechanical support.** The mechanics drive the arc. The writer delivers the moment that the mechanics have built.

4. **A tell that contradicts the NPC's suppression score.** Know the score before writing any tell into a scene.

5. **An NPC who is wrong about themselves in a way the player cannot eventually discover.** Blind self-deception with no player access is a narrative dead end.

---

## Module 7 — The submission pipeline

### How your work gets into the game

When a writer submits an NPC file, it does not go directly into the vault. It goes into a holding folder where it is reviewed by the lead writer against five criteria before it is admitted. This module tells you exactly what that process looks like so you can submit work that passes on the first attempt.

### Where to submit

All submissions go to:
```
NPCs/_Pending/Your-NPC-Name/
```

Your submission folder must contain exactly three files:

1. **`NPC-Name.md`** — the completed NPC file, built from the NPC Template v3.0
2. **`NPC-Name_Submission-Form.md`** — the completed Submission Form (one per NPC)
3. **`NPC-Name_Submission-Intake.md`** — the intake document with your contact details

A submission missing any of these three files will be returned immediately without review.

### How to notify the lead writer

Once your three files are in place, send an email to:

**stephenbrentjenkins@gmail.com**

Subject line format:
```
[NPC SUBMISSION] NPC-Name — Your Name — Date
```

Include your submission details from the intake document in the email body. The lead writer will respond within the review window.

### Review window

- Standard review: **5 business days**
- Priority review (Tier 4+ NPCs, story-critical characters): **3 business days**

### What the lead writer reviews

The lead writer reviews your submission against five criteria in order. Understanding these criteria is the fastest way to submit work that passes.

**Criterion 1 — Tone**
Is the NPC tired, not broken? Does any line read as a speech? Does the NPC monologue their inner state anywhere?

**Criterion 2 — Tell system**
Are all three tell tiers present? Is the surface tell active in all normal scenes? Is the deep tell the one that fires on lie-catch? Are all tells consistent across every scene in the file?

**Criterion 3 — Flag accuracy**
Are all frontmatter flags at correct starting values? Has any flag been set to TRUE without mechanical justification?

**Criterion 4 — Voice**
Does the dialogue match the voice in Layer 1? Does the NPC get simpler under pressure? Is there at least one silence written as stage direction?

**Criterion 5 — Decision map (Tier 3+ only)**
Is the in-world response line specific to this character? Does the decision map correctly reflect the NPC's alignment, Cunning score, and faction position?

### If your submission is approved

The lead writer will:
- Move your NPC file to `NPCs/NPC-Name.md` — it is now live in the vault
- Move your submission form to `NPCs/_Characters/NPC-Name/Submissions/`
- Send you an approval email confirming the NPC is live

The NPC will automatically appear in the Unreal Engine Dev Tools panel on the next Refresh Roster. Your character is in the game.

### If your submission is returned

The lead writer will:
- Complete the Lead Writer Review section of your submission form with specific, line-level notes on what needs to change
- Leave all files in `_Pending/` — nothing moves until it passes
- Send you a return email quoting the exact failures and what revision is needed

You revise only the returned items. Sections that passed do not need to be resubmitted. Send an email when your revision is complete — same subject line, append `(Revised)`.

### Version control — your responsibility

Before submitting a revision of an existing NPC (an upgrade), copy the current canonical file to:
```
NPCs/_Characters/NPC-Name/Versions/NPC-Name_v1.0_YYYY-MM-DD.md
```

Use a date stamp. The Versions folder is the permanent record of every state the character has been in. The lead writer will check that this has been done before approving an upgrade.

---

## Certification path

```
Read this primer in full (you are here)
         ↓
Complete the Writer Quiz — 80% required to pass
         ↓
Review the Writer Glossary — reference, no pass/fail
         ↓
Build your NPC using NPC Template v3.0
         ↓
Complete the NPC Submission Form
         ↓
Complete the Submission Intake document
         ↓
Place all three files in NPCs/_Pending/NPC-Name/
         ↓
Email stephenbrentjenkins@gmail.com
Subject: [NPC SUBMISSION] NPC-Name — Your Name — Date
         ↓
Lead writer reviews against 5 criteria (5 business days)
         ↓
Approved → NPC goes live in vault + Unreal panel
Returned → Revise specific items → Resubmit
```

---

*[[README|Back to vault index]] · [[_System/Writer-Standards|Writer Standards]] · [[_System/NPC-Intelligence-System|NPC Intelligence System]] · [[_System/Lead-Writer-Review-Workflow|Lead Writer Review Workflow]] · [[02-Writer-Quiz|Take the quiz]] · [[03-Writer-Glossary|Glossary]] · [[04-NPC-Submission-Form|Submission Form]]*
