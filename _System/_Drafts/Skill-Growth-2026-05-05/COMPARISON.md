# Skill Growth — Draft Comparison

Two drafts of the skill growth spec, written from the same design conversation
on 2026-05-05. Both encode the same mechanical model; they differ in where the
mechanic lives and how it positions itself relative to the rest of canon.

## The two drafts

### Append draft
**File:** `Deception-Perception-Skills_APPEND-DRAFT.md`
**Shape:** Existing `Deception-Perception-Skills.md` v1.0 with a new "Skill
growth" section appended. Frontmatter version bumped to 1.1. Changelog added.
**Net change to canon:** one file modified, no files added.

### Standalone draft
**File:** `Skill-Growth_STANDALONE-DRAFT.md`
**Shape:** New file `_System/Skill-Growth.md` v1.0. References the parent
skills doc but does not modify it. Includes its own "why a separate doc"
section explaining the split.
**Net change to canon:** one file added, parent doc unchanged.

## Trade-offs

**Discoverability.**
Append wins. A writer or engineer reading about Deception finds the growth
mechanic in the same file, no second click. Standalone requires the reader to
follow a cross-reference, which is cheap but never free.

**Maintainability.**
Standalone wins, but only if growth keeps evolving. The drafts include 6–7
pinned items each — the growth mechanic will be revised through PoC playtest
and again at full build. A standalone file means tuning passes don't touch
the canonical skills definition. An appended growth section means every tuning
pass bumps the parent doc's version too, which is fine for two skills and
gets noisier if more player skills are added later.

**Reusability.**
Standalone wins, hard, *if* additional player skills are added post-PoC. The
mechanic is genuinely skill-agnostic — bar model, growth events, difficulty
scaling, diminishing returns, alignment modifier — and a future Resolve,
Insight, Combat, or Lore skill would re-use the same machinery. Appended
growth has to either be duplicated into the new skill's section or extracted
later, and "extracted later" is a known anti-pattern.

If no further player skills are ever added, the reusability argument is moot
and the append wins on discoverability.

**Cross-reference weight.**
Standalone adds three new inbound references the doc graph has to support:
parent skills doc → standalone, PoC scope → standalone, simulation tick →
standalone. Append adds zero new inbound references; the mechanism is just
"in the parent doc" and existing parent-doc links already cover it.

This is a wash. The cross-reference structure of `_System/` already supports
documents that link richly to each other (Faction-Influence, Simulation-Tick,
NPC-Action-Vocabulary, Area-Factions-Engine all interlink heavily). Three
more links is normal weight.

**Tuning isolation.**
Standalone wins. The growth doc is a tuning surface — numbers will move. If
a designer is iterating on the rank-cost curve in the middle of playtest,
they want to be in a small file focused on the mechanic, not in a 200-line
file that also defines the entire rank ladder, the success formula, the
Liar's Mark, and Gray-path tension.

**PoC vs. full game readiness.**
Both drafts carry the same PoC content. Append tucks it into the existing
doc's Gray-path section; standalone has its own "Demonstrating growth in
the PoC" section that's slightly more explicit about the legibility surfaces
the demo thread needs.

If the PoC needs to land first and the rest evolves later, standalone gives
the demo thread a cleaner reference point. If the PoC just needs the rules
to exist and the parent doc to be coherent, append is fine.

## Where they're identical

The mechanic is the same in both drafts:

- Visible 0–100% bar per rank
- Hidden exponential point cost per rank (placeholder values match)
- Sought-after success = +1pp base, scaled by difficulty margin
- Failed-roll d100, 10% chance −1pp
- Linear diminishing returns by (NPC, check type) per in-world day
- Alignment growth modifier table (same values)
- Same six placeholder items pinned for v2.0
- Same five "what does not award growth" cases
- Starting state and PoC demonstration approach identical

If you adopt one and later regret it, the migration is trivial — the body
text moves, the frontmatter version resets, the cross-references update.
This is a low-stakes choice mechanically. The decision is about how the
docs read, not how the system works.

## Recommendation

**Standalone, if there's any chance of additional player skills post-PoC.**
The mechanic is genuinely skill-agnostic and benefits from being treated
that way from the start. It also keeps the canonical skills doc — which
defines what Deception and Perception *are* — separate from the tuning
surface that defines how they grow.

**Append, if the player's stat surface is committed to ending at Deception
and Perception only.** No skill ever joins the family, the mechanic never
needs to be referenced from a third doc, and the cost of a slightly larger
parent file is offset by the discoverability gain.

The question that decides this is whether you expect a third player skill
to be authored before the full game ships. Not the answer to "will the full
game have more skills" (probably yes), but to "will I write one before the
PoC ships." If yes — standalone, now. If no — append now, refactor later
if and when needed.

## The hybrid that isn't worth doing

It's tempting to put the growth mechanic in the standalone doc *and* link
it from a stub section in the parent skills doc. Don't. That introduces
two places to look for the same content, which is exactly the failure mode
both options were designed to avoid. Pick one home.
