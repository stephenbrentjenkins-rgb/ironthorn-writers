---
system_doc: true
doc_type: "Connection Map"
version: "2.0"
status: "Draft"
---

# Cross-NPC Connection Map

A small enough city — even Ironthorn at its scale — has key NPCs
who are aware of each other, directly or indirectly. This document
maps those connections and flags where they create story
opportunities, simulation triggers, or risks.

This document was rebuilt 2026-05-02 from a previous version
referencing non-canon factions and the old city of Ashford. The
old version is preserved in git history. This v2.0 is the
template-shaped scaffold; entries are added as NPCs are
authored and approved into `NPCs/`.

---

## How to use this document

A cross-NPC connection is a relationship between two named NPCs
that:

1. **Affects either NPC's priority calculation** in the daily
   simulation tick (see `Area-Factions-Engine.md`), AND/OR
2. **Creates story opportunity** — a thread the player can pull
   that involves both NPCs, AND/OR
3. **Flags a risk** — a way one NPC's action could cascade into
   the other's story.

Connections live here when they are *cross-faction* or
*cross-district*, where they are most likely to be lost in the
seams between faction-internal documents. Connections wholly
inside a single faction live in that faction's file.

When a connection is added here, both NPCs' files should
cross-reference this map. Faction files should also reference
relevant connections in their *Inter-faction relationships*
sections.

---

## Current NPC roster

> Filled in as Tier 3+ NPCs are approved into `NPCs/`. Each entry
> below is a placeholder until a real NPC fills the slot.

```dataview
TABLE npc_name, npc_tier, faction, location, alignment_true, status
FROM "NPCs"
WHERE npc_tier >= 3
SORT npc_tier DESC, faction ASC
```

---

## Connection entries

Each connection follows this shape:

### NPC A ↔ NPC B

**Type:** *Direct / Indirect-structural / Indirect-network /
Institutional / Personal-history*

**Summary:** one line on what the connection is.

**Awareness:**
- Does A know B exists? Yes / No / Suspects.
- Does B know A exists? Yes / No / Suspects.
- Public knowledge or hidden?

**Mechanical hooks:**
- Does either NPC's priority calculation reference the other?
- Does action by either NPC produce a flag, leverage, or
  threshold change in the other?
- Is this connection a `prerequisite` for any quest beat?

**Story potential:**
- What threads can the player pull here?
- What does each NPC stand to gain or lose if the connection
  becomes activated?

**Open design questions:**
- Decisions still to be made. Anything tagged here is fair game
  for the next design pass.

---

### Sevin → Auditor Vesh

**Type:** Indirect-network — one-directional surveillance.

