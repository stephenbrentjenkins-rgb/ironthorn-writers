---
system_doc: true
doc_type: "Architecture"
doc_name: "Story Architecture"
version: "1.0"
status: "Draft"
---

# Story Architecture

This is the model that governs how the main story, side questlines,
phasing, faction control, and everyday-life systems fit together.
It is the counterpart to `Writer-Standards.md` (which governs voice
and tone) and `NPC-Return-Taxonomy.md` (which governs NPC review
workflow). Read this before authoring any file in `WorldState/`,
`PhaseLayers/`, `Questlines/`, `DailyLife/`, `StoryInstances/`, or
`Instances/`.

If you change anything in this document, increment `version` in
the frontmatter and add an entry to the changelog at the bottom.

## The six state scopes

Every fact in the world lives at exactly one scope. The scope
determines who sees the fact, who can change it, and how it
serializes into Unreal.

NPCs (`NPCs/`) are tracked separately and not numbered here — see
`NPC-Intelligence-System.md`. Story scopes can read NPC state and
propose changes; NPC files remain the source of truth for fields
like `loyalty_resentment` or `trust_score`.

**1. World — server-shared, persistent.**
True for every player on the server, simultaneously. Survives
logouts, server restarts, expansions. Example: "the Iron Dominion
garrison sells the gate register to the Compact every Wednesday."
Lives in `WorldState/`. Authoritative.

**2. Phase — cohort-shared, story-driven.**
True for the subset of players who have reached a particular story
state. A phase is a *diff* against World, not a replacement. Two
players standing in the same district can be in different phases;
each sees a different version of that district. Example: "Hollows
entrance behind Ledger Row exists for players who have completed
the Compact missing-agent questline." Lives in `PhaseLayers/`.

**3. Questline — narrative spine.**
The structured beats of the main story or a side questline. Each
beat declares which phase layers it activates and which World
facts it writes. A beat is *not* world state itself — it is the
authoring unit that produces world and phase changes. Lives in
`Questlines/`.

**4. Daily — ambient world life.**
The recurring routines, rumors, and small frictions that make the
world feel inhabited. Daily content is not authoritative — it is
flavor that World and Phase can override. The Simulation Tick (see
`Simulation-Tick.md`) writes here, and the Compact / news criers /
gossip surfaces read from here. Lives in `DailyLife/`.

**5. StoryInstance — personal narrative chambers.**
Solo or near-solo private spaces for moments that genuinely need
isolation: the player's death and resurrection, a one-on-one with
a major antagonist, a vision sequence. Used **sparingly**. Most
main-story beats happen in shared phased world; StoryInstances are
reserved for moments that cannot work in shared space. Lives in
`StoryInstances/`.

**6. Instance — group / set-piece content.**
Hard-bounded shared spaces entered through portals: dungeons,
raids, scenarios. Distinct from StoryInstance because they are
group-based and repeatable. Authored more like traditional level
design than like phased world content. Lives in `Instances/`.

## Why this split, in one paragraph

