---
system_doc: true
doc_type: "System Reference"
doc_name: "NPC Action Vocabulary"
version: "1.0"
status: "Draft"
---

# NPC Action Vocabulary

The bounded set of actions NPCs can take on other NPCs and on the
world during the daily simulation tick. This is what extends
`NPC-Intelligence-System.md` from "NPC reacts to player" to "NPC
acts on world."

The vocabulary is **typed and closed**. Designers can extend it
through controlled additions (with new action definitions and
write-rule updates), but the simulation engine only knows about
declared actions. NPCs cannot do things outside this list.

This is the safety rail against simulation sprawl: bounded
vocabulary, bounded effects, predictable cost.

> **All numeric values in this document are starting values.** Risk
> weights, influence deltas, cunning floors, threshold pressures —
> none of them are tuned. They are gut-shaped placeholders meant to
> be moved during testing. Do not treat "–15 / –25 / –35 influence
> on assassinations" or any similar number as committed. The
> *structure* of effects is what matters here; the magnitudes will
> change.

## How NPC priority works

Each tick, every named NPC computes a priority score for each
action they could take. The action with the highest score is the
one they pursue today. Priority is driven by:

- **Stat alignment.** Actions tagged for cunning, fear, greed,
  loyalty, idealism, and their subs. An NPC's stats determine
  how strongly each action calls them.
- **Goal alignment.** Actions that advance the NPC's primary,
  secondary, or hidden goal score higher. Primary goal weight ×
  3, secondary × 2, hidden × 1.
- **Threshold pressure.** Sub-attribute thresholds (resentment
  ≥ 6, paranoia ≥ 7, etc.) force certain actions to the top of
  the list when crossed. A high-resentment NPC will pursue
  `defect` or `expose` over their normal priority.
- **Faction context.** Actions are filtered by faction membership
  and by the NPC's standing within their faction. A Tier 1
  Compact contact cannot order an assassination; a Tier 4
  Factor can.
- **Risk tolerance.** Actions have a risk score. NPCs with high
  cunning_paranoia or fear_suppression weigh risk more heavily
  than impulsive NPCs.

The priority math lives in the AFE engine. This document defines
the actions themselves.

## The action set — v1.0

Each action below has:

- **Description** — what the action does in fiction.
- **Performable by** — who can take it (cunning floor, faction
  rules, tier requirements).
- **Targets** — who or what it acts on.
- **Cost** — what the actor risks or spends.
- **Effects** — what the simulation writes when the action
  resolves successfully.
- **Failure modes** — what happens if the action is contested
  or misfires.

---

### `trade_info`

**Description.** Sell, share, or trade information with another
NPC or faction.

**Performable by.** Any NPC. Cunning floor: 3.
**Targets.** Another NPC, or a faction (via known contact).
**Cost.** None directly; the information itself may have been
costly to acquire.
**Effects.**
- Target NPC gains a `secrets_known` entry.
- Trust between actor and target increases by 1 (max 10).
- If target is in a different faction, the actor's `faction_alert_sent`
  flag is set if the information concerns their own faction.
**Failure modes.** Information was already known (no effect, no
cost). Information was a setup (target detects, sets `liar_mark_active`
on actor).

---

### `extort`

**Description.** Demand something (coin, favor, information)
from another NPC under implicit or explicit threat.

**Performable by.** NPCs with leverage. Requires `leverage_held: true`
against the target, or a faction-level claim.
**Targets.** Another NPC.
**Cost.** Risk of escalation. Actor's `cunning_paranoia` ticks up
by 1 after each extortion (the world is full of resentful debtors).
**Effects.**
- Target's `debt_flag_active` is set.
- Target's resentment toward actor's faction grows.
- Actor gains the demanded resource (coin/favor/info added to their state).
**Failure modes.** Target refuses and exposes the extortion to a
third party (faction leadership, the Compact, the player). Actor
may be marked, lose faction standing, or face countermove.

---

### `assassinate`

**Description.** Eliminate another NPC permanently.

**Performable by.** NPCs with cunning ≥ 7 or who command others
who have it. Requires faction sanction or sufficient hidden
agenda alignment.
**Targets.** Another NPC of equal or lower tier.
**Cost.** High risk. Failure exposes actor and faction.
**Effects (success).**
- Target NPC is marked dead in WorldState.
- Target's faction loses influence in target's home district
  (-15 if Tier 3, -25 if Tier 4, -35 if Tier 5).
- Target's `npc_writes` propose status change to "Dead".
- Compact dossier gains entry.
- News criers in affected district announce the death (if Tier 3+).
**Failure modes.** Botched attempt — target survives, knows who
ordered it, gains permanent leverage. Witnesses survive — the
Compact, a player, a third NPC. Actor faces faction blowback.

---

### `betray`

**Description.** Switch sides on a specific operation, plot, or
relationship while remaining publicly aligned with the original.

**Performable by.** Any NPC with cunning ≥ 5. Higher cunning
makes the betrayal harder to detect.
**Targets.** A specific operation or NPC the actor is publicly
allied with.
**Cost.** If detected, severe loyalty/trust loss with original
faction; permanent `liar_mark_active` if the player or Compact
becomes aware.
**Effects (success).**
- Target operation/plot is sabotaged or fails.
- Actor's `loyalty_resentment` toward original faction increases.
- Actor's hidden agenda advances.
**Failure modes.** Detection by faction leadership (assassination
or expulsion follows on a future tick). Detection by the Compact
(intelligence asset, leverage). Detection by a player (exposed in
dialogue).

