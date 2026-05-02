---
doc_type: "Writer Certification"
module: 2
title: "Writer Quiz — NPC System Certification"
version: "1.0"
passing_score: 80
question_count: 20
status: "Complete before accessing the Submission Form"
prerequisite: "[[01-Writer-Primer]]"
next: "[[03-Writer-Glossary]]"
---

# Writer Quiz
## NPC System Certification

> [!danger] Rules
> - Complete [[01-Writer-Primer]] before attempting this quiz.
> - Passing score: **80% or above (16 of 20 correct)**.
> - No references during the quiz. If you need to look something up, you are not ready.
> - Answers are at the bottom of this document — do not scroll until you have answered every question.
> - Submit your score and answer sheet to the lead writer before accessing [[04-NPC-Submission-Form]].

---

## Section A — Tone and Fundamentals (Questions 1–5)

**Question 1**
A writer submits a scene where a Tier III NPC, having just witnessed their family destroyed by the Ashen Veil, delivers a two-paragraph speech about their grief and desire for revenge. The lead writer returns it. Why?

A) The NPC is Tier III and cannot have that level of emotional complexity
B) The NPC is defining themselves by their suffering and performing grief rather than suppressing it — this violates the tone anchor
C) Two paragraphs of dialogue is too long regardless of content
D) Revenge is a Dark-alignment motivation and conflicts with the NPC's Covenant faction

---

**Question 2**
Which of the following is an example of the correct tone anchor applied to a Tier VI (Corrupted) NPC?

A) The NPC cackles when the player enters, describes in detail the suffering they have caused, and invites the player to join their darkness
B) The NPC is polite, efficient, and makes a single passing reference to the player's Liar's Mark that implies they have been watching since the first session
C) The NPC is visibly angry and tells the player directly that they do not trust them
D) The NPC refuses to engage until the player proves their alignment is Tier V or below

---

**Question 3**
An NPC's arc has been tracked mechanically — their resentment score has reached 8 and their disillusionment is at 7. The writer wants to accelerate the defection by having the NPC announce in dialogue that they have decided to leave their faction. Is this correct procedure?

A) Yes — if the mechanics support it, the writer can use dialogue to trigger the defection
B) No — the mechanics have built the arc, but the writer must wait for the specific tipping point event defined in the NPC file before writing the defection moment
C) Yes — disillusionment at 7 is close enough to the threshold that dialogue can bridge the gap
D) No — defection requires a trust score of 9+ with the player, which has not been established

---

**Question 4**
A writer is drafting a scene where an NPC under interrogation by a rival faction explains their hidden agenda in full to deflect suspicion. The logic is that revealing it would seem so unlikely that no one would believe it. Should this scene be written as drafted?

A) Yes — subverting expectations by having the NPC state their agenda directly is an effective narrative technique
B) Yes — if the player is not present, the NPC can reveal their agenda to other NPCs
C) No — an NPC never explains their own hidden agenda in dialogue. It surfaces through action and accumulation only
D) Yes — the interrogation context creates a special exception to the hidden agenda rule

---

**Question 5**
Which statement best describes the relationship between an NPC's backstory and their character?

A) Backstory is the foundation of character — the more detailed the backstory, the more real the NPC feels
B) Backstory is what happened to the NPC. Character is what they did with what happened to them. They are not the same thing.
C) Backstory should be revealed gradually through dialogue so the player can discover it naturally
D) Backstory determines alignment — a dark past produces dark alignment, and vice versa

---

## Section B — The Flag System (Questions 6–10)

**Question 6**
A player successfully lies to Ser Orvane (Perception threshold 6, Cunning 3) about their whereabouts during a restricted-hours patrol. The player's Deception skill is 7. What happens?

A) `liar_mark_active` sets on Orvane. The deep tell fires. Trust gains are halved going forward.
B) No flag sets. The lie succeeded — the memory log records "Watching" status only.
C) `debt_flag_active` sets because Orvane's goal is security and the lie threatened it.
D) `faction_alert_sent` fires immediately because Orvane is a Covenant-directed guard.

---

**Question 7**
An NPC has both `debt_flag_active` and `leverage_held` set to true. What is the difference between these two flags?

A) There is no meaningful difference — they are the same flag tracked in two places for Dataview purposes
B) `debt_flag_active` means the NPC knows something; `leverage_held` means the NPC has decided what to do with it and is timing deployment
C) `debt_flag_active` tracks player obligations; `leverage_held` tracks NPC obligations to the player
D) `debt_flag_active` is set by failed lies; `leverage_held` is set by successful ones

