---
phase_name: "PHASE NAME"
phase_slug: "phase-slug-kebab-case"
phase_group: "group-slug"
# Phases sharing a phase_group are mutually exclusive.
# A player is in exactly one phase per group, or in the implicit base state.
scope: "World/Region/Location-or-System"
# Where this phase applies. Outside this scope, the phase has no effect.
entry_conditions: []
# List of conditions that move a player into this phase.
# Each entry is a slug of a questline beat, world flag, or NPC threshold.
exit_conditions: []
# List of conditions that move a player out of this phase.
# Empty = sticky; once entered, the player stays in this phase.
overrides_world: []
# World flag slugs whose values are replaced for players in this phase.
overrides_daily: []
# DailyLife routine slugs that are suppressed or replaced for players in this phase.
npc_overrides: []
# NPC slugs whose dialogue, presence, or state is altered for players in this phase.
template_version: "1.0"
status: "Draft"
---

# `=this.phase_name`

> [!info] Phase at a glance
> **Slug:** `=this.phase_slug` · **Group:** `=this.phase_group`
> **Scope:** `=this.scope`
> **Status:** `=this.status`

---

## What changes in this phase

> REPLACE — one paragraph. From the player's perspective, what is
> different in the world while they are in this phase? Describe the
> experience, not the mechanism. "The grate behind the chandler's
> shop is open. Steam rises from it. Light from below. The chandler
> does not look at the grate."

## Why this is a phase, not a world flag

> REPLACE — one paragraph. Justify cohort-scoped state instead of
> server-shared state. The test: must two players standing next to
> each other be able to see different versions of the same place?
> If yes, this belongs here. If no, it belongs in WorldState.

## Phase group — what the alternatives are

This phase is a member of group `=this.phase_group`. The group
contains the following mutually exclusive phases:

| Phase slug | Entry trigger summary |
|---|---|
| REPLACE | REPLACE |
| REPLACE | REPLACE |
| (base state) | none of the above conditions met |

> REPLACE — describe the group's overall purpose. What aspect of
> the world does this group control? "Hollows access — four
> distinct ways a player can come to know the Hollows exist; each
> produces a different first encounter."

## Entry conditions

> REPLACE — describe in narrative terms what causes a player to
> enter this phase. List the formal conditions in `entry_conditions`
> above. Each condition is a slug referencing a beat, world flag,
> or NPC threshold.

## Exit conditions

> REPLACE — describe what causes a player to leave this phase.
> Most phases will be sticky (no exit). Phases that end — for
> example, a "during-the-siege" phase that resolves into an
> "after-the-siege" phase — declare their exits explicitly.

## What it overrides

**World flag overrides:**
> REPLACE — for each entry in `overrides_world`, state the flag
> slug, its World value, and its in-phase value. Justify each
> override.

**Daily routine overrides:**
> REPLACE — for each entry in `overrides_daily`, state which
> ambient routine is suppressed or replaced and what replaces it.

**NPC overrides:**
> REPLACE — for each entry in `npc_overrides`, state the NPC slug
> and what changes — dialogue branch, presence/absence, status
> ("the chandler is now boarded up; sign on the door reads
> `closed for repairs`"), or behavior tree.

## Conflict resolution

> REPLACE only if non-trivial. If a player qualifies for two
> phases in the same group simultaneously, which wins? Default
> rule: most-recent entry condition wins. Document exceptions
> here.

## Unreal mapping

| YAML field | UStruct field | Type |
|---|---|---|
| phase_slug | PhaseSlug | FName |
| phase_group | PhaseGroup | FName |
| scope | Scope | FString |
| entry_conditions | EntryConditions | TArray<FName> |
| exit_conditions | ExitConditions | TArray<FName> |
| overrides_world | OverridesWorld | TArray<FName> |
| overrides_daily | OverridesDaily | TArray<FName> |
| npc_overrides | NpcOverrides | TArray<FName> |

---

*[[../README|Back to Index]] · [[../_System/Story-Architecture]]*
