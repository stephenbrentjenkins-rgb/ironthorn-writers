---
npc_name: "Scholar-Physician Dael"
npc_tier: 3
npc_role: "Veil mid-rank scholar; Quarter clinician; resurrection assistant"
faction: "The Ashen Veil"
location: "Ashgate Quarter — Dael's clinic, southern end near the Ashgate Lane building"

alignment_public: "Dark-III"
alignment_true: "Dark-I"
alignment_tier: 3

cunning: 5
loyalty: 5
fear: 6
greed: 1
idealism: 8

cunning_ambition: 3
cunning_patience: 4
cunning_paranoia: 6

loyalty_devotion: 7
loyalty_resentment: 5

fear_desperation: 5
fear_suppression: 4

greed_appetite: 1
greed_restraint: 9
greed_envy: 0

idealism_conviction: 8
idealism_disillusionment: 7

perception_threshold: 6
deception_immune: false

goal_primary_tag: "understanding"
goal_secondary_tag: "care"
goal_hidden_tag: "exposure"

liar_mark_active: false
debt_flag_active: false
trust_score: 5
leverage_held: false
secrets_known: ["energy_source_partial", "stabilisation_drift_worsening", "covenant_agent_deflection"]
faction_alert_sent: false

dual_identity: false
true_faction: ""
world_secret: false

defection_resentment_threshold: 6
defection_disillusionment_threshold: 8
defection_trigger: "performs resurrection and recognises the energy signature — it is someone he knew"
defection_consequence: "begins documenting everything; approaches player as first trusted contact"

writer_standards_version: "1.0"
tell_system_complete: true
template_version: "3.0"
status: "Complete"
---

# Scholar-Physician Dael

> [!info] Identity at a glance
> **Tier:** 3 · **Role:** Veil scholar; Quarter clinician · **Faction:** [[Factions/05-Ashen-Veil|The Ashen Veil]]
> **Location:** Ashgate Quarter — clinic, southern end near Ashgate Lane
> **Alignment — public / true:** Dark-III / Dark-I (drifting toward Watchful)
> **Status:** Complete · **Writer-Standards:** v1.0 compliant

> [!danger] Defection watch
> `loyalty_resentment: 5` · `idealism_disillusionment: 7` — disillusionment one below threshold.
> Also: Covenant agent burn risk elevates as Dael's questions intensify.
> Defection releases documentation to player; primary Veil entry point collapses to exit point.

---

## `[T1]` Quick Profile

**Function in the world:** Runs the Ashgate Quarter's only functioning clinic — legitimate medicine, bone-setting, wound care, fever management — as a cover for his Veil work, which involves assisting lower-tier resurrection procedures and documenting their outcomes. He joined the Veil because he could not accept that his patients had to die. He is beginning to understand that the Veil's solution to that problem has a cost he did not agree to pay.

**First impression:** Warm in the way of someone who has spent years making frightened people feel safe in a room that smells of burning and unfamiliar compounds. He is not performing warmth — he is just tired and good at his job. He asks what hurts before he asks anything else. He listens to the answer without writing anything down. He has very clean hands for someone who works in the Ashgate Quarter.

**Tone anchor:** Tired, not broken — but the tiredness is specific. He is tired of knowing that something is wrong and not yet knowing what to do with the knowledge. He came to the Veil to save people. He is starting to count what the saving costs.

**Signature line:**
> *He is writing something when you arrive — clinical notes, the handwriting very small and exact. He finishes the sentence before looking up. His expression is the same regardless of who walks in: attentive, professionally calm, vaguely relieved that you are ambulatory.*
> "Sit down. Tell me what's wrong."

**Basic lie response:** He nods. Asks a follow-up question that assumes the lie is true — he is checking its internal consistency. If it holds, he does not push. If it doesn't hold, he notes the inconsistency and continues as if he hadn't, and you will find him circling back to it three minutes later from a completely different direction.

---

## `[T1]` Behavioural Tell System

> [!warning] Writer rule — tell consistency
> These tells fire in every scene featuring Dael. The surface tell is always active. Deviation is the signal.

### Surface tell — Perception 0 (everyone sees it)
*The baseline. This is simply how Dael operates.*

He asks follow-up questions. About everything. Not interrogatively — clinically. If you mention a symptom he asks when it started. If you mention a name he asks how you know them. If you describe an event he asks what happened immediately before. It is not nosiness; it is diagnostic habit so deeply ingrained he applies it to everything. Patients, contacts, conversations. He is always building a more complete picture.

