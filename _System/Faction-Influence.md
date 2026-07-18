---
system_doc: true
doc_type: "System Reference"
doc_name: "Faction Influence"
version: "1.0"
status: "Draft"
---

# Faction Influence

How factions hold, contest, and lose territory. The model is
**continuous influence with discrete tiers**: a hidden 0–100
backing value drives behavior, but designers and content authors
work against three named tiers.

This is a WorldState concern. Influence values are written by the
Area Factions Engine on the daily simulation tick and read by
NPCs, vendors, ambient routines, and any system that cares about
"who controls this district right now."

Influence is **not phased**. Two players standing in the same
district always see the same tier state. If a story beat needs to
make Sanctum Ward feel different for a particular cohort of
players, that's a Phase concern, not an influence concern.

## The model

Each district carries one influence value per faction, range 0–100.
The values do **not** sum to 100 — multiple factions can be
strong in the same district at once, and contested districts
typically have several factions in the 30–60 range simultaneously.

From those values, each faction has a **tier** in that district:

| Tier | Range | Meaning |
|---|---|---|
| **Absent** | 0–14 | Faction has no meaningful presence here. |
| **Minority** | 15–39 | Faction has presence but does not set the rules of the area. NPCs are deferential, prices unfavorable, fewer services. |
| **Contested** | 40–69 | Faction is one of several real powers in the area. NPCs are guarded; reactions depend heavily on player faction standing. |
| **Dominant** | 70–100 | Faction sets the rules of the area. Banners visible. Vendors stocked for faction members. NPC reactions favor faction-aligned players. |

The tier thresholds are stable. Designers and content authors
write content against tiers; the simulation moves the backing
values; the tier changes when the value crosses a threshold.

## Why continuous-with-tiers, not pure tiers or pure continuous

Pure discrete tiers feel jerky — Sanctum Ward "becomes Crimson-
contested" overnight when a single event flips the bit, and
players see a jarring discontinuity.

Pure continuous values are impossible to author content against —
you'd need vendor inventories that smoothly interpolate, dialogue
that linearly responds to a 0–100 scale, etc. That way lies
content explosion.

Continuous backing with discrete tiers gives both: the simulation
moves smoothly day to day, but the *visible* world only changes
when a real threshold is crossed. Designers author against three
states. The simulation does the smoothing.

## Reading influence in content

Vendors, NPC dialogue, daily routines, and ambient details query
influence by tier. A vendor profile declares:

```yaml
inventory_dominant: [...]
inventory_contested: [...]
inventory_minority: [...]
inventory_absent: [...]
```

Not three to seven separate vendor files per district. The vendor
is one entity; their stocked goods, prices, and attitude shift
based on which tier their faction occupies in their current
district.

Same pattern for NPC reactions. An NPC of Faction X in a district
where their faction is Dominant defaults to confident, casual,
welcoming-to-allies behavior. The same NPC in a Minority district
defaults to guarded, quiet, discreet behavior. One NPC file. Tier-
indexed behavior blocks.

## Writing influence — who writes what

Influence values are written by:

- **The Area Factions Engine** (daily simulation tick) — the
  primary writer. NPC actions on other NPCs, faction quest
  outcomes, and player territory contests resolve into influence
  deltas.
- **Questline beats** — explicit story-driven shifts. A main-story
  beat may write `iron-dominion-influence-sanctum-ward: -20` as
  part of its `world_writes:` block.
- **Designer manual override** — for testing, for crisis events,
  for set-piece moments. Logged with reason in the AFE event log.

Influence values are **never** written by:

- DailyLife routines (they read).
- PhaseLayers (they read; phasing is on top of influence, not
  parallel to it).
- NPC files (they describe themselves, not the world).

## Tier change triggers

When a faction's influence in a district crosses a tier threshold,
the AFE produces a **tier change event**. The event:

1. Writes the new tier value to WorldState.
2. Triggers in-world legibility: news criers announce the shift,
   tavern rumors update, the Compact files an internal report.
3. Refreshes vendor inventories, NPC dialogue branches, and
   ambient routines in the affected district on the next zone
   refresh.
4. Logs to the AFE event log for player-facing dossiers.

Tier change events are public knowledge in-fiction. The simulation
does not silently shift the world.

## The service floor as it relates to influence

The Service Floor invariant (see `Story-Architecture.md` and
`Area-Factions-Engine.md`) constrains influence shifts. The AFE
may not write an influence change that would remove the last
vendor or trainer from a district where players can be present,
unless a replacement is simultaneously spawned or routed through
an instance.

Practically: the AFE proposes deltas, the service-floor check runs
before commit, and proposals that violate the floor are either
clipped (delta reduced) or paired with a replacement spawn.

## Districts and faction registry

The list of districts and the factions tracked in each lives in
`WorldState/faction-influence-registry.md` (to be created). Each
district has its own influence file:
`WorldState/influence-<district-slug>.md`.

District file format is defined by the WorldState-Flag template
with `flag_type: "faction_influence_vector"` and a structured
`vector` block. See `_Templates/WorldState-Flag-Template.md` and
the registry for canonical examples.

## Anchored vs. shiftable districts

Some districts have factions baked in by lore. These are
**anchored**:

- **Sanctum Ward** — Aureate Covenant Dominant by default.
  Crisis events can push to Contested, but not below. Loss of
  Sanctum Ward is a once-per-expansion endgame event, not a
  Tuesday occurrence.
- **Greenward** — Verdant Circle Dominant by default. Same
  anchor logic.
- **The Hollows** — no faction is Dominant. The Hollows resist
  control by design.

Other districts are **shiftable**:

- **Ledger Row** — Gray Compact Dominant by default but
  legitimately movable; the Compact's hold is institutional, not
  territorial, and other factions can build influence here.
- **Wound Market**, **Ashgate Quarter** — already ambiguously
  controlled in lore. Faction movement here is *narratively
  normal*.

Anchors are declared in each district's influence file with an
`anchor_floor_<faction-slug>: <value>` entry — the AFE may not
reduce that faction below the floor without an explicit
designer-authored crisis event.

## Unreal mapping

| YAML field | UStruct field | Type |
|---|---|---|
| district_slug | DistrictSlug | FName |
| faction_<slug>_influence | FactionInfluenceMap | TMap<FName, int32> |
| faction_<slug>_anchor_floor | FactionAnchorFloors | TMap<FName, int32> |
| current_tier_<faction-slug> | CurrentTiers | TMap<FName, EFactionTier> |

## What this document does NOT cover

- **Player faction reputation** — how an individual player's
  standing with a faction works. Separate system; player-scoped,
  not world-scoped.
- **Combat-driven territory contests** (sieges, territory wars).
  Out of scope here. When implemented, those systems will produce
  influence deltas through the AFE write API like any other write
  source.

## Changelog

- **1.0 (Draft, 2026-05-02)** — Initial model. Continuous backing,
  discrete tiers (Absent / Minority / Contested / Dominant).
  Anchor floors defined. Service floor reference made explicit.

---

*[[../README|Back to Index]] · [[Story-Architecture]] · [[Area-Factions-Engine]] · [[Simulation-Tick]]*
