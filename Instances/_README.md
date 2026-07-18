# Instances

Group / set-piece content. Hard-bounded shared spaces entered through
portals: dungeons, raids, scenarios.

**Distinct from StoryInstances** because Instances are:
- Group-based (or supports multiple players, anyway).
- Repeatable (mostly).
- Self-contained — generally don't write back to WorldState.

**Use cases:**
- Dungeons.
- Raids.
- Public events / scenarios.
- The Hollows network (when accessed — though the Hollows themselves
  may live partly in shared world and partly in instance space; design
  TBD).

**Authoring:** template TBD. Instances are authored more like
traditional level design than like phased world content.

**Read this first:** `_System/Story-Architecture.md`.

Instances are entered via portals or Questline beats. They have their
own geometry. Typically they don't write to WorldState, but exceptions
exist (a raid completion that shifts faction influence in the world).
When an Instance does write outward, the writes go through the same
`world_writes:` mechanism as a Questline beat.
