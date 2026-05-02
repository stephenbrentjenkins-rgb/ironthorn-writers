---
doc_type: "Lead Writer Review Workflow"
version: "1.1"
lead_writer: "Stephen Brent Jenkins"
lead_writer_email: "stephenbrentjenkins@gmail.com"
---

# Lead Writer Review Workflow

This document defines exactly what happens when a writer submission arrives and what the lead writer does with it. Every return uses codes from the [[NPC-Return-Taxonomy]] — no vague feedback, no general notes. Every return is specific, located, and actionable.

---

## Step 1 — Submission arrives

Writer drops three files into `NPCs/_Pending/NPC-Name/`:
- `NPC-Name.md` — the NPC file
- `NPC-Name_Submission-Form.md` — the completed submission form
- `NPC-Name_Submission-Intake.md` — the intake document with writer contact info

Writer sends an email to **stephenbrentjenkins@gmail.com** with subject:
`[NPC SUBMISSION] NPC-Name — Writer Name — Date`

---

## Step 2 — Triage (Day 1)

On receiving the email, open `NPCs/_Pending/NPC-Name/` in Obsidian and check:

1. All three files present?
2. Quiz score logged and 80% or above?
3. Submission form has no placeholder "FILL IN" text remaining?
4. NPC file has no placeholder text from the template?

**If any triage check fails:** Return immediately using the incomplete codes from the taxonomy. Do not proceed to criteria review.

Copy `RETURN-NOTICE-TEMPLATE.md` into the submission folder, fill in the incomplete codes, and send the return email. Use subject:
`[RETURNED] NPC-Name — GameVault — Incomplete Submission`

**If triage passes:** Proceed to Step 3.

---

## Step 3 — Review against criteria (Day 1–3)

Review in order. Stop and log each failure with its exact return code from [[NPC-Return-Taxonomy]]. Do not skip ahead — a tone failure may indicate deeper problems downstream.

### Criterion 1 — Tone
Check: Is the NPC tired, not broken? Does any line read as a speech? Does the NPC monologue their inner state?

Relevant codes: TONE-01 through TONE-05

Open the Writer-Standards tone table. Read the file with it in mind. If a line makes you reach for a code, log it with the exact location.

---

### Criterion 2 — Tell system
Check: All three tiers present? Surface tell active in normal scenes? Deep tell fires on lie-catch? All tells writable as stage direction? Consistent across all scenes? Fires only where suppression permits?

Relevant codes: TELL-01 through TELL-10

Read the tell system section carefully against the suppression score in frontmatter. A common failure is TELL-07 — tell fires in a scene where the suppression score would block it.

---

### Criterion 3 — Flag accuracy
Check: All flags at correct defaults? Any flag set to true without mechanical justification? leverage_held and debt_flag_active travelling together?

Relevant codes: FLAG-01 through FLAG-08

Cross-reference every non-default flag value against the submission form Section 3. If the form doesn't justify it, it fails.

---

### Criterion 4 — Voice
Check: Dialogue matches Layer 1 voice? NPC simplifies under pressure? At least one silence written as stage direction?

Relevant codes: VOICE-01 through VOICE-05

Find the highest-pressure scene in the file. Read the dialogue in that scene. If it's longer and more composed than the NPC's normal voice, that's VOICE-02.

---

### Criterion 5 — Decision map (Tier 3+ only)
Check: Five steps present? In-world response line specific to this character? Alignment filter matches true alignment? Cunning filter matches Cunning score?

Relevant codes: DM-01 through DM-05

Read the true alignment in frontmatter (not public alignment) before checking Step 3 of the decision map. This is the most common error in Tier 3+ submissions.

---

## Step 4 — Issue return (if any criteria fail)