Shared-world MMOs that promise "the main story matters" usually
fail because they conflate scopes. They write a quest that "kills"
an NPC — but the NPC has to keep being alive for new players, so
the death is faked through phasing, but the phasing logic is
implicit in the quest script, so when a designer later wants to
reuse that NPC in a faction quest they can't tell whether the NPC
is dead, dead-for-some-people, or dead-only-during-this-quest.
This architecture forces the answer up front: the NPC's death
either changes World (everyone), a Phase (cohort), a StoryInstance
(this player's private chapter), an Instance (this dungeon run),
or nothing. You declare which one when you write the beat. The
cost of getting it wrong drops by an order of magnitude.

## How files reference each other

Cross-scope references go in defined directions only:

```
Questlines  →  PhaseLayers     →  WorldState
            →  StoryInstances  →  WorldState
            →  Instances       →  (mostly self-contained)
            →  DailyLife
            →  NPCs            (read; propose-only writes)

AFE (Sim)   →  WorldState      (faction influence writes)
            →  DailyLife       (event writes)
            →  NPCs            (propose-only writes)
```

A questline beat may activate a phase layer, send the player into
a story instance, and write a world flag. World state never
references questlines, phases, or instances — it is the substrate.

DailyLife reads from World and may be suppressed by Phase, but
DailyLife never writes to either. If a daily routine "should"
change because of story progress, the change belongs in a Phase
layer that overrides the routine.

The Area Factions Engine (`Area-Factions-Engine.md`) is the
server-side simulation; it writes into WorldState (faction
influence values) and DailyLife (events, rumors, NPC actions on
NPCs). It never writes Phases or Questlines directly.

NPC files are read-only from the perspective of all story scopes
and the AFE. If a beat or simulation event needs to change an
NPC's `trust_score` or set `liar_mark_active`, it declares the
proposed change in its `npc_writes:` block; the writer who owns
that NPC reviews and applies the change to the NPC's own file.
This preserves the existing NPC review workflow.

## Phase semantics

A phase is named, scoped, and exclusive within its scope group.

- **Named.** Every phase has a unique slug. `hollows-access-quest`,
  `hollows-access-alignment`, `hollows-access-perception`,
  `hollows-access-faction`. Names are stable; do not rename a
  phase once it has been referenced by a questline beat.
- **Scoped.** A phase declares the geography or system it affects.
  A Hollows-access phase is scoped to `World/Ironthorn/The-Hollows`
  and does not affect other locations.
- **Exclusive within group.** Phases that share a `phase_group`
  are mutually exclusive — a player is in exactly one of them at
  a time, or none. Hollows access is a single group with four
  member phases plus an implicit "no access" base state. This is
  what prevents player A from being in two contradictory versions
  of the same district.

A player's phase membership is per-group, per-scope. A player can
be in `hollows-access-perception` for The Hollows and
`covenant-aware` for Sanctum Ward simultaneously, because those
are different groups.

## Beat semantics

A questline beat is the smallest authoring unit that produces
state changes. Beats have:

- **Trigger** — what causes the beat to fire (player enters
  location, NPC reaches threshold, prior beat completes, etc.)
- **Body** — the narrative content; usually dialogue, cinematic,
  or environmental change
- **Effects** — declared state changes:
  - `phase_activations:` — which phase a player enters/exits
  - `world_writes:` — which World flags this beat sets
  - `npc_writes:` — proposed NPC changes, pending writer review
  - `instance_entry:` — if the beat sends the player into a
    StoryInstance or Instance, which one

A beat does not contain logic. It declares effects. The runtime
applies them. This is what allows beats to round-trip into Unreal
DataTables cleanly.

## Faction control

Faction control over an area is **continuous influence with
discrete tiers** — see `Faction-Influence.md` for the full model.
Each district carries a 0–100 influence value per faction. Tiers
(Minority / Contested / Dominant) are derived from those values
and are what content authors and runtime systems query against.

Influence is a WorldState concern: it is server-shared, persistent,
and updated by the Area Factions Engine on the daily simulation
tick. It is not phased. Two players in the same district always
see the same faction-tier state.

What *changes* with faction tier — vendor inventory, NPC reactions,
ambient routines — is parameterized, not duplicated. A vendor's
profile declares "what I sell when my faction is Dominant here vs.
Contested vs. Minority," not three separate vendor files.

## Service floor — a hard invariant

The simulation may not produce a player-hostile world.

For every district where a player can spawn, travel to, or be
funneled by quests, there must always be an accessible path to
core services: a vendor, a trainer (if relevant), a stable NPC
who can give faction-neutral information. If faction shifts would
remove the last vendor from a district, the simulation must
either:

- prevent that shift,
- spawn a replacement service NPC from a faction-neutral pool, or
- open a nearby instance/connector that provides the service.

This rule lives at the AFE level; see `Area-Factions-Engine.md`
for the enforcement detail. It is non-negotiable. The world
adapts; the player is never stranded.

## In-world legibility

The simulation is not allowed to be invisible. Every change the
AFE produces must be readable by players through in-world
surfaces:

- **Rumors and gossip.** Tavern NPCs, street NPCs, daily routine
  NPCs carry rumor lines that reflect recent simulation events.
- **News criers / public posts.** District-level public-facing
  channels that announce shifts in faction control.
- **The Compact dossier.** The Gray Compact's information economy
  is the canonical legibility surface for *deeper* simulation
  state — who is moving against whom, which NPCs are watch-flagged,
  what's about to break. Players can buy access. The lore already
  supports this; the architecture relies on it.

If the AFE produces an event that no in-world surface exposes,
that event is a bug. Players must be able to reason about cause
and effect through fiction, not through patch notes.

## Unreal serialization constraints

Every field in every template in this architecture must:

- Be a primitive (string, int, bool, float), an enum, or a flat
  array of primitives.
- Have a stable name. Renaming a field is a breaking schema
  change and must update `FQuestBeat_DataRow` /
  `FPhaseLayer_DataRow` / `FWorldFlag_DataRow` simultaneously.
- Use snake_case in YAML, mapped to PascalCase in the UStruct.
  This matches the existing NPC convention (`loyalty_resentment`
  → `LoyaltyResentment`).

No nested objects. No free-form structures. If a field needs
sub-data, it gets its own file with a stable slug, and the parent
references it by slug.

## What lives where — quick reference

| You are writing... | It lives in... |
|---|---|
| A persistent server-wide fact | `WorldState/` |
| A cohort-specific override of a fact | `PhaseLayers/` |
| A story beat with effects | `Questlines/<questline-slug>/` |
| An ambient routine, rumor, friction | `DailyLife/` |
| A solo private narrative chamber | `StoryInstances/` |
| A group dungeon / raid / scenario | `Instances/` |
| An NPC | `NPCs/` (existing) |
| AFE / simulation rules | `_System/Area-Factions-Engine.md` |
| Faction influence model | `_System/Faction-Influence.md` |
| Simulation tick cadence | `_System/Simulation-Tick.md` |
| NPC-on-NPC action types | `_System/NPC-Action-Vocabulary.md` |

## What this document does NOT cover

- **Combat / loot / itemization.** Out of scope for the story
  engine. Those will get their own architecture doc.
- **Player progression.** Levels, skills, experience curves —
  out of scope here. Phases reference player state but do not
  define it.
- **Authoring tools.** How writers create these files (Obsidian,
  Writer Portal, AFE admin dashboards) is a separate workflow
  concern, governed by the existing writer-standards docs and
  the AFE engine spec.

## Changelog

- **1.0 (Draft, 2026-05-02)** — Initial architecture. Six scopes
  named (World, Phase, Questline, Daily, StoryInstance, Instance).
  Cross-scope reference rules established. Phase and beat
  semantics defined. Unreal serialization constraints stated.
  Service floor invariant declared. In-world legibility surfaces
  named as first-class. AFE referenced as the simulation source.
