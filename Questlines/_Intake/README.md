# Beat Intake — Drop Zone

Drop a single `.md` or `.txt` file in this folder describing **one beat**.
The Beat Intake Watcher will pick it up within ~5 seconds, extract the
structured beat data, validate every reference against the live vault,
and drop the result into `Questlines/_Pending/<beat-slug>/` for review.

---

## File format

Name the file after the beat slug if you know it
(e.g. `hollows-compact-beat-03.md`), or after the beat's idea
(e.g. `Compact-Approaches-Player.md`) — the watcher will derive the
slug from the AI extraction.

Optional header (recommended — saves the AI guesswork):

```
Writer: Jane Smith
Email: jane@example.com
Questline: hollows-compact
Beat Index: 3
Trigger Type: location_entry
---
(prose below — describe what happens in this beat)
```

If you skip the header, write the prose only. The AI will infer what
it can; you'll fix the rest in review.

## What to write in the prose

Describe **one beat** — one moment in the questline. Cover:

- What happens, from the player's perspective.
- What triggers the beat (player walks somewhere, talks to a specific
  NPC, completes a prior beat, a flag flips, etc.).
- Who's involved by name. Use NPC names that exist in the vault — if
  you reference an NPC that hasn't been authored yet, the watcher will
  flag it in the validation report.
- What changes as a result. Phase changes, world flag changes, NPC
  stat changes. Be explicit. The watcher will translate intent into
  declared effects, but it can only declare what you describe.
- Tone: tired, not broken. Cinematic theatricality is a tone failure.

## What you'll get back

Inside `Questlines/_Pending/<beat-slug>/`:

- `<beat-slug>.md` — a filled-in beat file matching the canonical
  template, ready for review.
- `<beat-slug>_Validation-Report.md` — every reference checked against
  the vault. Errors must be fixed before approval.
- `<beat-slug>_Submission-Intake.md` — writer-facing summary.

Your original prose is preserved in
`Questlines/<questline-slug>/Notes/<beat-slug>_Origin-Prose.md`.

## Files this watcher will NOT process

- Anything starting with `_` or `.`
- `README.md`, `instructions.md`
- Anything that isn't `.md` or `.txt`

After processing, files move to `_Intake/_Done/` automatically.

## When the watcher complains

Most common issues:

1. **Prose too short** (under ~30 chars). Write a real description.
2. **Claude Code call failed.** Check that the Claude Code CLI is
   installed and authenticated: `claude --version` should work.
3. **Reference errors in the validation report.** The AI invented a
   slug that doesn't exist. Either correct it (replace with a real
   slug) or author the missing referent first.

---

*See `_Templates/Questline-Beat-Template.md` for the canonical beat
shape, and `_System/Story-Architecture.md` for how beats connect to
phases, world state, and NPCs.*