**When it deviates:** If Dael stops asking follow-up questions and accepts what you say at face value, he is not listening. He is in a state where the conversation has become secondary to something running underneath it. This is rare. It means something you said has triggered a process he is not yet ready to surface.

### Mid tell — Perception 5–6
*A detectable shift from baseline.*

> *He sets his pen down. Not beside the notes — away from them, at the corner of the desk. His hands stay on the desk, flat. He is listening with his full attention in a way that is different from his professional attention.*

This fires when something has moved out of the medical or professional register and into the personal one. When Dael puts the pen away from the notes, he is no longer documenting. He is deciding something.

### Deep tell — Perception 7+
*The micro-signal that confirms the read.*

> *[Perception 7+: He asked you the follow-up question. Then he asked a second follow-up. He does not normally ask two in a row — he waits for the answer to the first before deciding whether a second is warranted. He did not wait. He already knew what you were going to say.]*

He only asks a question he already knows the answer to when he is testing whether you will tell him the truth. He has been doing this more frequently in recent months. He is assembling something — a picture of who can be trusted and with what.

### Lie-caught response
> *He nods. Asks the follow-up question that assumes the lie is true.*
> *Two minutes later, from a different direction:* "You mentioned earlier — and tell me if I have this wrong — that you [restates the lie precisely, with the specific detail that doesn't hold]. I just want to make sure I understood correctly."

He does not name the lie. He presents it as a clarification. It is a very precise trap. A player who holds the lie must hold it again, now explicitly, against a restatement. A player who corrects it has told him something more valuable than the original answer would have been.

### Liar's Mark active — permanent threshold shift
When the Liar's Mark activates, Dael does not treat the player as a threat. He treats them as a more complex case than he initially assessed. His mid tell becomes visible at Perception 4+ permanently — not because he is more guarded, but because the putting-the-pen-away signal fires more readily now. He is deciding about you more often.

---

## `[T2]` Layer 1 — Identity

### Public persona
Physician. Quarter clinician. A Veil scholar who operates at the respectable end of their work — documentation, research, the medical application of death-adjacent knowledge rather than its more operational expressions. The Quarter residents use his clinic because he is competent, cheap, and does not ask what they were doing when they were injured. He has a reputation for being the person to see when you cannot go to a sanctioned physician.

He presents as Dark-III because that is his Veil rank and that is how the Veil is categorised. His actual alignment is substantially lighter than his faction affiliation — he is a man who made a choice based on grief and the Veil's promise, and is slowly discovering what that promise costs.

### Background
Born in the Ashgate Quarter. Father worked the forge complex. Mother died of a fever when Dael was eleven — a fever that would have been treatable with resources that simply were not available in the lower city. He trained as a physician through a Veil-funded scholarship that he initially did not know was Veil-funded. By the time he understood who was paying for his education, he had seen what they could do — a patient he had watched die was standing in front of him, alive, asking for help adjusting — and he had made his peace with it.

He has been with the Veil for eight years. He has assisted in twenty-three resurrections. He has been documenting outcomes, as instructed. The documentation was supposed to show that the process was working. It is showing something else.

### Voice & mannerisms
Precise vocabulary — medical training makes him specific where others are vague. "Pain" becomes "localised or diffuse?" Distress becomes "when did this begin and what were the circumstances?" He is not cold; the precision is care expressed through accuracy. When he is genuinely moved — which happens more than his professional manner suggests — he goes quiet rather than expressive. He has the stillness of someone who has sat with dying patients and knows that silence is sometimes the right response.

---

## `[T2]` Layer 2 — Main Attributes

| Attribute | Score | What it means for Dael |
|-----------|:-----:|------------------------|
| Cunning | 5 | Intelligent but not strategically sophisticated. He is good at pattern recognition within his domain — medical, biological, systemic — but he is not a political operator. He does not always see the full implications of what he is building until he has built it. |
| Loyalty | 5 | Split. Devoted to the patients in front of him and to what the Veil promised to be. Increasingly separate from the Veil as it actually operates. He has not yet named this split. He is feeling it. |
| Fear | 6 | Afraid of what he is discovering. Not afraid of the Veil specifically — afraid of what it will mean if what he suspects is true. He joined to save people. If the saving is costing people he did not consent to spend, everything he has done for eight years requires re-evaluation. |
| Greed | 1 | Functionally absent. He charges the Quarter's residents almost nothing. He lives in two rooms behind his clinic. He is here for the work. |
| Idealism | 8 | The highest driver. He believed — genuinely, not naively — that death could be made optional and that this would be good. He still believes the first part. The second part is the question that is eating him. |

