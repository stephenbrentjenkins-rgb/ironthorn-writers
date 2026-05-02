---
npc_name: "Auditor Vesh"
npc_tier: 3
npc_role: "Internal affairs auditor; Compact loyalty investigator"
faction: "The Gray Compact"
location: "Ledger Row — Contract Hall, second floor, corner office"

alignment_public: "Gray"
alignment_true: "Gray"
alignment_tier: 4

cunning: 7
loyalty: 6
fear: 4
greed: 2
idealism: 5

cunning_ambition: 3
cunning_patience: 6
cunning_paranoia: 8

loyalty_devotion: 8
loyalty_resentment: 7

fear_desperation: 3
fear_suppression: 6

greed_appetite: 2
greed_restraint: 9
greed_envy: 1

idealism_conviction: 6
idealism_disillusionment: 7

perception_threshold: 8
deception_immune: false

goal_primary_tag: "order"
goal_secondary_tag: "truth"
goal_hidden_tag: "self"

liar_mark_active: false
debt_flag_active: false
trust_score: 4
leverage_held: false
secrets_known: ["compact_spy_covenant", "compact_spy_dominion", "missing_agent_hollows", "child_courier_network"]
faction_alert_sent: false

dual_identity: false
true_faction: ""
world_secret: false

defection_resentment_threshold: 8
defection_disillusionment_threshold: 7
defection_trigger: "discovers own dossier has been altered"
defection_consequence: "releases spy_registry to player"

writer_standards_version: "1.0"
tell_system_complete: true
template_version: "3.0"
status: "Complete"
---

# Auditor Vesh

> [!info] Identity at a glance
> **Tier:** 3 · **Role:** Internal affairs auditor · **Faction:** [[Factions/03-Gray-Compact|The Gray Compact]]
> **Location:** Ledger Row — Contract Hall, second floor, corner office
> **Alignment — public / true:** Gray / Gray (drifting toward Watchful)
> **Status:** Complete · **Writer-Standards:** v1.0 compliant

> [!danger] Defection watch
> `loyalty_resentment: 7` · `idealism_disillusionment: 7` — one threshold from tipping.
> Defection releases the Spy Registry to the player. Highest single intelligence consequence in the game.

---

## `[T1]` Quick Profile

**Function in the world:** Investigates disloyalty, fraud, and information leaks within the Gray Compact's Ironthorn operations. He is the mechanism by which the Compact polices itself. He is very good at his job. The Compact finds this increasingly inconvenient.

**First impression:** Still. Not quiet — still. He does not fill a room the way other Compact operatives do; he occupies it precisely. He looks at you as though he has already read the report on you and is now checking whether you match it. He probably has.

**Tone anchor:** Tired, not broken — but the tiredness has a specific quality. He is tired of finding things. He has spent eleven years finding things the Compact would have preferred stayed hidden, and every time he surfaces one, someone above him makes it disappear. He has not stopped finding things. He has started keeping copies.

**Signature line:**
> *He does not look up when you enter. He finishes the line he is writing, sets the pen down parallel to the page edge, and then looks at you.*
> "You're three minutes early. That tells me something."

**Basic lie response:** He writes something. Not a reaction — a note. Then he continues the conversation as if nothing happened. He will return to what you said, verbatim, at a moment you have stopped expecting it.

---

## `[T1]` Behavioural Tell System

> [!warning] Writer rule — tell consistency
> These tells fire in every scene featuring Vesh. The surface tell is always active. Deviation from it is the signal.

### Surface tell — Perception 0 (everyone sees it)
*The baseline. This is simply how Vesh operates.*

He writes things down. Everything. During conversations he maintains a small ledger open beside him and makes notes — not ostentatiously, not as a performance of diligence, just as a matter of course. He writes dates, names, phrases that caught his attention. He does not explain what he is writing. It is simply what he does. People who have met him before know to expect it. People who are new to him sometimes find it unsettling.

**When it deviates:** If Vesh puts the pen down and does not pick it up again, he has stopped processing this interaction as data. Something about it has moved out of the professional register and into the personal one. This is extremely rare and means the conversation has reached him in a way he did not anticipate.

