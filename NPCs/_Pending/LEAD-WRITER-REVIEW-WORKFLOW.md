---
doc_type: "Lead Writer Review Workflow"
version: "1.0"
lead_writer: "Stephen Brent Jenkins"
lead_writer_email: "stephenbrentjenkins@gmail.com"
---

# Lead Writer Review Workflow

This document defines exactly what happens when a writer submission arrives and what the lead writer does with it.

---

## Step 1 — Submission arrives

Writer drops three files into `NPCs/_Pending/NPC-Name/`:
- `NPC-Name.md` — the NPC file
- `NPC-Name_Submission-Form.md` — the completed submission form
- `NPC-Name_Submission-Intake.md` — the intake document with writer contact info

Writer sends an email to **stephenbrentjenkins@gmail.com** with subject:
`[NPC SUBMISSION] NPC-Name — Writer Name — Date`

---

## Step 2 — Lead writer triage (Day 1)

On receiving the email, the lead writer:

1. Opens `NPCs/_Pending/NPC-Name/` in Obsidian
2. Checks the intake document — confirm all three files are present
3. Checks quiz score is logged and is 80% or above
4. If files are missing or quiz score is absent → return immediately with:
   > "Submission incomplete. Missing: [list]. Resubmit when complete."

If complete, proceed to review.

---

## Step 3 — Review against Writer-Standards (Day 1–3)

Review the NPC file and submission form against these five criteria in order:

### Criterion 1 — Tone
- Is the NPC tired, not broken?
- Does any line read as a speech or a performed emotion?
- Does the NPC monologue their inner state anywhere?

**Pass:** Tone is consistent with world standard, no performances, no monologues.
**Fail:** Flag the specific line(s). Return with: "Tone — [paste the line] — revise per Standard 1."

---

### Criterion 2 — Tell system
- Are all three tell tiers present (surface, mid, deep)?
- Is the surface tell active in normal scenes, not just pressure moments?
- Is the deep tell the one that fires on lie-catch?
- Are all tells writable as stage direction?
- Are all tells consistent across every scene in the file?

**Pass:** All three present, consistent, correctly gated.
**Fail:** Flag the specific tell and the specific failure. Return with: "Tell system — [which tell] — [what is wrong]."

---

### Criterion 3 — Flag accuracy
- Are all frontmatter flags at correct starting values?
- Has the writer set any flag to TRUE without mechanical justification?
- Does `leverage_held: true` appear without `debt_flag_active: true`?

**Pass:** All flags at correct defaults or correctly justified.
**Fail:** Flag the specific error. Return with: "Flag error — [flag name] — [what is wrong]."

---

### Criterion 4 — Voice
- Does the dialogue match the voice described in Layer 1?
- Does the NPC get simpler under pressure, not more eloquent?
- Is there at least one silence written as stage direction?

**Pass:** Voice consistent, pressure = simpler, silence present.
**Fail:** Flag the specific dialogue. Return with: "Voice — [paste the line] — [what is wrong]."

---

### Criterion 5 — Decision map (Tier 3+ only)
- Is the in-world response line specific to this character?
- Does the decision map correctly reflect the NPC's alignment, Cunning score, and faction position?

**Pass:** Specific, aligned, correct.
**Fail:** "Decision map — [step number] — [what is wrong]."

---

## Step 4 — Approval

If all five criteria pass:

1. Move `NPC-Name.md` from `_Pending/NPC-Name/` to `NPCs/NPC-Name.md`
2. Move `NPC-Name_Submission-Form.md` to `_Characters/NPC-Name/Submissions/`
3. Create `_Characters/NPC-Name/` folder with subfolders if it doesn't exist
4. Copy current canonical file to `_Characters/NPC-Name/Versions/NPC-Name_v1.0_DATE.md` before moving the new one in
5. Complete the Lead Writer Review section of the submission form:
   - All criteria: **Pass**
   - Overall: **Approved**
   - Lead writer signature and date
6. Send approval email to writer:

**Subject:** `[APPROVED] NPC-Name — GameVault`

**Body:**
```
[Writer name],

[NPC-Name] has been approved and is now live in the vault.

The NPC will appear in the Unreal Dev Tools panel on the next Refresh Roster.

[Any brief notes — optional]

Stephen
```

7. In Unreal Editor: **Window → NPC Dev Tools → Refresh Roster**
   - Confirm the new NPC appears in the panel table

---

## Step 5 — Return

If any criterion fails:

1. Complete the Lead Writer Review section of the submission form:
   - Failed criteria: **Fail** with specific notes
   - Overall: **Returned**
   - Lead writer signature and date
2. Leave all files in `_Pending/NPC-Name/` — do not move anything
3. Send return email to writer:

**Subject:** `[RETURNED] NPC-Name — GameVault — Action Required`

**Body:**
```
[Writer name],

[NPC-Name] has been returned for revision. Specific issues below.

[Paste the failed criteria with exact line references and what needs to change]

Revise and resubmit to _Pending/NPC-Name/ when ready.
No need to resubmit passing sections — only the returned items need revision.

Stephen
```

---

## Step 6 — Resubmission

Writer revises only the returned items and resubmits. Lead writer reviews only the returned criteria — passing criteria do not need re-review.

If a resubmission introduces new failures in previously passing criteria, these are flagged and the file is returned again. This is rare but possible when a revision cascades.

---

## Review tracking

All approved and returned submissions are logged in:
`_System/Writer-Certification/Records/`

One record file per submission cycle. Format:
`NPC-Name_Writer-Name_DATE_APPROVED.md` or `NPC-Name_Writer-Name_DATE_RETURNED.md`

---

*[[../../README|Back to Index]] · [[../../_System/Writer-Standards|Writer Standards]] · [[../../_System/Writer-Certification/04-NPC-Submission-Form|Submission Form]] · [[../README|NPC Index]]*
