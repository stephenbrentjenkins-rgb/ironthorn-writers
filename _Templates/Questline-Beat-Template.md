---
beat_name: "BEAT NAME"
beat_slug: "questline-slug-beat-NN"
# Convention: <questline-slug>-beat-<two-digit-number>
# Example: hollows-compact-beat-03
questline_slug: "questline-slug-kebab-case"
beat_index: 1
# Order within the questline. Sparse numbering allowed (1, 5, 10, 20)
# so beats can be inserted later without renumbering.
trigger_type: "location_entry"
# Trigger options:
#   location_entry      — player enters a named location
#   npc_interaction     — player initiates dialogue with a specific NPC
#   prior_beat_complete — previous beat in this questline was completed
#   world_flag          — a world flag reaches a specified value
#   npc_threshold       — an NPC's attribute crosses a threshold
#   manual              — fired by another beat or system explicitly
trigger_target: ""
# Slug of the location, NPC, beat, flag, or threshold that fires this beat.
prerequisites: []
# Beat slugs that must be completed before this beat can fire.
phase_activations: []
# Phases this beat moves the player into. Each entry: "phase-group:phase-slug".
# A beat may activate one phase per group.
phase_deactivations: []
# Phases this beat moves the player out of. Each entry: "phase-group:phase-slug"
# or "phase-group:base" to exit the group entirely.
world_writes: []
# World flag changes this beat performs. Each entry: "flag-slug:value".
npc_writes: []
# Proposed NPC changes — pending review by the writer who owns each NPC.
# Each entry: "npc-slug:field:value". Example: "factor-renne-saul:trust_score:7".
instance_entry: ""
# If this beat sends the player into a StoryInstance or Instance,
# name the slug here. Empty = no instance entry.
completion_condition: "auto_on_dialogue_end"
# Completion options:
#   auto_on_dialogue_end — beat completes when the body's dialogue closes
#   manual               — beat completes when explicitly marked done
#   condition            — beat completes when a stated condition is met
template_version: "1.0"
status: "Draft"
---

# `=this.beat_name`

> [!info] Beat at a glance
> **Slug:** `=this.beat_slug` · **Questline:** `=this.questline_slug` · **Index:** `=this.beat_index`
> **Trigger:** `=this.trigger_type` → `=this.trigger_target`
> **Status:** `=this.status`

---

## What happens in this beat

> REPLACE — one to three paragraphs. Describe the beat from the
> player's perspective. What do they see, hear, and choose? Stay
> in tone — tired-not-broken applies to story beats as much as
> NPC writing. Cinematic theatricality is a tone failure.

## Trigger

> REPLACE — describe in narrative terms what causes this beat to
> fire. The formal trigger is in the frontmatter; this section
> explains the *fictional* cause. "The player has been seen
> entering Ledger Row often enough that Factor Saul considers
> them worth approaching."

## Body

> REPLACE — the actual content of the beat. Dialogue, environmental
> change, cinematic, or whatever the beat consists of. If the body
> is dialogue, write it in standard dialogue format with speaker
> labels and parenthetical action notes. If the body is
> environmental, describe the change and what the player observes.

## Player choices

> REPLACE — list the meaningful choices the player has within this
> beat, if any. Each choice should map to one or more `phase_activations`,
> `world_writes`, or `npc_writes`. If a choice has no mechanical
> effect, mark it explicitly: "(narrative-only; no state change)".

## Effects — declared

This beat produces the following state changes (pulled from
frontmatter for review):

**Phase activations:** `=this.phase_activations`
**Phase deactivations:** `=this.phase_deactivations`
**World writes:** `=this.world_writes`
**NPC writes (proposed):** `=this.npc_writes`
**Instance entry:** `=this.instance_entry`

## Effects — justification

> REPLACE — for each effect declared above, state why it lives at
> the scope it does. World writes need to justify why the change
> is server-shared. Phase activations need to justify why the
> change is cohort-scoped. NPC writes need to justify what
> in-fiction event changed the NPC's state. Instance entry needs
> to justify why the moment requires private space.

This is the most important section to fill out honestly. If you
cannot justify a scope, the scope is wrong. Move the effect to
the right place before continuing.

## Completion

> REPLACE — describe how the beat ends. If `auto_on_dialogue_end`,
> describe what closes the conversation. If `condition`, state the
> condition narratively and formally.

## Downstream beats

> REPLACE — list beats that may fire after this one completes,
> with their trigger conditions. This is an authoring aid for
> tracking the questline's branching shape.

## Tone check

> REPLACE — one or two lines explaining how this beat reflects
> the world's tone. NPCs are tired, not broken. The world's
> exhaustion is the throughline. If this beat reads as triumphant,
> dramatic, or cinematic in a Saturday-morning way, flag it.

## Unreal mapping

| YAML field | UStruct field | Type |
|---|---|---|
| beat_slug | BeatSlug | FName |
| questline_slug | QuestlineSlug | FName |
| beat_index | BeatIndex | int32 |
| trigger_type | TriggerType | ETriggerType |
| trigger_target | TriggerTarget | FName |
| prerequisites | Prerequisites | TArray<FName> |
| phase_activations | PhaseActivations | TArray<FString> |
| phase_deactivations | PhaseDeactivations | TArray<FString> |
| world_writes | WorldWrites | TArray<FString> |
| npc_writes | NpcWrites | TArray<FString> |
| instance_entry | InstanceEntry | FName |
| completion_condition | CompletionCondition | ECompletionCondition |

---

*[[../README|Back to Index]] · [[../_System/Story-Architecture]] · [[../_System/Writer-Standards]]*