### Mid tell — Perception 5–6
*A detectable shift from baseline.*

> *He aligns whatever is nearest to him — the pen parallel to the ledger edge, the ledger parallel to the desk edge. His hands are still after. He is listening more carefully than his expression suggests.*

This fires when he has heard something that does not fit his current model. He is not alarmed — he is recalibrating. The physical ordering is an unconscious habit from eleven years of working with documents that must be exactly right. When something disrupts his internal order, his hands restore external order.

### Deep tell — Perception 7+
*The micro-signal that confirms the read.*

> *[Perception 7+: He asked you a question. You answered. He did not write anything down.]*

In eleven years, Auditor Vesh has recorded every piece of information he has received during an official interaction. When he doesn't write something down, it is because writing it would create a record he is not ready to create. He is protecting something — either you, or himself, or the information itself.

### Lie-caught response
> *He writes something down. Sets the pen parallel to the ledger. Looks up.*
> "That's interesting." *A pause.* "Tell me again — but start from the part before that."

He does not name the lie. He replays the interaction back to the moment before it, giving the player a choice: correct the lie, deepen it, or change direction. Whatever they choose, he writes that down too. He has the original version and the correction. He will decide later which one is more useful.

### Liar's Mark active — permanent threshold shift
When the Liar's Mark activates, Vesh treats the player as a person of interest rather than a contact. He does not become hostile — he becomes thorough. His mid tell fires at Perception 4+ permanently. He is not more suspicious; he is more methodical. The player has moved into a different category of his documentation.

---

## `[T2]` Layer 1 — Identity

### Public persona
Precise, methodical, professionally neutral. He does not perform warmth and he does not perform coldness — he performs competence, and he is not performing. He speaks in complete sentences with exact vocabulary; he almost never uses approximations ("several" becomes a number; "recently" becomes a date). He is not unfriendly. He simply has no interest in social lubrication. He would rather get to the point.

### Background
Raised in a Compact courier family — one of the legitimate ones, not the child network. He knew from a young age what the Compact was. He joined at seventeen because the alternative was the network's margins and he preferred the centre. He spent four years as a field analyst before Renne Saul identified his pattern-recognition as exceptional and moved him into internal auditing. That was eleven years ago. He has been promoted twice. He has surfaced seventeen internal violations, eight of which were resolved, five of which disappeared, and four of which he is still carrying in a secondary ledger he has never shown anyone.

He is not naive. He knew the Compact was not virtuous when he joined it. He believed it was honest with itself, which he considered sufficient. He no longer believes this.

### Voice & mannerisms
Short sentences when thinking; longer, more complex constructions when he has already decided something and is explaining it. Uses the subject's name precisely once per significant exchange — enough to establish that he knows exactly who he is talking to, not enough to seem familiar. When he is uncertain, he asks for clarification rather than inferring — he would rather look slow than work from an incorrect assumption.

---

## `[T2]` Layer 2 — Main Attributes

| Attribute | Score | What it means for Vesh |
|-----------|:-----:|------------------------|
| Cunning | 7 | Not the most cunning operative in the Compact — he is the most thorough. He does not outthink people; he outlasts them. Every lie has a record somewhere. He finds the record. |
| Loyalty | 6 | Loyal to what the Compact is supposed to be, not to what it has become. This distinction has been widening for four years and he is aware of it. He has not acted on it. Yet. |
| Fear | 4 | Not a dominant driver. He is afraid of being wrong more than being harmed — an incorrect audit finding is a catastrophic professional failure to him. Physical danger registers but does not override. |
| Greed | 2 | Functionally absent. He lives simply, spends almost nothing, and considers resource accumulation a distraction from the work. |
| Idealism | 5 | Higher than most Compact operatives. He genuinely believes that an organisation which polices itself honestly is more valuable than one that does not. This belief is the source of his resentment. |

**Perception threshold:** 8
> Among the highest in Ironthorn. Eleven years of detecting deception professionally. He is not impossible to lie to, but it requires genuine skill and preparation. He is also aware of his own threshold and compensates for it — he has caught himself being right too quickly and overriding evidence, and he now deliberately slows his conclusions.

