"""
GameVault NPC Character Folder Structure Builder
Creates the full _Characters folder hierarchy for all 42 named NPCs.

Each NPC gets:
  _Characters/NPC-Name/
    Current/        ← the live canonical file lives here (symlinked from NPCs/)
    Versions/       ← v1, v2, v3 etc — timestamped snapshots on each revision
    Submissions/    ← writer submission forms for this NPC
    Dialogue/       ← dialogue scripts, scene files, line reads
    Notes/          ← designer notes, reference images, inspiration

Run from: anywhere with Python
"""

import os

BASE = r"C:\Users\steph\Desktop\Game\GameVault\NPCs\_Characters"

NPCS = [
    # Sanctum Ward
    "Brother-Aldric",
    "Inquisitor-Commander-Leth",
    "Torven-Ashcroft",
    "Nelle-Davar",
    "Solta-Byrne",
    "Ser-Orvane",
    "Registrar-Celn-Avour",
    "Mirren",
    "Arnath",
    # Greenward
    "Grove-Keeper-Sennath",
    "Verath-of-the-Still-Hand",
    "Iravel",
    "Sellen",
    "Perris",
    "Warden-Duss",
    "Renn",
    # Ledger Row
    "Factor-Renne-Saul",
    "Auditor-Vesh",
    "Treasurer-Vasken-Oull",
    "Orvan-Sel",
    "Officer-Maret",
    "Oswin-Creel",
    "Doss",
    "Hallum",
    # Ashgate Quarter
    "Scholar-Physician-Dael",
    "Davan-Ord",
    "Maren-Voss",
    "Cress",
    "Works-Director-Havel",
    "Pell",
    "Mossa",
    "Watch-Lead-Brenk",
    "Grundt",
    # Wound Market
    "Petrov-Seld",
    "Sevin",
    "The-Collector",
    "Arcanist-Vorell",
    "Sel-Harrow",
    "Essa",
    "Oversight-Lead-Penra",
    "Kess",
    # The Hollows
    "Rynn-Ashav",
    "The-Guttered",
    # Commander Syla (seed NPC)
    "Commander-Syla",
]

SUBFOLDERS = [
    "Versions",
    "Submissions",
    "Dialogue",
    "Notes",
]

created = 0
for npc in NPCS:
    npc_path = os.path.join(BASE, npc)
    os.makedirs(npc_path, exist_ok=True)
    for sub in SUBFOLDERS:
        sub_path = os.path.join(npc_path, sub)
        os.makedirs(sub_path, exist_ok=True)
        created += 1

print(f"Created {len(NPCS)} NPC folders with {len(SUBFOLDERS)} subfolders each.")
print(f"Total directories created: {created}")
print(f"Base path: {BASE}")
