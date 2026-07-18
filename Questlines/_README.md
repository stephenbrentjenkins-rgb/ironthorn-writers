# Questlines

The narrative spine. Main story, side questlines, faction questlines.
Each questline is a folder; each beat is a file underneath.

**Folder structure:**

```
Questlines/
  hollows-compact/                      ← questline folder
    _questline.md                       ← questline header doc (TBD template)
    hollows-compact-beat-01.md          ← first beat
    hollows-compact-beat-05.md          ← sparse numbering (insertion-friendly)
    hollows-compact-beat-10.md
    ...
```

**Authoring beats:** use `_Templates/Questline-Beat-Template.md`.
Beat slug convention: `<questline-slug>-beat-<NN>` with sparse numbering
(1, 5, 10, 20) so beats can be inserted later without renumbering.

**Read this first:** `_System/Story-Architecture.md`,
`_System/Writer-Standards.md`.

A beat declares its effects in frontmatter:
- `phase_activations:` — which phases the beat moves the player into
- `world_writes:` — which World flags the beat sets
- `npc_writes:` — proposed NPC stat changes (queued for writer review)
- `instance_entry:` — if the beat sends the player into a StoryInstance
  or Instance

A beat does not contain logic. It declares effects. The runtime applies
them.

**Tone reminder:** NPCs are tired, not broken. The same applies to story
beats. Cinematic theatricality is a tone failure.
