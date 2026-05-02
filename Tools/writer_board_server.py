"""
GameVault Writer Board Server v1.0
====================================
Serves the writer board at http://localhost:7842
Reads NPC data directly from the vault filesystem -- no CORS issues.

USAGE:
  Double-click: start_writer_board.bat
  Then open: http://localhost:7842

WHAT IT DOES:
  - Serves ironthorn-writer-board.html at /
  - Exposes /api/npcs  -- returns all NPC frontmatter as JSON
  - Exposes /api/ping  -- returns vault status
  - Auto-opens the browser on startup
"""

import os
import re
import json
import webbrowser
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

VAULT_ROOT  = Path(r"C:\Users\steph\Desktop\Game\GameVault")
NPC_DIR     = VAULT_ROOT / "NPCs"
BOARD_FILE  = Path(r"C:\Users\steph\Desktop\Game\GameVault\Tools\ironthorn-writer-board.html")
PORT        = 7842

# ─── FRONTMATTER PARSER ───────────────────────────────────────────────────────

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
        # Strip quotes
        if len(val) >= 2 and val[0] in ('"', "'") and val[-1] == val[0]:
            val = val[1:-1]
        # Type conversion
        if val == 'true':
            val = True
        elif val == 'false':
            val = False
        elif val and val.lstrip('-').replace('.','',1).isdigit():
            val = float(val) if '.' in val else int(val)
        fm[key] = val
    return fm

def load_all_npcs():
    npcs = []
    if not NPC_DIR.exists():
        return npcs
    for f in NPC_DIR.iterdir():
        if not f.is_file():
            continue
        if not f.name.endswith('.md'):
            continue
        if f.name.startswith('_'):
            continue
        try:
            content = f.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)
            if fm.get('npc_name'):
                fm['_filename'] = f.name
                fm['_loaded'] = datetime.now().isoformat()
                npcs.append(fm)
        except Exception as e:
            print(f"  Warning: could not read {f.name}: {e}")
    npcs.sort(key=lambda n: -(n.get('npc_tier') or 0))
    return npcs

# ─── HTTP HANDLER ─────────────────────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Suppress default access log -- too noisy
        pass

    def send_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        path = self.path.split('?')[0]

        if path == '/' or path == '/index.html':
            self.serve_board()

        elif path == '/api/ping':
            self.serve_json({'status': 'ok', 'vault': str(VAULT_ROOT), 'time': datetime.now().isoformat()})

        elif path == '/api/npcs':
            npcs = load_all_npcs()
            print(f"  [API] /api/npcs -- returned {len(npcs)} NPCs")
            self.serve_json({'npcs': npcs, 'count': len(npcs), 'time': datetime.now().isoformat()})

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

    def serve_board(self):
        try:
            content = BOARD_FILE.read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(content))
            self.send_cors()
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Writer board HTML not found. Check BOARD_FILE path in server.py')

    def serve_json(self, data):
        body = json.dumps(data, default=str).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.send_cors()
        self.end_headers()
        self.wfile.write(body)

# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # Quick check
    if not VAULT_ROOT.exists():
        print(f"ERROR: Vault not found at {VAULT_ROOT}")
        input("Press Enter to exit...")
        raise SystemExit(1)

    if not BOARD_FILE.exists():
        print(f"ERROR: Writer board HTML not found at {BOARD_FILE}")
        input("Press Enter to exit...")
        raise SystemExit(1)

    npcs = load_all_npcs()
    print(f"")
    print(f"  GameVault Writer Board Server v1.0")
    print(f"  =====================================")
    print(f"  Vault:  {VAULT_ROOT}")
    print(f"  NPCs:   {len(npcs)} filed")
    print(f"  Board:  http://localhost:{PORT}")
    print(f"")
    print(f"  Opening browser...")
    print(f"  Ctrl+C to stop")
    print(f"")

    webbrowser.open(f"http://localhost:{PORT}")

    server = HTTPServer(('localhost', PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
