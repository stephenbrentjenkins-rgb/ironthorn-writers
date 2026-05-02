---
npc_name: FULL NAME
npc_tier: 1
npc_role: Role / Title
faction: Faction Name
location: Where they are usually found
alignment_public: Gray
alignment_true: Gray
alignment_tier: 4
cunning: 5
loyalty: 5
fear: 5
greed: 5
idealism: 5
cunning_ambition: 5
cunning_patience: 5
cunning_paranoia: 5
loyalty_devotion: 5
loyalty_resentment: 5
fear_desperation: 5
fear_suppression: 5
greed_appetite: 5
greed_restraint: 5
greed_envy: 5
idealism_conviction: 5
idealism_disillusionment: 5
perception_threshold: 5
deception_immune: false
goal_primary_tag: ""
goal_secondary_tag: ""
goal_hidden_tag: ""
liar_mark_active: false
debt_flag_active: false
trust_score: 5
leverage_held: false
secrets_known: []
faction_alert_sent: false
dual_identity: false
true_faction: ""
world_secret: false
template_version: "3.0"
status: Draft
---

# `=this.npc_name`

> [!info] Identity at a glance
> **Tier:** `=this.npc_tier` · **Role:** `=this.npc_role` · **Faction:** `=this.faction`
> **Location:** `=this.location`
> **Alignment — public / true:** `=this.alignment_public` / `=this.alignment_true`
> **Status:** `=this.status`

---

> [!example] Tier requirements — fill only what your tier needs
> **T1 Background** → Quick Profile only
> **T2 Supporting** → T1 + Layer 1 Identity + Main Attributes + Basic Lie Response
> **T3 Named** → T2 + Sub-Attributes + Goals + Decision Map + Memory Log header
> **T4 Major** → T3 + Hidden Agenda + Private Truth + Full Memory Log + Dialogue Hooks + Dataview
> **T5 Legendary** → T4 + Second Identity + Cross-Faction Influence Map
>
> Sections are marked `[T1]` through `[T5]`. Leave deeper sections blank until the NPC is promoted.

---

## `[T1]` Quick Profile

> [!note] Required: ALL tiers — complete before this NPC appears in any scene

**Function in the world:** REPLACE — one sentence. What they do. Why the player encounters them.

**First impression:** REPLACE — two sentences. What the player sees and feels on first contact. Surface only.

**Signature line:**
> *REPLACE — the one line or action that defines this NPC instantly. A merchant who never makes eye contact. A guard who checks your hands before your face. Write it so a voice actor knows exactly who this person is.*

**Basic lie response:** REPLACE — one line. What the player sees when they fail a Deception check with this NPC. All a Tier 1 NPC needs.

---

## `[T2]` Layer 1 — Identity

> [!note] Required: Tier 2+

### Public persona
*What the world sees. The mask.*

> REPLACE — tone, mannerisms, what they lead with. What they want people to believe about them.

### Background
*The history that made them. 3–5 sentences.*

> REPLACE — where they came from, what shaped them, what they have done they cannot undo. Specific details over general statements. One precise image beats three vague sentences.

### Voice & mannerisms
*How they sound. How they move.*

> REPLACE — one or two fragments in their actual voice. Physical tells — what they do when lying, when afraid, when they like you, when they don't.

---

## `[T2]` Layer 2 — Main Attributes

> [!note] Required: Tier 2+ (mains only) · Tier 3+ (mains + subs)

> [!tip] Scoring guide
> **1–3** Naive / Low · **4–6** Aware / Average · **7–9** Calculating / High · **10** Masterful / Exceptional

---

### Cunning — `=this.cunning`
*How this NPC processes advantage, information, and other people as pieces on a board.*

> REPLACE — what their cunning score means in practice for this specific character.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Ambition | `=this.cunning_ambition` | REPLACE — how actively they pursue advantage. Are they always working an angle, or opportunistic? |
| Patience | `=this.cunning_patience` | REPLACE — how long they'll sit on leverage before deploying it. High = dangerous stillness. Low = acts fast, sometimes too fast. |
| Paranoia | `=this.cunning_paranoia` | REPLACE — how burned they've been. High = pre-emptively suspicious, may strike first. Low = still extends basic good faith. |

