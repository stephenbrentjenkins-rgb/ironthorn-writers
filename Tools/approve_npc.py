"""
GameVault NPC Approval Tool v1.0
==================================
Automates the lead writer approval workflow:
  1. Snapshots the existing canonical NPC file (if one exists) to Versions/
  2. Moves the submitted NPC file from _Pending/ to NPCs/
  3. Moves the submission form to _Characters/NPC-Name/Submissions/
  4. Creates the _Characters/NPC-Name/ folder structure if it doesn't exist
  5. Prints a summary of everything that moved

USAGE:
  python approve_npc.py <npc-name>

EXAMPLE:
  python approve_npc.py "Factor-Renne-Saul"

The NPC name must match the folder name in NPCs/_Pending/
"""

import os
import shutil
import sys
import glob
from datetime import date

VAULT_ROOT = r"C:\Users\steph\Desktop\Game\GameVault"

NPCS_DIR       = os.path.join(VAULT_ROOT, "NPCs")
PENDING_DIR    = os.path.join(VAULT_ROOT, "NPCs", "_Pending")
CHARACTERS_DIR = os.path.join(VAULT_ROOT, "NPCs", "_Characters")

SUBFOLDERS = ["Versions", "Submissions", "Dialogue", "Notes"]

def get_version_from_file(filepath):
    """Read version from frontmatter."""
    import re
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if match:
            vm = re.search(r'^version:\s*["\']?([0-9]+\.[0-9]+)["\']?',
                           match.group(1), re.MULTILINE)
            if vm:
                return vm.group(1)
    except Exception:
        pass
    return "1.0"

def approve_npc(npc_name):
    today = date.today().strftime("%Y-%m-%d")

    pending_folder = os.path.join(PENDING_DIR, npc_name)
    canonical_file = os.path.join(NPCS_DIR, f"{npc_name}.md")
    char_folder    = os.path.join(CHARACTERS_DIR, npc_name)
    versions_folder = os.path.join(char_folder, "Versions")
    submissions_folder = os.path.join(char_folder, "Submissions")

    print(f"\n=== GameVault NPC Approval: {npc_name} ===\n")

    # Validate pending folder exists
    if not os.path.isdir(pending_folder):
        print(f"ERROR: Pending folder not found: {pending_folder}")
        print(f"       Check that the NPC name matches exactly.")
        sys.exit(1)

    # Find the NPC file in _Pending/
    npc_file_pending = os.path.join(pending_folder, f"{npc_name}.md")
    if not os.path.isfile(npc_file_pending):
        # Try any .md file that's not the submission form or intake doc
        md_files = [f for f in glob.glob(os.path.join(pending_folder, "*.md"))
                    if "Submission" not in f and "Intake" not in f and "Return" not in f]
        if len(md_files) == 1:
            npc_file_pending = md_files[0]
        else:
            print(f"ERROR: Cannot find NPC file in {pending_folder}")
            print(f"       Expected: {npc_name}.md")
            sys.exit(1)

    # Step 1 — Create _Characters/NPC-Name/ structure if it doesn't exist
    print(f"[1/5] Ensuring character folder exists...")
    for sub in SUBFOLDERS:
        os.makedirs(os.path.join(char_folder, sub), exist_ok=True)
    print(f"      ✓ {char_folder}")

    # Step 2 — Snapshot existing canonical file if it exists
    if os.path.isfile(canonical_file):
        version = get_version_from_file(canonical_file)
        snap_name = f"{npc_name}_v{version}_{today}.md"
        snap_path = os.path.join(versions_folder, snap_name)
        print(f"\n[2/5] Snapshotting existing canonical file...")
        shutil.copy2(canonical_file, snap_path)
        print(f"      ✓ {snap_path}")
    else:
        print(f"\n[2/5] No existing canonical file — skipping snapshot (first submission)")

    # Step 3 — Move NPC file from _Pending/ to NPCs/
    print(f"\n[3/5] Moving NPC file to canonical location...")
    shutil.move(npc_file_pending, canonical_file)
    print(f"      ✓ {canonical_file}")

    # Step 4 — Move submission form to _Characters/Submissions/
    print(f"\n[4/5] Moving submission documents...")
    moved_count = 0
    for fname in os.listdir(pending_folder):
        if fname.endswith(".md"):
            src = os.path.join(pending_folder, fname)
            dst = os.path.join(submissions_folder, fname)
            shutil.move(src, dst)
            print(f"      ✓ {fname} → Submissions/")
            moved_count += 1
    if moved_count == 0:
        print(f"      (no remaining documents to move)")

    # Step 5 — Remove empty pending folder
    print(f"\n[5/5] Cleaning up pending folder...")
    remaining = os.listdir(pending_folder)
    if not remaining:
        os.rmdir(pending_folder)
        print(f"      ✓ Removed empty folder: {pending_folder}")
    else:
        print(f"      ⚠  Pending folder not empty — leaving in place:")
        for f in remaining:
            print(f"         {f}")

    # Summary
    print(f"\n=== Approval Complete ===")
    print(f"  NPC file:   {canonical_file}")
    print(f"  Versions:   {versions_folder}")
    print(f"  Submissions:{submissions_folder}")
    print(f"\n  Next step: Refresh Roster in Unreal → Window → NPC Dev Tools → Refresh Roster")
    print(f"  Then send approval email to the writer.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    approve_npc(sys.argv[1])
