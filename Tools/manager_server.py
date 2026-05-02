"""
Ironthorn Manager Board Server v1.0
=====================================
Local manager interface for reviewing writer submissions, approving/returning
NPCs to the vault, and seeing all submission history from the Google Sheet.

USAGE:
  Double-click: start_manager_board.bat
  Then open: http://localhost:7843

WHAT IT DOES:
  - Serves manager-board.html at /
  - GET  /api/ping              -> health check
  - POST /api/auth              -> session login (shared password)
  - GET  /api/pending           -> list submissions in NPCs/_Pending/
  - GET  /api/intake            -> list files in NPCs/_Pending/_Intake/
  - GET  /api/submission/<name> -> file contents for a pending NPC
  - GET  /api/sheet             -> Google Sheet rows (read via service account or CSV export)
  - POST /api/approve           -> run approval flow, send email, update sheet
  - POST /api/return            -> stamp form, send return email, update sheet
  - POST /api/import-row        -> drop a sheet row into _Intake/ for the watcher

FIRST-RUN SETUP:
  1. Copy manager_config.example.json to manager_config.json
  2. Fill in:
     - shared_password
     - manager_email (Gmail address used to send notifications)
     - smtp_app_password (Gmail app password — generate at
       https://myaccount.google.com/apppasswords)
     - sheet_csv_url (publish-to-web CSV URL of the Submissions sheet, OR
       leave blank to disable sheet integration)
  3. Double-click start_manager_board.bat
"""

import os
import re
import json
import shutil
import smtplib
import secrets
import urllib.request
import urllib.parse
import webbrowser
from pathlib import Path
from datetime import date, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import StringIO
import csv

# ─── PATHS ────────────────────────────────────────────────────────────────────

VAULT_ROOT     = Path(r"C:\Users\steph\Desktop\Game\GameVault")
NPCS_DIR       = VAULT_ROOT / "NPCs"
PENDING_DIR    = NPCS_DIR / "_Pending"
INTAKE_DIR     = PENDING_DIR / "_Intake"
CHARACTERS_DIR = NPCS_DIR / "_Characters"
RECORDS_DIR    = VAULT_ROOT / "_System" / "Writer-Certification" / "Records"

TOOLS_DIR      = Path(__file__).parent
BOARD_FILE     = TOOLS_DIR / "manager-board.html"
CONFIG_FILE    = TOOLS_DIR / "manager_config.json"

PORT = 7843
SUBFOLDERS = ["Versions", "Submissions", "Dialogue", "Notes"]

# Files in _Pending/ that are NOT submission folders (workflow docs)
PENDING_NOISE = {
    "README.md", "LEAD-WRITER-REVIEW-WORKFLOW.md",
    "RETURN-NOTICE-TEMPLATE.md", "SUBMISSION-INTAKE-TEMPLATE.md",
}

# In-memory session token store (resets on server restart — fine for local use)
SESSIONS = set()

# ─── CONFIG ───────────────────────────────────────────────────────────────────

def load_config():
    if not CONFIG_FILE.exists():
        return None
    try:
        return json.loads(CONFIG_FILE.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"  ERROR: Could not parse {CONFIG_FILE.name}: {e}")
        return None

CFG = load_config()

# ─── FRONTMATTER PARSER (shared with writer_board) ────────────────────────────

def parse_frontmatter(content):
    fm = {}
    match = re.match(r'^---\r?\n([\s\S]*?)\r?\n---', content)
    if not match:
        return fm
    for line in match.group(1).split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        colon = line.find(':')
        if colon < 0:
            continue
        key = line[:colon].strip()
        val = line[colon+1:].strip()
        if len(val) >= 2 and val[0] in ('"', "'") and val[-1] == val[0]:
            val = val[1:-1]
        if val == 'true': val = True
        elif val == 'false': val = False
        elif val and val.lstrip('-').replace('.','',1).isdigit():
            val = float(val) if '.' in val else int(val)
        fm[key] = val
    return fm

# ─── PENDING SUBMISSIONS ──────────────────────────────────────────────────────