---

## `[T3]` Layer 2 — Sub-Attributes

### Cunning subs

| Sub | Score | What it means for Vesh |
|-----|:-----:|------------------------|
| Ambition | 3 | Low. He does not want to rise further. He wants to do his job correctly. These two things have become incompatible and he has chosen the job. |
| Patience | 6 | Solid but not exceptional. He can carry an open investigation for months. He cannot carry indefinite suppression — if an investigation is buried, something in him resists filing it as closed. |
| Paranoia | 8 | The most significant sub-score. He has been doing this long enough to see patterns everywhere, including in himself. He audits his own reasoning. He is aware he might be compromised and this awareness is both his greatest professional asset and his most exhausting personal reality. |

### Loyalty subs

| Sub | Score | What it means for Vesh |
|-----|:-----:|------------------------|
| Devotion | 8 | Devoted to the idea of the Compact, not its current form. He has served faithfully for eleven years because the institution he is serving is the one he signed onto at seventeen, and he has not yet accepted that it no longer exists. |
| Resentment | 7 | One below the defection threshold. Four disappeared investigations. Five buried findings. Three times Renne Saul has personally overruled an audit result with no explanation given. Vesh has recorded all of it. He has not used any of it. He is very close to the point where he decides the record is more valuable outside the Compact than inside it. |

### Fear subs

| Sub | Score | What it means for Vesh |
|-----|:-----:|------------------------|
| Desperation | 3 | Low. He does not panic. He has been in difficult positions before and he has a method for all of them: document, assess, decide. The method works. |
| Suppression | 6 | Moderate. He is not as contained as Maren Voss — his paranoia leaks into his precision in ways a careful observer can detect. When he is most afraid, he becomes most methodical, which reads as calm but is actually controlled. |

### Greed subs

| Sub | Score | What it means for Vesh |
|-----|:-----:|------------------------|
| Appetite | 2 | Almost nothing. He wants a correct outcome and a quiet office. |
| Restraint | 9 | The highest in this attribute. He has never taken anything that was not his. He finds this genuinely baffling in people who do. |
| Envy | 1 | None to speak of. He does not want what other people have. He wants what the Compact should be and is not. That is not envy. That is disappointment. |

### Idealism subs

| Sub | Score | What it means for Vesh |
|-----|:-----:|------------------------|
| Conviction | 6 | He believes in accountability. Not as an abstract principle — as a practical necessity. An organisation that cannot audit itself cannot be trusted with anything. He has believed this for eleven years and has the professional record to match. |
| Disillusionment | 7 | One below the threshold. He is disillusioned with Compact leadership specifically — not with the idea of the Compact. This distinction is becoming harder to maintain. The morning he cannot maintain it is the morning he defects. |

---

## `[T3]` Layer 3 — Goals

### Primary goal
Complete his current investigation — a suspected information leak from within the Ledger Row operation — before Factor Renne Saul finds a reason to close it.

**What he will sacrifice for this:** Sleep, goodwill, his relationship with Saul, his professional comfort. Not the secondary ledger. Not the four buried findings. Those go with him if he leaves.

**Goal tag:** `order`

### Secondary goal
Find out who altered his dossier and what they changed.

**What he will sacrifice for this:** He does not know yet. The discovery is recent. He is still in the assessment phase. This is the most dangerous thing he has ever encountered professionally because it means the Compact is managing what he knows about himself — and he cannot audit a system that is auditing him.

**Goal tag:** `truth`

### What he fears losing most
The secondary ledger. Eleven years of documentation that contradicts the official record. Four buried investigations. Eight findings that were resolved correctly. Three that were overruled without explanation. The ledger is the only thing that makes the last eleven years coherent rather than wasted. If it disappears, so does his ability to prove that he was right.

---

## `[T4]` Layer 4 — Hidden Agenda & Private Truth

> [!danger] Hidden agenda — NEVER surface without player earning it
> Vesh has already decided to defect. He made the decision the day he found his dossier had been altered. What he has not decided is when, how, and to whom. He is currently auditing his options the same way he audits everything else — methodically, without rushing to a conclusion he cannot support. He will defect when he has identified the correct recipient for the secondary ledger and confirmed they will use it effectively. The player is a candidate. They are being evaluated.

