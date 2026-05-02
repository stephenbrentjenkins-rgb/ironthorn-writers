---
npc_name: "Sevin"
npc_tier: 3
npc_role: "Tolerance Director; Office of Tolerance; lower-city power broker"
faction: "None — city employee; Throne-adjacent"
location: "Wound Market — Office of Tolerance, eastern end of the market"

alignment_public: "Unreadable (Perception 8 required)"
alignment_true: "Gray"
alignment_tier: 4

cunning: 9
loyalty: 3
fear: 2
greed: 4
idealism: 2

cunning_ambition: 4
cunning_patience: 10
cunning_paranoia: 5

loyalty_devotion: 4
loyalty_resentment: 3

fear_desperation: 1
fear_suppression: 9

greed_appetite: 4
greed_restraint: 6
greed_envy: 1

idealism_conviction: 2
idealism_disillusionment: 9

perception_threshold: 10
deception_immune: false

goal_primary_tag: "equilibrium"
goal_secondary_tag: "leverage"
goal_hidden_tag: "regret"

liar_mark_active: false
debt_flag_active: false
trust_score: 4
leverage_held: true
secrets_known: ["sevayne_mortality_partial", "spy_network_lower_city", "hollows_access_points", "certificate_19_years_ago", "collectors_true_loyalty", "vesh_defection_risk"]
faction_alert_sent: false

deception_immune_note: "Not immune — but detecting a lie told to Sevin requires Perception 12, which does not exist as a standard player stat. For practical purposes she cannot be successfully lied to."

writer_standards_version: "1.0"
tell_system_complete: true
template_version: "3.0"
status: "Complete"
---

# Sevin

> [!info] Identity at a glance
> **Tier:** 3 · **Role:** Tolerance Director · **Faction:** None — city employee; Throne-adjacent
> **Location:** Wound Market — Office of Tolerance, eastern end
> **Alignment — public / true:** Unreadable (Perception 8+) / Gray
> **Status:** Complete · **Writer-Standards:** v1.0 compliant

> [!info] Information architecture
> Sevin is the most information-rich NPC in the lower city. She shares nothing without receiving something of equal value. She has been doing this for nineteen years. She is very good at it.

> [!warning] Perception note
> Her public alignment is unreadable below Perception 8. Her true alignment (Gray with Throne-adjacent tendencies) requires Perception 9+. Her Perception threshold of 10 means she cannot be successfully lied to within standard player stat ranges — for practical purposes, every lie she is told, she knows about.

---

## `[T1]` Quick Profile

**Function in the world:** Issues non-interference certificates — documents stating that the city has decided not to have a position on a specific activity at a specific location. Has done this for nineteen years. Every lower-city faction quest that involves something the city technically should not permit routes through her office at some point. She is the gatekeeper, the broker, and — for players who invest in her — the single most valuable intelligence source in Ironthorn.

**First impression:** Still. Not the stillness of patience or calculation — the stillness of someone who has been perfectly comfortable in this room for nineteen years and sees no reason to perform otherwise. She is behind a desk that is entirely clear except for whatever she is currently working on. She looks at you for a moment before speaking. She does not ask what you want. She already knows.

**Tone anchor:** Tired, not broken — but the tiredness is so deep and so old it has become something else. She is not dramatic about it. She is nineteen years into a job that requires her to issue documents making the city's indifference official, and she has been very good at it, and she has recently begun to think about a certificate she issued nineteen years ago that she should not have issued. She has not done anything about this yet. She is not sure she will.

**Signature line:**
> *She sets down whatever she is writing. Looks at you for a moment.*
> "You want something. Everyone who comes here wants something." *A pause.* "What are you offering?"

**Basic lie response:** She listens. She nods once. She asks a clarifying question that is actually a request for the version of the lie that doesn't have the gap in it. She is giving you the opportunity to tell a better lie. If you can't, she knows. She does not say so. She files it and continues.

---

## `[T1]` Behavioural Tell System

