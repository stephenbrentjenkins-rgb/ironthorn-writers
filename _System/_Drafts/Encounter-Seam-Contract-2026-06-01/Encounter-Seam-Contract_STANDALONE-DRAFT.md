---
system_doc: true
doc_type: "System Reference"
doc_name: "Encounter Seam Contract"
version: "0.1"
status: "Draft — for review"
draft: true
authored: "2026-06-01"
related: ["NPC-Intelligence-System", "Deception-Perception-Skills", "Drives-Reference", "Alignment-Spectrum", "Simulation-Tick", "Area-Factions-Engine", "Story-Architecture", "PoC-Scope"]
---

# Encounter Seam Contract

The typed boundary between the **PC side**, the **NPC side**, and the
**shared spine** of a player↔NPC encounter. Its job is to let the two
sides be built and tested independently while guaranteeing they
integrate without drift.

This document is authored **before** the two decision maps (the
proactive NPC Encounter Decision Map and the existing reactive
lie-catch map) so that both are written against a fixed boundary
instead of drifting toward each other. Nail the contract first; author
the maps against it.

> This is a draft. Nothing here is canonical until promoted out of
> `_Drafts/`. Numbers and field names are reused from canonical
> sources where they exist; anything new is marked **[new]**.

## The three modules and which way they depend

```
PC side      ─┐
              ├─→  Shared spine   (Resolver · Alignment Ledger · Relationship Store)
NPC side     ─┘
```

- **PC side** depends on the shared spine only.
- **NPC side** depends on the shared spine only.
- **Neither side imports the other.** All crossing traffic is the five
  typed shapes below, adjudicated through the spine.

This mirrors the directed-reference discipline in `Story-Architecture.md`:
dependencies point one way, the substrate sits underneath, and the two
producers never reach into each other.

## Encounter lifecycle — a bounded transaction

The Player Interaction Pause (`Simulation-Tick.md`) already makes one
encounter an isolatable unit. The seam runs inside it:

1. **Begin.** PC enters conversation. The NPC is pulled from the
   simulation pool — not evaluated by the Priority Resolver, cannot be
   actor or target of any AFE action, stats not written by the sim.
2. **Stance.** NPC side resolves and emits an `NpcStance` (+ its
   `NpcCheckParams` and `NpcTells`).
3. **Move loop.** PC emits `PlayerMove`s. The Resolver adjudicates any
   that require a check. Effects are **staged**, not applied.
4. **End.** Conversation closes. Staged runtime effects commit first
   (per the Pause rules); canonical Drive shifts are queued as
   propose-writes; the NPC re-enters the pool; any AFE action queued
   against it fires on the **next** tick, never retroactively.

Because the whole thing is bounded with a clear begin/end and the rest
of the world is frozen, a single encounter is scriptable as one test
case.

## The crossing shapes

House rule (from `Story-Architecture.md` § *Unreal serialization*):
primitives, enums, or **flat arrays of primitives** only. No nested
objects. Small structures are encoded as delimited strings inside flat
arrays — the same pattern the beat template uses for
`"phase-group:phase-slug"`.

### PC → NPC

**`PlayerProfile`**

| Field | Type | Notes |
|---|---|---|
| `deception_rank` | int 1–10 | |
| `perception_rank` | int 1–10 | Used PC-side to filter `NpcTells`. |
| `alignment_tier` | enum `EAlignmentTier` (I–VII) | A **snapshot** read from the Alignment Ledger. |
| `faction_standing` | flat array of `"faction-slug:standing"` | Player faction reputation is post-PoC; PoC passes empty / neutral. |
| `relationship_ref` | FName | Opaque key the PC side **carries but never reads**. Handed to the NPC side / Relationship Store. See *Relationship Store* for arity. |

**`PlayerMove`**

| Field | Type | Notes |
|---|---|---|
| `move_type` | enum `EMoveType` { Truth, Deflect, Lie, Manipulate } | |
| `option_id` | FName | Which dialogue option was chosen. |
| `declared_min_rank` | int | The gate the option claimed; carried for audit, not for math. |

The PC side computes **no odds**. It declares a move; the Resolver
decides the outcome.

### NPC → PC

**`NpcStance`**

| Field | Type | Notes |
|---|---|---|
| `stance` | enum `ENpcEncounterStance` (8 values) **[new]** | withhold · probe · court · leverage · defer · warn · guard · avoid |
| `masked` | bool | Whether the stance is run behind the public persona. The mask is the existing **public-persona / private-truth gap** (`NPC-Intelligence-System.md`) expressed as a per-encounter flag — not a parallel concept. |
| `offer_mods` | flat array of `"channel:modifier"` | e.g. `"price:-10"`, `"secrets:open"`, `"quests:closed"`. Tier/alignment-driven adjustments to what the encounter makes available (per the `Alignment-Spectrum` reaction-by-tier table). |
| `branch` | FName | Which dialogue-hook branch opens: `first-encounter` · `trust-high` · `liar-mark` · `debt-deploy` · `radiant` · `void-touched`. |

