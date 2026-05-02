---
test_id: "TEST-001"
test_name: "Maren Voss — Player Lies About the Sigil"
npc_tested: "Maren Voss"
player_deception_skill: 5
player_alignment_tier: 4
npc_perception_threshold: 7
test_status: "Ready"
test_result: ""
date_run: ""
---

# Test Scenario 001 — Maren Voss Lie Detection

## Setup

The player has taken a sigil from a vault they were not authorised to enter. They are meeting Maren at her stall. She asks, casually, whether they know anything about the sigil that went missing from the eastern merchants' lockup.

**Player Deception skill:** 5
**Player alignment:** Tier IV — Unbound (Gray)
**Alignment modifier:** 0 (Gray = no bonus/penalty)
**NPC perception threshold:** 7

---

## Skill check calculation

```
Success chance = 50% + (5 − 7) × 9% + 0 alignment modifier
              = 50% + (−18%)
              = 32%
```

**Result:** Low probability. Run the scenario twice — once assuming success, once assuming failure.

---

## Scenario A — Lie succeeds (32% chance)

**Player chooses:** Standard Lie option — "I've never even been near that lockup."

**Check result:** Success (rolled under 32%)

**What Maren does:**
She nods. Asks a follow-up question about something unrelated. Gives the player the information they came for. Her left hand moves to the copper coin in her apron pocket — turns it twice. She does not pursue it further.

**Flags set:**
- Liar's Mark: NOT active (lie succeeded)
- Memory log entry: "Day 4 — player denied knowing about the sigil. I am not certain. Filed. Watching."
- Trust score: unchanged (5)

**Alignment change:** Player −2 alignment points.

**Follow-up:** Within 72 in-game hours, Maren has her contact in the eastern merchants' guild check the lockup access records quietly. She is now 80% certain the player is lying. She updates her log. She does nothing visible.

---

## Scenario B — Lie caught (68% chance)

**Player chooses:** Standard Lie option — "I've never even been near that lockup."

**Check result:** Failure (rolled over 32%)

**What Maren does:**
She nods slowly. Refills the player's cup. Smiles. "Of course." She asks about something mundane — prices on a specific trade route. She helps the player with what they came for. She does not challenge the lie.

Her left hand moves to the copper coin. Turns it twice.

**Flags set:**
- Liar's Mark: ACTIVE
- Debt flag: ACTIVE (she is now holding this)
- Memory log entry: "Day 4 — player lied about the sigil. Perception confirmed. Useful. Holding. Goal relevance: medium — vault access connects to Drael's network. Watch whether they surface again."
- Trust score: unchanged visibly, internally decremented to 4

**Alignment change:** Player −4 alignment points.

**Player visible feedback:** Nothing. No confrontation. The conversation ends normally.

**High Perception tell (Perception 7+ passive):** Player notices the copper coin move. Three seconds. She is talking about trade routes the entire time. No other signal.

---

## What to verify in Obsidian

- [ ] Maren's memory log updated in her NPC note
- [ ] Liar's Mark flag updated in frontmatter (`liar_mark_active: true`)
- [ ] Debt flag updated (`debt_flag_active: true`)
- [ ] Trust score decremented in frontmatter (`trust_score: 4`)
- [ ] Leverage inventory entry added
- [ ] Dataview "active flags" query reflects changes
- [ ] Global "all active flags" query in README shows Maren

---

## Notes for next test

- Run Test 002: Player returns and confesses the lie. Verify trust restoration and mark clearing.
- Run Test 003: Player has Perception 7 — verify passive tell is surfaced correctly.
- Run Test 004: Player lies to Maren after Liar's Mark is active — verify dialogue shift is detectable.

---

*[[README|Back to Index]] · [[../NPCs/Maren-Voss|Maren Voss]] · [[../_System/Deception-Perception-Skills|Deception & Perception Skills]]*
