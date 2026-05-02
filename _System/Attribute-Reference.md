---
system_doc: true
doc_type: "Attribute Reference"
version: "1.0"
---

# Attribute Reference

All NPCs have five main attributes and between two and three sub-attributes per main. Mains are stable character traits. Subs are dynamic — they shift during play based on what happens to the NPC.

**Scoring:** 1–10 for all attributes.
> **1–3** Naive / Low · **4–6** Aware / Average · **7–9** Calculating / High · **10** Masterful / Exceptional

---

## Cunning *(3 subs — most complex)*

**Main — Cunning**
How this NPC processes advantage, information, and other people as pieces on a board. High Cunning NPCs operate on everyone around them. Low Cunning NPCs react to events rather than anticipate them.

| Sub | What it measures |
|-----|-----------------|
| **Ambition** | How actively they pursue advantage. High = always working an angle. Low = content where they are, opportunistic not scheming. |
| **Patience** | How long they will wait before deploying what they know. High = holds leverage for months, deploys at the perfect moment. Low = acts quickly, sometimes too quickly. |
| **Paranoia** | How much past burns have made them pre-emptively suspicious. High = assumes everyone is working an angle, may strike first. Low = still extends basic good faith. |

**Interaction note:** Patience and Paranoia pull against each other. High Patience + High Paranoia = a very dangerous NPC — they are both suspicious and controlled enough to wait for the optimal moment to act on it. High Paranoia + Low Patience = unpredictable, may escalate on suspicion alone.

---

## Loyalty *(2 subs)*

**Main — Loyalty**
Who they are bound to and how that binding holds under pressure. Loyalty can be to a person, a cause, a faction, or an ideal. The sub-attributes reveal the texture of that loyalty.

| Sub | What it measures |
|-----|-----------------|
| **Devotion** | How deep the loyalty actually runs. High = genuine bond, would absorb significant harm to protect. Low = loyal by circumstance or self-interest. |
| **Resentment** | The pressure building beneath the loyalty. High = has given too long without adequate return. The powder keg beneath the devoted surface. |

> [!warning] Resentment threshold
> When `loyalty_resentment` reaches **8 or above**, the NPC is a betrayal risk regardless of their Devotion score. Flag for story team. This is the most common source of unexpected NPC behaviour in playtesting.

**Interaction note:** High Devotion + High Resentment = one of the most volatile NPC states in the system. They will not betray easily — but when they do, it will be total.

---

## Fear *(2 subs)*

**Main — Fear**
What they are afraid of, and what that fear does to their behaviour. Fear is not weakness — high Fear NPCs are often the most dangerous because they are operating under constant threat-pressure.

| Sub | What it measures |
|-----|-----------------|
| **Desperation** | Whether fear drives reckless action. High = will take dangerous risks to escape the feared outcome. Makes them exploitable. |
| **Suppression** | How well they bury and perform past the fear. High = appears calm and may appear brave. The fear is fully operational underneath. |

**Interaction note:** High Suppression NPCs read as confident. They are not. A player with Perception 7+ may catch the tells. High Desperation + Low Suppression = the NPC whose fear is readable and whose decisions are therefore predictable — and manipulable.

---

## Greed *(3 subs — most complex)*

**Main — Greed**
What they want, how much they want it, and what form that wanting takes. Greed is not always material — it can be for power, safety, information, freedom, or someone else's specific life.

| Sub | What it measures |
|-----|-----------------|
| **Appetite** | How hungry they are for more. High = never satisfied, always reaching, risk-tolerant for gain. Low = satisfied with enough, situational. |
| **Restraint** | How well they conceal the appetite. High = their greed is invisible until they move. Low = their wanting is visible and manipulable. |
| **Envy** | Whether their greed is directional — fixed on what a specific person or group has. High = fixated, produces sabotage and targeted rivalry rather than general accumulation. |

**Interaction note:** Appetite and Envy are different kinds of greed that produce opposite behaviours. High Appetite = accumulation behaviour. High Envy = targeted disruption behaviour. An NPC can have both, but one will usually dominate.

---

## Idealism *(2 subs)*

**Main — Idealism**
What principles they hold, what cause or value they think justifies their existence, and how firm those principles are when the world applies pressure.

| Sub | What it measures |
|-----|-----------------|
| **Conviction** | How firm the principles are under pressure. High = will not bend regardless of consequence. Low = principles flex when the stakes are high enough. |
| **Disillusionment** | How much the world has eroded the belief. High = still says the right words but the faith is hollow. One bad day from switching sides. |

> [!warning] Disillusionment threshold
> When `idealism_disillusionment` reaches **7 or above**, the NPC's idealism is largely performance. Their Conviction score now represents stubbornness as much as principle. Flag for story team.

**Interaction note:** High Idealism + High Disillusionment is the most interesting combination — they believe deeply in something they no longer trust the world to provide. This often produces the most morally complex NPC decisions.

---

## Perception threshold

Not a personality attribute — a difficulty rating for deceiving this NPC.

| Threshold | What it means |
|-----------|--------------|
| 1–3 | Low awareness. Most players can deceive this NPC. |
| 4–6 | Average. Standard Deception skill check. |
| 7–8 | Alert. High-skill deception required. |
| 9 | Exceptional. Only maxed Deception with alignment bonus has realistic odds. |
| 10 | Near-impossible. Reserved for NPCs specifically built to read people. |

Situational modifiers are defined in each NPC's individual profile — threshold may drop in specific circumstances (distracted, drunk, emotionally compromised) or rise (hypervigilant, actively suspicious).

---

## Deception immune

A boolean flag. When true, no player Deception skill check can fool this NPC regardless of score or alignment modifier. Must be explained in-world with a reason that feels earned — not "they're just very smart." Examples: an oracle who reads truth, a blind seer who hears only what is real, a parent who simply knows. Applied rarely. Overuse collapses the skill system.

---

## How sub-attributes shift during play

Sub-attributes are the living layer of the system. They change in response to events:

| Event | Likely sub-attribute shift |
|-------|---------------------------|
| Player betrays NPC | Resentment +2, Devotion −1, Desperation +1 |
| Player helps NPC at personal cost | Resentment −1, Devotion +1 |
| NPC's primary goal is threatened | Desperation +2, Paranoia +1 |
| NPC successfully deploys leverage | Appetite −1 (satisfied), Ambition +1 |
| NPC is publicly humiliated | Paranoia +2, Resentment +2 |
| Player confesses a previous lie | Trust score +2, Resentment −1 |

Sub-attribute shifts are defined per-event in each NPC's profile. The values above are suggested defaults — designers can override for specific characters.

---

*[[README|Back to Index]] · [[NPC-Intelligence-System]] · [[Deception-Perception-Skills]] · [[NPC-Tier-Reference]]*
