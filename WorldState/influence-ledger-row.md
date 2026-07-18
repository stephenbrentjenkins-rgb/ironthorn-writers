---
flag_name: "Faction Influence — Ledger Row"
flag_slug: "influence-ledger-row"
flag_type: "faction_influence_vector"
flag_default: "see vector block"
scope: "World/Ironthorn/Ledger-Row"
authority: "Area Factions Engine (daily simulation tick)"
mutability: "tick"
write_sources:
  - area-factions-engine
read_consumers:
  - daily-life routines in Ledger Row
  - vendors in Ledger Row
  - npc dialogue branches in Ledger Row
  - news criers (district-level)
  - compact dossier (regional summary)
vector:
  aureate-covenant: 25
  verdant-circle: 15
  gray-compact: 80
  iron-dominion: 20
  ashen-veil: 10
  crimson-throne: 15
  void-eternum: 0
anchor_floors:
  gray-compact: 60
template_version: "1.0"
status: "Draft"
---

# Faction Influence — Ledger Row

> [!info] Flag at a glance
> **Slug:** `=this.flag_slug` · **Type:** `=this.flag_type`
> **Scope:** `=this.scope`
> **Authority:** `=this.authority` · **Mutability:** `=this.mutability`
> **Status:** `=this.status`

---

## What this fact is

Ledger Row is the seam between Upper and Lower Ironthorn, and it is
where the city's commerce and information economy live. The Gray
Compact is dominant here by long convention — the Ledger House sits
across the divide and serves both sides — but the district is
genuinely contested. Aureate Covenant and Iron Dominion both keep
quiet presences for their own intelligence reasons. The Ashen Veil
and Crimson Throne maintain minimal footholds. Verdant Circle's
presence is institutional, not territorial: a few healers, an old
contract with the Compact for medical neutrality during disputes.

The current vector reflects that landscape: Compact dominant
(80), no other faction over 30. The district is *Contested* under
the tier model for everyone except the Compact, who are
*Dominant*.

## Why it lives at World scope

Two players standing in Ledger Row always see the same banners,
the same Compact offices, the same unmarked doors. Faction
control here is not phased per cohort — it is a public fact
visible to anyone who walks the street. If a story beat needs to
make Ledger Row feel different to a particular player (an
infiltration mission where the Compact has temporarily withdrawn
their public presence, for instance), that's a Phase concern,
not an influence concern.

## Tick or trigger

The AFE writes this flag on the daily simulation tick. Influence
deltas come from:

- NPC actions resolved in the district (sabotage, extort, expose)
- Faction quest outcomes in the district
- Compact internal events (rare; Compact rarely loses ground here)
- Designer-authored crisis events (manual override)

The Compact's anchor floor of 60 prevents ordinary tick behavior
from reducing them below *Dominant* without an explicit
designer-authored crisis event. This matches lore: the Compact's
hold on Ledger Row is institutional, and would require a
significant story beat to break.

## Read consumers

- **Vendors in Ledger Row.** Compact-Dominant tier means brokers
  are open and stocked; non-Compact vendors operate quietly with
  reduced inventories.
- **NPC dialogue.** NPCs of non-Compact factions in this district
  default to *Minority* tier behavior (guarded, discreet,
  watching the room).
- **News criers (district-level).** Read the vector daily for
  shift announcements.
- **Compact dossier.** Aggregates this with neighboring districts
  for the player-facing regional summary.

## Authority

The Compact's dominance here is institutional rather than martial.
The Ledger House is a network, not a fortress. The authority is
the long convention that all factions need information services
and the Compact provides them — break the convention and every
faction loses something. This is why anchor-floor protection makes
narrative sense: you can't unseat the Compact from Ledger Row by
attrition. It takes a story event.

## Anchor floor justification

`gray-compact: 60` keeps the Compact at *Contested* minimum
through ordinary simulation. They cannot drop to Minority or
Absent without a designer-authored crisis event that explicitly
overrides the floor. This is intentional — the Compact's hold on
Ledger Row is a load-bearing piece of the world's information
economy.

## Unreal mapping

| YAML field | UStruct field | Type |
|---|---|---|
| flag_slug | FlagSlug | FName |
| flag_type | FlagType | EFlagType |
| scope | Scope | FString |
| vector | InfluenceMap | TMap<FName, int32> |
| anchor_floors | AnchorFloors | TMap<FName, int32> |

---

*[[../README|Back to Index]] · [[../_System/Story-Architecture]] · [[../_System/Faction-Influence]]*