1. Copy `NPCs/_Pending/RETURN-NOTICE-TEMPLATE.md` into the submission folder
2. Rename it: `NPC-Name_Return-Notice_DATE.md`
3. Fill in every section — return codes, locations, current text, what must change
4. List all passing criteria explicitly so the writer knows what not to touch
5. Complete the Lead Writer Review section of the original submission form:
   - Each failed criterion: **Fail** + return code(s)
   - Each passed criterion: **Pass**
   - Overall: **Returned**
   - Sign and date

6. Create a return record in `_System/Writer-Certification/Records/`:
   - Filename: `NPC-Name_Writer-Name_DATE_RETURNED.md`
   - Contents: copy of the return notice

7. Send the return email — see email template below

**Do not move any files.** Everything stays in `_Pending/NPC-Name/` until the resubmission passes.

### Return email template

**To:** writer's email (from intake document)
**Subject:** `[RETURNED] NPC-Name — GameVault — Action Required`

```
[Writer name],

[NPC-Name] has been returned for revision. Details below.

── RETURN ITEMS ──────────────────────────────────────

[CODE] — [Location]
[Paste current text]
What to change: [specific instruction from taxonomy]

[CODE] — [Location]
[Paste current text]
What to change: [specific instruction from taxonomy]

── WHAT PASSED ───────────────────────────────────────

[List passing criteria — do not revise these]

── RESUBMISSION ──────────────────────────────────────

Revise only the return items above.
Before resubmitting, version your file to:
  NPCs/_Characters/[NPC-Name]/Versions/[NPC-Name]_v[X]_[DATE].md

Email when ready:
  stephenbrentjenkins@gmail.com
  Subject: [NPC SUBMISSION] [NPC-Name] — [Your Name] — [Date] (Revised — Return [N])

Review window for resubmissions: 3 business days.

Stephen
```

---

## Step 5 — Approve (all criteria pass)

1. Move `NPC-Name.md` from `_Pending/NPC-Name/` to `NPCs/NPC-Name.md`
2. Move `NPC-Name_Submission-Form.md` to `_Characters/NPC-Name/Submissions/`
3. Move the return notice (if any) to `_Characters/NPC-Name/Submissions/` as well — the full history travels with the character
4. Create `_Characters/NPC-Name/` folder with subfolders if it doesn't exist
5. Archive the previous canonical version to `_Characters/NPC-Name/Versions/NPC-Name_v[X]_DATE.md` if this is an upgrade
6. Complete the Lead Writer Review section of the submission form:
   - All criteria: **Pass**
   - Overall: **Approved**
   - Sign and date
7. Create an approval record in `_System/Writer-Certification/Records/`:
   - Filename: `NPC-Name_Writer-Name_DATE_APPROVED.md`
8. Send the approval email
9. In Unreal Editor: **Window → NPC Dev Tools → Refresh Roster** — confirm the new NPC appears

### Approval email template

**To:** writer's email (from intake document)
**Subject:** `[APPROVED] NPC-Name — GameVault`

```
[Writer name],

[NPC-Name] has been approved and is now live in the vault.

The NPC will appear in the Unreal Dev Tools panel on the next Refresh Roster.

[Optional: one brief note about what worked particularly well — specific, not generic]

Stephen
```

---

## Step 6 — Resubmission review

When a revised submission arrives:
- Review only the returned criteria — do not re-review passing sections unless the revision has introduced changes to them
- If the revision corrects all return items: approve (Step 5)
- If the revision introduces new failures in previously passing sections: return again with new codes for those sections. Note in the return email that previously passing sections were altered and now require re-review.
- Update the return record in `_System/Writer-Certification/Records/` with the resubmission date and outcome

---

## Return taxonomy reference

All return codes are defined in:
[[NPC-Return-Taxonomy]]

Every return must use codes from that document. Freeform return notes without codes are not permitted — they create inconsistency across writers and make the resubmission process unclear.

---

*[[../../README|Back to Index]] · [[NPC-Return-Taxonomy|Return Taxonomy]] · [[Writer-Standards|Writer Standards]] · [[Writer-Certification/04-NPC-Submission-Form|Submission Form]]*
