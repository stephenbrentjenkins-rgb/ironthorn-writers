---
system_doc: true
doc_type: "Attribute Reference (reserved)"
version: "2.0"
previous_version: "Attribute-Reference_v1.0_2026-05-14.md"
version_note: "Original content moved to Drives-Reference.md. This file is now reserved for the standard six capability attributes (Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma — final shape TBD), not yet defined in the vault. The five-stat behavioral system that previously lived here was always Drives, never capability — see Drives.md and Drives-Reference.md."
status: "Reserved — content not yet authored"
---

# Attribute Reference *(reserved)*

> [!info] This doc is a placeholder.
> Attributes — capability scores in the classical RPG sense — are
> not yet defined in this vault. This file exists to reserve the
> name and to redirect anyone looking for "main attributes" to
> the correct system (Drives), which used to live here under a
> misleading title.

## What Attributes will be

When defined, Attributes will be the standard six (or whatever
final shape the design lands on — likely some variation of):

- **Strength** — physical power, lifting, melee force
- **Dexterity** — agility, reflexes, fine motor control, ranged accuracy
- **Constitution** — physical endurance, resistance to injury, recovery rate
- **Wisdom** — perception, intuition, judgement under uncertainty
- **Intelligence** — recall, reasoning, learned knowledge, magical theory
- **Charisma** — social presence, persuasion, force of personality

Attributes will govern *what an NPC or player character can do*.
They are the capability layer.

A character with high Strength can lift the gate. A character with
high Constitution can survive the wound. A character with high
Wisdom is hard to deceive (though Perception threshold currently
lives in Drives-Reference for legacy reasons).

## What Attributes are NOT

Attributes are not Drives. Drives govern *what a character chooses
to do*. The five Drives (Cunning, Loyalty, Fear, Greed, Idealism)
and their sub-Drives live in `Drives-Reference.md`. They were
historically called "attributes" in this vault; that usage is
deprecated.

If you arrived at this file looking for the system that defines
Cunning, Loyalty, Fear, Greed, and Idealism — that's `Drives.md`
for the overview and `Drives-Reference.md` for the full per-Drive
definitions.

## Open design questions for Attributes

Before this doc is filled in, three architectural questions need
resolution:

**1. Are there six Attributes or seven?** Faith as a seventh
attribute is a real option for a setting where religious magic
has its own dimension. Alternatively, Faith may be a facet of
Wisdom, or may not be an Attribute at all and instead emerge from
the Drives (Idealism + Loyalty) and alignment.

**2. How do Attributes interact with the magic cost-channel
system?** `Magic.md` references "physical attributes," "mental
attributes," and "faith/conviction" as cost channels. Once
Attributes are defined, those mappings need to be made explicit:
which Attributes drive the Physical cost channel, which drive
the Mental cost channel, which (if any) drive the Faith / Moral
channel.

**3. Player Attributes vs NPC Attributes — same system or
different?** It is possible the player character uses a richer
Attribute system than NPCs do, with NPCs getting a simplified
capability snapshot. To be decided.

These questions are not blocking. The PoC does not require
Attributes to be defined. They are the next system to design after
Magic, Drives, and the simulation tick layer are stable.

---

*[[README|Back to Index]] · [[Drives|Drives System (formerly mis-named Attributes)]] · [[Drives-Reference|Drives Reference]] · [[Magic|Magic System]]*