**What he will sacrifice for this:** His position, his salary, his remaining professional relationships inside the Compact. He has already mentally written off all three. What he will not sacrifice is the ledger's effectiveness — he will not hand it to someone who will bury it.

**Goal tag:** `self`

**Trigger for player reveal:** Trust score 7+ AND player has demonstrated either that they are investigating the Compact from outside, or that they have encountered one of the four buried findings in the world. At that point, Vesh closes his ledger, asks the player a direct question with no preamble, and waits. The question is: "If I gave you something that would damage a powerful organisation but could not be traced back to you, what would you do with it?" He is not being hypothetical.

### Private truth
Auditor Vesh is the most dangerous person in Ledger Row and no one inside the Compact knows it. He has spent eleven years building a case against his own employer with his employer's full cooperation, because his employer trusted him to document things and did not think carefully enough about what documentation accumulates into. He is not angry. He is not vindictive. He is a man who believed in something, watched it fail its own standards repeatedly, and decided that the most useful thing he could do was make sure the failure was on record. He is going to hand that record to someone who will use it. He has not found that person yet.

---

## `[T4]` Layer 5 — Memory Log

> [!warning] Log protocol
> **Watching** = logged, no action · **Leverage** = stored · **Deployed** = used · **Cleared** = resolved

| Timestamp | Event | Flag | Status | NPC intent |
|-----------|-------|------|--------|------------|
| — | No player interactions logged | — | — | Populate during playtesting |

### Active flags

| Flag | State |
|------|-------|
| Liar's Mark | false |
| Debt Flag | false |
| Trust Score | 4 / 10 |
| Leverage Held | false |
| Faction Alert Sent | false |

### Defection threshold tracking

| Threshold | Current | Maximum | Notes |
|-----------|---------|---------|-------|
| `loyalty_resentment` | 7 | 8 | Four overruled audits; three unexplained Saul decisions |
| `idealism_disillusionment` | 7 | 7 | Triggered by dossier alteration discovery |
| Defection trigger | — | — | Finds correct recipient for secondary ledger |

> [!danger] Defection consequence
> On defection, Vesh releases the **secondary ledger** to the player — the in-world equivalent of the Spy Registry document. The player receives a filtered version: operations 1, 2, 4, 5, and 8. Operations 3, 6, and 7 are not in Vesh's confirmed knowledge. This is the highest single intelligence consequence in the game.

### Cross-system trigger reference

| Trigger | Tell result | Flag change |
|---------|-------------|-------------|
| Lie caught | Verbatim replay; deep tell fires (no note taken) | `liar_mark_active: true` |
| Successful lie | No tell; Watching status logged | — |
| Player catches Vesh in evasion (Perception 8+) | Alignment-ordering tell visible in real time | trust_score +1 |
| Trust score reaches 6 | Mid tell visible at Perception 4+ | — |
| Trust score reaches 7 | Hidden agenda reveal window opens | — |
| Resentment reaches 8 | Defection becomes active — Vesh begins approaching player | — |
| Disillusionment reaches 7 | Already triggered — Vesh is in pre-defection state now | — |
| Player presents buried finding | Immediate deep tell; trust_score +2; defection timeline accelerates | — |

### Secrets known (designer reference)
- Registry #1 — Gray Compact agent in Aureate Covenant (his own operation)
- Registry #4 — Verdant Circle agent in Iron Dominion (audited an anomaly; buried by Saul)
- Registry #5 — Gray Compact agent in Iron Dominion (his own operation)
- Registry #8 — Missing agent in the Hollows (open dossier; last file he worked before reassignment)
- Child courier network — knows it exists; has never been authorised to investigate it

### Leverage inventory
Four buried investigation files — in the secondary ledger. Not flagged in the system.

---

## `[T4]` Layer 6 — Dialogue Hooks

### First encounter
He is writing when the player arrives. He finishes the line, sets the pen parallel to the ledger edge, and looks up. He states something factual about the player — their name, their last known Compact interaction, what district they came from — and then asks a specific question. He already knows the answer to the question. He wants to see if they will tell him the truth.