---

**Question 8**
`faction_alert_sent` has been set on a player by Factor Renne Saul (Gray Compact). The player has since completed three quests for the Compact and raised their trust score with Saul to 8. Does the alert clear?

A) Yes — trust score 8+ with the alerting NPC resets the network flag
B) Yes — completing quests demonstrates good faith and clears outstanding flags
C) No — once sent, a faction alert cannot be recalled. The network awareness persists regardless of trust recovery with individual NPCs.
D) No — the alert only clears when the player reaches Compact rank 5

---

**Question 9**
A player shares the secret of Sevayne's mortality with Scholar-Physician Dael during a trust-building scene. Dael is a Tier 3 Veil NPC. What is the correct mechanical outcome?

A) The secret enters Dael's `secrets_known` array and remains there — it has no further mechanical effect at Tier 3
B) The secret enters Dael's `secrets_known` array. Because Dael is a spy for the Void Eternum's Issara, the secret may travel to the Veil's Quorum through their relationship network
C) Nothing — secrets_known only activates for Tier 4+ NPCs
D) The secret enters Dael's `secrets_known` and `debt_flag_active` sets immediately because the information has value

---

**Question 10**
An NPC's `liar_mark_active` is set. The player approaches a different NPC in the same faction. The second NPC has Cunning 8. What happens?

A) Nothing — the Liar's Mark is specific to the NPC who caught the lie and does not transfer
B) The second NPC receives a passive awareness of the player via the faction network. Their dialogue quality shifts to "measured."
C) The second NPC immediately refuses to deal with the player until the mark is cleared
D) The second NPC's trust score with the player drops by 2 automatically

---

## Section C — Behavioural Tells (Questions 11–14)

**Question 11**
A writer submits the following scene direction for a tense interrogation moment: *"She looks nervous and suspicious, clearly hiding something important from the player."* What is wrong with this direction?

A) It is too long and should be condensed to one word
B) It labels emotions rather than describing specific observable behaviour — it is not a tell, it is an emotion label
C) It reveals too much of the NPC's internal state to a player who may not have sufficient Perception
D) "Nervous" and "suspicious" are contradictory states that cannot occur simultaneously

---

**Question 12**
A player with Perception rank 4 is in a scene with Registrar Celn Avour. Celn's mid tell (he adjusts his collar when pressed) fires during the conversation. Does the player see it?

A) Yes — Perception 4 is above the mid tell threshold of 3+
B) No — mid tells require Perception 5–6 minimum. The player sees only Celn's surface tell.
C) Yes — mid tells are visible to all players regardless of Perception when the NPC's resentment is above 6
D) No — mid tells only fire when `liar_mark_active` is set

---

**Question 13**
An NPC's surface tell is that she always makes direct eye contact when speaking. A writer drafting a scene where the NPC is calm and comfortable writes her as avoiding the player's gaze to convey thoughtfulness. Is this correct?

A) Yes — thoughtfulness can override the surface tell in calm scenes
B) Yes — tells only need to be consistent in high-pressure scenes
C) No — the surface tell is the baseline and must be active in all normal scenes. Deviation from it is the signal. Writing the deviation in a calm scene corrupts the tell.
D) No — eye contact behaviour is not a valid surface tell because it is too dependent on staging

---

**Question 14**
A player with Perception rank 7 is in a conversation with Auditor Vesh. Vesh is lying about the outcome of an internal investigation. How is this written?

A) Standard dialogue only — the player does not receive any special information about a lie they have not yet detected
B) A bracketed stage direction appears: *[Perception 7+: a description of Vesh's deep tell firing — the specific micro-behaviour that breaks surface under maximum pressure]*
C) A pop-up notification reads: "You sense that Vesh is not being fully honest"
D) The scene branches — Perception 7+ players see a completely different version of the conversation

---

## Section D — Decision Map and Voice (Questions 15–18)

**Question 15**
An NPC with true alignment Gray-IV catches a player lie. Working through the decision map: the lie does not threaten the NPC's survival or primary goal. What is the next step, and what does the Gray alignment filter produce?