**Summary:** Sevin has been quietly tracking Vesh's defection risk
for six months. Vesh does not know Sevin is watching. The link is
encoded in Sevin's `secrets_known: ["vesh_defection_risk"]` and
in her leverage inventory ("Vesh defection risk — Watching, held
6 months").

**Awareness:**
- Does Sevin know Vesh exists? **Yes.** She has built a profile of
  him from questioning-pattern reports out of Ledger Row.
- Does Vesh know Sevin exists? **Probably as a name.** He has not
  audited her office and has no record of her watching him. The
  Office of Tolerance is outside his Compact remit.
- Public knowledge or hidden? **Hidden.** Sevin's intelligence on
  Vesh is filed in her leverage inventory, not surfaced through
  any in-world channel.

**Mechanical hooks:**
- Sevin's `cunning_patience: 10` and Vesh's defection thresholds
  (`loyalty_resentment: 7/8`, `idealism_disillusionment: 7/7`)
  put both NPCs at simulation-active state. The AFE will produce
  meaningful priority scores for both on every tick.
- If the AFE simulates Vesh's defection, Sevin's surveillance is
  the most likely third party with both knowledge and capability
  to influence the outcome (warn the Compact, warn Vesh,
  facilitate the handoff to a recipient she trusts, or do
  nothing and watch).
- Sevin's hidden agenda is `regret` (the 19-year-old certificate);
  Vesh's is `self` (deciding when and to whom to defect). The
  agendas are *adjacent* — both NPCs are quietly auditing the
  institutions they have spent their careers serving. A player
  who works both NPCs may discover that they would have
  recognised each other if they had ever met.

**Story potential:**
- A player who has built trust with Sevin and triggers Vesh's
  defection becomes the hinge of a three-way negotiation: who
  receives the secondary ledger, who knows about it afterwards,
  what Sevin trades for not having to choose.
- A player who triggers Vesh's defection without involving Sevin
  may discover *afterwards* that Sevin saw it coming and chose
  not to intervene. This is leverage — Sevin held information
  that could have prevented or accelerated the event and acted
  on neither.
- The Compact-internal consequences of Vesh's defection are
  catastrophic for Compact influence in Ledger Row (see
  `WorldState/influence-ledger-row.md`); Sevin's
  *equilibrium* primary goal puts her at odds with letting that
  happen unmanaged.

**Open design questions:**
- Does Sevin act on the Vesh intelligence before defection fires,
  during, or after? Each timing produces different stories.
- If a player tells Vesh about Sevin's surveillance, what is the
  failure mode — does Vesh accelerate (Sevin can't be allowed to
  control the timing) or pause (he needs to know what she knows
  first)?
- Is there a Compact-side consequence for Sevin if she is later
  seen to have known and not warned them? The Compact does not
  formally police bystanders — but Renne Saul does not forget.

---

### Davan Ord ↔ Scholar-Physician Dael

**Type:** Direct — quiet co-located professional contact.

**Summary:** Davan and Dael operate within yards of each other in
the Ashgate Quarter, near the same Ashgate Lane building. Davan
holds two relevant secrets: `veil_delivery_materials` (he knows
the Veil moves materials through his end of the Quarter) and
`ashgate_lane_building_access` (he knows how to get into the
building adjacent to Dael's clinic). Dael, for his part, runs the
Quarter's only functioning clinic and survives there in part
because neighbouring tradesmen do not ask the wrong questions.

**Awareness:**
- Does Davan know Dael exists? **Yes**, as a neighbour and as a
  Veil scholar. He knows which materials Dael's clinic receives
  and roughly when.
- Does Dael know Davan exists? **Yes**, as the forge-master next
  door and as someone whose silence is reliable. Dael does not
  hold Davan in his `secrets_known`, which suggests the awareness
  is professional/social rather than operationally exploitable.
- Public knowledge or hidden? **Public-but-quiet.** Anyone in the
  Quarter would know they're neighbours. The exact nature of
  Davan's knowledge of Veil deliveries is not public.

**Mechanical hooks:**
- Davan's `secrets_known` makes him a candidate target for AFE
  `extort` or `trade-info` actions originating from any faction
  that wants to surveil Veil logistics. The connection here is
  the *plausible vector*: any such action plays out in Ashgate
  and affects Dael by proxy.
- Dael's defection trigger ("performs resurrection and recognises
  the energy signature — it is someone he knew") implies a future
  state where Dael begins documenting Veil operations. Davan's
  knowledge of the delivery patterns becomes corroborating
  evidence — Dael's documentation plus Davan's observation =
  a credible internal case.
- Both NPCs have moderate-to-high `idealism_disillusionment`
  (Davan 6, Dael 7). Both are watch-flagged in soft ways. A
  faction shift in Ashgate (Veil losing influence, Compact or
  Throne gaining) puts both under pressure simultaneously.

**Story potential:**
- A player investigating the Veil's logistics through Davan can
  surface details that reach Dael via local circulation. If Dael
  hears those details from a neighbour rather than from the
  Veil's own mouth, his disillusionment ticks.
- A player who has built trust with Dael and is later seen with
  Davan signals to careful observers that the player is mapping
  Veil operations from two angles. Veil-internal NPCs may
  respond — in fiction, by withdrawing access; mechanically, by
  AFE actions targeting both NPCs.
- The Ashgate Lane building is a likely future quest location.
  Davan can grant access; Dael's proximity makes him a witness
  whether or not he wants to be.

**Open design questions:**
- Does Davan formally know what the Veil does with the materials
  he sees them deliver, or does he know only the *fact of
  delivery*? The distinction changes the danger he is in.
- If the Veil suspects Davan of leaking, do they pressure him
  through Dael (whose clinic depends on Veil approval to
  function) or directly? The two routes produce different
  failure modes.
- When Dael defects, does Davan get warned in advance, swept up
  in the consequences, or quietly ignored? Each option signals
  something different about Dael's view of his neighbours.

---

### Maren Voss ↔ Davan Ord

**Type:** Direct — long-tenure professional contact.

**Summary:** Maren has been smuggling out of Ashgate Quarter for
years. Davan has been running the only functioning forge in
Ashgate for years. They have done business. The relationship is
the quiet kind that exists between two people who have seen each
other in difficult circumstances and have agreed, without ever
saying so, not to remember the specifics.

Maren's `secrets_known` includes `davan_ord_repair_history` —
she knows Davan repairs gear that the Iron Dominion garrison
would prefer not to circulate, and she knows he doesn't ask
where the gear came from. Davan's `secrets_known` includes
`maren_voss_smuggling_pattern` — he knows roughly when her
shipments come and go and which of them carry the kind of
materials that need quiet handling.

**Awareness:**
- Does Maren know Davan exists? **Yes.** She's used his forge
  for years. He is one of her routine professional contacts.
- Does Davan know Maren exists? **Yes.** She's a regular client
  whose work pattern he has read by attrition.
- Public knowledge or hidden? **Public-but-quiet.** Anyone in
  Ashgate would know they do business. The exact contents of
  that business are not public.

**Mechanical hooks:**
- Either NPC's `secrets_known` makes the other a candidate
  target for AFE `extort` or `trade-info` actions originating
  from any faction wanting to map Compact smuggling logistics or
  Ashgate's grey-market supply chain.
- Maren's `cunning_patience: 9` and Davan's `cunning_patience: 7`
  mean neither moves on the other quickly. The relationship is
  stable under most simulation conditions; it would take a
  significant external pressure (faction shift in Ashgate, a
  Compact directive, a Dominion crackdown) to fracture it.
- Davan is an independent NPC. If the Veil ever directly
  pressures him via Dael, Maren is the most likely third party
  he would warn or seek shelter through — the Compact's
  presence in Ashgate is small but it is steadier than the
  Veil's, and Maren is his most trusted Compact-aligned contact.

**Story potential:**
- A player who has built trust with Maren can be introduced to
  Davan as a "reliable mender" — trust transfer between NPCs is
  one of the cleanest narrative tools the relationship enables.
- A player investigating Davan can use Maren as the social
  vouch. The reverse also works — Davan can vouch for someone
  to Maren when she would otherwise be guarded.
- If the Veil ever leans on Davan via Dael (see
  `Davan Ord ↔ Scholar-Physician Dael`), Maren is the natural
  escape route. A three-way scene becomes possible: Veil
  pressure on Davan, Davan reaching out to Maren, Maren
  deciding whether to help — and what to extract for it.

**Open design questions:**
- Davan repairs Iron Dominion equipment that has been
  liberated. Does Maren know exactly *what* he repairs, or
  only *that* he repairs things she would not want named? The
  distinction matters for what a player can learn from her.
- If a Dominion sweep ever traces a piece of liberated gear
  back to Davan's forge, Maren is the most likely casualty by
  association. Does she know this? Does she have a contingency?
- The relationship is professional but old. Is there any
  personal dimension — mutual respect, mild fondness, an old
  debt either way? The default is no. The richer story is yes,
  carefully under-stated.

---

### Ashgate triangle — design note (not yet a connection)

Maren Voss (Compact, Ashgate eastern stall), Davan Ord
(independent forge, Ashgate central), and Scholar-Physician Dael
(Veil clinic, Ashgate southern end) all operate within a few
minutes' walk of each other. Three different factions, three
different goals, one small district.

Maren ↔ Davan and Davan ↔ Dael are now both encoded canon
(see entries above). The remaining edge is **Maren ↔ Dael**:
neither has the other in `secrets_known`. The triangle is
two-thirds connected; the third edge is geographical only.

This is flagged as a design opportunity — a tight three-NPC web
in a contested district where every pair *should* plausibly
know each other but doesn't yet, in canon. When one or more of
these NPCs gains awareness of the others (via writer pass,
player action, or AFE simulation), this section becomes real
connection entries.

**Suggested first concrete edge:** Maren ↔ Dael. The route is
Davan: he knows Maren and he knows Dael, and a player who
develops both relationships will surface a connection between
them whether or not the NPCs are formally aware of each other.
The simplest seed is a piece of secondhand awareness — Maren
knows Davan repairs things for the clinic, Dael knows the
forge-master is also tied to Compact circulation — without
either having directly transacted with the other.

---

## Faction tensions — quick reference

> This table mirrors the *Inter-faction relationships* sections
> already present in each faction file, summarized here for
> writers who need a fast cross-reference. Update when faction
> files change.

| Faction pair | Relationship | Primary friction |
|-------------|-------------|----------------|
| Aureate Covenant ↔ Gray Compact | Cold client | Covenant uses Compact intelligence while publicly condemning the organization |
| Aureate Covenant ↔ Verdant Circle | Strained allies | Both Light-aligned but disagree on means |
| Gray Compact ↔ Verdant Circle | Transactional | Information-for-access; neither faction likes the other |
| Gray Compact ↔ Iron Dominion | Stable client | Dominion pays reliably and asks few moral questions |
| Gray Compact ↔ Ashen Veil | Managed relationship | Veil is dangerous to deal with; the Compact charges accordingly |
| Gray Compact ↔ Crimson Throne | High-risk client | Profitable but volatile; the Compact keeps an exit always open |
| Iron Dominion ↔ everyone | Garrison-only | Dominion holds the Great Gate; interior is the city's problem |
| Ashen Veil ↔ Aureate Covenant | Existential opposition | Light-V vs. Dark-III on doctrinal terms |
| Crimson Throne ↔ Aureate Covenant | Underground conflict | Throne's pain economy is illegal in Covenant-controlled districts |
| Void Eternum ↔ everyone | No relationship | Eternum has no interest in alliances or conflicts; they wait |

> **Cross-reference:** each row above should match the
> corresponding entry in the `Inter-faction relationships`
> section of the faction file. If they drift, the faction file
> wins — fix this table.

---

## Open design questions — flagged for the design team

> Replace as real NPCs are added. Examples of the *kinds* of
> questions that belong here:

- Which factions have spies inside other factions, and at what
  tier? (See `Spy-Registry.md`.)
- Are there NPC pairs whose hidden agendas are mutually
  destructive — one's success is the other's ruin?
- Are there cross-faction romances, mentorships, or feuds that
  predate the current faction landscape?
- Does any NPC believe another NPC is dead, when they are not?
  (This is one of the richest possible connections — the player
  who carries that information becomes a connection node
  themselves.)

---

## Relationship to the Area Factions Engine

The AFE's NPC↔NPC action vocabulary (`NPC-Action-Vocabulary.md`)
operates on connections. A connection here is what allows two
NPCs to be plausibly aware of each other for the purposes of
`betray`, `extort`, `trade-info`, or `assassinate` actions.

When a connection escalates to action by the simulation, the
AFE's Legibility Publisher generates rumors, news crier lines,
and Compact dossier entries that surface the connection to
players. The connection map is therefore both **design
documentation** and **simulation input** — when an NPC pair is
added to this map, the simulation gains the right to involve
them in each other's lives.

---

*[[README|Back to Index]] · [[NPC-Intelligence-System]] · [[Area-Factions-Engine]] · [[NPC-Action-Vocabulary]] · [[Spy-Registry]]*
