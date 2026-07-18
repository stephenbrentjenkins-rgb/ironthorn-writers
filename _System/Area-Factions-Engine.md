---
system_doc: true
doc_type: "Engine Specification"
doc_name: "Area Factions Engine"
version: "1.0"
status: "Draft"
---

# Area Factions Engine (AFE)

The server-side simulation that drives NPC-on-NPC action,
faction territory shifts, and the daily living-world tick. This
document specifies the engine's architecture; the cadence rules
are in `Simulation-Tick.md`, the action set is in
`NPC-Action-Vocabulary.md`, and the influence model is in
`Faction-Influence.md`.

The AFE is the only system permitted to write faction influence
values automatically. It reads NPC state, resolves their actions
on each other, produces influence deltas and world events,
enforces invariants, and surfaces results through in-world
legibility channels.

## What the AFE is, and what it isn't

**Is:**
- A daily simulation tick that evaluates every named NPC.
- The arbiter of NPC-on-NPC action outcomes.
- The writer of faction influence values to WorldState.
- The producer of legibility-surface content (rumors, criers,
  Compact dossier entries) for the day's events.
- The enforcer of the service floor invariant.

**Isn't:**
- A questline runner. Questlines have their own progression rules
  in `Questlines/`.
- A phasing system. Phasing is separate; the AFE writes World,
  not Phase.
- A combat resolver. NPC-on-NPC actions resolve through stat-and-
  cunning math, not combat simulation.
- A real-time process. The AFE runs once per server day.
- A player-action handler. Player interactions with NPCs go
  through the existing dialogue/quest systems; the AFE only
  notices the *consequences* (NPC stat changes that come out of
  player conversations) on the next tick.

## Architecture

The AFE is a server-side process composed of five subsystems:

1. **Priority Resolver.** Computes each eligible NPC's preferred
   action this tick. Reads NPC stats, goals, faction context.
   Outputs a per-NPC `(action, target, priority)` tuple.

2. **Action Arbiter.** Resolves contests between NPCs whose
   actions intersect (assassinate vs. defend, sabotage vs.
   reinforce, etc.). Produces a final per-NPC action outcome.

3. **Influence Writer.** Translates resolved actions into faction
   influence deltas per district. Applies anchor floors. Proposes
   changes to WorldState.

4. **Service Floor Sentinel.** Validates proposed WorldState
   changes against the service floor invariant. Clips deltas or
   pairs them with replacement spawns when floor would be
   violated.

5. **Legibility Publisher.** Generates rumors, news crier
   scripts, Compact dossier entries, and faction internal
   communications for the day's events. Updates DailyLife.

The five subsystems run sequentially per tick. Each is
transactional and idempotent — a tick that fails partway through
rolls back fully.

## Priority Resolver — detail

For each NPC not in player conversation, the resolver:

1. Pulls the NPC's stats, goals, faction, and current district.
2. Iterates through every action in `NPC-Action-Vocabulary.md`.
3. For each action, computes:
   - **Eligibility.** Does the NPC meet the action's performable-
     by floor? (Cunning level, faction tier, leverage held, etc.)
   - **Goal alignment score.** How much does this action advance
     the NPC's primary goal (×3), secondary goal (×2), hidden
     goal (×1)?
   - **Stat-driven score.** How strongly does the NPC's stat
     profile call them to this action? (e.g., high greed_appetite
     + low greed_restraint pushes toward `extort`.)
   - **Threshold pressure.** Are any sub-attribute thresholds
     crossed? (Resentment ≥ 6 forces `defect` and `expose` to top
     of list.)
   - **Risk weight.** Discount the score by the action's risk
     score, weighted by the NPC's `cunning_paranoia` and
     `fear_suppression`.
4. Picks the highest-scoring eligible action.
5. Selects a target if the action requires one (typically the
   NPC against whom the actor has the highest motive — leverage,
   resentment, paranoia, or goal alignment).

Output: a flat list of `(actor_npc_id, action, target_id_or_null,
priority_score)` tuples for the tick.

## Action Arbiter — detail

