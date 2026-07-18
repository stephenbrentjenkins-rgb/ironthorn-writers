# StoryInstances

Solo or near-solo private narrative chambers. Used **sparingly** —
reserved for moments that genuinely need isolation from the shared
world.

**Use cases:**
- The player's death and resurrection.
- A one-on-one with a major antagonist.
- A vision sequence.
- Memory / dream / interrogation chambers.

**Not for:**
- Ordinary main-story beats. Those happen in shared phased world.
- Dungeons or raids. Those go in `Instances/`.
- Anywhere the player should be able to feel the living world around
  them.

**Authoring:** template TBD. StoryInstances are authored more like
Questline beats than like phased world content — they have their own
geometry and run linear scenes.

**Read this first:** `_System/Story-Architecture.md`.

StoryInstances are entered via Questline beats with an `instance_entry:`
field. They have a clear entry trigger and exit condition; no player
"lingers" in a StoryInstance.

**Editorial principle:** if you find yourself wanting to put a beat in
a StoryInstance because the shared-world version would be "messy" or
"hard to coordinate," that's usually a sign the beat is fighting the
architecture. Try it in shared phased world first. Fall back to
StoryInstance only when the moment cannot work otherwise.
