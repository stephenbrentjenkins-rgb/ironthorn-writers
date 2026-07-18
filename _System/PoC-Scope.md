---
system_doc: true
doc_type: "Project Scope"
doc_name: "Proof of Concept — Scope and Milestones"
version: "1.0"
status: "Draft"
---

# Proof of Concept — Scope and Milestones

This document defines what the Ironthorn Proof of Concept is, what it
must demonstrate, and what is explicitly out of scope. The PoC is a
business artifact — a bounded build whose purpose is to prove the
core design hypothesis works end-to-end, in a form that can be shown
to investors and used to scope a full team build.

The PoC is **not** a vertical slice of the shipped game. It is a
deliberately incomplete build that demonstrates one specific claim:
that an authored simulation can produce a living world where faction
politics shift visibly and players can read causation through fiction.

If you change anything in this document, increment `version` in the
frontmatter and add an entry to the changelog at the bottom.

## The core hypothesis the PoC proves

> NPCs are tired, not broken. An authored simulation can produce a
> living world where faction politics shift visibly, NPCs act on each
> other in fictionally legible ways, and players can read causation
> through in-world surfaces.

Every scope decision in this document traces back to this hypothesis.
If a system would not strengthen the demonstration of this claim, it
is out of scope for the PoC, even if it is in scope for the full
build.

## Team and timeline

- **Stephen** — engineering, architecture, tooling, ops, vault
  authoring lead.
- **Writer** (full-time) — NPC authoring, dialogue, gossip lines,
  test play, proof-of-life playthroughs.
- **Timeline:** 18 months target, internal deadline. Back-end
  flexibility — milestones over hard dates.

## Engine and platform commitment