def list_pending_submissions():
    """Each subfolder of _Pending/ is a submission. Returns list of dicts."""
    out = []
    if not PENDING_DIR.exists():
        return out
    for item in sorted(PENDING_DIR.iterdir()):
        if not item.is_dir():
            continue
        if item.name.startswith('_'):  # skip _Intake
            continue
        files = sorted([f.name for f in item.iterdir() if f.is_file()])
        # Try to read the NPC file or submission form for metadata
        meta = {'npc_name': item.name, 'tier': '', 'faction': '',
                'district': '', 'writer': '', 'email': '',
                'submitted_date': '', 'files': files}
        # Try the canonical NPC file first
        for fname in [item.name + '.md', item.name + '_Submission-Form.md',
                      item.name + '_Submission-Intake.md']:
            fpath = item / fname
            if not fpath.exists(): continue
            try:
                fm = parse_frontmatter(fpath.read_text(encoding='utf-8'))
                if not meta['tier']         and fm.get('npc_tier'):       meta['tier'] = fm['npc_tier']
                if not meta['faction']      and fm.get('faction'):        meta['faction'] = fm['faction']
                if not meta['district']     and fm.get('location'):       meta['district'] = fm['location']
                if not meta['writer']       and fm.get('writer_name'):    meta['writer'] = fm['writer_name']
                if not meta['writer']       and fm.get('writer'):         meta['writer'] = fm['writer']
                if not meta['writer']       and fm.get('submitted_by'):   meta['writer'] = fm['submitted_by']
                if not meta['email']        and fm.get('writer_email'):   meta['email'] = fm['writer_email']
                if not meta['email']        and fm.get('submitted_email'):meta['email'] = fm['submitted_email']
                if not meta['submitted_date'] and fm.get('submitted_date'):meta['submitted_date'] = fm['submitted_date']
                if not meta['submitted_date'] and fm.get('date'):         meta['submitted_date'] = fm['date']
            except Exception:
                pass
        out.append(meta)
    return out

def list_intake_files():
    """Files in _Intake/ that haven't been processed yet."""
    out = []
    if not INTAKE_DIR.exists():
        return out
    for item in sorted(INTAKE_DIR.iterdir()):
        if not item.is_file(): continue
        if item.name.startswith('_'): continue
        if item.name.lower() in {'readme.md', 'readme.txt', 'instructions.md'}: continue
        if not (item.name.endswith('.md') or item.name.endswith('.txt')): continue
        stat = item.stat()
        out.append({
            'filename': item.name,
            'size': stat.st_size,
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
        })
    return out

def get_submission_files(npc_name):
    """Read all files for one pending submission."""
    folder = PENDING_DIR / npc_name
    if not folder.is_dir():
        return None
    files = {}
    for f in folder.iterdir():
        if f.is_file() and f.name.endswith('.md'):
            try:
                files[f.name] = f.read_text(encoding='utf-8')
            except Exception as e:
                files[f.name] = f"(could not read: {e})"
    return files

# ─── GOOGLE SHEET ─────────────────────────────────────────────────────────────

def fetch_sheet_rows():
    """
    Read rows from the Submissions sheet via its publish-to-web CSV URL.
    Returns list of dicts keyed by column header. Returns empty list if the
    URL is not configured or the fetch fails.

    To get the CSV URL:
      1. Open the Google Sheet
      2. File -> Share -> Publish to web
      3. Choose: Submissions sheet, CSV format
      4. Copy the URL into manager_config.json under sheet_csv_url
    """
    if not CFG or not CFG.get('sheet_csv_url'):
        return []
    try:
        with urllib.request.urlopen(CFG['sheet_csv_url'], timeout=10) as r:
            text = r.read().decode('utf-8')
        reader = csv.DictReader(StringIO(text))
        rows = []
        for i, row in enumerate(reader):
            row['_row_index'] = i + 2  # +2 because: 1-indexed + header row
            rows.append(row)
        # Most recent first
        rows.reverse()
        return rows
    except Exception as e:
        print(f"  Sheet fetch failed: {e}")
        return []

