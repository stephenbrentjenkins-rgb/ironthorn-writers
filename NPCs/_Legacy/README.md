---
doc_type: "Legacy NPCs README"
---

# _Legacy NPCs

NPCs in this folder were built for a previous version of the world (Ashford / Northern Watch / Iron Compact / Crown structure) and have not yet been ported to current canon (Ironthorn / Iron Dominion / faction structure).

These files are preserved intact — the writing is good and worth keeping. They are excluded from:
- Live `NPCs/` Dataview queries (because of folder location)
- Unreal Dev Tools roster export (DevTools reads `NPCs/` directly, not subfolders)
- The active build queue in `World/Ironthorn/Ironthorn-NPC-Roster.md`

## Current legacy NPCs

| NPC | Tier | Old faction | Old city | Status |
|-----|:----:|-------------|----------|--------|
| Commander Syla | 4 | The Iron Compact | Ashford | Awaiting port to Iron Dominion / Great Gate |

## To reactivate

1. Rewrite the file for current canon (faction names, city, structures, references to other NPCs)
2. Update frontmatter: remove `legacy: true`, `legacy_reason`, `legacy_date`
3. Move file back to `NPCs/`
4. Add the NPC to `Ironthorn-NPC-Roster.md` in the appropriate district table
5. Run an end-to-end Dataview query check

## Why not just delete?

Because the character work is good. Syla's psychology, decision map, and tell system are exemplary writing. Throwing it away to start fresh would be wasteful. Better to port it carefully when there is time.