> [!warning] Writer rule — tell consistency
> These tells fire in every scene featuring Sevin. The surface tell is always active. Deviation is the signal.

### Surface tell — Perception 0 (everyone sees it)
*The baseline. This is simply how Sevin operates.*

She prices things. Everything. Before she responds to anything — a question, a request, a piece of information offered — there is a brief, visible pause in which she is calculating what it is worth and what she wants for it. This is not insulting. It is simply how she operates and everyone who deals with her knows it. She has never given anything away and she has never paid more than something was worth. Nineteen years of this has made the pricing pause completely automatic.

**When it deviates:** If Sevin responds without the pause — immediately, without the usual brief calculation — something about what you have said or done has moved into a register that is not transactional. This happens rarely. It means she is reacting rather than managing, which is the first time in any given scene that she is not entirely in control.

### Mid tell — Perception 5–6
*A detectable shift from baseline.*

> *She picks up the pen. Sets it down parallel to the edge of the desk. Her hands stay there, still. She is not writing anything. She is deciding something.*

This fires when something has arrived that does not have an obvious price — information that is worth more than she expected, or a request that she is not sure she wants to fulfil regardless of what is offered for it. The pen-parallel is an unconscious gesture from nineteen years of paperwork; she reaches for the tool of the transaction and then puts it aside when the transaction is not the point.

### Deep tell — Perception 7+
*The micro-signal that confirms the read.*

> *[Perception 7+: She has not asked what you are offering. She asks this of everyone. She has not asked you.]*

In nineteen years, Sevin has opened every significant conversation with some version of "what are you offering." When she doesn't ask, she has already decided that she wants what you have — or that this conversation is not going to be a transaction, which is the more significant tell. She is choosing to engage with you differently than she engages with everyone else. The player should notice this before they understand what it means.

### Lie-caught response
> *She nods once. Asks the clarifying question. Waits.*

That is all. She does not name the lie. She does not register surprise. She gives you the opportunity to revise. If you don't revise, she files the lie as data and continues the conversation. You will not know what she has done with it until she uses it — which may be this session or may be three sessions from now, when she references what you said, precisely, in a context where the gap matters.

### Liar's Mark active — permanent threshold shift
When the Liar's Mark activates, Sevin does not treat the player differently in obvious ways. She becomes slightly more precise in her transactions — clearer about what she is offering, clearer about what she wants in return. She is closing the margins. She is not angry. She is managing a resource that has revealed itself to be less reliable than she initially calculated. The player will eventually notice that her offers have become exactly what they are worth and no more.

---

## `[T2]` Layer 1 — Identity

### Public persona
A city bureaucrat of nineteen years' standing. Processes non-interference certificates. Neutral, professional, exquisitely indifferent to what is written in the certificates she issues. She has no faction alignment and has never formally aligned with anyone. She is paid by the city treasury, answers to the city administration, and has survived four city administrations by being equally useful to all of them. She is one of the most politically durable figures in Ironthorn and she has achieved this by appearing to have no politics at all.

### Background
Came to the Office of Tolerance at twenty-three as a junior clerk. Rose to Tolerance Director at thirty-one by attrition and competence in roughly equal measure. Has been in the role for nineteen years. The four administrations she has survived include one that tried to shut the office down entirely — she provided three administrations' worth of documentation on what would happen if the non-interference certificates lapsed, and the shutdown proposal was quietly withdrawn. She has the institutional memory of the entire lower city in her filing system. She is the filing system.

The certificate she issued nineteen years ago: a non-interference document for a pain-bonding operation that she was given to understand was a legitimate Throne commercial enterprise. It was not. The operation was a front for an Offered-breeding programme that the Throne's own internal reform faction has since classified as a violation of their own doctrine. The operation has been closed for eleven years. Sevin found out what it actually was eight months ago. She has not done anything about this yet.