def find_sheet_row_for_npc(npc_name):
    """Find the most recent sheet row matching this NPC name."""
    rows = fetch_sheet_rows()
    needle = npc_name.replace('-', ' ').lower().strip()
    for row in rows:
        sheet_name = (row.get('NPC Name') or '').replace('-', ' ').lower().strip()
        if sheet_name == needle:
            return row
    return None

# ─── EMAIL ────────────────────────────────────────────────────────────────────

def send_email(to_addr, subject, body):
    """Send via Gmail SMTP using app password from config."""
    if not CFG:
        return False, "Config not loaded"
    user = CFG.get('manager_email')
    pw = CFG.get('smtp_app_password')
    if not user or not pw:
        return False, "manager_email or smtp_app_password not set in manager_config.json"

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as s:
            s.login(user, pw)
            s.send_message(msg)
        return True, "Sent"
    except Exception as e:
        return False, str(e)

# ─── APPROVE / RETURN ─────────────────────────────────────────────────────────

def get_version_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if match:
            vm = re.search(r'^version:\s*["\']?([0-9]+\.[0-9]+)["\']?',
                           match.group(1), re.MULTILINE)
            if vm: return vm.group(1)
    except Exception: pass
    return "1.0"

def approve_submission(npc_name, manager_name, send_notification=True):
    """
    Replicates approve_npc.py's logic, plus emails the writer and writes a
    record file. Returns (success, message_lines).
    """
    today = date.today().strftime("%Y-%m-%d")
    log = []

    pending_folder = PENDING_DIR / npc_name
    canonical_file = NPCS_DIR / f"{npc_name}.md"
    char_folder = CHARACTERS_DIR / npc_name
    versions_folder = char_folder / "Versions"
    submissions_folder = char_folder / "Submissions"

    if not pending_folder.is_dir():
        return False, [f"ERROR: Pending folder not found: {pending_folder}"]

    # Find the NPC file in _Pending/
    npc_file_pending = pending_folder / f"{npc_name}.md"
    if not npc_file_pending.exists():
        # Try any .md file that's not the form / intake / return
        candidates = [f for f in pending_folder.glob("*.md")
                      if "Submission" not in f.name and "Intake" not in f.name and "Return" not in f.name]
        if len(candidates) == 1:
            npc_file_pending = candidates[0]
        else:
            return False, [f"ERROR: Cannot find NPC file in {pending_folder}. Expected: {npc_name}.md"]

    # 1 — Ensure character folder structure exists
    for sub in SUBFOLDERS:
        (char_folder / sub).mkdir(parents=True, exist_ok=True)
    log.append(f"Character folder ready: {char_folder.name}/")

    # 2 — Snapshot existing canonical if present
    if canonical_file.exists():
        version = get_version_from_file(canonical_file)
        snap_name = f"{npc_name}_v{version}_{today}.md"
        shutil.copy2(canonical_file, versions_folder / snap_name)
        log.append(f"Snapshotted previous canonical -> Versions/{snap_name}")

    # 3 — Move NPC file to NPCs/
    shutil.move(str(npc_file_pending), str(canonical_file))
    log.append(f"Moved NPC file to canonical: NPCs/{canonical_file.name}")

    # 4 — Move all remaining .md files in pending folder to _Characters/<npc>/Submissions/
    moved_count = 0
    for fname in os.listdir(pending_folder):
        if fname.endswith(".md"):
            src = pending_folder / fname
            dst = submissions_folder / fname
            shutil.move(str(src), str(dst))
            moved_count += 1
    log.append(f"Moved {moved_count} submission documents -> Submissions/")

    # 5 — Remove empty pending folder
    try:
        if not list(pending_folder.iterdir()):
            pending_folder.rmdir()
            log.append(f"Removed empty _Pending/{npc_name}/")
    except Exception:
        log.append(f"Note: _Pending/{npc_name}/ not empty — left in place")

    # 6 — Write approval record
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    sheet_row = find_sheet_row_for_npc(npc_name)
    writer = (sheet_row or {}).get('Writer Name', 'Unknown')
    writer_email = (sheet_row or {}).get('Writer Email', '')
    record_name = f"{npc_name}_{writer.replace(' ','-')}_{today}_APPROVED.md"
    record_path = RECORDS_DIR / record_name
    record_path.write_text(f"""---
doc_type: "Approval Record"
npc_name: "{npc_name}"
writer: "{writer}"
writer_email: "{writer_email}"
manager: "{manager_name}"
status: "Approved"
date: "{today}"
---

# Approval Record — {npc_name}

**Writer:** {writer}
**Manager:** {manager_name}
**Date:** {today}

## Actions taken

{chr(10).join('- ' + line for line in log)}

## Next step

Open Unreal Editor → Window → NPC Dev Tools → Refresh Roster

The new NPC will appear in the panel after refresh.
""", encoding='utf-8')
    log.append(f"Wrote approval record -> Records/{record_name}")

    # 7 — Send email
    if send_notification and writer_email:
        subject = f"[APPROVED] {npc_name} — GameVault"
        body = f"""{writer},

{npc_name} has been approved and is now live in the vault.

The NPC will appear in the Unreal Dev Tools panel on the next Refresh Roster.

— {manager_name}
"""
        ok, msg = send_email(writer_email, subject, body)
        log.append(f"Email to {writer_email}: {'sent' if ok else 'FAILED — ' + msg}")
    elif send_notification:
        log.append("No writer email on file — skipped notification")

    # 8 — Update sheet (best effort)
    if sheet_row:
        log.append(f"Sheet row #{sheet_row.get('_row_index')} — manually flip Status to 'Approved'")
        # We don't write to the sheet directly; the manager's Apps Script web app
        # is what owns the sheet. The CSV publish-to-web is read-only.

    log.append("")
    log.append("REMINDER: Refresh Unreal NPC Dev Tools roster.")
    return True, log


