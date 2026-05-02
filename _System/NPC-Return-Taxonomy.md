---
doc_type: "Return Taxonomy"
version: "1.0"
applies_to: "All NPC submissions — used by lead writer when issuing a return"
---

# NPC Submission Return Taxonomy

This document defines the exact language used when returning a submission. Every return uses one or more codes from this list. The code appears in the Lead Writer Review section of the submission form, in the return record file, and in the return email to the writer.

Returns are specific. "Doesn't feel right" is not a return. "TONE-02: NPC states inner emotional state in dialogue — Layer 6, first encounter, line 3" is a return.

---

## Criterion 1 — Tone

| Code | Fail condition | What the writer must fix |
|------|---------------|--------------------------|
| TONE-01 | NPC defined by suffering — backstory presented as character | Identify what the NPC did with what happened to them and rewrite the relevant section to lead with that response, not the history |
| TONE-02 | NPC monologues inner state in dialogue | Find the line. Rewrite it as observable behaviour — stage direction, not declaration |
| TONE-03 | NPC performs emotion rather than suppresses it | The feeling is on the surface. Find the suppression score. Rewrite to match — the feeling should show as a physical action or behavioural shift, not as an expressed state |
| TONE-04 | NPC's most dramatic line reads as a speech | Cut it to the bone. The line that lands is the one that sounds like something a real person would say in that moment, not something composed for impact |
| TONE-05 | NPC arc accelerated through dialogue without mechanical support | A writer cannot move an NPC's arc through dialogue alone. The mechanics drive it. Identify which sub-attribute score would need to be at threshold for this moment to be valid — then either wait for the mechanics or set the score correctly in frontmatter with justification |

---

## Criterion 2 — Tell system

| Code | Fail condition | What the writer must fix |
|------|---------------|--------------------------|
| TELL-01 | Surface tell missing | Add a surface tell — a baseline behaviour that is simply how this NPC operates. It must be specific enough to write as stage direction. |
| TELL-02 | Mid tell missing | Add a mid tell — a detectable shift from baseline that fires at Perception 5–6. Must be a specific observable action, not an emotion label. |
| TELL-03 | Deep tell missing | Add a deep tell — a micro-signal that fires at Perception 7+ and also breaks surface on lie-catch regardless of Perception. |
| TELL-04 | Surface tell is not active in normal scenes | The surface tell is the baseline — it is always present, not just under pressure. Rewrite it as something that is simply part of how this NPC operates in every scene. |
| TELL-05 | Deep tell does not fire on lie-catch | The deep tell is the one that breaks surface when a lie is caught. Confirm this in the decision map and the Liar's Mark section. If the current deep tell cannot serve this function, replace it with one that can. |
| TELL-06 | Tell is not writable as stage direction | The tell names an emotion rather than an action. Rewrite it as something a director could give to an actor — a specific physical or behavioural action, not an internal state. |
| TELL-07 | Tell fires in a scene where suppression score prevents it | Check the suppression score. A high suppression NPC's tells do not surface in low-pressure scenes. Remove the tell from scenes where it would be blocked by suppression, or lower the suppression score in frontmatter with justification. |
| TELL-08 | Tell is inconsistent between scenes | The same tell fires differently in different scenes. Tells are fixed. Standardise across all scenes. |
| TELL-09 | Multiple tells written for the same emotional state | One tell per emotional state maximum. Choose the most specific one and remove the others. |
| TELL-10 | Tell named explicitly in dialogue | A tell is never named in standard dialogue. Remove the explicit reference. The player reads stage direction, not a notification. |

---

## Criterion 3 — Flag accuracy

| Code | Fail condition | What the writer must fix |
|------|---------------|--------------------------|
| FLAG-01 | `liar_mark_active` set to true without mechanical trigger documented | This flag is set by a specific mechanic — the NPC catching a player lie. If this NPC has not yet encountered the player, this flag must be false. Remove the true value. |
| FLAG-02 | `debt_flag_active` set to true without `leverage_held` also true | These flags travel together — they cannot exist independently. Set both or neither. |
| FLAG-03 | `leverage_held` set to true without `debt_flag_active` also true | Same as FLAG-02 — set both or neither. |
| FLAG-04 | `faction_alert_sent` set to true at submission | This flag cannot be set true at submission — it requires a specific in-world event. Set to false. |
| FLAG-05 | `trust_score` set above 5 at submission without justification | The default is 5. If this NPC starts above 5, Section 3.5 of the submission form must document why. If that justification is absent or insufficient, reset to 5. |
| FLAG-06 | `trust_score` set below 4 at submission without justification | Same as FLAG-05 in the other direction. If starting below 4, justify it explicitly. |
| FLAG-07 | `secrets_known` populated at submission without explanation | The secrets_known array should be empty at submission unless the submission form documents exactly what mechanic placed each item there. |
| FLAG-08 | Boolean flag contains a non-boolean value | Flags are true or false only — no strings, no null, no placeholder text. |

