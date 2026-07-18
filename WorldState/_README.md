# WorldState

Server-shared, persistent facts. True for every player on the server,
simultaneously. Survives logouts, server restarts, expansions.

**Examples:**
- "The Iron Dominion garrison sells the gate register to the Compact every Wednesday."
- Faction influence values per district (the largest write source — driven by the AFE).
- Permanent backstory facts that systems need to query.

**Authoring:** use `_Templates/WorldState-Flag-Template.md`. One file per flag.

For faction influence vectors specifically, set `flag_type: faction_influence_vector`
and use the `vector` block format (see template).

**Read this first:** `_System/Story-Architecture.md`, `_System/Faction-Influence.md`.

WorldState is written by:
- The Area Factions Engine (daily simulation tick) — most writes.
- Questline beats (explicit story-driven shifts via `world_writes:`).
- Designer manual override (logged with reason in the AFE event log).

WorldState is read by phases, daily routines, NPC dialogue, vendors,
and the AFE itself.