def return_submission(npc_name, codes, notes, manager_name, send_notification=True):
    """
    Stamp the submission form with a Lead Writer Review section, write a return
    record, and email the writer with the return codes. Files stay in _Pending/.
    """
    today = date.today().strftime("%Y-%m-%d")
    log = []

    pending_folder = PENDING_DIR / npc_name
    if not pending_folder.is_dir():
        return False, [f"ERROR: Pending folder not found: {pending_folder}"]

    # Stamp the submission form's Lead Writer Review section
    form_file = pending_folder / f"{npc_name}_Submission-Form.md"
    if form_file.exists():
        try:
            content = form_file.read_text(encoding='utf-8')
            stamp = f"""

---

## Lead writer review — RETURNED on {today}

**Manager:** {manager_name}
**Decision:** Returned
**Date:** {today}

**Return codes:**
{chr(10).join('- ' + c for c in codes) if codes else '- (none specified)'}

**Specific notes:**

{notes or '(none provided)'}

---
"""
            # Append (don't overwrite) — the form has its own Lead Writer Review section
            # but we're adding a timestamped one for the latest review pass
            form_file.write_text(content + stamp, encoding='utf-8')
            log.append(f"Stamped Submission Form with return notes")
        except Exception as e:
            log.append(f"Warning: could not stamp form: {e}")
    else:
        log.append(f"Note: no submission form found in _Pending/{npc_name}/")

    # Write return record
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    sheet_row = find_sheet_row_for_npc(npc_name)
    writer = (sheet_row or {}).get('Writer Name', 'Unknown')
    writer_email = (sheet_row or {}).get('Writer Email', '')
    record_name = f"{npc_name}_{writer.replace(' ','-')}_{today}_RETURNED.md"
    record_path = RECORDS_DIR / record_name
    record_path.write_text(f"""---
doc_type: "Return Record"
npc_name: "{npc_name}"
writer: "{writer}"
writer_email: "{writer_email}"
manager: "{manager_name}"
status: "Returned"
date: "{today}"
return_codes: {json.dumps(codes)}
---

# Return Record — {npc_name}

**Writer:** {writer}
**Manager:** {manager_name}
**Date:** {today}

## Return codes
{chr(10).join('- ' + c for c in codes) if codes else '- (none specified)'}

## Notes

{notes or '(none provided)'}

## Files

Files remain in `NPCs/_Pending/{npc_name}/` for revision and resubmission.
""", encoding='utf-8')
    log.append(f"Wrote return record -> Records/{record_name}")

    # Send email
    if send_notification and writer_email:
        subject = f"[RETURNED] {npc_name} — GameVault — Action Required"
        codes_str = "\n".join("  - " + c for c in codes) if codes else "  - (none specified)"
        body = f"""{writer},

{npc_name} has been returned for revision. Specific issues below.

Return codes:
{codes_str}

Notes:
{notes or '(none provided)'}

Revise and resubmit to NPCs/_Pending/{npc_name}/ when ready.
No need to resubmit passing sections — only the returned items need revision.

The full return taxonomy and what each code means is in
GameVault/_System/NPC-Return-Taxonomy.md.

— {manager_name}
"""
        ok, msg = send_email(writer_email, subject, body)
        log.append(f"Email to {writer_email}: {'sent' if ok else 'FAILED — ' + msg}")
    elif send_notification:
        log.append("No writer email on file — skipped notification")

    return True, log


