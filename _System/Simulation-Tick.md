---
system_doc: true
doc_type: "System Reference"
doc_name: "Simulation Tick"
version: "1.0"
status: "Draft"
---

# Simulation Tick

The cadence and rules of the Area Factions Engine simulation.
This document defines **when** the simulation runs, **what** it
can do on each run, and **what bounds** keep it from eating the
project.

Read this alongside `Area-Factions-Engine.md` (the engine's
overall architecture), `Faction-Influence.md` (what the
simulation writes), and `NPC-Action-Vocabulary.md` (the typed
actions available to NPCs).

## Cadence

The simulation runs **once per server day**, at a fixed in-world
hour (target: 04:00 server local time, before peak login). Every
NPC and faction is evaluated in this single tick.

> **TBD:** the actual tick hour is an ops decision, not a design
> decision. 04:00 is a placeholder shaped by traditional MMO
> off-peak windows. Revisit when the live server's timezone and
> peak-load profile are known.

Some sub-systems run on multi-day intervals tied to the daily
tick:

- **Weekly events** fire on day-of-week 0 (the "garrison sells
  the gate register to the Compact" pattern is a weekly tick).
- **Monthly events** fire on day-of-month 1 (faction council
  rotations, long-arc economic shifts).
- **Seasonal events** fire on day-of-year 1, 92, 183, 274
  (faction high holidays, shifts in light/shadow boundary).

All higher-cadence events are scheduled by checking the day-of
modulus during the daily tick. There is no separate weekly or
monthly process.

## Why daily

Hourly produces noise players cannot track. A faction shift that
happens between login and logout looks random unless the player
was watching. Daily aligns with traditional MMO server reset
patterns and with the world's own pacing — gossip, news, weekly
schedules.

Weekly is too slow for engaged players. A daily player would see
six log-in/log-out cycles between any visible change. The world
would feel static.

Daily is the sweet spot: a player who logs in every day notices
movement; a player who returns after a week sees a meaningful
delta; a player who returns after a month sees the world has
moved on without them, in a way they can investigate through the
Compact and other legibility surfaces.

## What runs in a tick

Each daily tick evaluates, in order:

1. **NPC priority resolution.** For every named NPC not currently
   in a player conversation (see *Player Interaction Pause*
   below), compute the action the NPC would most prefer to take
   today, based on stat-driven priority. See `NPC-Action-Vocabulary.md`
   for the action set and the priority math.

2. **NPC action arbitration.** Some NPC actions target other
   NPCs (`assassinate`, `extort`, `betray`, etc.). Targets get
   to react based on their own stats. The AFE resolves who wins,
   who survives, who escapes, with what consequence.

3. **Faction influence deltas.** Resolved NPC actions produce
   influence changes for affected districts. Dead NPCs subtract
   their faction's influence by their tier weight; defections
   move influence between factions; assassinations of high-tier
   NPCs cascade into multi-district shifts.

4. **Service floor enforcement.** Before any influence change
   commits, the proposed world-state is checked against the
   service floor invariant. Proposals that would strand players
   are clipped or paired with replacement spawns.

5. **Tier change events.** Where influence values cross tier
   thresholds, tier change events are produced.

6. **Legibility surface updates.** Rumors are generated. News
   criers receive their daily script. The Compact's internal
   ledger updates with the day's events.

7. **NPC propose-writes queued for review.** NPC stat changes
   produced by the tick (trust score changes, watch-flag shifts,
   etc.) are queued as proposed-writes against the affected NPC
   files. Writers review and apply through normal workflow.

8. **PC skill-check counter reset.** The per-(NPC, check type)
   counters that drive Skill-Growth's diminishing-returns rule
   reset to zero. See [[Skill-Growth]] under *Anti-grind:
   diminishing returns*. This is a small, deterministic
   bookkeeping step — it does not commit any world-state writes
   and is not subject to the service floor or invariant checks.

The tick is **transactional** — if any step fails or produces an
invariant violation, the tick aborts and the world stays in
yesterday's state. There is no partial commit.

## Player Interaction Pause

NPCs in active conversation with a player are excluded from the
tick. Their priority is not evaluated; they cannot be the actor
or the target of any AFE action; they cannot have their stats
written by the simulation.

When the conversation ends:

1. Stat changes from the conversation commit first.
2. The NPC's priority is re-evaluated against the new stats.
3. The NPC re-enters the simulation pool.
4. **Queued actions targeting this NPC** (an assassination that
   would have fired today, deferred because the target was in
   conversation) fire on the next tick, not retroactively.

This means a player can effectively shield an NPC from the
simulation by talking to them. This is intentional — it is a
soft form of player agency. Players who suspect an NPC is in
danger can buy time.

**Edge case — the conversation never ends.** A player who logs
out mid-conversation, or who lingers in a conversation across a
tick boundary, holds the NPC out of the simulation indefinitely.
After 24 in-world hours of conversation lock, the NPC is force-
released into the simulation pool. This prevents griefing and
prevents accidental indefinite shields from logged-out players.

## Bounds — what the simulation may not do

These are hard rules. Violation is a bug.

1. **The simulation may not violate the service floor.** No
   proposal commits if it strands players from core services.
   See `Story-Architecture.md` and `Area-Factions-Engine.md`.

2. **The simulation may not write outside its declared targets.**
   The AFE writes WorldState (faction influence) and DailyLife
   (events, rumors). It does **not** write Phases, Questlines,
   or Instances. NPC writes are propose-only, queued for writer
   review.

3. **The simulation may not produce events that no in-world
   surface exposes.** If the AFE does something, players must be
   able to learn about it through fiction (rumors, news criers,
   the Compact, dialogue). Invisible simulation is forbidden.

4. **The simulation may not violate anchor floors.** Lore-anchored
   factions in their home districts (Aureate Covenant in Sanctum
   Ward, Verdant Circle in Greenward) cannot be reduced below
   their declared anchor floor by ordinary tick behavior. Crisis
   events that override anchors must be designer-authored and
   logged.

5. **The simulation may not cascade indefinitely.** A single
   tick produces at most one round of action and consequence per
   NPC. If NPC A's action provokes NPC B, NPC B's response fires
   on the next tick, not the same tick. This caps the per-tick
   computation budget and gives players a day to react.

## Computation budget

A daily tick should complete in under 60 seconds of server-side
processing for a server with up to 1,000 named NPCs across all
districts. If the tick exceeds budget, the engine logs a warning
and the next tick runs in **degraded mode** — only NPCs above
Tier 2 evaluate their actions, lower-tier NPCs hold yesterday's
state.

This is a backstop, not a feature. If degraded mode fires more
than three days in a row, the engine should be considered
broken and the on-call should investigate.

## Designer override

For testing, crisis events, and set-piece moments, designers can
manually run a tick or inject specific NPC actions outside the
daily schedule. All overrides are logged in the AFE event log
with reason and designer name. Override-driven changes are
always legibility-surfaced — there is no silent designer hand.

## In-world legibility

Every event the tick produces gets a legibility surface:

| Event type | Surface |
|---|---|
| Tier change in district | News criers (district-level), tavern rumors |
| NPC death (named, Tier 3+) | News criers, Compact dossier, NPC routine update |
| NPC defection | Compact dossier (paid), faction internal channels |
| Faction action (siege, sabotage) | News criers, multi-district rumors |
| NPC watch-flag escalation | Compact dossier (paid, high tier) |
| Quiet NPC stat drift | Not surfaced; not player-perceivable yet |

The Compact dossier is the deepest legibility surface — players
who pay can read events that no other surface exposes. This is
the lore-coherent way to expose simulation depth without breaking
fiction.

## Unreal mapping

The simulation tick itself is a server-side process, not a
DataTable row. What it writes (influence values, events, NPC
proposed changes) maps through the existing UStruct types:

| Write target | UStruct |
|---|---|
| Faction influence | FFactionInfluenceRow |
| Tier change event | FFactionEventRow |
| NPC action event | FNpcActionEventRow |
| NPC proposed stat change | FNpcProposedWriteRow (queued) |

The tick's own state (last-run timestamp, degraded-mode flag,
override log) lives in `FAfeTickStateRow` — a singleton row for
runtime introspection.

## Changelog

- **1.0 (Draft, 2026-05-02)** — Initial spec. Daily cadence
  established. Player interaction pause defined. Five hard
  bounds declared. Computation budget and degraded mode named.

---

*[[../README|Back to Index]] · [[Story-Architecture]] · [[Area-Factions-Engine]] · [[Faction-Influence]] · [[NPC-Action-Vocabulary]] · [[Skill-Growth]]*
