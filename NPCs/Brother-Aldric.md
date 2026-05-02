---
npc_name: "Brother Aldric"
npc_tier: 3
npc_role: "Cleric; spiritual director; public face of the Covenant in the Sanctum Ward"
faction: "Aureate Covenant"
location: "Ironthorn — Sanctum Ward (Chapter House public wing; Healer's Annex; Ward patrol route)"

alignment_public: "Light-III"
alignment_true: "Light-I"
alignment_tier: 3
# Public: Steadfast — principled, consistent, morally reliable
# True: Watchful — cautiously good, calculates the cost, not yet beyond doubt

cunning: 4
loyalty: 7
fear: 6
greed: 2
idealism: 8

cunning_ambition: 2
cunning_patience: 6
cunning_paranoia: 3

loyalty_devotion: 8
loyalty_resentment: 6
# WATCH: Resentment at 6 and climbing. Devotion is still higher — but the gap is closing.
# Defection becomes possible when resentment reaches 8, regardless of devotion.

fear_desperation: 3
fear_suppression: 7

greed_appetite: 1
greed_restraint: 9
greed_envy: 2

idealism_conviction: 8
idealism_disillusionment: 6
# WATCH: Disillusionment at 6. He still says the right words and means most of them.
# At 8, the performance and the belief become indistinguishable — even to him.

perception_threshold: 6
deception_immune: false

goal_primary_tag: "protection"
goal_secondary_tag: "redemption"
goal_hidden_tag: "truth"

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
status: "Draft"
---

# Brother Aldric

> [!info] Identity at a glance
> **Tier:** `=this.npc_tier` · **Role:** `=this.npc_role` · **Faction:** `=this.faction`
> **Location:** `=this.location`
> **Alignment — public / true:** `=this.alignment_public` / `=this.alignment_true`
> **Status:** `=this.status`

---

> [!danger] Writer anchor — read before writing any scene with this NPC
> **Tone:** Tired, not broken. He is still functioning. He still means what he says. The weight is real and he carries it without showing it except in small, specific ways.
> **The rule:** He never declares his inner state. He straightens things. He stops using names. He asks how you are. When he stops doing these things, something has changed.
> See [[_System/Writer-Standards]] before writing any dialogue or scene direction for this NPC.

---

## `[T1]` Quick Profile

**Function in the world:** Aldric is the Covenant's street-level face in the Sanctum Ward — he runs public services, performs spiritual direction for registered penitents (including the Throne spy he doesn't know is a spy), and is the first Covenant NPC most players will form a relationship with. He is also the first one whose doubt becomes visible.

**First impression:** A man of middle age in Covenant white who looks like he has been awake since before you arrived. He is courteous without being warm, attentive without being curious. He asks how you are before you ask him anything, and he listens to the answer in a way most people don't.

**Signature line:**
> *He does not argue. He sets whatever he is holding down, gives you his full attention, and says:*
> "Tell me what actually happened."

**Basic lie response:** He tilts his head slightly. Something in his face closes. He finishes the conversation politely and does not initiate one again that session.

---

## `[T1]` Behavioural Tell System

> [!important] Writer rule
> Tells are consistent across every scene. They do not vary by writer. Suppression score (7) means most tells are invisible under routine conditions — only fire under the specific pressures listed. Read [[_System/Writer-Standards]] Standard 2 before writing any tell into a scene.

### Surface tell — Perception 0 (everyone sees this)
**Baseline behaviour:** He asks how you are before you ask him anything. Every time. It is not performance — it is a habit so deep it has become structural. He is genuinely interested in the answer, and the genuineness is what makes the baseline legible.

**What deviation means:** When Aldric does not ask how you are, something has already happened in his internal state before the scene began. The player does not need high Perception to notice the absence — they need prior exposure to establish the baseline. First encounter: no signal. Third encounter: the absence registers.

**Scene writing note:** Write this tell into every scene with Aldric that is not a scene of acute crisis. In crisis, suppression overrides and he does not ask — that IS the tell firing as absence. In routine function (public ceremonies, standard meetings), he asks. Always.

---

### Mid tell — Perception 5–6
**Observable shift:** He straightens things. Specifically, objects near his hands — a book, a candle, a cup, whatever is on the surface nearest to him. He is not aware he does it. The objects do not need straightening. He sets them right anyway.