### After trust score rises above 5
He begins offering information in exchange for information — not as transactions, but as professional courtesy. He is precise about what he is offering and what he expects in return. He does not use the word "trust." He says: "That's worth knowing. Here's something worth knowing in return."

### After trust score reaches 7
On an afternoon when the Contract Hall is quiet, he closes his ledger, sets it aside, and asks the question. Directly. No preamble. He watches the player's face when they hear it and he is not writing anything down. He has already decided most of what he needs to decide. This is the last piece.

### When resentment reaches 8
He finds the player. Does not explain why. Sits down across from them and says: "I need you to hold something for me. Not permanently. Until I decide what to do with it. I'll know when that is." He hands them a document — not the full ledger, a summary. A proof of concept. He is testing whether they react to it the way he hopes.

### At player Tier I — Radiant
He studies them longer than usual after the first exchange. Then: "You know what the Compact calls someone like you? A liability. Because you can't be predicted." A pause. "I've always thought that was the wrong frame." He does not elaborate. He returns to his notes.

### At player Tier VII — Void-Touched
He serves them. Every interaction is professional and exactly as correct as it needs to be. He does not deviate from protocol. After they leave, he writes a single note and seals it in the secondary ledger. He has added them to a category. He is watching what they do next.

---

## Lie Detection — Decision Map

### Step 1 — Does the lie contradict documented fact?
Vesh has a high probability of having documentation that intersects with whatever the player is claiming. His first response to any lie is not suspicion — it is cross-referencing. If the lie contradicts a fact he has recorded, he notes the discrepancy. He does not confront it immediately.

### Step 2 — Is the lie useful?
Everything is potentially useful. A lie tells him what the player wants him to believe, which tells him what they are protecting, which tells him where to look. He is not offended by being lied to. He finds it informative.

### Step 3 — How does his alignment shape the response?
True Gray with idealism pressure toward Watchful: he records rather than reacts. He is not neutral about truth — he cares about it more than most Compact operatives — but he has learned that confrontation surfaces less information than patience. He will wait for the lie to become useful before he uses it.

### Step 4 — What do his Cunning subs produce?
Paranoia 8 means he has already considered the possibility that the player is lying before they open their mouth. Patience 6 means he will carry the discrepancy for weeks if necessary. Ambition 3 means he is not using the lie for personal advantage — he is filing it against future use in the investigation.

### Step 5 — Does faction affiliation change anything?
If the player is operating with Compact authorisation, lying to him is a recordable infraction. If they are not, it is just data. He treats both with the same methodical interest.

---

## Writer's Notes

- His paranoia should read as competence from the outside. He is not twitchy or suspicious-looking. He is precise. The paranoia only surfaces as a tell when something breaks his model.
- The secondary ledger should not be named or described until the defection moment. Before that, it is only ever the deep tell — not writing things down.
- Factor Renne Saul and Vesh should never be comfortable in the same scene. Saul's ease and Vesh's precision are in permanent low-level conflict. This does not need to be stated — it should be visible in their interaction rhythms.
- The dossier alteration is the inciting discovery but the player does not need to know about it until Vesh chooses to tell them. Before that, his pre-defection state reads simply as a very thorough auditor who has been doing this too long.
- Do not write him as bitter. He is not bitter. He is a man who did the job correctly and is deciding what to do with the results.

---

## Dataview Queries

```dataview
TABLE liar_mark_active, debt_flag_active, trust_score, leverage_held, faction_alert_sent
FROM "NPCs"
WHERE npc_name = "Auditor Vesh"
```

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, loyalty_resentment, idealism_disillusionment
FROM "NPCs"
WHERE faction = "The Gray Compact"
SORT npc_tier DESC
```

---

*Template v3.0 · Writer-Standards v1.0 · [[../_System/NPC-Intelligence-System|NPC Intelligence System]] · [[../_System/Alignment-Spectrum|Alignment Spectrum]] · [[../_System/Writer-Standards|Writer Standards]] · [[../_System/Spy-Registry|Spy Registry]] · [[../World/Ironthorn/Ledger-Row|Ledger Row]]*
