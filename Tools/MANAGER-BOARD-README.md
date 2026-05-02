# Ironthorn Manager Board

A local web app for reviewing writer submissions, approving NPCs into the vault, and returning submissions for revision with structured return codes and email notifications.

Runs entirely on your machine. No cloud, no public URL.

---

## What it does

Four tabs:

1. **Pending Review** — every folder in `NPCs/_Pending/<NPC-Name>/`. Click an NPC to see all three submitted files (NPC file, submission form, intake doc) side-by-side. Approve or return with structured codes from `NPC-Return-Taxonomy.md`.

2. **Intake Queue** — files sitting in `NPCs/_Pending/_Intake/` waiting for the watcher. Useful to confirm the watcher is actually running and not jammed.

3. **Sheet History** — every row from the writer portal's Google Sheet, most recent first. Status, writer, NPC name, faction, district. One-click "Import to _Intake/" if a row never made it through (e.g. watcher was offline when submitted).

4. **Settings** — server status, manager name (used as signature on records and emails).

### Approve flow

When you click Approve, the server:

- Snapshots the existing canonical file to `_Characters/<NPC>/Versions/<NPC>_v<X.Y>_<date>.md` if one exists
- Moves `<NPC>.md` from `_Pending/` to `NPCs/`
- Moves the submission form and intake doc to `_Characters/<NPC>/Submissions/`
- Creates `_Characters/<NPC>/{Versions,Submissions,Dialogue,Notes}/` if missing
- Removes the now-empty `_Pending/<NPC>/` folder
- Writes a record to `_System/Writer-Certification/Records/<NPC>_<Writer>_<date>_APPROVED.md`
- Emails the writer (Gmail SMTP — configurable, can be turned off per-action)
- Reminds you to **Refresh Roster in Unreal → Window → NPC Dev Tools → Refresh Roster**

The Unreal refresh has to be done by you in the editor — there's no CLI hook for it.

### Return flow

When you click Return:

- Stamps the submission form's "Lead Writer Review" section with the date, your name, the return codes, and your specific notes
- Files stay in `_Pending/<NPC>/` for the writer to revise and resubmit
- Writes a record to `_System/Writer-Certification/Records/<NPC>_<Writer>_<date>_RETURNED.md`
- Emails the writer with the return codes, the official "what to fix" guidance from `NPC-Return-Taxonomy.md`, and your specific notes

---

## First-run setup

### 1. Files in place

These files all go in `C:\Users\steph\Desktop\Game\GameVault\Tools\`:

- `manager_server.py`
- `manager-board.html`
- `start_manager_board.bat`
- `manager_config.example.json`

(All four are in this delivery.)

### 2. Config

Copy `manager_config.example.json` to `manager_config.json` (same folder). Open it and set:

- **`shared_password`** — pick anything. The web page asks for it on first load. Sessions persist in browser localStorage.

- **`manager_email`** — the Gmail address that sends approval/return emails. Almost certainly `stephenbrentjenkins@gmail.com`.

- **`smtp_app_password`** — Gmail won't accept your normal password for SMTP. You need an "app password":
  1. Go to https://myaccount.google.com/apppasswords (you must have 2-Step Verification on for this to work — Google forces it)
  2. Click "Select app" → "Other (custom name)" → name it "Ironthorn Manager Board"
  3. Click Generate. You get a 16-character string. Paste it (without spaces) into `smtp_app_password`.
  4. The app password is shown once. If you lose it, generate a new one and revoke the old.

- **`sheet_csv_url`** — optional. To enable the Sheet History tab:
  1. Open the Submissions Google Sheet
  2. **File → Share → Publish to web**
  3. In the dropdown, choose the **Submissions** sheet (not "entire document")
  4. Format: **Comma-separated values (.csv)**
  5. Click Publish. Copy the URL it gives you.
  6. Paste into `sheet_csv_url`.

  Leave as `""` to disable the Sheet tab. Approve/return still work without it — the writer's email is read from the submission form's frontmatter rather than the sheet.

### 3. Run it

Double-click `start_manager_board.bat`.

The server starts on port 7843 and your browser opens automatically. Enter the shared password. You're in.

Subsequent runs: same .bat, same browser. Sessions resume from localStorage so you don't re-enter the password unless the server restarts.

---

## Config file is git-ignored — keep it that way

`manager_config.json` contains an SMTP app password. Don't commit it. If the vault is in source control, add a `.gitignore` entry for it.

---

## What this does NOT do

- **Doesn't refresh the Unreal NPC Dev Tools panel.** Has to be done in the editor. The approval flow ends with a reminder.
- **Doesn't write to the Google Sheet.** The sheet is owned by the Apps Script web app. The CSV publish-to-web URL is read-only. So when you approve/return, the sheet's Status column doesn't auto-flip — you'd flip it manually in the sheet, or live with the discrepancy. (If this matters, the next iteration could use a Google Sheets API service account to enable two-way writes, but it adds setup steps.)
- **Doesn't replace the intake watcher.** The watcher still has to be running to process raw prose drops in `_Intake/`. The manager board reviews what the watcher produces.
- **No HTTPS.** It's localhost-only — there's no certificate. If you ever want to access this from another machine on your LAN, that's a different setup conversation.

---

## Daily workflow

1. Writer submits a Dossier in the Apps Script portal → row lands in the Google Sheet
2. Writer (or you) clicks "Download intake file" and saves it into `_Intake/`
3. `intake_watcher.py` (running in its own window) picks it up within ~5 seconds, calls Claude, produces the pre-filled submission form and origin story, and creates `_Pending/<NPC>/`
4. You open the manager board, see the new pending submission, review it
5. Approve → file moves to `NPCs/`, email goes out, you refresh Unreal
6. (Or) Return → form gets stamped, email goes out with return codes, writer revises

Three tools running in their own windows: `start_intake_watcher.bat`, `start_manager_board.bat`, and (for the read-only NPC overview) `start_writer_board.bat`. They don't conflict — different ports, different files.

---

## Troubleshooting

**"Auth failed"** — `shared_password` in `manager_config.json` doesn't match what you typed. Restart the server after editing the config (it reads on startup).

**Approve emails fail with "Authentication failed"** — the SMTP app password is wrong, expired, or 2-Step Verification isn't on for your Gmail account. Generate a new app password.

**Sheet tab is empty** — `sheet_csv_url` is empty, or the publish-to-web URL points at the wrong tab. Open the URL in a browser; you should see CSV. If you see HTML, you grabbed the wrong URL (publish-to-web URLs end in `/pub?...output=csv`, not `/edit`).

**Pending tab is empty but you know there are submissions** — they're probably still in `_Intake/` waiting for the watcher. Check the Intake tab. If files are sitting there, start the watcher.

**Server says "manager_config.json not found"** — you created it in the wrong folder. It must live next to `manager_server.py` in `Tools/`.