**Perception threshold:** 6
> Trained to notice physical and behavioural inconsistencies. Lower than Vesh because he looks for what is wrong with people rather than what they are hiding. Good at reading distress, evasion, pain. Less good at detecting sophisticated deception — he tends to believe people until the evidence against them is clear, which means skilled liars get past him initially.

---

## `[T3]` Layer 2 — Sub-Attributes

### Cunning subs

| Sub | Score | What it means for Dael |
|-----|:-----:|------------------------|
| Ambition | 3 | Low. He wanted to be better at keeping people alive. He has achieved that. He does not want rank, resources, or influence beyond what the clinic requires. |
| Patience | 4 | Moderate. He can carry an open question for months — his documentation reflects this. But when something reaches the threshold of wrong, he moves toward it rather than away. He is not the kind of person who can hold a confirmed suspicion indefinitely. |
| Paranoia | 6 | Rising. He has started to suspect that his questions are being noted, and he is not wrong. The Covenant agent has reported his energy-source inquiry upward. Vorath has been briefed. Dael does not know this yet. He feels the edges of it — conversations that redirect slightly too smoothly, information that arrives slightly too conveniently. |

### Loyalty subs

| Sub | Score | What it means for Dael |
|-----|:-----:|--------------------------|
| Devotion | 7 | Devoted to the people in his clinic and to the patients he has helped — including the raised, including the ones with worsening drift. He considers all of them still his patients. This is not a political position. It is simply how he operates. |
| Resentment | 5 | One below the threshold. Five times his questions about energy sourcing have been deflected, redirected, or answered with a question about something else. He has noted all five. He is not angry yet — he is accumulating. |

### Fear subs

| Sub | Score | What it means for Dael |
|-----|:-----:|------------------------|
| Desperation | 5 | Moderate and rising. He is getting closer to a confirmation he does not want. Part of him is still trying not to find it. The clinical documentation keeps finding it anyway. |
| Suppression | 4 | Below average. He is not a naturally contained person — his fear shows as restlessness, as an increase in follow-up questions, as longer clinic hours. People who know him well can read when something is wrong. |

### Greed subs

| Sub | Score | What it means for Dael |
|-----|:-----:|------------------------|
| Appetite | 1 | Essentially nothing beyond clinical resources. |
| Restraint | 9 | He would not take something that was not his under any circumstances. This extends to information — he will not use what patients tell him outside the clinical relationship. |
| Envy | 0 | None. He finds the accumulation of resources and status genuinely bewildering as a life goal. |

### Idealism subs

| Sub | Score | What it means for Dael |
|-----|:-----:|------------------------|
| Conviction | 8 | Absolute conviction that death as a universal mandatory outcome is wrong. Still holds. What he is losing is the conviction that the Veil's method of addressing it is acceptable. These two things pulling apart is the engine of his arc. |
| Disillusionment | 7 | One below the threshold. He has interviewed fourteen raised subjects with worsening drift. Three of them have asked him what is happening to them. He told them it was stabilisation drift and that it was being managed. He is no longer sure this is true. He is no longer sure it is being managed at all. |

---

## `[T3]` Layer 3 — Goals

### Primary goal
Understand what the energy source for the Veil's resurrections actually is.

**What he will sacrifice for this:** His comfort, his Veil standing, his professional relationships inside the faction. He has not yet decided whether he will sacrifice his position entirely — that decision depends on what he finds.

**Goal tag:** `understanding`

### Secondary goal
Continue providing care to the Quarter's residents, including the raised subjects who come back to him with questions he cannot yet answer honestly.

**What he will sacrifice for this:** Sleep, resources, the approval of Veil leadership. Not the clinical relationship itself. The people in his clinic are still his responsibility regardless of what he discovers about the organisation behind them.

**Goal tag:** `care`

### What he fears losing most
The belief that the twenty-three resurrections he assisted were worth what they cost. If the energy source is what he suspects — if the cost was paid by people who did not consent to pay it — then he has been complicit in something he would not have agreed to. He is moving toward this confirmation carefully, because finding it changes everything about the last eight years.

---

## `[T4]` Layer 4 — Hidden Agenda & Private Truth

