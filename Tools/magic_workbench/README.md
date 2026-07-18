# Magic Workbench

Local Flask server that provides an authoring suite for Ironthorn's
magic system. Vault is canonical; SQLite is an in-memory cache;
all writes go back to the vault in the same shape the intake
watcher already understands.

## Running

```
start_magic_workbench.bat
```

First run requires Flask. If you see `ModuleNotFoundError: flask`,
install it once using the bundled Python:

```
"C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe" -m pip install flask
```

Then launch the bat file again.

The server runs on **http://localhost:7844**. Manager Board uses
7843; Writer Board uses 7842; these don't conflict.

## Architecture

- **Vault is canonical.** Every fact lives in the GameVault Markdown
  files. The Workbench reads them and writes back to them.
- **SQLite is a cache.** Rebuilt on startup from the vault. Also
  rebuilt every 60 seconds by a background poller when vault files
  change. Manual refresh via the "↻ Refresh" button in the nav.
- **Routes are per-tool.** Each tool gets its own URL (`/practitioner`,
  `/explorer`, `/aesthetics`). Adding a new tool is adding a new
  route, not a new server.
- **Magic constants are server-canonical.** Traditions, faction
  credentials, valid combinations, preferred channels — defined
  in `workbench_server.py` and served via `/api/magic-constants`.
  The form pulls from this API rather than hardcoding lists in HTML.

## Current state — v0.1 (foundation commit)

What works:
- Server starts, vault gets read, cache is built
- Home page shows index stats
- Three tool pages exist as routed placeholders
- Refresh button rebuilds the cache live
- Background poller picks up vault file changes
- Magic constants API serves the canonical enum tables

What does NOT work yet:
- The Practitioner Builder form (lands in v0.2)
- The full Explorer (lands in v0.3)
- The Aesthetics Guide content (lands in v0.3 and grows)
- Vault submission writes (lands in v0.2)
- Watchdog file-watch support (using poll fallback for now)

## Roadmap

| Version | Commit focus |
|---------|-------------|
| **v0.1** | Foundation: server, routing, cache, base templates. **← you are here** |
| v0.2 | Practitioner Builder: multi-step form, live validation, vault submission |
| v0.3 | Explorer and Aesthetics skeletons fleshed out; tradition cards interactive |
| v0.4 | Obsidian deep-links; cross-tool navigation between Builder and Explorer |
| v0.5+ | Cosmology Tracker (designer-only), Workings catalog, simulation tools |

## File layout

```
magic_workbench/
├── workbench_server.py          ← Flask app + vault reader + cache
├── start_magic_workbench.bat    ← Launch script (bundled Python)
├── workbench_cache.sqlite       ← Built at runtime; do not commit
├── README.md                    ← this file
├── STAGING_NPC-Template-v3.1.md ← v3.1 template; apply manually (see below)
├── templates/
│   ├── base.html                ← Header, nav, footer, refresh button
│   ├── home.html                ← Dashboard / index
│   ├── practitioner.html        ← Builder (placeholder in v0.1)
│   ├── explorer.html            ← Reference (placeholder in v0.1)
│   └── aesthetics.html          ← Style guide (placeholder in v0.1)
└── static/
    └── workbench.css            ← Shared dark theme
```

## Required next step: apply the NPC template v3.1 bump

The Practitioner Builder (v0.2) writes NPCs with the new magic
frontmatter fields. Those fields must exist in the canonical
NPC template before the Builder can submit valid files.

To apply the bump:

1. Snapshot the current v3.0 template:
   ```
   cd C:\Users\steph\Desktop\Game\GameVault\Tools
   python version_snapshot.py "_Templates\NPC-Template-v3.md"
   ```
2. Apply the changes from `STAGING_NPC-Template-v3.1.md` to the
   canonical `_Templates/NPC-Template-v3.md`. The staging file
   documents every change — frontmatter additions, the new Magic
   section, new Dataview queries, footer cross-link.
3. The bumped template's `previous_version` field should reference
   the snapshot file just created.
4. Delete the staging file after the bump is applied.

This is a manual step on purpose — overwriting load-bearing
canonical files via tooling without a snapshot first is the kind
of action that should require human intent.