**What it indicates:** Unresolved discomfort. Something in the current situation or conversation is pressing against something he has not yet processed. This is not the same as catching a lie — it is the signal that he is carrying more than the scene is surfacing.

**Suppression interaction:** His suppression score (7) means this tell does not fire in low-stakes scenes even when he is carrying something. It fires when the unresolved discomfort is in active tension with the current context — when what is happening in front of him connects to what he has been not-thinking about.

**Cross-NPC interaction:** Ser Orvane has shared patrol routes with Aldric for eleven years. Orvane's Perception threshold is 6 — high enough to catch the mid tell in a direct interaction, but more relevantly, he has baseline familiarity. Orvane does not need a Perception check to know the straightening means something. He has seen it before. When writing a scene between Aldric and Orvane, Orvane can register the tell through relationship context, not skill — but the writer must not give Orvane more specific knowledge than relationship would supply. He knows something is wrong. He does not know what.

*[Perception 5–6: His hand moves to the nearest object — a candlestick, already level. He sets it right anyway. He does not seem to notice he did it.]*

---

### Deep tell — Perception 7+ (passive mode)
**Micro-signal:** He stops using your name. He was using it before, casually, the way a person does when they are fully present in a conversation. After the moment where something registers — a caught inconsistency, an unanswered question, a thing that does not fit — he stops. He does not do this consciously. He does not do it at all from that point in the conversation forward.

**What it confirms:** He has logged the player as carrying something he does not yet understand. He is not confronting. He is watching. The trust relationship is not broken, but it has entered a new phase.

**Perception 7+ stage direction format:**
*[Perception 7+: He has not used your name in three exchanges. He was using it before — it is not a formal mode he slips into. It is an absence.]*

**Cross-system link — lie catch:** When a player fails a Deception check against Aldric, the deep tell breaks surface regardless of Perception. Every player sees it: he stops using the name. In this context it is not subtle — it is the tell escaping suppression under pressure. The in-world response line plays immediately after.

**Cross-system link — Liar's Mark:** After Liar's Mark activates, the mid tell (straightening) becomes visible at Perception 4+ in all subsequent interactions. His suppression threshold has effectively dropped by 3 for that player only. The mark has changed how he carries himself around them specifically.

**Cross-NPC interaction — Maren Voss:** Voss has a Perception threshold of 8 and has worked in the same building as Aldric for seven years. She knows his deep tell. She has seen it fire once before, in a conversation with Inquisitor-Commander Leth that she was not supposed to observe. She noted it. She has not raised it with Aldric. If a scene brings Voss and Aldric into the same space when his deep tell is active, she registers it immediately — and the writer must decide whether she acts on that registration in the scene, banks it, or adds it to what she is already carrying.

---

### Tell state table — quick reference for writers

| NPC internal state | Surface tell | Mid tell | Deep tell | Suppression override |
|-------------------|-------------|----------|-----------|---------------------|
| Calm / routine function | Active (asks how you are) | Absent | Absent | No override |
| Carrying unresolved discomfort | Active | Active (Perception 5+) | Absent | No override |
| Active lie caught / suspicion triggered | Absent (deviation) | Active | Active (breaks surface) | Override — tell fires regardless |
| In formal/public Covenant function | Active | Absent | Absent | Yes — suppression 7 fully active |
| Resentment ≥ 8 | Active degrading | Active in low-stakes scenes | Occasional surface without trigger | Suppression weakening |
| Disillusionment ≥ 8 | Inconsistent | Active without pressure | Active without trigger | Suppression failing |
| Post-defection | New baseline — does not ask | New tell TBD | New tell TBD | New NPC, new system |

---

## `[T2]` Layer 1 — Identity

### Public persona
A devout, reliable, accessible cleric. The Covenant's institutional face at ground level — the person ordinary Ward residents go to with problems that are too complicated for the guard post and too small for the Archivist. He is present, unhurried, and consistent. People trust him because he has not yet given them a reason not to, and because his faith reads as genuine, which it is — or was, and now survives on momentum and a refusal to examine the gap.

### Background
Aldric came to the Covenant at seventeen, from a minor family in one of the occupied settlements outside Ironthorn. His family did not object. The Covenant paid well for early vocational commitments, and his family needed the payment. He has been told, and told himself, that this was a calling. He is no longer fully certain which part was true.