---

## Criterion 4 — Voice

| Code | Fail condition | What the writer must fix |
|------|---------------|--------------------------|
| VOICE-01 | Dialogue does not match the voice established in Layer 1 | Read Layer 1's voice and mannerisms section. Find the lines that drift. Rewrite them in the NPC's actual vocabulary and rhythm. |
| VOICE-02 | NPC becomes more eloquent under pressure | Under pressure, vocabulary simplifies. Find the high-pressure scene. If the dialogue is longer or more composed than the NPC's normal voice, cut it down. |
| VOICE-03 | No silence written as stage direction | Add at least one moment of silence written explicitly as stage direction — a pause, a non-answer, a changed subject. Silence is dialogue. |
| VOICE-04 | Test dialogue lines appear in the submitted file | The three test lines written before drafting a scene should never appear in the final file. Remove them. |
| VOICE-05 | NPC vocabulary exceeds background constraints | This NPC uses words or constructions their background would not produce. Find the lines. Rewrite them in vocabulary appropriate to who this person is and where they came from. |

---

## Criterion 5 — Decision map (Tier 3+ only)

| Code | Fail condition | What the writer must fix |
|------|---------------|--------------------------|
| DM-01 | Decision map missing | Add the five-step decision map. Each step must reflect this NPC's specific attributes, alignment, and faction — not a generic template response. |
| DM-02 | In-world response line is generic | The in-world response line must be specific to this character. It should not be transferable to any other NPC without revision. Find what is generic and make it specific — to this NPC's voice, their relationship with the player, and their internal state when the lie is caught. |
| DM-03 | Step 3 (alignment filter) does not match true alignment | The decision map must reflect the NPC's TRUE alignment, not their public alignment. Check the frontmatter. If the true alignment is Gray and the decision map response is a Light-style gentle confrontation, this is an error. Correct to match. |
| DM-04 | Step 4 (Cunning filter) does not match Cunning score | A Cunning 8 NPC does not blurt discomfort. A Cunning 2 NPC does not build a months-long case. Match the decision map step to the actual score. |
| DM-05 | Step 5 (faction filter) incorrect or missing | Faction affiliation shapes what the NPC does with caught-lie intelligence. If this NPC is in a faction with an enforcement arm, the faction filter should reflect that. If they are independent, the response is personal. Check and correct. |

---

## Incomplete submission codes (pre-review — returned before criteria check)

| Code | Condition | Action |
|------|-----------|--------|
| INCOMPLETE-01 | NPC file missing from submission folder | Resubmit with all three files present |
| INCOMPLETE-02 | Submission form missing from submission folder | Resubmit with all three files present |
| INCOMPLETE-03 | Submission intake document missing | Resubmit with all three files present |
| INCOMPLETE-04 | Quiz score absent or below 80% | Complete or retake the quiz. 80% minimum required before submission. |
| INCOMPLETE-05 | Submission form contains placeholder text | Complete all sections. "FILL IN" is not an answer. |
| INCOMPLETE-06 | NPC file contains placeholder text from the template | Complete all sections before submitting. |

---

## How return codes appear in the return email

Each return email includes:
- The return code(s)
- The specific location in the file (Layer, section, line where possible)
- What needs to change (pulled directly from the "What the writer must fix" column above)

**Example return email excerpt:**
```
TELL-06 — Mid tell (Layer [T1], mid tell section)
Current: "She seems suspicious of the player"
This is an emotion label, not an observable action. Rewrite it as something
a director could give to an actor. Reference the Writer-Standards tell table
for examples of the distinction.

VOICE-02 — High-pressure scene (Layer [T4], dialogue hooks, "when resentment reaches 8")
The dialogue in this scene is longer and more composed than this NPC's normal
voice. Under pressure, vocabulary simplifies. Cut this exchange to its
minimum and let the silences carry the weight.
```

---

*[[../../README|Back to Index]] · [[../Lead-Writer-Review-Workflow|Lead Writer Review Workflow]] · [[../Writer-Standards|Writer Standards]] · [[../Writer-Certification/04-NPC-Submission-Form|Submission Form]]*
