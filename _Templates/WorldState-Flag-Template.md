---
flag_name: "FLAG NAME"
flag_slug: "flag-slug-kebab-case"
flag_type: "boolean"
# Type options: boolean | integer | string | enum | faction_influence_vector
flag_default: "false"
scope: "World/Region/Location-or-System"
authority: "Faction Name OR System Name"
# Who or what is the in-world cause of this fact being true?
mutability: "tick"
# Mutability options:
#   permanent  — never changes once set
#   tick       — changes on a recurring world tick (daily, weekly, etc.)
#   triggered  — changes only when a questline beat or system writes it
write_sources: []
# List of slugs (questline beats, system processes) authorized to write this flag.
# Empty array = no authorized writers (use for permanent flags).
read_consumers: []
# List of files (phases, dailylife routines, NPC dialogue) that read this flag.
# Authoring aid; not enforced.
template_version: "1.0"
status: "Draft"
---

# `=this.flag_name`

> [!info] Flag at a glance
> **Slug:** `=this.flag_slug` · **Type:** `=this.flag_type` · **Default:** `=this.flag_default`
> **Scope:** `=this.scope`
> **Authority:** `=this.authority` · **Mutability:** `=this.mutability`
> **Status:** `=this.status`

---

## What this fact is

> REPLACE — one paragraph. State the fact in plain language. What
> is true in the world when this flag has its non-default value?
> Who in the world would know this is true, and how would they
> know? Avoid mechanical language; describe the in-world reality.

## Why it lives at World scope

> REPLACE — one paragraph. Justify why this is server-shared and
> not phased per cohort. The test: would two players standing next
> to each other always agree this is true? If yes, World. If
> "depends on which one has done the quest," it belongs in
> PhaseLayers, not here.

## Tick or trigger

**If `mutability: tick`:**
> REPLACE — describe the recurring schedule. "Every Wednesday at
> server reset, the Iron Dominion garrison sells the gate register
> to the Gray Compact." Be specific about period and authority.

**If `mutability: triggered`:**
> REPLACE — list the beats or systems that may write this flag.
> Cross-reference each one in `write_sources` above.

**If `mutability: permanent`:**
> REPLACE — state when this flag was set in world history. "Set at
> world creation; the city has always been built downstream of the
> Sanctum Ward." Permanent flags are usually backstory facts that
> design needs to query.

## Read consumers

> REPLACE — list which phases, daily routines, NPC dialogue
> branches, or systems consult this flag. This is an authoring
> aid: when you change the flag's semantics, you know what else
> to review.

## Authority

> REPLACE — who or what causes this fact to be true in-world?
> A faction's policy? A natural process? A historical event?
> The authority field links the mechanical flag to a narrative
> cause, which prevents the flag from drifting into "just a
> boolean a designer set."

## Special note: faction_influence_vector type

If `flag_type: faction_influence_vector`, this flag describes a
district's faction influence values. Add a `vector` block to
frontmatter:

```yaml
vector:
  aureate-covenant: 75
  verdant-circle: 20
  gray-compact: 35
  iron-dominion: 15
  ashen-veil: 5
  crimson-throne: 10
  void-eternum: 0
anchor_floors:
  aureate-covenant: 60   # Sanctum Ward example
```

See `_System/Faction-Influence.md` for the full model.

## Unreal mapping

| YAML field | UStruct field | Type |
|---|---|---|
| flag_slug | FlagSlug | FName |
| flag_type | FlagType | EFlagType |
| flag_default | FlagDefault | FString (parsed by type) |
| scope | Scope | FString |
| mutability | Mutability | EFlagMutability |

> Note: write_sources and read_consumers are authoring metadata
> and do not need to round-trip into Unreal. They live in the
> vault for designer-side dependency tracking.

---

*[[../README|Back to Index]] · [[../_System/Story-Architecture]]*