He has served in the Ward for eleven years. In that time he has performed last rites for forty-three people he knew by name, vouched for twelve people to the Inquisitorial Sub-Order's administrative process, and discovered — quietly, late — that three of the twelve were later classified as case files by the Sub-Order. He does not know what that classification means in practice. He has chosen, so far, not to find out.

The Throne spy in his caseload — a minor noble seeking absolution — has been meeting with him monthly for eighteen months. Aldric finds the meetings uncomfortable in a way he cannot name. The noble's penitence is technically correct but produces no change. He has been considering raising it with someone. He has not yet decided who.

### Voice & mannerisms
Measured. Uses full sentences. Never interrupts. There is a pause before his answers that is slightly too long — not hesitation, but consideration. He gives the impression of having heard worse, which is both reassuring and, if you think about it for a moment, not entirely.

When he is unsettled, he straightens things. When he is genuinely moved, he goes very still. It lasts about two seconds. He recovers cleanly.

> *Sample voice — on first meeting:*
> "The Ward keeps its own hours. You'll find that useful, or you won't. Either way, I'm here most mornings. Knock."

> *Sample voice — when something troubles him:*
> "I don't have an answer for that. I want to say I'll find one. I'm not sure that's honest."

> *Sample voice — when the player earns genuine trust:*
> "There are things I've been told not to ask about. I've been trying to decide whether that instruction is the kind that means something, or the kind that means someone was afraid of the answer."

---

## `[T2]` Layer 2 — Main Attributes

### Cunning — `=this.cunning` (4)
Aldric is not a schemer and knows it. He is perceptive enough to notice when he is being managed, slow enough to not always know why, and honest enough to be uncomfortable when he figures it out. His low cunning is not naivety — it is a genuine preference for directness that the Covenant's institutional culture has spent eleven years failing to erode.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Ambition | `=this.cunning_ambition` (2) | He wants nothing more than what he has. This is not contentment — it is a deliberate narrowing of desire, because wanting things inside the Covenant is how you learn what you are willing to do to get them. |
| Patience | `=this.cunning_patience` (6) | He will sit with discomfort for a long time before acting. This is both a virtue and the reason he has not yet done anything about the three people he vouched for. |
| Paranoia | `=this.cunning_paranoia` (3) | He still extends basic good faith. He is beginning to wonder if that was a mistake. |

---

### Loyalty — `=this.loyalty` (7)
He is loyal to the Covenant's stated purpose — the protection of the innocent, the eradication of genuine corruption — more than to its institutional structure. This distinction has not yet forced a decision. When it does, it will be the most important moment of his life.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Devotion | `=this.loyalty_devotion` (8) | He still believes. The belief is real. It is also increasingly doing a lot of heavy lifting for things that don't quite add up. |
| Resentment | `=this.loyalty_resentment` (6) | Eleven years of questions he was told not to ask. Three people he vouched for. A caseload of penitents whose penance never produces change. The resentment is not rage — it is the specific exhaustion of a person who has been doing the right thing and is beginning to wonder if the institution defines right the same way he does. |

> [!warning] Resentment watch
> `=this.loyalty_resentment` is at 6 and rising. Track this carefully. The tipping point is discovering that one of the people he personally vouched for was executed by the Sub-Order. At that point, resentment reaches 8 regardless of other factors, and defection becomes mechanically possible.

---

### Fear — `=this.fear` (6)
He is afraid of becoming someone who was wrong the whole time and didn't notice. This is not abstract — it is the specific fear of a man who has asked other people to account for themselves and is beginning to wonder if he has the same obligation.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Desperation | `=this.fear_desperation` (3) | He does not act recklessly when afraid. He goes quieter. This makes him harder to read at exactly the moments he is most at risk. |
| Suppression | `=this.fear_suppression` (7) | He performs composure better than almost anyone in the Ward. The tells are small: the straightening of things, the slightly overlong pause, the way he asks how you are. High suppression means most of what he is carrying does not surface without significant pressure. |

---

### Greed — `=this.greed` (2)
Functionally absent. He is not tempted by wealth, position, or material advantage. The Covenant's financial arrangements — the confiscated wealth, the century-old assets — produce a discomfort he files under doctrine and tries not to examine.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Appetite | `=this.greed_appetite` (1) | None. He would be easier to manage if there were. |
| Restraint | `=this.greed_restraint` (9) | His lack of greed is so visible it reads as a choice, which it is. |
| Envy | `=this.greed_envy` (2) | He does not want what others have. He occasionally wonders what it would be like to want something simple. |