**`NpcCheckParams`**

| Field | Type | Notes |
|---|---|---|
| `perception_threshold` | int 1–10 | From the NPC's `perception_threshold` field. |
| `situational_mod` | int (signed) | NPC side resolves situational rules ("drops to 3 when drinking") to a single number before handing over. |
| `deception_immune` | bool | From the NPC's `deception_immune` field. |

**`NpcTells`**

| Field | Type | Notes |
|---|---|---|
| `tells` | flat array of `"rank:text"` | `rank` is the Perception rank at which the tell becomes visible, e.g. `"7:her hand moves to the ring"`. Surface / mid / deep tells and the single cunning tell all encode here. PC side filters by `perception_rank` and passive mode (7+). |

## The Resolver — shared; owns the check formula

The check math lives **here and only here**. Putting it on the PC side
would force the PC to read NPC internals; putting it on the NPC side
forces the reverse. Both sides call the Resolver instead.

```
resolve(move: PlayerMove,
        profile: PlayerProfile,
        params: NpcCheckParams,
        alignment: AlignmentSnapshot) -> CheckOutcome
```

Rules:

- **Lie** → `success% = clamp( 50 + (deception_rank − (perception_threshold + situational_mod)) × 9 + alignment_mod , 5 , 95 )`. Roll against it. (Formula and the dark-positive / light-negative alignment modifier are from `Deception-Perception-Skills.md`.)
- **`deception_immune` true** → auto-caught, no roll.
- **Manipulate** → no roll; forced compliance. Validated here: requires `deception_rank ≥ 9` **and** `alignment_tier` in V–VII. Costs −3 alignment.
- **Truth / Deflect** → no roll.

**`CheckOutcome`**

| Field | Type | Notes |
|---|---|---|
| `result` | enum { Believed, Caught, AutoCaught, Forced, NoCheck } | |
| `alignment_delta` | int | The canonical delta from the `Alignment-Spectrum` shift table (lie intent −1, success −2, caught −4, truth-when-lie-available +1, caught-NPC-lying +2, confess +3, manipulate −3). Applied via the Ledger. |
| `npc_flag_proposals` | flat array of `"field:value"` | e.g. `"liar_mark_active:true"`. Staged — routed to the Relationship Store on commit, not applied inline. |

On a `Caught`/`AutoCaught` result the NPC side's **lie-catch decision
map** (`NPC-Intelligence-System.md`) takes over. The Resolver decides
*whether the lie lands*; the lie-catch map decides *what the NPC does
about it*.

## The Alignment Ledger — shared; player-scoped

One ledger per player. The cross-cutting dependency that, if owned by
either side, creates circular coupling — so it's a shared service both
import.

```
tier(player)            -> EAlignmentTier
raw(player)             -> int            // underlying point value
apply(player, delta, reason)              // from the shift table
```

- **PC side and the Resolver write** via `apply()`.
- **NPC side reads** `tier()` / `raw()` to colour its stance. It never
  writes alignment.
- **PoC status: real.** Visible alignment movement is in PoC scope —
  `Skill-Growth` and the demonstration beat require a visible
  rank-up / option-unlock sequence. So the ledger exists in the PoC,
  unlike the relationship store's per-player form (below).

## The Relationship Store — shared; cardinality-agnostic

The one dependency whose **cardinality** changes with the deferred
scope decision but whose **API does not**. This is what lets the
contract survive that decision without a reshape.

- **PoC:** `relationship_ref = npc_id`. Relationship facts are
  NPC-global runtime flags.
- **Post-PoC:** `relationship_ref = npc_id|player_id`. Per-(NPC, player)
  state — the deferred "player-scoped state" system named in
  `Area-Factions-Engine.md`, `Faction-Influence.md`, and `PoC-Scope.md`.

**`RelationshipState`** (mirrors the existing NPC flags):

| Field | Type |
|---|---|
| `trust_score` | int 1–10 |
| `liar_mark_active` | bool |
| `debt_flag_active` | bool |
| `leverage_held` | bool |
| `faction_alert_sent` | bool |
| `secrets_shared` | flat array of FName |
| `watching` | bool |