---

### `expose`

**Description.** Publicly reveal information that damages a
target NPC or faction.

**Performable by.** Any NPC. NPCs with high `idealism_disillusionment`
are pushed toward this action by threshold pressure.
**Targets.** Another NPC or a faction.
**Cost.** Actor often loses position with their own faction
(exposed information is rarely "supposed to" come out). May
trigger `assassinate` against actor on a future tick.
**Effects.**
- Target's faction loses influence in affected districts.
- Target's `liar_mark_active` is set if applicable.
- Public-knowledge fact is created (news criers, Compact dossier).
- Actor's faction standing drops; faction may write actor as
  defected/expelled.
**Failure modes.** Information is suppressed or discredited. The
exposure becomes the actor's exposure — the simulation flips the
event into a `defect` or worse for the actor.

---

### `ally_with`

**Description.** Form a working alliance with another NPC or
faction outside one's own.

**Performable by.** Any NPC. Cunning floor: 4.
**Targets.** Another NPC, or a faction.
**Cost.** Time (some alliances take multiple ticks to formalize).
Risk that own faction sees the alliance as defection.
**Effects.**
- Trust between actor and target increases by 2.
- Both parties gain shared `secrets_known` entries (small ones).
- If the alliance is between factions or across them, both
  factions gain a small influence boost in shared districts.
**Failure modes.** Target refuses, with no prejudice. Own faction
discovers and treats as defection-in-progress (escalates to
`expose` or `assassinate` on a future tick).

---

### `defect`

**Description.** Leave one's faction openly and join another.

**Performable by.** Any NPC. Pushed by threshold pressure when
`loyalty_resentment ≥ 8` and `idealism_disillusionment ≥ 7`.
**Targets.** Self (state change). Optionally takes intelligence
or assets to the new faction.
**Cost.** Permanent. Old faction marks actor as enemy.
**Effects.**
- NPC's `faction` field updates (proposed write, pending writer
  review).
- Old faction loses influence in actor's home district.
- New faction gains influence in actor's home district (smaller
  than the loss; defectors are net-negative for the world).
- Compact dossier gains a high-value entry.
- News criers announce if actor is Tier 3+.
**Failure modes.** Actor is killed before reaching the new
faction (`assassinate` queued by old faction on the same tick or
the next). New faction refuses (actor becomes a `gray_compact`
walk-in or a wandering NPC, depending on circumstances).

---

### `sabotage`

**Description.** Damage an operation, building, supply line, or
asset belonging to a target faction.

**Performable by.** NPCs with cunning ≥ 5 or specific faction
sanction.
**Targets.** A faction's operation or holding in a district.
**Cost.** Detection risk. If caught in the act, immediate
escalation by the affected faction.
**Effects.**
- Target faction loses 5–15 influence in the affected district.
- Sabotage event surfaces through news criers and rumors.
- Actor's faction gains 0–5 influence (smaller than the loss).
**Failure modes.** Caught in the act (`assassinate` follows, or
arrest depending on faction). Sabotage misfires (no effect, but
detected anyway).

---

### `reinforce`

**Description.** Spend resources to strengthen one's own
faction's hold in a district. Used by faction leaders and senior
NPCs.

**Performable by.** Tier 3+ faction NPCs, or any NPC with a
faction-sanctioned reinforcement budget.
**Targets.** A district where the actor's faction has presence.
**Cost.** Faction resources (tracked at faction level, not
individually).
**Effects.**
- Actor's faction gains 5–10 influence in the target district.
- District legibility surface notes the reinforcement (banners
  raised, new patrols, etc.).
**Failure modes.** Resources insufficient (no effect). Rival
faction counter-reinforces same tick (net-zero or net-negative
result).

---

### `wait`

**Description.** Take no action this tick. Continue current
posture.

**Performable by.** Any NPC.
**Targets.** None.
**Cost.** None.
**Effects.** None directly. NPC re-evaluates next tick.
**Use case.** Default action when no other action scores high
enough to fire. Many NPCs wait most days. The world is mostly
people getting on with their lives.

---

## Adding new actions

A new action joins the vocabulary through a controlled process:

1. Designer writes a proposal: name, description, performable-by,
   targets, cost, effects, failure modes — same shape as above.
2. Proposal is reviewed against existing actions for overlap.
   Two actions with the same effects are a smell.
3. AFE engine code is updated to recognize the new action,
   compute its priority contribution, and apply its effects.
4. UStruct enum `ENpcActionType` is updated.
5. Action is added to this document with a version note.

Removing an action is harder — existing NPCs may have it queued.
Removing requires a deprecation period (one major version) where
the action is unavailable to new NPCs but still resolves for any
queued instances.

## Unreal mapping

| YAML / engine concept | UStruct |
|---|---|
| Action type | ENpcActionType (enum) |
| Action priority calc | Server-side computation, not stored |
| Action event log | FNpcActionEventRow |
| Queued action | FNpcQueuedActionRow |
| Action effect application | Resolved by the AFE process; writes through existing flag/influence/event UStructs |

## Changelog

- **1.0 (Draft, 2026-05-02)** — Initial vocabulary. Ten actions:
  trade_info, extort, assassinate, betray, expose, ally_with,
  defect, sabotage, reinforce, wait. Priority rules outlined.

---

*[[../README|Back to Index]] · [[NPC-Intelligence-System]] · [[Area-Factions-Engine]] · [[Simulation-Tick]] · [[Faction-Influence]]*