---

### Idealism — `=this.idealism` (8)
The engine of everything. His faith in the Covenant's stated purpose — not its practice, its purpose — is still high. This is both the source of his resentment (the gap between purpose and practice) and the thing that will eventually make him dangerous, because a person with high idealism and rising disillusionment does not become cynical. They become a different kind of true believer, pointing somewhere else.

#### Sub-attributes

| Sub | Score | What it means for this NPC |
|-----|:-----:|----------------------------|
| Conviction | `=this.idealism_conviction` (8) | His principles do not bend under social pressure. They bend under evidence. You cannot argue him out of his beliefs, but you can show him something that makes the beliefs insufficient. |
| Disillusionment | `=this.idealism_disillusionment` (6) | He still means the words. He is beginning to notice that meaning them and acting on them are producing different results than he expected. This is the gap the player can walk through. |

---

### Perception threshold — `=this.perception_threshold` (6)
Moderate. He notices inconsistency in behaviour before he notices inconsistency in what is said — a player who is lying smoothly but acting strangely will register before the lie is caught. Threshold drops to 4 in private meetings. Rises to 8 in formal public Covenant function — he is performing the role and giving less attention to the individual.

### Deception immune — `=this.deception_immune`
False. He can be fooled. He is harder to fool than his base score suggests when the lie involves someone he has personally vouched for — the emotional investment lowers his threshold by 2 in those specific contexts.

---

## `[T3]` Layer 3 — Goals

### Primary goal
To do his job in a way that he can account for. He wants to look back at what he has done and find that it was actually what he thought it was while he was doing it.

**What he will sacrifice for this:** Comfort. Social standing within the Covenant. Eventually, the Covenant itself.
**Goal tag:** `=this.goal_primary_tag` (protection)

### Secondary goal
To understand what happened to the three people he vouched for. He has not yet asked the question out loud. He is constructing it internally — what to ask, who to ask, what the answer might mean for everything that came before it.

**What he will sacrifice for this:** The ability to keep not-knowing. Once he asks the question, he cannot un-ask it.
**Goal tag:** `=this.goal_secondary_tag` (redemption)

### What he fears losing most
The eleven years. If the Covenant's practice has been something other than its stated purpose, then eleven years of his life served that other thing. This is not a small thing to lose.

---

## `[T3]` Lie Detection — Decision Map

### Step 1 — Does the lie threaten his survival or primary goal?
Lies implicating him in harm — that he covered something up, that he vouched for someone he knew was dangerous — threaten his primary goal directly. He does not respond immediately. He files it. It surfaces later in a question that seems unrelated.

Lies about the player's own circumstances: noted, not acted on unless they compound.

### Step 2 — Can he bank this lie as leverage?
No. He does not think in terms of leverage. He holds the discrepancy in mind and waits for it to either resolve or accumulate into something he cannot explain away. Low cunning, high patience — he does not deploy what he knows, he accumulates until it forces a conclusion.

### Step 3 — How does his true alignment shape the response?
True Light-I (Watchful): he will not confront immediately. He offers the player a quiet opportunity to correct the record — a question framed as curiosity rather than accusation. If the correction comes, trust rises. If it doesn't, the discrepancy compounds.

He does not perform outrage. He gets quieter.

### Step 4 — What do his sub-attributes produce?
Low ambition + high patience + low paranoia: he does not convert the lie to advantage and does not pre-emptively escalate. He waits. The danger is that waiting is invisible — the player may not realise they are accumulating a record until Aldric asks a question that reveals he has been counting.

High suppression (7): his face gives almost nothing. The tells are the only external signals. Players below Perception 5 will miss them entirely.

### Step 5 — Does faction affiliation change anything?
He does not report automatically to the Sub-Order. He is currently holding back information about his penitent caseload — he is already in the habit of not fully reporting. A player who catches this can use it.

### In-world response line
> [!quote] What the player sees when the lie is caught
> *He finishes listening. A pause, slightly longer than usual. He picks up whatever is nearest — a candle, a book — and sets it down again.*
> "I appreciate you telling me that." *He does not say anything else.*
> *He is still present. He is now also watching. He does not use your name again in this conversation.*

