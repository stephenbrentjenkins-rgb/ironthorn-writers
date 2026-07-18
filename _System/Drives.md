---
system_doc: true
doc_type: "Drives System"
version: "1.0"
status: "Active"
---

# Drives

The Drives system is how NPCs make choices under pressure. It is
the behavioral simulation layer of the world — distinct from the
capability layer (Attributes), which governs what a character can
do, and from the alignment layer, which governs the moral character
of what they have done.

A character is a knot of three systems:

| Layer | What it measures | Examples |
|-------|------------------|----------|
| **Attributes** | What a character can do — physical and mental capacities | Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma *(reserved; not yet defined in vault)* |
| **Drives** | What pushes them to choose under pressure | Cunning, Loyalty, Fear, Greed, Idealism — defined here |
| **Alignment** | The moral character of what they have done | See `Alignment-Spectrum.md` |

Drives are the simulation's primary handle on NPC behavior. When
the AFE engine asks "what does this NPC do next," it queries their
Drives, their sub-Drives, and the live deltas the world has pushed
against those values. Attributes determine *whether the NPC can
execute the chosen action*; Drives determine *what they choose*;
Alignment is the running record of *what they've done*.

This doc is the system overview. For the full definition of each
of the five Drives and their sub-Drives, see `Drives-Reference.md`.

---

## The five Drives

Each NPC has five main Drives, scored 1–10. Each main has two or
three sub-Drives that texture how the main expresses itself.

- **Cunning** — how the NPC processes advantage, information, and
  other people as pieces on a board. Subs: Ambition, Patience,
  Paranoia.
- **Loyalty** — who they are bound to and how that binding holds
  under pressure. Subs: Devotion, Resentment.
- **Fear** — what they are afraid of and what that fear does to
  their behavior. Subs: Desperation, Suppression.
- **Greed** — what they want, how much, and what form the wanting
  takes. Subs: Appetite, Restraint, Envy.
- **Idealism** — the principles they hold and how firm those
  principles are when tested. Subs: Conviction, Disillusionment.

---

## Stable mains, dynamic subs

Main Drives are stable across an NPC's life. A character with a
high Cunning main is a thinker; that does not change in normal
play. An NPC with a low Idealism main is unprincipled; that, too,
does not change without a major redemptive or corrupting arc.

Sub-Drives are the living layer. They shift in response to events:
betrayal pushes Resentment up, a kept promise pushes Devotion up,
a public humiliation pushes Paranoia and Resentment together.

The world is mostly made of sub-Drive shifts. Mains rarely move.
When a main moves, it is a story event worth tracking explicitly.

---

## Why Drives are not Attributes

This distinction is load-bearing. The Drives system was sometimes
called "attributes" in earlier vault content; that usage is
deprecated. Read all such references as Drives.

Attributes — when they exist — will be capability scores in the
classical RPG sense. Whether the NPC can lift the gate. Whether
they can recall the obscure ledger code from memory. Whether they
survive the wound. Attributes shape what an NPC *can* do.

Drives shape what they *choose* to do. A weak character can have
high Cunning. A strong character can have low Conviction. A wise
character can be deeply Disillusioned. The two systems are
orthogonal by design.

When the standard six Attributes are defined (likely Strength,
Dexterity, Constitution, Wisdom, Intelligence, Charisma — but
final shape TBD), the magic cost-channel system in `Magic.md` will
draw from them. Drives will remain the behavioral simulation handle.

---

## Watch thresholds

A handful of sub-Drive values are *betrayal-class signals* and
should be tracked across the roster:

| Sub-Drive | Watch threshold | What it indicates |
|-----------|----------------|------------------|
| `loyalty_resentment` | 7+ | Approaching betrayal regardless of Devotion score |
| `loyalty_resentment` | 8+ | Betrayal risk — flag for story team |
| `idealism_disillusionment` | 7+ | Idealism is largely performance; one bad day from switching sides |
| `cunning_paranoia` | 7+ | Pre-emptive escalation risk — may strike first on suspicion |

These thresholds are enforced via Dataview queries on `README.md`
and in the AFE simulation's per-tick scan.

---

## How sub-Drives shift in play

The full event-to-shift table lives in `Drives-Reference.md`. Per
NPC, designers can override defaults. The pattern is consistent:
events that betray, threaten, or expose an NPC push sub-Drives
toward volatility. Events that confirm bonds, satisfy goals, or
restore principles push sub-Drives toward stability.

This is the architecture by which the world feels reactive. Player
choices write to NPC sub-Drives. NPC sub-Drives drive NPC
behavior. The loop is the simulation.

---

## What this doc does NOT cover

- **Per-Drive definitions and sub-Drive descriptions.** Those live
  in `Drives-Reference.md`.
- **The full event-to-shift table.** Also `Drives-Reference.md`.
- **The decision map** — how an NPC's Drives produce the specific
  in-world behavior they exhibit. Lives in
  `NPC-Intelligence-System.md`.
- **Perception threshold and Deception immunity.** These are
  related but separate; they live in
  `Deception-Perception-Skills.md`.
- **Capability Attributes.** Reserved; not yet defined.

---

*[[README|Back to Index]] · [[Drives-Reference]] · [[NPC-Intelligence-System]] · [[Alignment-Spectrum]] · [[Attribute-Reference|Attributes (reserved)]]*