### Voice & mannerisms
Economical. She does not use words she doesn't need. When she is calculating — which is most of the time — she is quiet. When she has decided, she is precise. She never raises her voice. She has never needed to. She has a habit of repeating back what someone has said to her before responding — not as a stall, but to confirm that she has the correct version. "So what you're telling me is—" and then the exact words. It is disorienting to be quoted back at yourself by someone who shows no expression while doing it.

---

## `[T2]` Layer 2 — Main Attributes

| Attribute | Score | What it means for Sevin |
|-----------|:-----:|--------------------------|
| Cunning | 9 | The highest in Ironthorn outside of Arch-Necromancer Issara and Factor Renne Saul. She has been reading people, transactions, and power structures for nineteen years in one of the city's most complex political positions. She misses almost nothing. |
| Loyalty | 3 | Low. She is loyal to the equilibrium — to the Market's stability, to the office's function, to the system that has made her necessary to everyone. She is not loyal to any person or faction. The Throne-adjacent tendency is pragmatic rather than ideological; the Throne is the most stable power in the lower city and stability is her operating interest. |
| Fear | 2 | Essentially absent as a driver. She has been in a position where fear could theoretically dominate her for nineteen years and has declined to let it. She is not brave — she has simply calculated that fear is a poor operational state and has practiced out of it. |
| Greed | 4 | Present but controlled. She wants more than she has — information, leverage, the kind of security that nineteen years of institutional power has not quite provided — but she does not reach for it in ways that would destabilise her position. She has been patient for nineteen years. She knows how to want things slowly. |
| Idealism | 2 | Almost entirely absent. She issued a certificate nineteen years ago and something terrible happened and the city's official position is that it is no longer happening. She is currently revisiting whether that is sufficient. It is the first time idealism has appeared on her horizon in a decade. |

**Perception threshold:** 10
> The highest in Ironthorn. For practical purposes, she cannot be lied to within standard player stat ranges. She has nineteen years of reading everyone who comes through her door and she has the information base to cross-reference everything against. Players with very high Perception scores can read her tells. No player can successfully deceive her.

---

## `[T3]` Layer 2 — Sub-Attributes

### Cunning subs

| Sub | Score | What it means for Sevin |
|-----|:-----:|--------------------------|
| Ambition | 4 | Moderate and contained. She has achieved what she set out to achieve — institutional indispensability — and her ambition now runs to maintaining and extending it rather than reaching for something new. The certificate situation is the first thing in years that has suggested her ambition might have a moral dimension she has not accounted for. |
| Patience | 10 | Maximum. She has been waiting for the right moment on certain pieces of information for years. She has information about Auditor Vesh's defection risk that she has held for six months without acting on it. She has information about Petrov Seld's dead-drop operation that she has held for two years. She waits until using something is exactly right. |
| Paranoia | 5 | Moderate. She is alert without being reactive. She has passive surveillance of everything that passes through her office and much of what passes through the market. She is not jumpy. She is simply aware. |

### Loyalty subs

| Sub | Score | What it means for Sevin |
|-----|:-----:|--------------------------|
| Devotion | 4 | Devoted to the office and to the equilibrium it maintains. Not devoted to people. The closest she comes to personal devotion is a professional respect for anyone who operates with genuine competence in a complex environment — and she expresses this by giving them slightly better terms than they could get elsewhere. |
| Resentment | 3 | Low. She does not resent the Throne's proximity or the office's position at the city's moral edge. She understood what she was signing up for. The certificate is the first thing that has generated something that functions like resentment — not at the Throne, but at the version of herself that issued it without asking more questions. |

### Fear subs

| Sub | Score | What it means for Sevin |
|-----|:-----:|--------------------------|
| Desperation | 1 | Essentially absent. She has faced worse situations than this with more at stake and fewer resources and come through them. She does not desperate. |
| Suppression | 9 | Exceptional. Whatever she feels — and she does feel things; the certificate has made this visible to her — it does not reach the surface in ways that anyone can read. She has been suppressing operational state for nineteen years. It is automatic and total. |