---

### Loyalty — `=this.loyalty`
*Who they are bound to, and how that binding holds under pressure.*

> REPLACE — loyal to whom. What that loyalty looks like from the outside. What would make it break.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Devotion | `=this.loyalty_devotion` | REPLACE — how deep it actually runs. Genuine bond or circumstantial alliance? |
| Resentment | `=this.loyalty_resentment` | REPLACE — the pressure building underneath. High resentment + high devotion = the powder keg. What stoked it? |

> [!warning] Resentment watch
> If `=this.loyalty_resentment` reaches 8 or above, this NPC is a betrayal risk regardless of their Devotion score. Flag for story team.

---

### Fear — `=this.fear`
*What they are afraid of, and what that fear does to their behaviour.*

> REPLACE — what specifically they fear. Not "failure" — "the specific person who would come if they failed." Name it.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Desperation | `=this.fear_desperation` | REPLACE — does fear make them act recklessly? High = will take dangerous gambles to escape what they fear. Exploitable. |
| Suppression | `=this.fear_suppression` | REPLACE — how well they bury it. High suppression reads as bravery. It is not. What cracks the surface? |

---

### Greed — `=this.greed`
*What they want, how much they want it, and what form that wanting takes.*

> REPLACE — what is the specific object of their greed. Wealth, power, safety, information, someone else's life. Be precise.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Appetite | `=this.greed_appetite` | REPLACE — how hungry. High = never satisfied, always reaching, risk-tolerant for gain. Low = situational, satisfied with enough. |
| Restraint | `=this.greed_restraint` | REPLACE — how invisible they keep it. High restraint = their greed is unreadable until they move. Low = obvious, manipulable. |
| Envy | `=this.greed_envy` | REPLACE — is their greed directional? High envy means they are fixated on what a specific person or group has. Produces sabotage, not accumulation. Who do they envy and why? |

---

### Idealism — `=this.idealism`
*What principles they hold, and how firm those principles are when tested.*

> REPLACE — what do they actually believe in. What cause, value, or person do they think justifies their existence.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Conviction | `=this.idealism_conviction` | REPLACE — how firm under pressure. High = will not bend regardless of cost. Low = principles flex when stakes get high enough. |
| Disillusionment | `=this.idealism_disillusionment` | REPLACE — how much the world has eroded the belief. High = still says the right words but the faith is hollow. One bad day from switching sides. What disillusioned them? |

---

### Perception threshold — `=this.perception_threshold`
> REPLACE — what makes them easy or hard to fool. Include situational modifiers. "Threshold drops to 3 when drinking. Rises to 9 when discussing their daughter."

### Deception immune — `=this.deception_immune`
> Fill only if true. Explain the in-world reason — it must feel earned, not arbitrary. Delete this line if false.

---

## `[T3]` Layer 3 — Goals

> [!note] Required: Tier 3+

> [!tip] Writer's note
> Specificity is everything here. "Power" is not a goal. "Control the northern trade routes before the new governor's fleet arrives in spring" is a goal. The hidden agenda (Layer 4) is the most important thing you will write about this NPC. Even at Tier 3, goals should be concrete enough that a writer can construct scenes from them.

### Primary goal
> REPLACE — what are they actively working toward right now?

**What they will sacrifice for this:** REPLACE
**Goal tag:** `=this.goal_primary_tag`

### Secondary goal
> REPLACE — something they also want. How does it support or complicate the primary?

**What they will sacrifice for this:** REPLACE
**Goal tag:** `=this.goal_secondary_tag`

### What they fear losing most
*Not a goal — a vulnerability. The exposed nerve.*

> REPLACE — be specific. "The letter hidden in the vault" beats "their reputation." The more precise, the more useful in play and the more real the NPC feels.

---

## `[T3]` Lie Detection — Decision Map

> [!note] Required: Tier 3+

*Work through all five steps for this specific character. Generic answers are not useful here.*

### Step 1 — Does the lie threaten their survival or primary goal?
> REPLACE — yes or no, and the exact behaviour in each case for this NPC.

### Step 2 — Can they bank this lie as leverage?
> REPLACE — would this NPC store it? What would they do with it specifically? Not all NPCs are leverage collectors — some react immediately and have no patience for games.