def import_sheet_row_to_intake(row_index):
    """
    Take a sheet row by its row index and write it as an intake file in
    _Intake/ — same format the writer portal's Download button produces, so
    the watcher can process it.
    """
    rows = fetch_sheet_rows()
    target = next((r for r in rows if r.get('_row_index') == row_index), None)
    if not target:
        return False, f"Row #{row_index} not found in sheet"

    npc_name = (target.get('NPC Name') or '').strip()
    if not npc_name:
        return False, "Row has no NPC Name"

    slug = re.sub(r'\s+', '-', npc_name)
    slug = re.sub(r'[^A-Za-z0-9_\-]', '', slug)

    prose = (target.get('The Sketch (Original Prose)') or '').strip()
    if not prose:
        return False, "Row has no prose"

    header = []
    if target.get('Writer Name'):  header.append(f"Writer: {target['Writer Name']}")
    if target.get('Writer Email'): header.append(f"Email: {target['Writer Email']}")
    if target.get('NPC Tier'):     header.append(f"Tier: {target['NPC Tier']}")
    if target.get('District'):     header.append(f"District: {target['District']}")

    content = "\n".join(header) + "\n---\n" + prose + "\n" if header else prose + "\n"

    INTAKE_DIR.mkdir(parents=True, exist_ok=True)
    target_path = INTAKE_DIR / f"{slug}.md"
    if target_path.exists():
        return False, f"{slug}.md already exists in _Intake/ — watcher may have already processed this row"
    target_path.write_text(content, encoding='utf-8')
    return True, f"Wrote {slug}.md to _Intake/. Watcher will pick it up within ~5 seconds."