### Tell cross-reference — lie catch
When this response line plays:
- Deep tell fires (name stops) — visible to ALL players regardless of Perception
- Mid tell fires (straightening) — visible to Perception 5+
- Liar's Mark activates in memory log
- Mid tell threshold drops to Perception 4+ for all future interactions with this player

### Cunning tell *(passive — Perception 7+ only)*
He stops using your name. He was using it before. He is not doing it consciously.

*[Perception 7+: He has not used your name in three exchanges. He was using it before — it is not a formal mode he slips into. It is an absence.]*

---

## `[T3]` Layer 4 — Memory Log

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

### Tell accumulation log
*Separate from the memory log — tracks how many times each tell has fired with this player. Used to determine when accumulated context changes how the tell is written.*

| Tell tier | Times fired | Context threshold reached? |
|-----------|------------|---------------------------|
| Surface (name ask) | 0 | No — need 2 exposures for baseline |
| Mid (straightening) | 0 | No — need 3 for pattern recognition |
| Deep (name stop) | 0 | No — fires once = signal; twice = confirmed |

---

## Dataview Queries

```dataview
TABLE liar_mark_active, debt_flag_active, trust_score, leverage_held, faction_alert_sent
FROM "NPCs"
WHERE npc_name = "Brother Aldric"
```

```dataview
TABLE npc_name, faction, loyalty, loyalty_devotion, loyalty_resentment
FROM "NPCs"
WHERE loyalty_resentment >= 5
SORT loyalty_resentment DESC
```

```dataview
TABLE npc_name, faction, idealism, idealism_conviction, idealism_disillusionment
FROM "NPCs"
WHERE idealism_disillusionment >= 5
SORT idealism_disillusionment DESC
```

---

## Writer's Notes

### Tone anchor
Tired, not broken. He is still functioning. He still means what he says. The weight is real and he carries it without showing it except in the three tells above. Every scene with Aldric is calibrated to this. If a scene feels like it is about his suffering, it is the wrong scene. The scene is about what he does despite the weight — and whether the player notices the weight at all.

### Cross-NPC tell interactions
- **Ser Orvane** — eleven years of shared patrol routes gives Orvane relationship-based baseline familiarity. He can register the surface tell absence without a Perception check. He cannot read the mid or deep tell without Perception 5+. Write their scenes with this gap: Orvane knows something has changed, does not know specifically what.
- **Maren Voss** — Perception threshold 8; has seen the deep tell fire once before in a scene she was not supposed to observe. She knows what it means. She has not told him she knows.
- **Throne Spy (penitent)** — Aldric's mid tell fires consistently during their monthly sessions. The spy has been observing it for eighteen months without understanding what it signals. This is a high-Perception player discovery: the spy cannot read the tell but the player can, and the tell is telling them something is wrong with this particular relationship.

### Story function
Aldric is the player's moral reference point in the early game. He needs to be genuinely sympathetic. If he reads as naive, his defection means nothing. If he reads as already-disillusioned, the reveal has no weight. The note to hold: a good person inside a bad institution, and the last one to fully know it.

### Quest hooks
- **"The Vouching"** — early game; Aldric asks the player to verify a former penitent's circumstances. The answer is wrong in a way Aldric has not let himself notice.
- **"Three Names"** — mid-game; player brings evidence about the missing case files. Resentment +2. Disillusionment +1. The pivot point of his arc.
- **"What the Archivist Knows"** — defection trigger; can be started by Aldric or Voss. They do not know the other is asking the same question.

### Defection consequence
When Aldric defects, he takes Maren Voss's sealed records with him — not planned, but the only evidence he can carry. Where he takes them depends on the player's trust score at defection time. Trust 8+: he comes to the player first. Trust below 4: he goes elsewhere, and the player has to find out who.

---

*[[../README|Back to Index]] · [[../Factions/01-Aureate-Covenant|Aureate Covenant]] · [[../World/Ironthorn/Sanctum-Ward|Sanctum Ward]] · [[../_System/Writer-Standards|Writer Standards]] · [[../_System/NPC-Intelligence-System|NPC Intelligence System]] · [[../_System/Alignment-Spectrum|Alignment Spectrum]]*
