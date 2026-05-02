---
doc_type: "Developer Tools"
version: "1.0"
status: "Active"
---

# GameVault Developer Tools

## Layer C — Obsidian Connected Panel

**File:** `gamevault-devtools.html`  
**How to use:** Open this file in any browser while Obsidian is running with the Local REST API plugin active.

### What it does
- **NPC Roster tab** — Live reads all NPC files from the vault. Click any NPC to inspect flag state, attribute scores, and threshold watch status.
- **Submit NPC tab** — Load an existing NPC to edit, or create a new one. Writes the completed `.md` file directly to `NPCs/` and logs a submission record to `_System/Writer-Certification/Records/`.
- **Certify Writer tab** — Log quiz results. Creates certification records in the vault.
- **Export → Unreal tab** — Exports NPC frontmatter as typed JSON for Unreal DataTable import. Also provides download buttons for all C++ plugin source files.

### Connection config
The tool connects to Obsidian at `http://localhost:27123` using the API key in `data.json`.  
If the vault is offline, the status dot in the header turns red.

---

## Layer D — Unreal Engine 5 Plugin

Download the four C++ files from the **Export → Unreal** tab:

| File | Purpose |
|------|---------|
| `NPC_DataRow.h` | UStruct definition — all NPC frontmatter fields typed for Unreal |
| `VaultBridge.h/.cpp` | HTTP bridge — reads/writes Obsidian REST API from within the editor |
| `NPCEditorTool.h` | UEditorUtilityWidget — dockable panel in the Unreal Editor |
| `NPCDevTools.Build.cs` | Module build file — dependency declarations |

### Setup in Unreal
1. Create `Source/NPCDevTools/` in your project
2. Add all four files to that folder
3. Add `NPCDevTools` to your `.uproject` Plugins array with `"Type": "Editor"`
4. Regenerate project files and build
5. In Unreal Editor: **Window → NPC Dev Tools** to open the dockable panel
6. Export JSON from the browser DevTools panel and import as a DataTable using `NPC_DataRow` as the row structure

### Data flow
```
GameVault (.md frontmatter)
        ↕ REST API (port 27123)
Browser DevTools Panel
        ↕ JSON export
NPC_DataTable.json
        ↕ Unreal DataTable import
FNPC_DataRow structs in-engine
        ↕ FVaultBridge (HTTP)
Live vault read/write from editor
```

---

*Vault version 1.7 · Session 13*