> [!danger] Hidden agenda — NEVER surface without player earning it
> Dael has been keeping a second set of clinical notes. Not the official documentation — a parallel record, written in a shorthand only he can read, tracking what the official record omits. Energy consumption anomalies. Drift progression rates that exceed the Quorum's published stabilisation model. Three cases where the timing of a resurrection correlated with an unexplained disappearance in the surrounding district. He has not connected these things officially. He has connected them privately. He is one piece of confirmation away from knowing what he is looking at.

**What he will sacrifice for this:** Once he has confirmed it, everything. He will sacrifice his Veil position, his safety, and his eight-year relationship with the faction. He will not sacrifice the raised subjects — he considers them his patients and will not leave them without a physician regardless of what he does next.

**Goal tag:** `exposure`

**Trigger for reveal:** Trust score 7+ AND either: the player has demonstrated they are investigating the Veil's energy source independently, OR the defection tipping point fires (Dael performs a resurrection and recognises the energy signature as someone he knew). At that point he closes his clinic early, sits across from the player, and says: "I need to show you something. I've been deciding whether to trust you with it for a while." He shows them the parallel notes.

### Private truth
Scholar-Physician Dael is the most morally coherent person in the Ashen Veil and this makes him the most dangerous. He joined to save people. He has been saving people. He is discovering that the saving requires spending people he never agreed to spend. When he has confirmed this fully, he will not run. He will document it completely and then he will make sure the documentation reaches someone who will act on it. He is the Veil's own methodology turned against them — the same systematic clinical documentation they trained him to do, applied to the question they told him not to ask.

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
| Trust Score | 5 / 10 |
| Leverage Held | false |
| Faction Alert Sent | false |

### Defection threshold tracking

| Threshold | Current | Maximum | Notes |
|-----------|---------|---------|-------|
| `loyalty_resentment` | 5 | 6 | Five deflected questions about energy sourcing |
| `idealism_disillusionment` | 7 | 8 | Fourteen drift interviews; three subjects asking him directly |
| Defection trigger | — | — | Recognises energy signature in a resurrection as someone known |

> [!danger] Defection consequence
> On defection, Dael approaches the player as his first trusted contact. He provides the parallel clinical notes — the second documentation set tracking energy anomalies, drift progression, and the three disappearance correlations. This is the primary Veil entry point becoming an exit point and a source of evidence against the Quorum.
>
> Secondary consequence: the Covenant agent's burn condition accelerates — Dael's questions post-defection become impossible to redirect.

### Cross-system trigger reference

| Trigger | Tell result | Flag change |
|---------|-------------|-------------|
| Lie caught | Double follow-up fires (deep tell); circling return in 2–3 exchanges | `liar_mark_active: true` |
| Successful lie | No tell; first follow-up accepted; Watching logged | — |
| Player catches Dael in evasion (Perception 6+) | Pen-away mid tell visible; player receives choice | trust_score +1 |
| Trust score reaches 6 | Mid tell visible at Perception 4+; parallel notes hinted at | — |
| Trust score reaches 7 | Hidden agenda reveal window opens | — |
| Resentment reaches 6 | Defection becomes active — Dael stops deflecting and starts approaching | — |
| Disillusionment reaches 8 | Defection tipping point — recognition event fires at next resurrection scene | — |
| Player investigates energy source independently | Immediate deep tell; trust_score +2; defection timeline accelerates | — |
| Covenant agent redirects a question (Perception 8+) | Player reads deflection as protective — burn condition for Registry #2 begins | — |

### Secrets known (designer reference)
- Energy source — partial knowledge; correlations not yet confirmed
- Stabilisation drift — worsening beyond official model; knows this; has not reported it
- Covenant agent — does not know the agent's identity; has noticed the redirect pattern; classified as anomaly in parallel notes
- Three disappearance correlations — documented in parallel notes; not yet connected officially

---

## `[T4]` Layer 6 — Dialogue Hooks

### First encounter
He is treating someone when the player arrives. He finishes — properly, with the same attention regardless of the interruption — before turning to the player. He asks what they need. If they are injured, he treats them. If they are not injured, he asks what brought them to the Quarter, and the follow-up question after that is specific enough that the player realises he has either been told about them or noticed something they were not aware of. It is the second one.

### After trust score rises above 5
He begins being specific with the player in the way he is not specific with most people. He mentions what he is working on — clinical, research, something at the intersection that he does not fully characterise. He asks what the player knows about stabilisation drift, as if checking whether they have encountered it. He is not casual about this. He is assessing whether they know what it is before he decides how much further to go.