```
read(relationship_ref)                       -> RelationshipState   // runtime
commitRuntime(relationship_ref, deltas[])                            // immediate, live state
proposeSeedWrite(npc_id, field, value, reason)                       // -> FNpcProposedWriteRow queue (writer review)
```

This is where the **runtime-vs-seed split is enforced.** Encounter
effects commit to live state through `commitRuntime`; canonical NPC
Drive changes go through `proposeSeedWrite`, which reuses the existing
propose-write queue (`Simulation-Tick.md` step 7). Per-player runtime
state never proposes to seed.

## Mock contracts — the "pull apart" mechanism

- **`MockNpc`** satisfies `NpcStance` / `NpcCheckParams` / `NpcTells`
  with fixed authored values and a stub `RelationshipState`. Lets the
  **PC side** be tested fully alone: option gating per rank, the
  success formula against a known threshold, tell reveal at Perception
  7+, alignment deltas — no NPC brain required.
- **`MockPc`** is a scripted sequence of one `PlayerProfile` plus a
  list of `PlayerMove`s, emitting encounter events. Lets the **NPC
  side** be tested alone: correct stance for a given Drive profile,
  lie-catch flag-setting, AFE-pending-action colouring — no real player
  or dice required.
- **Golden seam suite.** One contract-test suite that **both** the mock
  and the real implementation of each side must satisfy. Swapping
  mock → real is guaranteed compatible because both pass the same
  suite. This is the mechanism that makes "mesh and pull apart" a
  property of the build rather than a hope.

## The async seam to the simulation — "mesh as one" without coupling

The AFE is explicitly **not a player-action handler**
(`Area-Factions-Engine.md`). The encounter never calls the AFE.
Encounter outcomes land in runtime state and the propose-write queue;
the AFE notices the **consequences on its next tick**.

One-way and deferred: you can run encounters in isolation indefinitely
and the simulation just sees a consequence queue later. The NPC
brain / sim and the encounter are therefore already async-decoupled —
"meshing" them is running both processes against the same store, not
wiring them together.

## Build & test independence — summary

| Module | Built against | Tested in isolation for |
|---|---|---|
| PC side | `MockNpc` | option gating · success formula · tell reveal · alignment shifts |
| NPC side | `MockPc` | stance selection · lie-catch flags · AFE-bias colouring |
| Shared spine | both real sides | golden seam suite · resolver formula · ledger · store cardinality |

## Scope hook — the one place the deferral touches the contract

The **arity of `relationship_ref`** is the sole point where the
deferred per-player decision reaches the seam: `npc_id` (PoC) vs
`npc_id|player_id` (post-PoC). Flipping it is a key-arity change, not a
reshape of any message or signature. By design, the contract does
**not** block the per-player scope decision.

## Unreal mapping

| Concept | Unreal |
|---|---|
| PlayerProfile · PlayerMove · NpcStance · NpcCheckParams · NpcTells · CheckOutcome | transient server-side structs (not DataTable rows) |
| `ENpcEncounterStance` · `EMoveType` · `EAlignmentTier` | enums **[new for the first two]** |
| RelationshipState (runtime) | DB-backed runtime row — NPC-global in PoC; `FNpcPlayerDispositionRow` post-PoC **[new]** |
| `proposeSeedWrite` | `FNpcProposedWriteRow` (existing, queued) |
| Alignment ledger | player-scoped runtime (DB); snapshot passed as `EAlignmentTier` |

## Open questions

1. **`secrets_shared` cardinality.** In the NPC-global PoC store, a
   secret shared with one player is shared with all. Acceptable for the
   demo, wrong for the full build — same per-player deferral as the
   rest of `RelationshipState`, noted so it isn't a surprise later.
2. **Manipulate gating ownership.** The Resolver validates the
   Deception-9 + Tier-V–VII gate, but the *option* also has to be
   gated PC-side so it doesn't appear at all below the threshold.
   Two-place gate; the contract test should assert both agree.

## Changelog

- **0.1 (Draft, 2026-06-01)** — Initial seam contract. Three modules +
  one-way dependency direction. Five crossing shapes (PlayerProfile,
  PlayerMove, NpcStance, NpcCheckParams, NpcTells). Resolver owns the
  check formula. Alignment Ledger (player-scoped; real in PoC).
  Relationship Store (cardinality-agnostic; NPC-global in PoC).
  Mock contracts + golden seam suite. Async AFE seam. Per-player
  deferral isolated to `relationship_ref` arity.

---

*Draft · [[../../Story-Architecture]] · [[../../NPC-Intelligence-System]] · [[../../Deception-Perception-Skills]] · [[../../Simulation-Tick]] · [[../../Area-Factions-Engine]]*