Some actions intersect. NPC A's `assassinate` against NPC B is
contested by B's own action (which might be `wait`, `betray`, or
something else entirely) and by B's stats (perception, paranoia,
fear_suppression).

Arbitration rules:

- **Assassination contest.** Actor's cunning + cunning_patience
  vs. target's perception_threshold + cunning_paranoia. Margin
  determines outcome (clean kill, kill with witnesses, botched
  attempt with target survival, botched attempt with actor
  exposure).
- **Sabotage detection.** Actor's cunning vs. average perception
  of target faction's NPCs in the affected district.
- **Extortion resistance.** Target's idealism_conviction +
  fear_suppression vs. actor's cunning + leverage strength.
  Successful resistance flips the action into an `expose`
  against the actor.
- **Defection interference.** Actor's faction may attempt last-
  minute prevention if any same-faction NPC has motive and
  capability to act. Resolved as a sub-tick interaction.

Where multiple NPCs target the same NPC in the same tick, the
arbiter resolves them in priority-score order, with each
resolution potentially altering the state for subsequent ones.

Output: per-NPC outcome (action_succeeded, action_failed_with_X,
action_misfired, etc.) and any chained-event flags for the next
tick.

## Influence Writer — detail

Resolved actions produce influence deltas via the rules in each
action's effects (see `NPC-Action-Vocabulary.md`).

Deltas are aggregated per-district before commit. If multiple
actions in the same tick affect the same `(district, faction)`
pair, the deltas sum.

Anchor floors are applied: a delta that would push a faction's
influence below its anchor floor in its anchored district is
clipped at the floor. Designer-authored crisis events bypass
anchor floors and are tagged as such in the event log.

Tier change events are produced where the post-commit influence
crosses a tier threshold (Absent ↔ Minority ↔ Contested ↔
Dominant).

Output: a proposed WorldState diff and a list of tier-change
events.

## Service Floor Sentinel — detail

Before the proposed WorldState diff commits, the sentinel checks:

- For every district where players can spawn, travel, or be
  funneled by quests, after the diff applies:
  - Is there at least one vendor accessible (in-district or via
    a connected instance)?
  - Is there at least one trainer accessible (if the district is
    in a trainer-required region)?
  - Is there at least one faction-neutral information NPC
    accessible?

For any district that fails the check:

- **Clip the delta.** Reduce the proposed influence shift to the
  largest value that does not violate the floor.
- **Or, pair with a spawn.** If the delta is narratively
  important (driven by a story beat or designer override), spawn
  a faction-neutral replacement service NPC from the floor pool.
  These NPCs are stable, lore-thin (deliberate; they're system
  characters), and replaceable.
- **Or, route to instance.** If the district has a connected
  service instance, mark it as the active service path for the
  district until the floor is restored organically.

Floor violations that cannot be resolved by clipping, spawning,
or routing are logged as **engine errors**, the tick aborts,
and on-call investigates. This should not happen in normal
operation — it's a backstop, not a feature.

## Legibility Publisher — detail

For every event the tick produces, the publisher generates:

- **Rumor lines** for tavern NPCs and street NPCs in affected
  districts. Generated from event templates (see
  `_System/Rumor-Templates.md`, to be created).
- **News crier scripts** for district-level public-facing
  channels. One crier line per significant event.
- **Compact dossier entries** for events of sufficient depth
  (NPC defections, watch-flag escalations, hidden-agenda
  movements). Surfaced only to players who pay for Compact
  access at the appropriate tier.
- **Faction internal communications** — NPCs within affected
  factions get knowledge updates that drive their next-tick
  priority calculations.

The publisher writes to `DailyLife/`. The vault tools
(`Tools/`) include a snapshot generator that exports the day's
legibility content to JSON for the AFE Admin web tools.

## Designer override interface

Designers can:

- Manually trigger a tick outside the daily schedule (for
  testing, crisis events, debugging).
- Inject a specific NPC action that bypasses the priority
  resolver (for set-piece moments).
- Adjust faction influence values directly (for testing or
  crisis events). All adjustments are logged.
