# PhaseLayers

Cohort-shared, story-driven world overrides. A phase is a *diff* against
WorldState — players who have reached a particular story state see a
different version of a place than players who haven't.

**Examples:**
- "Hollows entrance behind Ledger Row exists for players who have completed
  the Compact missing-agent questline."
- "After the siege, the bridge is rubble — for players who participated
  in the siege beat."

**Authoring:** use `_Templates/PhaseLayer-Template.md`. One file per phase.

Phases are organized by `phase_group`. All phases sharing a group are
mutually exclusive — a player is in exactly one of them at a time, or in
the implicit base state.

**Read this first:** `_System/Story-Architecture.md`.

Phases are activated by Questline beats via `phase_activations:`. They
read from WorldState; they cannot write to it. They override what daily
routines, NPC presence, and dialogue look like for players in the phase.

**The test for whether something belongs here, not in WorldState:** must
two players standing next to each other be able to see different
versions of the same place? If yes, Phase. If no, World.