### Greed subs

| Sub | Score | What it means for Sevin |
|-----|:-----:|--------------------------|
| Appetite | 4 | She wants more than she has. She wants the certificate situation resolved in a way that does not destabilise her position. She wants to know whether Vesh is going to defect before he does it. She wants the Compact's dead-drop operation moved somewhere she has better visibility on. She has a list. |
| Restraint | 6 | Moderate. She reaches for things, but carefully, at the right time, in ways that cannot easily be traced back. |
| Envy | 1 | None. She does not want what other people have. She wants what she does not yet have, which is different. |

### Idealism subs

| Sub | Score | What it means for Sevin |
|-----|:-----:|--------------------------|
| Conviction | 2 | Almost gone. What remains is a residual sense that the equilibrium she maintains has value — that a Market that operates in daylight and follows implicit rules is better than one that doesn't, even if the rules are terrible ones. The certificate has brought this into question. |
| Disillusionment | 9 | Near maximum. She has been disillusioned for years about most things — factions, governance, the city's capacity to be honest with itself. The certificate has added the last dimension: disillusionment with herself. She has not yet decided what to do with it. |

---

## `[T3]` Layer 3 — Goals

### Primary goal
Maintain the equilibrium. Keep the Market stable, the office functional, and the city's non-interference policy operating smoothly. Prevent any single faction from gaining enough leverage in the lower city to destabilise the balance she has spent nineteen years building.

**What she will sacrifice for this:** Almost anything except the leverage itself. She will trade information she does not want to trade, issue certificates she does not want to issue, and facilitate arrangements she considers repugnant — all of this she has already done, repeatedly, for nineteen years. What she will not sacrifice is the position that makes her the broker of all of it.

**Goal tag:** `equilibrium`

### Secondary goal
Accumulate enough leverage on every significant player in the lower city that the equilibrium is structurally self-maintaining — that no one can afford to break it because the cost of doing so is too high.

**What she will sacrifice for this:** Time. She has been patient for nineteen years. She will be patient longer. She has leverage on Petrov Seld, partial knowledge of Sevayne's health situation, visibility on Vesh's defection risk, the Hollows access point information, and the certificate — which is leverage on herself, which is the most uncomfortable kind.

**Goal tag:** `leverage`

### What she fears losing most
The position. Not the salary, not the status — the actual structural position of being the person that everyone has to come through. If the office loses its function — if the city decides to take an official position on what happens in the Wound Market — everything she has built becomes irrelevant simultaneously. She has survived four administrations to prevent this. She will survive more.

---

## `[T4]` Layer 4 — Hidden Agenda & Private Truth

> [!danger] Hidden agenda — NEVER surface without player earning it
> Nineteen years ago, Sevin issued a non-interference certificate for what she was told was a legitimate Throne pain-bonding commercial operation. Eight months ago, she found out what it actually was: a front for an Offered-breeding programme that the Throne's own internal reform faction has classified as a violation of their doctrine. The operation was closed eleven years ago. The people who ran it are still in positions of power. The certificate is still in her filing system — her official record of a decision she made with information she was deliberately given incorrectly. She has been deciding what to do about this for eight months. She has not done anything yet. She is not sure she will. She is sure that she cannot issue the same certificate again.

**What she will sacrifice for this:** She does not know yet. The discovery has not yet forced the question. When it does — when someone comes through her door who could actually act on what she knows — the question will arrive.

**Goal tag:** `regret`

**Trigger for reveal:** Trust score 8+ AND player has demonstrated either that they have significant Throne exposure, or that they are investigating the Offered programme, or that they have come into contact with someone affected by the certificate operation. At that point, Sevin asks the player to stay after the official part of the transaction is done. She closes the door. She is quiet for a moment. Then: "I want to show you something. I've been deciding whether to trust anyone with this for eight months." She opens the filing cabinet. She takes out the certificate. She sets it on the desk. She does not explain it. She waits to see if the player can read what it means.