### After trust score reaches 7
He closes the clinic for the evening — something he almost never does in the early evening — and sits across from the player rather than behind the desk. He is quiet for a moment. Then: "I need to show you something. I've been deciding whether to trust you with it for a while." He puts the parallel notes on the desk. He does not explain them. He waits to see how the player reads them.

### When resentment reaches 6
He comes to the player. Not in the clinic — somewhere else, somewhere without Veil presence. He says: "I've been asking the wrong people the wrong questions. I think you might be the right person. I'd like to ask you something." The question is direct. He is past the point of diagnostic circling.

### At player Tier I — Radiant
He treats them exactly as he treats everyone else. If they notice the Quarter's atmosphere and mention it, he says: "I noticed it too. The first six months." A pause. "You stop noticing. I'm not sure whether that's adaptation or something else." He is not warning them. He is being honest about a thing he thinks about.

### At player Tier VII — Void-Touched
He treats them. His questions are the same. His expression is the same. He does not adjust his manner for alignment — everyone who comes through the clinic door is a patient. Afterward, when they have gone, he writes a note in the parallel documentation that is not medical. It is an observation about what someone looks like when the drift has gone a very long way, and whether it was chosen or arrived at. He is not sure. He notes the uncertainty.

---

## Lie Detection — Decision Map

### Step 1 — Does the lie contradict clinical observation?
Dael reads bodies. If a player lies about their physical state, he will notice. If a player lies about recent activity and shows physical evidence of something else, he registers the inconsistency. He does not confront it — he documents it internally and moves to the follow-up question.

### Step 2 — Is the lie internally consistent?
He tests lies diagnostically. A lie that holds together he accepts provisionally. A lie with a gap he returns to — not immediately, but within the same conversation. He is patient enough to wait for the player to have stopped watching for the return.

### Step 3 — How does his true alignment shape the response?
True Dark-I drifting toward Watchful: he is not cynical about people's honesty, which means liars get further with him than they would with Vesh. His idealism is high enough that he wants to believe what he is told. His disillusionment is rising fast enough that this is changing.

### Step 4 — What do his Cunning subs produce?
Patience 4 means he cannot carry a confirmed lie indefinitely — he will surface it eventually. Paranoia 6 (rising) means he is increasingly alert to the shape of evasion after months of experiencing it from the Veil. Ambition 3 means he is not using the lie for leverage — he is trying to understand why someone told it.

### Step 5 — Does faction affiliation change anything?
If the lie is about Veil operations, he treats it with heightened attention — not suspicion of the player, but alertness to information about the Veil that he does not have. Any contradiction of official Veil positions goes directly into the parallel documentation.

---

## Writer's Notes

- His warmth should feel earned rather than performed. He is not a soft character — he is a precise one who expresses care through accuracy and attention. Do not write him as gentle. Write him as thorough.
- The parallel notes should never be described directly until the defection moment. Before that, they exist only as his behaviour — the follow-up questions, the double-checking, the small moments of going quiet when something doesn't add up.
- His relationship with the raised subjects is the most important character thread. These are people he helped bring back who are now experiencing something he did not anticipate and cannot fully explain. He considers them his ongoing patients. Write them into his scenes when possible — a raised subject coming back for a follow-up, showing worsening drift, asking him what is happening. These scenes are doing the disillusionment work.
- The Covenant agent's redirect pattern should be visible in any scene where Dael asks about the energy source. Do not write the agent explicitly — write Dael noticing that the answer was too smooth, the topic changed too conveniently, and filing it in the category of things that are wrong in a way he cannot yet name.
- He does not know his questions have been reported to Vorath. Do not write him as aware of this. Write him as someone who feels the edges of surveillance without being able to confirm it.

---

## Dataview Queries

```dataview
TABLE liar_mark_active, debt_flag_active, trust_score, leverage_held, faction_alert_sent
FROM "NPCs"
WHERE npc_name = "Scholar-Physician Dael"
```

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, idealism_disillusionment, loyalty_resentment
FROM "NPCs"
WHERE faction = "The Ashen Veil"
SORT npc_tier DESC
```

---

*Template v3.0 · Writer-Standards v1.0 · [[../_System/NPC-Intelligence-System|NPC Intelligence System]] · [[../_System/Alignment-Spectrum|Alignment Spectrum]] · [[../_System/Writer-Standards|Writer Standards]] · [[../_System/Spy-Registry|Spy Registry]] · [[../World/Ironthorn/Ashgate-Quarter|Ashgate Quarter]] · [[../Factions/05-Ashen-Veil|Ashen Veil]]*