### Step 3 — How does their true alignment shape the response?
> REPLACE — true Light confronts gently, offers the player a correction. True Gray files it silently and watches. True Dark stores it as ammunition and deploys it at the worst possible moment. Write the specific behaviour for this character's true alignment, not the public one.

### Step 4 — What do their Cunning subs produce?
> REPLACE — Ambition, Patience, and Paranoia interact here. A high-Patience NPC gives nothing away and waits. A high-Paranoia NPC may pre-emptively escalate even on a *suspected* lie. A high-Ambition NPC immediately calculates how the lie can be converted to advantage. Describe the specific combination for this character.

### Step 5 — Does faction affiliation change anything?
> REPLACE — report to the network? Protect the player if same faction? Use it as intelligence against a rival? Handle it entirely alone?

### In-world response line
> [!quote] What the player sees when the lie is caught
> *REPLACE — write as stage direction + dialogue fragment, exactly as it would appear on screen.*
> *"She sets down her cup. A long pause."*
> "I see." *She does not look at you again for the rest of the conversation.*

### Cunning tell *(passive — Perception 7+ only)*
> REPLACE — the micro-behaviour a high-Perception player notices even when the NPC gives nothing away. The hand moving to a ring. A breath held one beat too long. Only write one. It must be specific to this character.

---

## `[T4]` Layer 4 — Hidden Agenda & Private Truth

> [!note] Required: Tier 4+

> [!danger] Hidden agenda — NEVER surface in dialogue without player earning it
> REPLACE — write this as the reveal moment: *"Oh. That's what was going on the whole time."*
> It must recontextualise every prior interaction when discovered.

**What they will sacrifice for this:** REPLACE
**Goal tag:** `=this.goal_hidden_tag`

**Trigger for reveal:** REPLACE — define it exactly. A specific alignment tier? Faction rank? Perception check difficulty 9+? Trust score 9+ with a specific confession trigger? A chain of discoveries across multiple quests?

### Private truth
*The full reality beneath the public persona. The lie they live every day.*

> REPLACE — complete private history. Real wounds, hidden acts, the thing that drives everything under the surface. This should fully explain the hidden agenda. When you know the private truth, the public persona should feel like a costume.

---

## `[T4]` Layer 5 — Memory Log

> [!note] Required: Tier 4+

> [!warning] Log protocol
> Each entry: in-world timestamp · what happened · flag set · NPC's intent.
> **Leverage** = stored, not yet used · **Deployed** = used · **Cleared** = resolved · **Watching** = logged, no action yet

| Timestamp | Event | Flag | Status | NPC intent |
|-----------|-------|------|--------|------------|
| — | No interactions logged | — | — | — |

### Active flags

| Flag | State |
|------|-------|
| Liar's Mark | `=this.liar_mark_active` |
| Debt Flag | `=this.debt_flag_active` |
| Trust Score | `=this.trust_score` / 10 |
| Leverage Held | `=this.leverage_held` |
| Faction Alert Sent | `=this.faction_alert_sent` |

### Leverage inventory
> Empty until interactions logged. What does this NPC hold, and what do they plan to do with it?

### Faction network — alerts sent
> Empty until interactions logged. What intelligence has been passed, to whom, and when?

---

## `[T4]` Layer 6 — Dialogue Hooks

> [!note] Required: Tier 4+

*Scene seeds — not full scripts. Enough for a writer to build the moment.*

### First encounter
> REPLACE — the opening beat. What does the player get on first contact? An immediate want, a test, a deflection? What unanswered question do they leave with?

### After trust score rises above 7
> REPLACE — what changes? What do they offer, reveal, or risk that they wouldn't show a stranger?

### After Liar's Mark activates
> REPLACE — how does dialogue shift? Contrast from their normal state specifically.

### When debt is deployed
> REPLACE — the scene beat when they cash in leverage. Should feel earned. One of the most memorable moments in any NPC relationship.

### At player Tier I — Radiant
> REPLACE — awe, suspicion, being broken open by it, something stranger. Specific to this character.

### At player Tier VII — Void-Touched
> REPLACE — fear, service, fascination, or withdrawal. Specific to this character.

