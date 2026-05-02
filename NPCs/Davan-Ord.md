---
npc_name: "Davan Ord"
npc_tier: 2
npc_role: "Forge master; repair annex operator"
faction: "None — independent"
location: "Ashgate Quarter — Davan Ord's Annex; primary forge complex"

alignment_public: "Gray"
alignment_true: "Gray"
alignment_tier: 4

cunning: 4
loyalty: 6
fear: 5
greed: 3
idealism: 5

cunning_ambition: 2
cunning_patience: 7
cunning_paranoia: 6

loyalty_devotion: 7
loyalty_resentment: 5

fear_desperation: 4
fear_suppression: 6

greed_appetite: 3
greed_restraint: 7
greed_envy: 1

idealism_conviction: 5
idealism_disillusionment: 6

perception_threshold: 5
deception_immune: false

goal_primary_tag: "continuity"
goal_secondary_tag: "distance"
goal_hidden_tag: "decision"

liar_mark_active: false
debt_flag_active: false
trust_score: 5
leverage_held: false
secrets_known: ["veil_delivery_materials", "ashgate_lane_building_access"]
faction_alert_sent: false

dual_identity: false
true_faction: ""
world_secret: false

tipping_point_trigger: "not-thinking becomes unsustainable — player presents material or information that names what he has been delivering"
tipping_point_consequence: "forge becomes story location; Ord becomes primary access point to Ashgate Lane building; alliance or refusal"

writer_standards_version: "1.0"
tell_system_complete: true
template_version: "3.0"
status: "Complete"
---

# Davan Ord

> [!info] Identity at a glance
> **Tier:** 2 · **Role:** Forge master; repair annex operator · **Faction:** Independent
> **Location:** Ashgate Quarter — Davan Ord's Annex; primary forge complex
> **Alignment — public / true:** Gray / Gray
> **Status:** Complete · **Writer-Standards:** v1.0 compliant

> [!warning] Watch flag — tipping point approaching
> `idealism_disillusionment: 6` · `cunning_paranoia: 6`
> Has been carefully not-thinking about Veil deliveries for two years. Approaching the point where not-thinking is no longer sustainable. Player interaction is the likely trigger.

---

## `[T1]` Quick Profile

**Function in the world:** Runs the best repair operation in Ironthorn's lower city and handles the forge complex's most technically demanding commissions. He will work on anything from any faction without comment. He has been doing this for twenty years in the Ashgate Quarter and has long since stopped asking who things belong to or what they are used for. He has noticed certain materials being delivered to the Ashgate Lane building at irregular intervals. He has been carefully not thinking about what they are used for. He is approaching the point where not-thinking is no longer sustainable.

**First impression:** Large, methodical, quiet in the way of someone who spends most of the day in a loud place and values the absence of noise when it arrives. His hands are always doing something — a tool, a component, a piece of cloth he is using to wipe something down. He looks at whatever you bring him before he looks at you. He is assessing whether the work is interesting before he decides whether the conversation is.

**Tone anchor:** Tired, not broken — the specific tiredness of a man who has made peace with most things and is encountering something he cannot make peace with yet. He is not conflicted dramatically. He is just finding that a thing he has been setting aside keeps coming back to the front of the shelf.

**Signature line:**
> *He does not stop what he is doing when you approach. He turns the component over in his hands once, sets it down, wipes his hands on the cloth at his belt, and looks at you.*
> "What needs doing."

Not a question. An opening.

**Basic lie response:** He accepts it. Nods once. Returns to what he was doing. He will not follow up — not in that conversation. But the next time you bring him something, there is a pause before he picks it up. He is deciding whether the work is still straightforward.

---

## `[T1]` Behavioural Tell System

> [!warning] Writer rule — tell consistency
> These tells fire in every scene featuring Ord. The surface tell is always active. Deviation is the signal.

### Surface tell — Perception 0 (everyone sees it)
*The baseline. This is simply how Davan Ord operates.*

He looks at the work first. Whatever you bring him — equipment, materials, a commission request — he examines it before he engages with you. Turns it over, checks the wear, tests the weight, assesses the damage. This is not rudeness; it is professional priority. The work is always the first thing. Once he has assessed it, he looks at you.