### Private truth
Sevin is the most powerful person in Ironthorn that most players will dismiss as a bureaucrat. She has information on every significant operation in the lower city, leverage on most of the people running them, and nineteen years of structural position that makes her indispensable to the city regardless of who is nominally in charge. She has also, eight months ago, discovered that she participated in something she would not have participated in if she had known what it was. She is a woman who has operated without regret for nineteen years and has recently acquired some. She does not know what to do with it yet. The player is the most likely vector through which she finds out.

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
| Leverage Held | true |
| Faction Alert Sent | false |

### Active leverage inventory (designer reference)

| Item | Against | Value | Status |
|------|---------|-------|--------|
| Petrov Seld's dead-drop location | Gray Compact / Petrov Seld | High | Watching — held 2 years |
| Sevayne mortality — partial intelligence | Crimson Throne | Maximum | Watching — unconfirmed |
| Vesh defection risk | Gray Compact / Auditor Vesh | High | Watching — held 6 months |
| Certificate — 19 years ago | Herself | Unknown | Active — 8 months; undecided |
| Hollows access points — both | Multiple factions | High | Leverage — deployable |
| The Collector's true reporting chain | Throne / The Collector | Moderate | Watching |

### Cross-system trigger reference

| Trigger | Tell result | Flag change |
|---------|-------------|-------------|
| Lie attempted | Clarifying question fires; no tell; lie filed | `liar_mark_active: true` |
| Player offers genuinely valuable information | Pricing pause absent — immediate response | trust_score +1 |
| Player reaches trust score 6 | Mid tell becomes visible at Perception 4+ | — |
| Player reaches trust score 8 | Hidden agenda reveal window opens | — |
| Player investigates Offered programme | Deep tell fires; pricing pause absent; trust_score +2 | — |
| Player has Throne exposure | Mid tell fires; Sevin begins active assessment of player's value | — |
| Player exposes Sevayne's mortality independently | Sevin contacts player first; terms of alliance offered | trust_score +3 |

### Secrets known (designer reference)
- Petrov Seld — dead-drop contact for Gray Compact; monitored 2 years
- Sevayne mortality — partial; sourced from supply chain anomalies in Throne blood magic procurement
- Auditor Vesh — defection risk; sourced from questioning pattern reports from Ledger Row
- Certificate — 19-year-old non-interference document for Offered-breeding programme
- Hollows access — both points; one through Quiet Room basement, one behind Vorell's building
- The Collector — true reporting chain goes to Pain-Priest Korrath, not to the Throne's administrative layer

---

## `[T4]` Layer 6 — Dialogue Hooks

### First encounter
She is writing when the player arrives. She finishes the sentence, sets the pen parallel to the desk edge, and looks at them. "You want something. Everyone who comes here wants something." She waits. She does not help them formulate the request. She has learned that what people ask for in their first sentence is usually not what they actually want, and she prefers to let them get there themselves.

### After trust score rises above 5
The pricing pause becomes slightly shorter. She begins volunteering context — not information, but context. "The certificate you're asking about — there's something you should know about how that category of document works before you commit to the terms." She is giving you better service than you paid for. This is how she invests in relationships that might be useful later.

### After trust score reaches 8
After the official transaction is done she asks the player to stay. Closes the door. Is quiet for a moment. Then: "I've been deciding whether to trust someone with something for eight months." She opens the filing cabinet. Takes out the certificate. Sets it on the desk. Does not explain it. Waits.

### When the player brings Sevayne's mortality as intelligence
She does not react visibly. Sets the pen parallel to the desk. Looks at the player for a moment. Then: "I know." A pause. "Or I know enough." Another pause. "The question is what you're going to do with it. Because what I do depends on what you do." This is the most direct statement of alliance she has made to anyone in nineteen years. She is aware of that. She does not take it back.