A) Step 2 (Leverage check) — if leverageable, the Gray NPC logs silently and sets `debt_flag_active`. If not, Step 3 produces: files silently, no reaction, watches, uses when useful.
B) Step 2 (Leverage check) — if leverageable, confronts the player immediately. Gray alignment means no patience for deception.
C) Step 3 (Alignment filter) — Gray produces a gentle confrontation offering the player a correction door.
D) Step 3 (Alignment filter) — Gray stores it as ammunition and deploys at the worst possible moment.

---

**Question 16**
An NPC has Cunning 8, Patience 9, and Paranoia 3. A player successfully lies to them. The NPC's deception-immune flag is false and the lie passes the Perception threshold. What does the Cunning filter produce?

A) The NPC blurts their discomfort and the player is immediately aware they are suspected
B) The NPC logs quietly. Dialogue shifts slightly. They will not confront until they have built a sufficient case. Their patience means they will hold this for a very long time.
C) The NPC deploys the information immediately — high Cunning means they act fast
D) The NPC's Paranoia (3) overrides the Cunning score and they extend good faith automatically

---

**Question 17**
A writer is drafting dialogue for Brother Aldric in a scene where the player accuses him of covering up Sub-Order activities. The writer has Aldric respond with an articulate, three-sentence defence of the Covenant's methods. What is wrong?

A) Aldric should not be defending the Sub-Order at this stage of his arc
B) Three sentences is too short — Aldric's high Idealism warrants a longer response
C) An NPC under pressure gets simpler, not more eloquent. Aldric under accusation should use fewer words and shorter sentences, not a composed defence.
D) Aldric cannot speak about the Sub-Order without player Covenant rank 3+

---

**Question 18**
A writer is working on a scene featuring Solta Byrne (Hearthstone innkeeper) for the first time. What must they do before writing any dialogue?

A) Read the voice fragments in Layer 1 of Solta's NPC file, then write three test lines in her voice before writing the scene
B) Read the full NPC file from start to finish, then begin the scene immediately
C) Ask the lead writer which faction Solta leans toward before writing her dialogue
D) Review the district file for the Sanctum Ward to establish environmental context

---

## Section E — Application Scenarios (Questions 19–20)

**Question 19**
You are writing a scene between Ser Orvane (Watch Commander, Perception threshold 6, Cunning 3) and Brother Aldric. Aldric's mid tell (straightening nearby objects) is currently active — he is carrying unresolved discomfort. Orvane's Perception threshold is 6, which is below Aldric's suppression score of 7. Can Orvane register the mid tell in this scene?

A) No — Orvane's Perception is below Aldric's suppression score, so the tell is invisible to him through skill alone. However, eleven years of shared patrol routes gives Orvane relationship-based baseline familiarity. He can notice that something is different — not through skill but through knowing Aldric. This is written as Orvane observing the deviation from baseline, not identifying the internal state.

B) No — Orvane cannot register any tell from Aldric because his Perception is below the suppression score. The scene should be written as if Orvane notices nothing.

C) Yes — mid tells are visible to all NPCs in the same district regardless of Perception scores.

D) Yes — Orvane's Cunning (3) is irrelevant; only his Perception threshold matters, and Perception 6 is sufficient for mid tells.

---

**Question 20**
You are building a new Tier 3 NPC for the Ashgate Quarter — a fence who trades in goods of unclear provenance. You have written three possible surface tells. Which one is correct?

A) "She always looks slightly guilty, like someone who knows they are doing something wrong but cannot stop."

B) "Before answering any question about pricing or sourcing, she glances toward the door. It is a habit so consistent that regulars have started using it as a signal — if she glances twice, something is wrong outside."

C) "She is wary and guarded, reading every customer as a potential threat before deciding whether to engage."

D) "She counts her coins when she is nervous — a tell that experienced players will notice immediately."

---

## Answer Key

> [!warning] Do not scroll here until you have answered all 20 questions on a separate sheet.

---

**1 — B**
The NPC is defining themselves by their suffering and performing grief rather than suppressing it. The tone anchor requires tired, not broken. A two-paragraph speech about grief is performed damage, not suppressed weight.

**2 — B**
Tired, not broken applies at every alignment tier. A Tier VI NPC who is polite, efficient, and makes a quiet, specific reference to the player's history is far more unsettling — and correct — than one who performs darkness. Option A is a broken NPC performing their alignment.

**3 — B**
The mechanics build the arc. The writer delivers the tipping-point moment — the specific event defined in the NPC file — not a dialogue-driven shortcut. Resentment at 8 makes defection mechanically possible; it does not make it automatic or writable without the tipping-point trigger.