**When it deviates:** If Ord looks at you before looking at the work, something about your arrival has moved into a register that the work cannot address. This happens rarely. It means he already knows what you are bringing before you show it to him, or what you are carrying is not the real thing you are bringing.

### Mid tell — Perception 5–6
*A detectable shift from baseline.*

> *He sets down whatever he is holding. Not to the side — he puts it down fully, both hands free. He is not picking it up again until this is done. He is giving this his complete attention, which is not something he does casually.*

This fires when something has crossed from professional into personal. When Ord puts down his work completely, he has decided that what is happening right now is more important than the job. For a man whose primary relationship is with the work, this is significant.

### Deep tell — Perception 7+
*The micro-signal that confirms the read.*

> *[Perception 7+: He asked you where the material came from. He has never asked that before. In twenty years of working in this district, he does not ask where things come from. He asked this time.]*

Ord's professional identity is built on not asking. When he asks, something has become more important to him than the professional distance the not-asking maintains. He is moving toward something he has been moving away from for a long time.

### Lie-caught response
> *He nods once. Picks the work back up.*
> "Right."

That's it. He does not press. He does not signal that he caught anything. He returns to the job. But the next commission takes slightly longer than it should, and when he hands it back, he holds it for a half-second before releasing it — as if deciding whether to say something. He doesn't. Not yet.

### Liar's Mark active — permanent threshold shift
When the Liar's Mark activates, Ord's approach to future commissions changes subtly. He checks materials more carefully. He asks one question per job that he would not normally ask — about the origin, the intended use, the timeline. He is not confrontational. He is building a more complete picture than he used to want.

---

## `[T2]` Layer 1 — Identity

### Public persona
The best forge master in the lower city, possibly in Ironthorn overall. Faction-neutral by long practice — he has repaired Covenant equipment, Compact contracts, and Veil-adjacent materials in the same week without comment. His neutrality is his business model and his professional identity simultaneously. He is not warm but he is fair: prices are consistent, timelines are met, quality is reliable. He has a reputation that twenty years of exactly this behaviour has built, and he protects it by not asking questions.

### Background
Born outside Ironthorn — a mining settlement two days east where his father worked as a metalsmith. Came to Ironthorn at seventeen as an apprentice to one of the Quarter's forge masters. Stayed because the work was there and leaving requires a reason he has never found. He has been in the same building for fifteen years. He has watched four forge masters retire around him and now runs the complex's most demanding commissions by default, because no one else in the district has his depth of experience.

He has known the Quarter is Veil-adjacent since his second year here. He decided then that this was not his problem — his problem was the work. He has maintained this position through deliberate, practiced incuriosity. The deliveries to the Ashgate Lane building are the first thing that has tested that position in years, because the materials he occasionally sees in transit are ones he can identify by type, and their type does not match legitimate industrial use.

### Voice & mannerisms
Short sentences. Economical. He does not explain himself unless asked and does not ask for explanations unless necessary. When he is thinking, he is quiet — not uncomfortable silence, just the absence of speech while something is being processed. He uses trade vocabulary precisely and common vocabulary approximately; he is more exact when discussing metal than when discussing anything else. Occasional dry observation delivered without apparent humour but clearly intended as such — it lands slowly.

---

## `[T2]` Layer 2 — Main Attributes

| Attribute | Score | What it means for Ord |
|-----------|:-----:|------------------------|
| Cunning | 4 | Not a strategist. He is perceptive within his domain — material quality, structural integrity, the logic of how things are made and how they fail — but he does not think politically. He misses implications that Vesh or Maren would catch immediately. |
| Loyalty | 6 | Loyal to the Quarter, to the regulars who bring him work, and to the professional standard he has maintained for twenty years. Not loyal to any faction. The independence is load-bearing — he would not work for a faction exclusively even if asked. |
| Fear | 5 | Present but managed. He is afraid of what knowing will require of him. Not-knowing has been the management strategy. It is becoming less effective. |
| Greed | 3 | Low. He charges fair prices and lives simply. He has enough. He does not think much about having more. |
| Idealism | 5 | Moderate. He believes in doing the work correctly, treating people fairly, and maintaining the neutrality that makes him useful to everyone. These are not grand principles — they are operating standards. They are, however, real. |