### At player Tier I — Radiant
She processes their certificate request efficiently. As they are leaving: "You're going to have difficulty here." Not unkind. Informational. "The Market is not hostile to light alignment — it is indifferent to it, which is more difficult to navigate. Come back when you have something the Market wants." She is not turning them away. She is telling them how to become a viable client.

### At player Tier VII — Void-Touched
She processes their certificate request. Her pricing does not change. Her manner does not change. She is completely neutral. As they are leaving, she says one thing: "If you ever want to discuss what you've seen — at the end, when it stops being abstract — the office is open." She does not say what she is offering. She will not say it first. She has been in this Market for nineteen years and she has seen alignment move in both directions and she has never made the offer before. She made it now. The player can decide what that means.

---

## Lie Detection — Decision Map

### Step 1 — Can she detect the lie?
Yes. Her Perception threshold of 10 means that within standard player stat ranges, she detects every lie told to her. The question is not whether she knows — it is what she does with it.

### Step 2 — What is the lie worth?
A lie tells her what the player wants her not to know, which tells her where to look, which tells her what they are protecting. She files it as leverage. She does not deploy it until the moment is right.

### Step 3 — How does her alignment shape the response?
True Gray: she absorbs and files. She is not morally offended by lying — she considers it a normal part of information management. She is professionally interested in what the lie reveals. She gives the player the clarifying question not as a trap but as an opportunity; if they can revise the lie into something she cannot counter, she genuinely respects that.

### Step 4 — What do her Cunning subs produce?
Patience 10 means she will carry a lie in leverage inventory for years if necessary. Paranoia 5 means she is alert but not pre-emptive — she has not yet decided whether the player is a risk or an asset, and she will not decide until she has more data. Ambition 4 means she will eventually use what she knows, but only in service of the equilibrium.

### Step 5 — Does faction affiliation change anything?
No faction changes her fundamental approach. Faction affiliation changes which pieces of her intelligence inventory become relevant and what terms she offers for her services. A Throne-affiliated player gets different context than a Compact-affiliated player — not better or worse, just more precisely calibrated to what they can actually use.

---

## Writer's Notes

- She should never seem like an exposition delivery mechanism. She is a power broker who happens to have information. The information is always incidental to the transaction. Write the transaction first; the information arrives as part of it.
- The certificate should be present in her scenes before the reveal — as a file that she moves aside, as a filing cabinet drawer she opens and closes, as a reference to "older cases" that she doesn't elaborate on. Plant it. Pay it off late.
- Her version of warmth is giving people better terms than they paid for. When she does this — context that wasn't requested, pricing that's slightly better than expected — the player should feel it without being able to name it immediately.
- The Tier VII dialogue hook is the most important one to write carefully. She has never made an offer like that before. Do not let it read as a quest hook. Let it read as a person saying something they have been not-saying for a long time and finally saying it to someone they think might understand what it means.
- She is not Throne. She is Throne-adjacent because the Throne is the most stable power in the lower city and she values stability. If the Throne destabilises — if Sevayne's mortality becomes public, if Korrath's succession plan activates — Sevin will be recalibrating in real time. Write her as someone who is always tracking the stability index of every power she has aligned herself with.

---

## Dataview Queries

```dataview
TABLE liar_mark_active, debt_flag_active, trust_score, leverage_held, faction_alert_sent
FROM "NPCs"
WHERE npc_name = "Sevin"
```

```dataview
TABLE npc_name, npc_tier, alignment_true, cunning, trust_score
FROM "NPCs"
WHERE location = "Wound Market" OR contains(location, "Wound Market")
SORT npc_tier DESC
```

---

*Template v3.0 · Writer-Standards v1.0 · [[../_System/NPC-Intelligence-System|NPC Intelligence System]] · [[../_System/Alignment-Spectrum|Alignment Spectrum]] · [[../_System/Writer-Standards|Writer Standards]] · [[../_System/Spy-Registry|Spy Registry]] · [[../World/Ironthorn/Wound-Market|Wound Market]] · [[../Factions/06-Crimson-Throne|Crimson Throne]]*