# ─── HTTP HANDLER ─────────────────────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Session')

    def do_OPTIONS(self):
        self.send_response(200); self._cors(); self.end_headers()

    def _json(self, data, code=200):
        body = json.dumps(data, default=str).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self._cors(); self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get('Content-Length', 0))
        if length == 0: return {}
        try:
            return json.loads(self.rfile.read(length).decode('utf-8'))
        except Exception:
            return {}

    def _authed(self):
        return self.headers.get('X-Session') in SESSIONS

    def do_GET(self):
        path = self.path.split('?')[0]
        params = urllib.parse.parse_qs(self.path.split('?',1)[1]) if '?' in self.path else {}

        if path == '/' or path == '/index.html':
            try:
                content = BOARD_FILE.read_bytes()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(content))
                self._cors(); self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_response(404); self.end_headers()
                self.wfile.write(b'manager-board.html not found')
            return

        if path == '/api/ping':
            return self._json({
                'status': 'ok',
                'vault': str(VAULT_ROOT),
                'config_loaded': CFG is not None,
                'sheet_configured': bool(CFG and CFG.get('sheet_csv_url')),
                'time': datetime.now().isoformat()
            })

        # All other endpoints require auth
        if not self._authed():
            return self._json({'error': 'Not authenticated'}, 401)

        if path == '/api/pending':
            return self._json({'submissions': list_pending_submissions()})

        if path == '/api/intake':
            return self._json({'files': list_intake_files()})

        if path == '/api/submission':
            name = (params.get('name') or [''])[0]
            if not name:
                return self._json({'error': 'name required'}, 400)
            files = get_submission_files(name)
            if files is None:
                return self._json({'error': 'not found'}, 404)
            return self._json({'npc_name': name, 'files': files})

        if path == '/api/sheet':
            return self._json({'rows': fetch_sheet_rows()})

        self.send_response(404); self.end_headers()
        self.wfile.write(b'not found')

    def do_POST(self):
        path = self.path.split('?')[0]

        if path == '/api/auth':
            data = self._read_json()
            if not CFG:
                return self._json({'error': 'Server not configured. Create manager_config.json.'}, 500)
            if data.get('password') == CFG.get('shared_password'):
                token = secrets.token_urlsafe(32)
                SESSIONS.add(token)
                return self._json({'success': True, 'session': token,
                                   'manager_email': CFG.get('manager_email','')})
            return self._json({'error': 'Wrong password'}, 401)

        # All other POSTs require auth
        if not self._authed():
            return self._json({'error': 'Not authenticated'}, 401)

        data = self._read_json()

        if path == '/api/approve':
            npc = (data.get('npc_name') or '').strip()
            manager = (data.get('manager_name') or 'Lead Writer').strip()
            if not npc: return self._json({'error': 'npc_name required'}, 400)
            ok, log_lines = approve_submission(npc, manager,
                                               send_notification=data.get('send_email', True))
            return self._json({'success': ok, 'log': log_lines})

        if path == '/api/return':
            npc = (data.get('npc_name') or '').strip()
            codes = data.get('codes') or []
            notes = (data.get('notes') or '').strip()
            manager = (data.get('manager_name') or 'Lead Writer').strip()
            if not npc: return self._json({'error': 'npc_name required'}, 400)
            ok, log_lines = return_submission(npc, codes, notes, manager,
                                              send_notification=data.get('send_email', True))
            return self._json({'success': ok, 'log': log_lines})

        if path == '/api/import-row':
            try:
                row_index = int(data.get('row_index') or 0)
            except Exception:
                return self._json({'error': 'row_index must be integer'}, 400)
            ok, msg = import_sheet_row_to_intake(row_index)
            return self._json({'success': ok, 'message': msg})

        self.send_response(404); self.end_headers()
        self.wfile.write(b'not found')

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    if not VAULT_ROOT.exists():
        print(f"ERROR: Vault not found at {VAULT_ROOT}")
        input("Press Enter to exit..."); return
    if not BOARD_FILE.exists():
        print(f"ERROR: manager-board.html not found at {BOARD_FILE}")
        input("Press Enter to exit..."); return
    if CFG is None:
        print()
        print(f"  WARNING: {CONFIG_FILE.name} not found or invalid.")
        print(f"  Copy manager_config.example.json to manager_config.json and fill it in.")
        print(f"  The server will start, but auth and email will not work until you do.")
        print()

    print()
    print(f"  Ironthorn Manager Board v1.0")
    print(f"  =============================")
    print(f"  Vault:   {VAULT_ROOT}")
    print(f"  Pending: {len(list_pending_submissions())} submissions")
    print(f"  Intake:  {len(list_intake_files())} unprocessed files")
    print(f"  Board:   http://localhost:{PORT}")
    print(f"  Config:  {'loaded' if CFG else 'NOT LOADED'}")
    print(f"  Sheet:   {'configured' if (CFG and CFG.get('sheet_csv_url')) else 'not configured'}")
    print()
    print(f"  Opening browser... Ctrl+C to stop.")
    print()

    webbrowser.open(f"http://localhost:{PORT}")
    server = HTTPServer(('localhost', PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")

if __name__ == '__main__':
    main()
