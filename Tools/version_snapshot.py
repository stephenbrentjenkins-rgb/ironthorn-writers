"""
GameVault Version Snapshot Tool v1.0
=====================================
Snapshots any canonical file to its correct Versions/ folder before editing.
Takes user error out of the version control loop.

USAGE:
  python version_snapshot.py <path_to_file>

EXAMPLES:
  python version_snapshot.py "C:\\Users\\steph\\Desktop\\Game\\GameVault\\NPCs\\Maren-Voss.md"
  python version_snapshot.py "C:\\Users\\steph\\Documents\\Unreal Projects\\Ironthorn\\Content\\Python\\ironthorn_blockout.py"
  python version_snapshot.py "_System\\Writer-Standards.md"  (relative to GameVault root)

WHAT IT DOES:
  1. Reads the file's current version from YAML frontmatter (defaults to 1.0)
  2. Determines the correct Versions/ folder for this file type
  3. Copies the file to Versions/ with the correct naming format
  4. Prints a clear confirmation before you edit anything

WHAT IT DOES NOT DO:
  - Does not edit the canonical file
  - Does not increment the version number (you do that after editing)
  - Does not move or delete anything
"""

import os
import re
import shutil
import sys
from datetime import date

# ─── VAULT AND PROJECT ROOTS ──────────────────────────────────────────────────

VAULT_ROOT  = r"C:\Users\steph\Desktop\Game\GameVault"
UNREAL_ROOT = r"C:\Users\steph\Documents\Unreal Projects\Ironthorn"

# ─── VERSIONS FOLDER MAP ──────────────────────────────────────────────────────
# Maps canonical file locations to their Versions/ folders.
# Entries are checked in order — first match wins.

VERSIONS_MAP = [
    # NPC files — each NPC has its own Versions/ folder inside _Characters/
    {
        "pattern": os.path.join(VAULT_ROOT, "NPCs") + os.sep,
        "exclude": [
            os.path.join(VAULT_ROOT, "NPCs", "_Characters"),
            os.path.join(VAULT_ROOT, "NPCs", "_Pending"),
        ],
        "versions_fn": lambda path: _npc_versions_folder(path),
    },
    # System docs
    {
        "pattern": os.path.join(VAULT_ROOT, "_System") + os.sep,
        "exclude": [],
        "versions_fn": lambda path: os.path.join(VAULT_ROOT, "_System", "Versions"),
    },
    # Faction files
    {
        "pattern": os.path.join(VAULT_ROOT, "Factions") + os.sep,
        "exclude": [os.path.join(VAULT_ROOT, "Factions", "Versions")],
        "versions_fn": lambda path: os.path.join(VAULT_ROOT, "Factions", "Versions"),
    },
    # World files
    {
        "pattern": os.path.join(VAULT_ROOT, "World") + os.sep,
        "exclude": [os.path.join(VAULT_ROOT, "World", "Ironthorn", "Versions")],
        "versions_fn": lambda path: _world_versions_folder(path),
    },
    # Python scripts
    {
        "pattern": os.path.join(UNREAL_ROOT, "Content", "Python") + os.sep,
        "exclude": [os.path.join(UNREAL_ROOT, "Content", "Python", "Versions")],
        "versions_fn": lambda path: os.path.join(UNREAL_ROOT, "Content", "Python", "Versions"),
    },
]

# ─── HELPER FUNCTIONS ─────────────────────────────────────────────────────────

def _npc_versions_folder(path):
    """For NPC files, the Versions folder is inside _Characters/NPC-Name/Versions/"""
    filename = os.path.splitext(os.path.basename(path))[0]
    return os.path.join(VAULT_ROOT, "NPCs", "_Characters", filename, "Versions")

def _world_versions_folder(path):
    """For World files, Versions/ lives alongside the file in its district folder."""
    folder = os.path.dirname(path)
    return os.path.join(folder, "Versions")

def read_version_from_frontmatter(filepath):
    """Read the version: field from YAML frontmatter. Returns '1.0' if not found."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Look for YAML frontmatter block
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if match:
            frontmatter = match.group(1)
            version_match = re.search(r'^version:\s*["\']?([0-9]+\.[0-9]+)["\']?', 
                                      frontmatter, re.MULTILINE)
            if version_match:
                return version_match.group(1)
    except Exception:
        pass
    return "1.0"

def get_versions_folder(filepath):
    """Determine the correct Versions/ folder for this file."""
    abs_path = os.path.abspath(filepath)
    
    for entry in VERSIONS_MAP:
        pattern = entry["pattern"]
        excludes = entry["exclude"]
        
        if abs_path.startswith(pattern):
            # Check it's not in an excluded subfolder
            excluded = any(abs_path.startswith(ex) for ex in excludes)
            if not excluded:
                return entry["versions_fn"](abs_path)
    
    # Fallback: Versions/ folder alongside the file
    return os.path.join(os.path.dirname(filepath), "Versions")

def build_snapshot_name(filepath, version):
    """Build the versioned filename: FileName_vMAJOR.MINOR_YYYY-MM-DD.ext"""
    base = os.path.splitext(os.path.basename(filepath))[0]
    ext  = os.path.splitext(filepath)[1]
    today = date.today().strftime("%Y-%m-%d")
    return f"{base}_v{version}_{today}{ext}"

def snapshot(filepath):
    """Main function — snapshot the file to its Versions/ folder."""
    
    # Resolve path
    if not os.path.isabs(filepath):
        filepath = os.path.join(VAULT_ROOT, filepath)
    filepath = os.path.abspath(filepath)
    
    # Validate
    if not os.path.isfile(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    
    # Read version
    version = read_version_from_frontmatter(filepath)
    
    # Determine Versions/ folder
    versions_folder = get_versions_folder(filepath)
    
    # Ensure Versions/ folder exists
    os.makedirs(versions_folder, exist_ok=True)
    
    # Build snapshot filename
    snapshot_name = build_snapshot_name(filepath, version)
    snapshot_path = os.path.join(versions_folder, snapshot_name)
    
    # Check if snapshot already exists
    if os.path.exists(snapshot_path):
        print(f"\n⚠  Snapshot already exists: {snapshot_path}")
        answer = input("   Overwrite? (y/n): ").strip().lower()
        if answer != 'y':
            print("   Snapshot cancelled. Edit the canonical file and update its version number before snapshotting again.")
            sys.exit(0)
    
    # Copy
    shutil.copy2(filepath, snapshot_path)
    
    # Confirm
    print(f"\n✓  Snapshot complete")
    print(f"   Source:   {filepath}")
    print(f"   Snapshot: {snapshot_path}")
    print(f"   Version:  v{version}")
    print(f"\n   You can now edit the canonical file.")
    print(f"   When done, update 'version:' in the frontmatter and set 'previous_version: {snapshot_name}'")

# ─── ENTRY POINT ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    
    snapshot(sys.argv[1])
