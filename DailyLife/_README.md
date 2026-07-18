# DailyLife

Ambient world life. The recurring routines, rumors, and small frictions
that make the world feel inhabited.

**Examples:**
- The chandler in Sanctum Ward complains about the price of tallow on
  market days.
- Tavern rumors reflecting recent simulation events.
- News crier scripts for district announcements.
- Compact dossier entries (paid-access content for player legibility).
- NPC daily routines.

**Authoring:** templates TBD as we identify the recurring shapes. Most
DailyLife content will be written by the Area Factions Engine's
Legibility Publisher on the daily tick, not authored manually.

**Read this first:** `_System/Story-Architecture.md`,
`_System/Area-Factions-Engine.md` (Legibility Publisher section).

DailyLife is **not authoritative** — it is flavor. World and Phase can
override it. DailyLife reads from WorldState and may be suppressed by
PhaseLayers; DailyLife never writes to either.

If a daily routine "should" change because of story progress, the change
belongs in a Phase layer that overrides the routine.