**4 — C**
The hidden agenda rule has no exceptions. It surfaces through action and accumulation only. The interrogation context does not create an exception — it creates a scene where the NPC's behaviour under pressure is observable, not a licence to have them explain themselves.

**5 — B**
Backstory is what happened. Character is what they did with what happened. These are not the same thing, and conflating them produces NPCs who are defined by their suffering rather than their response to it.

**6 — B**
The lie succeeded — the player's Deception (7) exceeded Orvane's Perception threshold (6). No flag sets on a successful lie. The memory log records "Watching" status. Orvane has a low-level suspicion that does not cross into action unless it compounds.

**7 — B**
Debt is passive — the NPC knows something and is waiting. Leverage is active — the NPC has decided what to do with it and is timing the deployment. Debt without leverage is possible (still deciding). Leverage without debt is not possible.

**8 — C**
Faction alerts cannot be recalled. The network awareness is permanent regardless of individual trust recovery. This is one of the most consequential flags in the system — once the network knows, it knows.

**9 — B**
The secret enters Dael's secrets_known. Because Dael's relationship with Quorum Member Issara (Void Eternum agent) exists within the Veil network, intelligence can travel through the relationship chain. The writer must check the Cross-NPC Connection Map before assuming a secret stays with one NPC.

**10 — B**
NPCs with Cunning 7+ share Liar's Mark intelligence within their faction network. The second NPC receives passive awareness — their dialogue shifts to "measured." They do not immediately refuse or automatically drop trust; they carry the awareness into all future interactions.

**11 — B**
"She looks nervous and suspicious" labels emotions. A tell must be a specific observable action writable as stage direction. What does she do with her hands? Where does she look? What does she stop doing?

**12 — B**
Mid tells require Perception 5–6 minimum. A player at Perception 4 sees only surface tells — the NPC's baseline behaviour and deviations from it that do not require skill to notice.

**13 — C**
The surface tell is the baseline and must be active in all normal scenes. Deviating from it in a calm scene to convey thoughtfulness corrupts the tell — now the player cannot distinguish between "the NPC is thinking" and "something is wrong." The signal has been polluted.

**14 — B**
High-Perception players receive bracketed stage direction describing the NPC's deep tell firing. They do not receive explicit notifications or completely alternate scene versions. The interpretation is theirs.

**15 — A**
Step 2 comes after confirming no survival threat. Gray alignment filter (Step 3): files silently, no visible reaction, watches, uses when useful. This is the correct Gray response — not confrontation, not immediate ammunition, but patient accumulation.

**16 — B**
Cunning 8 with Patience 9 produces maximum composure and extended waiting. Paranoia 3 means they extend basic good faith until the case is built. High Cunning is not speed — it is sophistication. They will hold this until deployment serves them optimally.

**17 — C**
An NPC under pressure gets simpler, not more eloquent. Aldric under direct accusation should use shorter sentences and fewer words — not a composed three-sentence defence. High idealism does not produce eloquence under pressure; it produces quietness.

**18 — A**
Read Layer 1 voice fragments first. Write three test lines in the NPC's voice. Do not use the test lines — they are warm-up. Then write the scene. This sequence is mandatory regardless of how familiar a writer is with the NPC.

**19 — A**
This is the correct answer and the most important distinction in the NPC-NPC tell system. Orvane cannot read the tell through skill (Perception below suppression score). But relationship-based familiarity — eleven years of shared patrol routes — allows him to notice the deviation from baseline without identifying the internal state. The scene is written as Orvane observing that something is different, not what it means.

**20 — B**
Option B is the only specific observable action writable as stage direction. It has a consistent baseline (always before answering pricing/sourcing questions), a deviation signal (glancing twice means outside trouble), and it is specific to this character and this context. Options A, C, and D are emotion labels or vague descriptions.

---

## Scoring

| Score | Result |
|-------|--------|
| 20/20 | Perfect — proceed directly to the submission form |
| 16–19 | Pass — review missed questions before proceeding |
| 13–15 | Near pass — re-read the relevant primer modules and retest |
| Below 13 | Fail — re-read the full primer before attempting the quiz again |

---

*[[01-Writer-Primer|Back to Primer]] · [[03-Writer-Glossary|Glossary]] · [[04-NPC-Submission-Form|Submission Form (passing score required)]]*
