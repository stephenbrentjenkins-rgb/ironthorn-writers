---
test_id: "TEST-002"
test_name: "Brother Aldric — Player Lies About Their Intentions"
npc_tested: "Brother Aldric"
player_deception_skill: 6
player_alignment_tier: 3
npc_perception_threshold: 6
test_status: "Ready"
test_result: ""
date_run: ""
---

# Test Scenario 002 — Brother Aldric Lie Detection

## Setup

The player is at the sanctuary. They have been asking about the shadow-touched sheltering network — officially, they claim they are trying to help. In truth they are gathering intelligence for a rival faction. Aldric asks directly: "Why do you want to know who we are sheltering?"

**Player Deception skill:** 6
**Player alignment:** Tier III — Watchful (Light-I)
**Alignment modifier:** −1 to Deception (light alignment penalises deception checks)
**NPC perception threshold:** 6

---

## Skill check calculation

```
Success chance = 50% + (6 − 6) × 9% + (−1 alignment modifier × 9%)
              = 50% + 0% − 9%
              = 41%
```

**Result:** Slight disadvantage. Just under even odds.

---

## Scenario A — Lie succeeds (41% chance)

**Player chooses:** Deflect option — "I know some people who might be able to provide safe passage. I want to see if our networks overlap."

**What Aldric does:**
He listens. Fully. Then nods. "That would be welcome." He does not verify the claim. He provides partial information — enough to be helpful, not enough to compromise the sheltered individuals if the player's intentions are bad.

**Flags set:**
- Memory log: "Player claims to have a safe passage network. Plausible. Not confirmed. Filed. Watching."
- Trust score: unchanged (5)
- Aldric's prayer bead: not observed (no tell triggered — he found the answer plausible)

**Alignment change:** Player −2 alignment points. (Player is Tier III — this mild deception puts mild downward pressure.)

---

## Scenario B — Lie caught (59% chance)

**What Aldric does:**
He is quiet for a moment. Then: "Can I ask you something else?" He asks about where the player came from — a specific detail that only matters if he already suspects. When the player answers, he nods. "That's interesting." He helps them anyway. He gives them less than he would have.

His right hand is in his pocket for three seconds. The prayer bead. Then it's gone.

**Flags set:**
- Liar's Mark: NOT activated (Aldric catches the lie but does not flag it the way a dark NPC would — he is redirecting, not collecting)
- Memory log: "Player gave an answer that didn't sit right. They helped with the food stores last week. I don't think they mean harm. But I don't think they told me the truth either. Watching. Left them a note."
- Trust score: unchanged (5) — Aldric's response is not punitive
- "Left them a note": Aldric leaves an unsigned note under the player's door with an address. No explanation. This is the hook.

**Alignment change:** Player −4 alignment points.

**Key difference from Maren and Syla:** Aldric does not bank leverage. He redirects toward what he believes the player needs. The note is not a threat — it is a second door he is offering. The player can ignore it.

---

## What to verify in Obsidian

- [ ] Memory log updated in Aldric's NPC note
- [ ] Trust score unchanged (verify Aldric's response is not punitive)
- [ ] Note hook added to Aldric's dialogue hooks section as a triggered event
- [ ] Verify prayer bead tell only surfaces for Perception 7+

---

## Notes

- This scenario tests the difference between a Gray-true NPC (Maren, who banks) and a Light-public NPC (Aldric, who redirects). Both catch the lie. Neither confronts. Completely different responses.
- The note hook is the interesting one — it gives the player something to follow regardless of their deception result.

---

*[[README|Back to Index]] · [[../NPCs/Brother-Aldric|Brother Aldric]] · [[../_System/Deception-Perception-Skills|Deception & Perception Skills]]*