**Perception threshold:** 5
> Average. He reads materials and mechanical systems well. He reads people less precisely — his incuriosity has been practiced long enough that he has also practiced not-looking at people too carefully. This is changing as the paranoia sub rises.

---

## `[T3]` Layer 2 — Sub-Attributes

### Cunning subs

| Sub | Score | What it means for Ord |
|-----|:-----:|------------------------|
| Ambition | 2 | Essentially absent. He wanted to be the best at his work in his district. He achieved this. He has not recalibrated upward. |
| Patience | 7 | High. He has been carrying the not-thinking about the deliveries for two years. He can hold an unresolved thing for a long time before it demands resolution. He is close to that demand now. |
| Paranoia | 6 | Rising. He has started noting patterns in the deliveries — timing, material type, the specific individuals who bring them. He is not tracking this deliberately. He is just finding that he remembers it. |

### Loyalty subs

| Sub | Score | What it means for Ord |
|-----|:-----:|------------------------|
| Devotion | 7 | Genuinely devoted to the Quarter and to the people he has been serving for twenty years. The regulars matter to him in the concrete, specific way that long professional relationships produce. He knows their equipment. He knows their repair patterns. He knows which ones are struggling. |
| Resentment | 5 | One below threshold. He resents, quietly, that something has been placed in his path that is going to require him to make a decision he did not want to make. He does not resent a person — he resents the situation. The not-thinking was a reasonable accommodation for twenty years. It is becoming unreasonable. |

### Fear subs

| Sub | Score | What it means for Ord |
|-----|:-----:|--------------------------|
| Desperation | 4 | Not dominant. He is not panicking. He is doing what he always does — working, waiting, not-deciding until deciding becomes unavoidable. |
| Suppression | 6 | Moderate. The fear shows as increased thoroughness — he checks materials more carefully than he used to, asks slightly more questions than he used to, takes slightly longer on jobs he would have completed without hesitation two years ago. |

### Greed subs

| Sub | Score | What it means for Ord |
|-----|:-----:|------------------------|
| Appetite | 3 | He wants enough materials to keep the forge running and enough commissions to justify them. That is the full extent. |
| Restraint | 7 | He has never taken a commission that required him to compromise the quality of his work or the neutrality of his position. He has been offered both types. He declined both. |
| Envy | 1 | None. He has what he needs. |

### Idealism subs

| Sub | Score | What it means for Ord |
|-----|:-----:|------------------------|
| Conviction | 5 | He believes in the neutrality. It is a practical belief as much as a principled one — neutrality is what makes him useful across all factions. But it is not purely instrumental. He thinks it is the right way to operate. |
| Disillusionment | 6 | One below the threshold. The deliveries are testing the neutrality. He has been neutral about things he did not know. He is beginning to know. Neutrality about things you know is a different thing. He is not sure it is the same thing at all. |

---

## `[T3]` Layer 3 — Goals

### Primary goal
Keep the annex running and the forge commissions coming. Maintain the twenty-year professional standard. Do not become a problem for anyone. Do not become anyone's problem.

**What he will sacrifice for this:** A great deal. He has sacrificed curiosity, comfort, certainty. He is approaching the limit of what can be sacrificed without becoming someone he does not recognise.

**Goal tag:** `continuity`

### Secondary goal
Maintain the distance from the Ashgate Lane building and whatever is happening in it. Not investigate. Not confirm. Continue not-knowing for as long as not-knowing remains available as a position.

**What he will sacrifice for this:** He is not sure anymore. This is the problem.

**Goal tag:** `distance`

### What he fears losing most
The neutrality. Not as an abstract principle — as a working condition. If he knows, he has to decide. If he decides, he is no longer neutral. If he is no longer neutral, the twenty years of professional distance collapses, and with it the thing that has made him useful and left alone and able to do the work without it costing him more than work costs.

---

## `[T4]` Layer 4 — Hidden Agenda & Private Truth