---

## `[T5]` Second Identity Layer

> [!note] Required: Tier 5 only

> [!danger] Legendary NPC — not who they appear to be at any level
> A complete second identity beneath the first. Different name. Different faction. A history that contradicts everything the player has learned.

**True name:** REPLACE
**True faction:** `=this.true_faction`

**Alignment stack:**
- Surface identity: `=this.alignment_public`
- Known true alignment: `=this.alignment_true`
- Deepest true self: REPLACE

**How the second identity was buried:** REPLACE — the specific moment they chose to become someone else. The emotional core of the character.

**What triggers the full reveal:** REPLACE — must require significant player investment. A chain of discoveries. The moment when both identities can no longer coexist.

---

## `[T5]` Cross-Faction Influence Map

> [!note] Required: Tier 5 only

| Faction | Relationship | What they know | What they want from it |
|---------|-------------|----------------|------------------------|
| REPLACE | REPLACE | REPLACE | REPLACE |

**World secret:** `=this.world_secret`
> REPLACE — if true, what does this NPC know that could change the shape of the world? Who else knows? What does it cost to extract? What happens when it becomes public?

---

## Dataview Queries

> [!note] Required: Tier 4+ · These run live in Obsidian with the Dataview plugin active

### This NPC — active flags
```dataview
TABLE liar_mark_active, debt_flag_active, trust_score, leverage_held, faction_alert_sent
FROM "NPCs"
WHERE npc_name = this.npc_name
```

### Resentment watch — all NPCs approaching betrayal threshold
```dataview
TABLE npc_name, faction, loyalty, loyalty_devotion, loyalty_resentment
FROM "NPCs"
WHERE loyalty_resentment >= 7
SORT loyalty_resentment DESC
```

### Paranoia watch — NPCs likely to pre-emptively escalate
```dataview
TABLE npc_name, faction, cunning, cunning_paranoia, cunning_patience
FROM "NPCs"
WHERE cunning_paranoia >= 7
SORT cunning_paranoia DESC
```

### High-envy NPCs — directional greed targets
```dataview
TABLE npc_name, faction, greed, greed_envy, greed_restraint
FROM "NPCs"
WHERE greed_envy >= 7
SORT greed_envy DESC
```

### All NPCs in this faction — ranked by cunning
```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, cunning_ambition, cunning_patience, cunning_paranoia, perception_threshold
FROM "NPCs"
WHERE faction = this.faction AND npc_name != this.npc_name
SORT cunning DESC
```

### All NPCs with active flags
```dataview
TABLE npc_name, faction, trust_score, liar_mark_active, debt_flag_active, leverage_held
FROM "NPCs"
WHERE liar_mark_active = true OR debt_flag_active = true OR leverage_held = true
SORT trust_score ASC
```

### NPCs sharing goal tags — potential allies or rivals
```dataview
TABLE npc_name, faction, npc_tier, goal_primary_tag, goal_hidden_tag
FROM "NPCs"
WHERE (goal_primary_tag = this.goal_primary_tag OR goal_hidden_tag = this.goal_hidden_tag)
AND npc_name != this.npc_name
```

### Disillusionment watch — idealists approaching collapse
```dataview
TABLE npc_name, faction, idealism, idealism_conviction, idealism_disillusionment
FROM "NPCs"
WHERE idealism_disillusionment >= 7
SORT idealism_disillusionment DESC
```

### Full NPC roster
```dataview
TABLE npc_name, npc_tier, faction, alignment_public, alignment_true, cunning, status
FROM "NPCs"
SORT npc_tier DESC, cunning DESC
```

---

## Writer's Notes

> [!tip] Scratchpad — clear before final production

> REPLACE — open questions, quest hooks, cross-NPC connections not yet formalised, tone flags. Write it now, it won't survive the next conversation.

---

*Template v3.0 · [[_System/NPC-Intelligence-System|NPC Intelligence System]] · [[_System/Alignment-Spectrum|Alignment Spectrum]] · [[_System/Deception-Perception-Skills|Deception & Perception Skills]] · [[_System/Tier-Reference|NPC Tier Reference]] · [[_System/Attribute-Reference|Attribute Reference]]*