- Force a tier change event (for narrative purposes).
- Inspect the priority math for any NPC (read-only).

Override interface lives in the AFE Admin web tools (see
*Admin Tooling* below).

## Player Interaction Pause

NPCs in active conversation with a player are excluded from the
tick. See `Simulation-Tick.md` for the full rules. Summary:

- Conversation NPC: skipped by Priority Resolver.
- Action targeting conversation NPC: queued for next tick.
- Conversation timeout: 24 in-world hours, then NPC released to
  pool.

## Admin tooling

The AFE has a small set of web-based admin tools, hosted locally
from `Tools/` (see `Story-Architecture.md` for the hosting
decision). Tools planned for v1:

- **Faction Influence Dashboard** — read-only view of current
  influence values and tiers per district. Shows the day's
  changes. Future: manual adjustment with logged reason.
- **NPC Priority Inspector** — pick an NPC, see what actions
  their stats are currently driving them toward, with the
  priority math exposed.
- **Tick Previewer** — dry-run the next tick. Shows what events
  the simulation would produce. Optional commit.
- **Event Log Viewer** — read the AFE event log. Filter by
  district, faction, NPC, event type, date.

All tools read from a daily-generated JSON snapshot in
`Tools/snapshots/`. The snapshot generator is a Python tool
that walks the GameVault frontmatter and the AFE event log.

The tools are vanilla HTML/JS, hosted as files opened locally
by the user. Promotion to GitHub Pages is a one-line config
change when collaborators need access.

## Unreal mapping

The AFE is a server-side process, not a DataTable. What it
writes is what crosses into Unreal:

| AFE output | Unreal target |
|---|---|
| Faction influence values | FFactionInfluenceRow (DataTable) |
| Tier change event | FFactionEventRow (DataTable) |
| NPC action event | FNpcActionEventRow (DataTable) |
| NPC proposed stat change | Vault frontmatter (queued for writer review; not auto-pushed to UE) |
| Rumor / crier / dossier content | FDailyLifeContentRow (DataTable) |
| Tick state (last-run, degraded-mode flag) | FAfeTickStateRow (singleton DataTable) |

The Unreal-side reads these DataTables via VaultBridge or its
successor, the same pattern already established for NPCs.

## Implementation order — recommended

If we build this v1.0 in order, the dependencies are:

1. **WorldState/ folder + influence-vector flag template.**
   Without somewhere to write, the AFE has nothing to do.
2. **Faction influence registry + per-district influence files.**
   Initial values, anchor floors, list of tracked factions.
3. **Snapshot generator.** Python tool that reads the vault and
   produces JSON. Needed before any web tooling.
4. **Faction Influence Dashboard.** First read-only admin tool.
   Validates the snapshot and the model.
5. **Priority Resolver + NPC Priority Inspector.** Next, because
   it's the next testable unit.
6. **Action Arbiter + Tick Previewer.** Once we can preview
   actions, we can debug them before they commit.
7. **Influence Writer + Service Floor Sentinel.** The first
   pieces that produce real WorldState changes.
8. **Legibility Publisher.** Last. The world has to do the right
   thing before we expose the doing.

This is build order, not commitment. Each step is testable on
its own.

## What this document does NOT cover

- **Player faction reputation.** Player-scoped, not world-scoped.
- **Combat / siege / territory war systems.** When implemented,
  those produce influence deltas through the AFE write API. The
  AFE is consumer-side from those systems' perspective.
- **Specific action tuning numbers.** The action effects in
  `NPC-Action-Vocabulary.md` are starting values. Tuning happens
  during testing, not in this doc.

## Changelog

- **1.0 (Draft, 2026-05-02)** — Initial spec. Five-subsystem
  architecture. Designer override interface defined. Admin
  tooling roadmap. Implementation order proposed.

---

*[[../README|Back to Index]] · [[Story-Architecture]] · [[Simulation-Tick]] · [[NPC-Action-Vocabulary]] · [[Faction-Influence]] · [[NPC-Intelligence-System]]*