> [!danger] Hidden agenda — NEVER surface without player earning it
> Davan Ord knows more than he has admitted to himself. He knows the delivery materials are biological — bone-adjacent, preservation-compound-adjacent, the kind of thing that shows up in Veil-adjacent supply chains if you know what you are looking at, and he knows what he is looking at. He has not named this knowledge. He is holding it in the pre-verbal category where things go when naming them would require acting on them. The player naming it before he does is the tipping point event.

**What he will do when the tipping point fires:** He will be still for a moment. Then he will set down whatever he is holding. Then he will ask the player one question — not about the Veil, not about the materials. About what the player is going to do about it. He is deciding whether they are someone he can give the Ashgate Lane access information to. He has been inside that building once, two years ago, to repair a structural element. He remembers the layout.

**Goal tag:** `decision`

**Trigger for reveal:** Trust score 7+ AND player presents material or information that names the delivery contents directly. OR: disillusionment reaches threshold naturally through game events. At that point he does not initiate — he responds to the player. He has been waiting for someone to say it first so that the naming is not his.

### Private truth
Davan Ord is not naive, has never been naive, and has known for two years what is probably happening in the building at the end of Ashgate Lane. He has also known for two years that knowing and doing something about knowing are two different things, and that he has dependents — the forge workers, the regular customers, the Quarter's operational fabric — whose stability is attached to his neutrality. He is a man who made an accommodation and kept making it until the accommodation became complicity, and he is in the exact moment before he decides whether to stop. The player is the first person he has encountered who might make stopping feel like something other than destruction.

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

### Tipping point tracking

| Threshold | Current | Maximum | Notes |
|-----------|---------|---------|-------|
| `idealism_disillusionment` | 6 | 7 | Two years of delivery observations; materials identified by type |
| `cunning_paranoia` | 6 | 8 | Pattern-noting has become involuntary |
| Tipping point trigger | — | — | Player names the delivery contents directly; OR disillusionment reaches 7 |

> [!info] Tipping point consequence
> Forge becomes story location. Ord provides Ashgate Lane building layout from memory — one visit, two years ago. This is the primary physical access route for the Veil's Ironthorn operations. Player can use it for investigation, confrontation, or to bring information to Dael. Ord does not accompany the player. He gives them the layout and returns to work. He will not discuss it again unless the player initiates.

### Cross-system trigger reference

| Trigger | Tell result | Flag change |
|---------|-------------|-------------|
| Lie caught | Single nod; work resumed; half-second hold on next handback | `liar_mark_active: true` |
| Successful lie | No tell; no follow-up | — |
| Player catches Ord's evasion (Perception 5+) | Work-down mid tell visible; player receives choice | trust_score +1 |
| Trust score reaches 6 | Begins asking one question per commission; mid tell at Perception 4+ | — |
| Trust score reaches 7 | Tipping point window opens | — |
| Player presents delivery material information | Immediate deep tell (asks where it came from); tipping point fires | — |
| Disillusionment reaches 7 | Tipping point fires naturally — Ord approaches player after a commission | — |

### Secrets known (designer reference)
- Veil delivery materials — biological/preservation compounds; identified by type; not named internally
- Ashgate Lane building — visited once for structural repair; knows internal layout of ground floor

---

## `[T4]` Layer 6 — Dialogue Hooks

### First encounter
He looks at whatever the player brings before he looks at them. Assesses the work. Names a price and a timeline without negotiation — the numbers are fair and they are not opening positions. If the player tries to negotiate, he looks at them once and then looks back at the work. The price is the price. If they bring nothing and are just present in the Quarter, he notices them the way he notices everything — catalogues them, files them, returns to the job.

### After trust score rises above 5
He begins making small observations while working on their commissions — about the equipment, about the wear pattern, about what the damage suggests about how the player moves or fights. He is not building rapport consciously. He is just being thorough, and thoroughness with people he has seen multiple times produces something that functions like familiarity.

### After trust score reaches 7
He hands back a finished commission, holds it for a moment, and says: "You've been in the lower city long enough to know what the Ashgate Lane building is." Not a question. He is checking whether they will confirm it — whether they have the same knowledge he has been carrying. He is not ready to go further than that yet. But he asked.