- **Unreal Engine 5.5.** Continuing on the existing project at
  `C:\Users\steph\Documents\Unreal Projects\Ironthorn\`.
- **Single-shard, listen-server or local-host.** Full dedicated
  server / persistent shared world infrastructure is **deferred**
  to the post-PoC build. The PoC server runs when needed for demos
  and play tests; it does not need to be always-on.
- **HeroEngine evaluated and shelved.** See
  `_System/Decisions/Engine-Selection.md` (to be created) for the
  full evaluation if needed. Summary: vendor risk and HSL talent
  pool considerations outweighed the faster-start advantage.

## In scope

### World

- **2-3 districts.** Targets:
  - **Ledger Row** (Compact-anchored, contested, narratively most
    active — already has `WorldState/influence-ledger-row.md`).
  - **One Lower district** (Ashgate Quarter or Wound Market —
    Veil/Crimson tension, demonstrates faction churn).
  - **One Upper district** (Sanctum Ward or Greenward — anchored
    stability, demonstrates the other end of the influence model).
- Two committed; the third built if scope permits at month 12 review.

### NPCs (Option β — tiered fidelity)

- **42 named NPCs total**, distributed across the chosen districts.
- **10–15 NPCs at Tier 3+ full depth.** These are the AFE actors —
  the characters the simulation moves on. Full Writer-Standards
  treatment: layered profile, decision map, in-world response line,
  surface/mid/deep tells, full goal architecture, AFE-tunable
  priority weights.
- **Remaining 27–32 NPCs at Tier 1–2 depth.** World dressing —
  vendors, district background, faction membership. Present, named,
  with basic ambient dialogue and tier-keyed reaction blocks. Not
  AFE actors but visible to the player.
- The 6 currently-approved canonical NPCs stay; the rest are
  authored during the PoC build.

### AFE — daily simulation

All five subsystems implemented at PoC fidelity:

1. **Priority Resolver** — per-NPC action scoring against goals,
   stats, threshold pressure, faction context.
2. **Action Arbiter** — resolves contests between intersecting
   actions.
3. **Influence Writer** — translates resolved actions into
   district-level faction influence deltas; applies anchor floors;
   detects tier crossings.
4. **Service Floor Sentinel** — validates proposed diffs; clips,
   spawns, or routes to keep core services accessible. Full
   invariant enforced even at PoC scale.
5. **Legibility Publisher** — generates rumor lines, news crier
   scripts, Compact dossier entries, faction internal events.

Cadence: daily tick, accelerated for demos (compress in-world day
to ~1 real minute when needed for investor walkthroughs).

### Player-facing systems

- **Walking the world.** Standard third-person navigation across
  the chosen districts.
- **Dialogue with named NPCs.** Tier 3+ NPCs have dialogue trees
  that respond to current faction state, the NPC's stats, and
  conversation history. Tier 1–2 NPCs have shorter, tier-keyed
  reaction blocks.
- **Vendor interactions** — tier-keyed inventory and pricing.
  Demonstrates the Faction-Influence content pattern (one vendor
  file, four behavior blocks, tier-indexed selection).
- **Ambient gossip** — tavern NPCs and street NPCs speak rumor
  lines reflecting recent simulation events.
- **News criers** — district-level public-facing channels announce
  shifts in faction control.
- **Compact dossier UI** — in-fiction paid access to deeper
  simulation events. Player can subscribe at PoC tier and read
  events that other surfaces don't expose.

- **Visible PC skill growth.** Deception and Perception skills
  grow per [[Skill-Growth]]. The demonstration thread (see
  below) must produce at least one beat where bar advance,
  rank-up, and dialogue-option unlock are all visible to the
  player in succession. The full stat-evolution amendment
  (broader PoC scope around how PC and NPC stats change) is
  pending its own version.

### Player Interaction Pause

Functional. Talking to an NPC pauses them in the simulation;
24-hour timeout backstop. Conversation lock owned server-side.
This is part of the demonstrated design — players who suspect an
NPC is in danger can buy time by talking to them.

### The propose-write queue

Functional end-to-end:
- AFE produces NPC stat-change proposals each tick.
- Runtime applies changes immediately to live state.
- Vault seed only changes after writer review.
- Manager Board extended to surface the proposed-writes queue
  alongside new submissions.
- Writer (or Stephen) reviews, approves/edits/rejects, vault seed
  updates with git commit.

This is part of what the PoC proves works.

### The "watch from above" observer view

A live designer/investor-facing dashboard showing the simulation
running. Built on the same lineage as the existing
`Tools/faction-influence-dashboard.html` and
`Tools/architecture-maps.html`.

Shows:
- Current influence values per district, per faction, per tier.
- Recent tier change events.
- NPC priority math (who's pursuing what action, why).
- Queued AFE actions and their reasons.
- Live event log.
- AFE tick state (last run, next scheduled, override status).

This is the second view of the PoC: investors play in-world for
5 minutes, then watch from above for 5 minutes, and the connection
between the two views is the demonstration.

### One demonstration thread

A single faction tension thread plays out across the demo period.
Candidates:
- Compact internal politics (a Compact NPC is exposed as a Veil
  asset over the course of a simulated week).
- Veil-vs-Dominion friction in the Lower districts.
- An anchored faction pushed toward its floor via a sequence of
  designer-injected events, recovering through normal AFE behavior.

The thread is authored — it is not emergent. The point is to
demonstrate that the simulation can carry a designed beat from
trigger through resolution while producing legible surface
events for the player.

## Out of scope (explicit)

These are out of scope for the PoC and will not be built during
this 18-month window:

- **Combat** — no combat system, no weapons, no health, no enemies.
  NPCs do not fight the player. NPC-on-NPC violence is simulation
  output (text/event), not playable combat.
- **Quests beyond the demonstration thread** — no quest log, no
  quest tracker, no branching quest trees. The single demonstration
  thread is run by the AFE, not by a quest system.
- **Player progression** — no levels, no skills, no XP, no
  character development.
- **Inventory beyond vendor demonstration** — no full inventory
  system. Vendor interactions show tier-keyed pricing/availability
  but the player does not actually accumulate goods.
- **Persistent shared world / dedicated server / always-on
  infrastructure** — single-shard local hosting is sufficient.
- **Account system, authentication, payment** — not needed for
  PoC.
- **GM tools, customer support tooling, anti-cheat** — not needed.
- **The remaining four districts** beyond the chosen 2-3.
- **Combat-driven territory contests, sieges, faction wars** — out
  of scope; the simulation moves through NPC actions only.
- **Player faction reputation as a system** — player is observed
  by the simulation but the simulation does not move based on
  player reputation in the PoC. (The hooks are designed; they're
  not implemented.)

## Non-negotiables

These must be in the PoC for it to make its claim:

- **The Service Floor invariant must hold.** No proposed AFE diff
  commits if it would strand the player from core services. This
  is a load-bearing piece of the design philosophy.
- **In-world legibility must work.** Every event the AFE produces
  must be readable through at least one in-world surface. If the
  simulation does something the player can't perceive through
  fiction, that's a bug.
- **The propose-write queue must be functional.** Writer authority
  over runtime drift is part of what's being proven.
- **NPCs are tired, not broken.** Voice and tone in all PoC
  content must hold the line. See `_System/Writer-Standards.md`.

## Build phases

Phases overlap. Authoring and engineering run in parallel.

### Phase 1 — Foundation (months 1–3)

- Unreal target splits: Editor / Game / Server target files.
- Server target compiles cleanly.
- Local Postgres (or SQLite for early prototyping) stood up.
- Schema definitions for NPCs, WorldState, phases, events, queue.
- `Tools/` build pipeline: vault → JSON → DB seed.
- NPCDevTools split: existing VaultBridge stays for authoring;
  new runtime path reads from DB.
- AFE C++ scaffolding (priority resolver and arbiter as stubs).
- One vertical-slice test: a single test NPC's stats live in the
  DB, the runtime reads them, the player sees them.

**Exit criteria:** server target runs, DB seeded from vault,
runtime reads DB, one NPC visible in-world with tier-keyed
reaction block working.

### Phase 2 — AFE core (months 4–9)

- Priority Resolver — full implementation, tunable weights.
- Action Arbiter — full implementation including all 10 actions
  from `NPC-Action-Vocabulary.md`.
- Influence Writer — deltas, aggregation, anchor floors, tier
  detection.
- Service Floor Sentinel — full invariant enforcement.
- Legibility Publisher — rumor templates, crier scripts, dossier
  entries.
- Tested end-to-end against the 6 existing canonical NPCs first,
  then against the growing roster.
- Designer override interface (manual tick, action injection).

**Exit criteria:** AFE runs daily ticks against the live roster,
producing influence deltas and legibility content. Tick logged.
Service floor never violated.

### Phase 3 — Authoring (months 4–14, parallel)

Writer authors NPCs in parallel with engineering. Approximate
cadence: 1 deep NPC per week, faster for shallow ones.

- Months 4–8: 10–15 deep NPCs to Tier 3+ standard.
- Months 6–14: 27–32 shallow NPCs to Tier 1–2 standard.
- Rolling test play by writer as content lands.

**Exit criteria:** all 42 NPCs in the live roster at their
target fidelity. Stephen has reviewed; Writer-Standards held.

### Phase 4 — Player-facing (months 9–14)

- Dialogue system wired to AFE state.
- Ambient gossip pulling from DailyLife.
- Vendor tier-keyed inventories.
- Compact dossier UI.
- Player Interaction Pause functional.
- Demonstration thread implemented.

**Exit criteria:** writer can play a session in-world, talk to
NPCs, observe gossip and crier events, purchase dossier access,
and read events that the AFE produced.

### Phase 5 — Observer view (months 13–16)

- Live faction influence dashboard reading from running server.
- NPC priority inspector.
- Tick previewer.
- Event log viewer.
- Demo flow: in-world → dashboard switch → in-world.

**Exit criteria:** Stephen can run a simulated week, switch to
dashboard, narrate what happened to a non-developer.

### Phase 6 — Integration and polish (months 16–18)

- Full demo walkthrough rehearsed end-to-end.
- Bug fixing.
- Demo script written.
- Investor pitch materials assembled.
- Recovery plan for any phase that slipped.

**Exit criteria:** PoC is demo-ready. Stephen can run the full
walkthrough on demand.

## Milestones over deadlines

The 18-month target is internal and the back-end is flexible.
Milestones, not dates, define progress:

- **M1 — Foundation done.** Phase 1 exit criteria met.
- **M2 — AFE first tick.** A real tick runs end-to-end against
  the 6 existing NPCs and produces influence deltas + legibility
  events.
- **M3 — Roster authored.** All 42 NPCs at target fidelity.
- **M4 — Player-facing live.** Writer can play a session and
  read AFE events through fiction.
- **M5 — Observer view live.** Dashboard shows the running
  simulation.
- **M6 — Demo-ready.** Full walkthrough rehearsed.

Slippage is acceptable. Quality gates are not. A milestone is
not "done" until its exit criteria are met.

## Risks

Named, not solved:

- **NPC authoring outpaces engineering.** Writer finishes the
  roster faster than the AFE can simulate them. Mitigation:
  writer also runs test play and proof-of-life sessions; idle
  authoring time goes to dialogue depth, gossip lines, and
  Compact dossier content.
- **Engineering outpaces authoring.** AFE is ready, NPCs aren't.
  Mitigation: AFE is testable against the 6 existing canonical
  NPCs from M2 onward.
- **Schema drift between vault and runtime.** The single most
  common pipeline failure. Mitigation: schema validator in the
  build pipeline; CI step that fails the build if vault and DB
  schemas disagree.
- **Service Floor edge cases produce sterile worlds.** Floor
  enforcement is too aggressive and the simulation can't move.
  Mitigation: tunable floor parameters; degraded-mode visibility
  in the observer dashboard.
- **The "watch from above" view becomes the demo.** Investors
  prefer the dashboard to the in-world play. This is partly fine
  (the dashboard is the proof) and partly a trap (the dashboard
  isn't the game). Mitigation: demo script anchors on in-world
  play first, dashboard as confirmation.
- **18 months is aggressive even with flexibility.** Mitigation:
  the third district is the first thing cut; the dashboard is the
  second; the dossier UI is the third. Demonstration thread,
  10-15 deep NPCs, two districts, AFE running, in-world play,
  observer view — that's the floor.

## What this document does NOT cover

- **The full game design.** The PoC demonstrates a slice; the
  full game's combat, quests, progression, economy, content
  cadence, and live ops are outside this scope and live in
  separate (mostly future) documents.
- **Funding strategy and pitch materials.** The PoC enables those
  conversations; it doesn't define them.
- **Post-PoC architecture.** The full Option C build (dedicated
  server, persistent shared world, backend services, scaling)
  is the *next* document, written after the PoC validates the
  design.

## Changelog

- **1.0 (Draft, 2026-05-02)** — Initial PoC scope. 18-month
  target, two-person team, 2-3 districts, 42 NPCs (Option β
  tiered fidelity), AFE all five subsystems, observer view,
  single demonstration thread. Combat/quests/progression
  explicitly deferred. HeroEngine evaluated and shelved; staying
  on Unreal 5.5.

---

*[[../README|Back to Index]] · [[Story-Architecture]] · [[Area-Factions-Engine]] · [[Writer-Standards]] · [[Skill-Growth]] · [[CLAUDE|CLAUDE.md]]*
