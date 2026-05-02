# CLAUDE.md — GameVault (Ironthorn RPG)

This file is the orientation guide for any Claude instance working in
this project. Read it first before doing anything substantive.

## What this is

Ironthorn is a dark fantasy RPG. The GameVault is the Obsidian-based
authoring environment for everything narrative — NPCs, factions, world
lore, story threads. It feeds an Unreal Engine project.

The vault lives at: `C:\Users\steph\Desktop\Game\GameVault\`
The Unreal project lives at: `C:\Users\steph\Documents\Unreal Projects\Ironthorn\`

## Tone anchor

The single most important thing about this world: **NPCs are tired,
not broken.** Every character has a private life, private fear,
private goal, private memory of the player. They suppress, they don't
perform. Read `_System/Writer-Standards.md` and
`_System/Writer-Certification/01-Writer-Primer.md` before generating
or critiquing any NPC content.

## Top-level structure

- `NPCs/` — Approved canonical NPC files (e.g. `Brother-Aldric.md`).
  These are the "live" NPCs the Unreal Dev Tools panel reads.
- `NPCs/_Pending/<NPC-Name>/` — Submissions awaiting review. Each
  folder holds the NPC file, submission form, and intake doc.
- `NPCs/_Pending/_Intake/` — Raw prose drops the intake watcher
  picks up and processes.
- `NPCs/_Characters/<NPC-Name>/` — Per-NPC subfolder with
  `Versions/`, `Submissions/`, `Dialogue/`, `Notes/`. Created on
  approval.
- `Factions/` — Faction files (Compact, Veil, Covenant, etc.)
- `World/` — Districts, locations, world lore.
- `_System/` — Reference materials (alignment spectrum, attribute
  reference, return taxonomy, tier reference, intelligence system,
  cross-NPC connection map).
- `_System/Writer-Certification/` — Writer Primer, Quiz, Glossary,
  Submission Form template, DevTools README.
- `_System/Writer-Certification/Records/` — Approval and return
  records, one per review pass.
- `_Templates/NPC-Template-v3.md` — Canonical template all NPC
  files must follow.
- `Tools/` — Local Python tooling (see below).

## NPC template

`_Templates/NPC-Template-v3.md` defines 41 frontmatter keys and the
layered body structure (T1 Quick Profile, T2 Identity / Attributes,
T3 Goals / Decision Map). All canonical NPC files conform to this.
Don't invent new frontmatter keys without checking against the
template — the Unreal `FNPC_DataRow` UStruct (in the Unreal project,
not the vault) has to match exactly.

## The submission pipeline

1. **Writer Portal** (Google Apps Script web app) — quiz-gated form
   that captures writer name/email + NPC prose + structured stats.
   Drops a single `.md` into `_Intake/` with header + prose format.
   Sheet ID: `1WO2e70KJ9USmKL3pEvzYzYxzCrxPNnCa7Ux4Q_bWEv4`.
   Code lives in Apps Script (not in this repo). Latest source is
   in `Tools/Code.gs` for reference.

2. **Intake Watcher** (`Tools/intake_watcher.py`) — runs locally,
   watches `_Intake/`, calls Claude Code CLI on each new file, and
   produces:
   - `_Pending/<NPC>/<NPC>_Submission-Form.md`
   - `_Pending/<NPC>/<NPC>_Submission-Intake.md`
   - `_Characters/<NPC>/Notes/Origin-Story.md`
   Started by `start_intake_watcher.bat`. Must be running for new
   submissions to process.

3. **Manager Board** (`Tools/manager_server.py` +
   `manager-board.html`) — local web app on `localhost:7843` for
   reviewing pending submissions, approving (file moves +
   email + record), or returning with structured codes from
   `_System/NPC-Return-Taxonomy.md`. Started by
   `start_manager_board.bat`.

4. **Approve script** (`Tools/approve_npc.py`) — the legacy
   command-line equivalent of the Manager Board's approve action.
   Still works; kept for emergencies. Use the Manager Board by
   default.

5. **Writer Board** (`Tools/writer_board_server.py` +
   `ironthorn-writer-board.html`) — read-only NPC overview at
   `localhost:7842`. Useful for browsing what's in the vault.
   Started by `start_writer_board.bat`.

6. **Unreal Dev Tools panel** — reads `NPCs/` via the Obsidian Local
   REST API plugin (port 27123) and exports JSON for Unreal to
   ingest as a DataTable of `FNPC_DataRow` structs. The panel HTML
   and the UStruct definition live in the Unreal project, not here.
   Refreshed manually after approval — there's no CLI hook.

## Python on this machine

There is NO system Python on PATH. The Python that runs all these
tools is bundled with Claude Desktop at:

C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

Every `.bat` in `Tools/` hard-codes that path via `set PYTHON=...`
and calls `"%PYTHON%" script.py`. New `.bat` files must follow this
pattern. `python script.py` will fail.

## Manager Board config

`Tools/manager_config.json` holds the manager password, Gmail SMTP
app password, and (optional) Sheet publish-to-web CSV URL.
**This file contains secrets** — must be in `.gitignore`. The
example template is `manager_config.example.json`.

## Standards and conventions

- NPC names use hyphens in slugs: `Brother-Aldric.md` not
  `Brother Aldric.md`. Slugifier is `re.sub(r'\s+', '-', name)`
  followed by removing non-alphanumeric/hyphen/underscore chars.
- Frontmatter is YAML with `template_version: "3.0"`. Status values:
  `Draft`, `Live`, `Returned`, `Archived`.
- All approval/return records go to
  `_System/Writer-Certification/Records/<NPC>_<Writer>_<date>_APPROVED.md`
  or `_RETURNED.md`.
- Return codes follow `_System/NPC-Return-Taxonomy.md` exactly.
  Don't invent new codes.
- Every Tier 3+ NPC must have a Decision Map and an in-world response
  line. Every NPC must have surface/mid/deep tells.

## Things to NOT do

- Don't write fake NPC content into approved files. If a writer
  submitted a file, the Original Sketch section is sacred — preserve
  verbatim.
- Don't auto-set flags (`liar_mark_active`, `debt_flag_active`, etc.)
  when generating NPC files. Flags are mechanical state, not narrative
  choice.
- Don't reproduce song lyrics, copyrighted character names from other
  IP, or trademarked franchise material in NPC content.
- Don't modify `Code.gs` or `Index.html` (in the Apps Script project)
  without first reading what's currently deployed — they live outside
  this repo and version drift causes bugs.
- Don't suggest cloud-based solutions (GitHub Actions, Codespaces,
  Apps Script web apps doing file moves) for anything that needs to
  touch the local filesystem. The local Python tools are the right
  layer for that.

## Current state

- v4.2 of the Apps Script Writer Portal is deployed (login removed,
  intake-only download).
- Manager Board v1.0 is functional. Sheet History tab requires
  configuring `sheet_csv_url` in `manager_config.json`.
- The vault is not yet in source control — GitHub setup is the next
  scheduled task.