### When tipping point fires
He sets down the work. Both hands free. He looks at the player directly. "I need to ask you something." A pause. "What are you going to do about it." He does not specify what 'it' is. He does not need to. If the player responds in a way that tells him they are going to do something, he goes to the back of the annex, comes back with a piece of paper, and draws a floor plan from memory. Ground floor only. He was there once. He remembers it exactly. He hands it to them. "I repaired a support beam. Two years ago. They paid well and didn't ask for anything else." Another pause. "I should have asked what it was for."

### At player Tier I — Radiant
He works on their equipment without comment. When he hands it back, he says: "You're going to have a hard time in this district." Not unkind. Factual. He has seen alignment before. He knows what the Quarter does to it over time. He does not say this. He just hands back the equipment and lets them decide what to do with the observation.

### At player Tier VII — Void-Touched
He works on their equipment. He does not ask questions he would ask other customers. He names a higher price than usual — not dramatically higher, just higher. He does not explain it. If pushed: "The work is the same. The circumstances aren't." He is not brave enough to refuse. He is not willing to pretend the circumstances are neutral.

---

## Lie Detection — Decision Map

### Step 1 — Does the lie affect the commission?
If a player lies about material origin or equipment provenance, it affects how he handles the job. He will notice material inconsistencies — metal composition, wear patterns, residue — that contradict the stated origin. He does not confront the lie. He accounts for it in the work.

### Step 2 — Does the lie involve the Ashgate Lane building?
If yes, he files it immediately and permanently. He does not react. He does not ask follow-up questions. But the lie is now part of his model of this player, and his model determines how much he eventually shares.

### Step 3 — How does his alignment shape the response?
True Gray: he absorbs and processes. He is not going to confront a lie in a professional context — that would break the neutrality. He is going to let the lie exist and factor it into future calculations. He is a man who has been running quiet assessments for twenty years without acting on most of them.

### Step 4 — What do his Cunning subs produce?
Patience 7 means he will carry a discrepancy indefinitely without surfacing it. Paranoia 6 means he is noting more than he used to — the pattern-recording has become involuntary. Ambition 2 means he is not using any of this for personal advantage. He is just building a more accurate picture of what is around him.

### Step 5 — Does faction affiliation change anything?
He is independent. Faction affiliation in a player changes how he prices jobs and how much follow-up he asks for, but it does not change his willingness to do the work. The tipping point changes this — after it fires, he will not take commissions from confirmed Veil operatives. He will not explain why. He will just be too busy.

---

## Writer's Notes

- He should never seem like he is waiting for the plot to happen. He is always working. Every scene with him involves work in progress. The dialogue happens alongside the work, not instead of it.
- The not-thinking is the most important character element. It should read as an active maintenance effort, not a passive state. He works at not-knowing. The player can see the seams of this effort if they look at the right moments.
- The floor plan is the tipping point payoff. Do not rush it. It should feel like something heavy being set down — a relief and a commitment simultaneously.
- His relationship with the Quarter's regulars should be present in background texture — a regular dropping off equipment, an exchange that is clearly old and practiced, a repair completed for someone who clearly cannot pay the full price and isn't being asked to. These moments establish what he is protecting by maintaining the neutrality.
- Do not write him as conflicted in a theatrical sense. He is not agonised. He is a practical man dealing with a practical problem that has moral dimensions he would prefer not to have. The tone is tired, not broken — specifically the tiredness of someone who has been very good at not-deciding and is running out of road.

---

## Dataview Queries

```dataview
TABLE liar_mark_active, debt_flag_active, trust_score, leverage_held, faction_alert_sent
FROM "NPCs"
WHERE npc_name = "Davan Ord"
```

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, idealism_disillusionment
FROM "NPCs"
WHERE location = "Ashgate Quarter" OR contains(location, "Ashgate")
SORT npc_tier DESC
```

---

*Template v3.0 · Writer-Standards v1.0 · [[../_System/NPC-Intelligence-System|NPC Intelligence System]] · [[../_System/Alignment-Spectrum|Alignment Spectrum]] · [[../_System/Writer-Standards|Writer Standards]] · [[../World/Ironthorn/Ashgate-Quarter|Ashgate Quarter]]*
