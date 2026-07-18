---
cssclasses:
  - ironthorn-home
---

# IRONTHORN

> [!quote] **NPCs are tired, not broken.**  
> They suppress, they don't perform. Every character has a private life, a private fear, a private goal, and a private memory of the player.

<div class="iron-sigils">

```dataviewjs
const factions = [
  { key: "aureate",  glyph: "☼", name: "Aureate",  match: "Aureate Covenant" },
  { key: "verdant",  glyph: "❦", name: "Verdant",  match: "Verdant Circle" },
  { key: "compact",  glyph: "⚖", name: "Compact",  match: "Gray Compact" },
  { key: "dominion", glyph: "⚒", name: "Dominion", match: "Iron Dominion" },
  { key: "veil",     glyph: "☾", name: "Veil",     match: "Ashen Veil" },
  { key: "crimson",  glyph: "✷", name: "Crimson",  match: "Crimson Throne" },
  { key: "void",     glyph: "✶", name: "Void",     match: "Void Eternum" },
];
const npcs = dv.pages('"NPCs"').where(p => p.npc_name && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy") && !p.file.path.includes("_Characters"));
const html = factions.map(f => {
  const count = npcs.where(p => p.faction === f.match).length;
  return `<div class="iron-sigil ${f.key}"><span class="glyph">${f.glyph}</span><span class="name">${f.name}</span><span class="count">${count}</span></div>`;
}).join("");
dv.paragraph(html);
```

</div>

<div class="iron-grid">

<div class="iron-card">
<h3>Live NPCs</h3>

```dataviewjs
const n = dv.pages('"NPCs"').where(p => p.npc_name && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy") && !p.file.path.includes("_Characters")).length;
dv.paragraph(`<span class="iron-stat">${n}</span><span class="iron-label">canonical</span>`);
```

</div>

<div class="iron-card">
<h3>Pending</h3>

```dataviewjs
const n = dv.pages('"NPCs/_Pending"').where(p => p.npc_name).length;
dv.paragraph(`<span class="iron-stat">${n}</span><span class="iron-label">awaiting</span>`);
```

</div>

<div class="iron-card">
<h3>Tier 3+</h3>

```dataviewjs
const n = dv.pages('"NPCs"').where(p => p.npc_tier && p.npc_tier >= 3 && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy")).length;
dv.paragraph(`<span class="iron-stat">${n}</span><span class="iron-label">named & deep</span>`);
```

</div>

<div class="iron-card">
<h3>Factions</h3>

```dataviewjs
const n = dv.pages('"Factions"').where(p => p.faction_name && !p.file.path.includes("Versions")).length;
dv.paragraph(`<span class="iron-stat">${n}</span><span class="iron-label">active powers</span>`);
```

</div>

<div class="iron-card">
<h3>On the Edge</h3>

```dataviewjs
const n = dv.pages('"NPCs"').where(p => p.npc_name && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy") && ((p.loyalty_resentment ?? 0) >= 6 || (p.fear_desperation ?? 0) >= 6 || (p.idealism_disillusionment ?? 0) >= 6)).length;
dv.paragraph(`<span class="iron-stat">${n}</span><span class="iron-label">drifting</span>`);
```

</div>

<div class="iron-card">
<h3>World Files</h3>

```dataviewjs
const n = dv.pages('"NPCs" or "Factions" or "World" or "_System"').where(p => !p.file.path.includes("_Legacy")).length;
dv.paragraph(`<span class="iron-stat">${n}</span><span class="iron-label">total entries</span>`);
```

</div>

</div>

<hr class="iron-divider">

<div class="iron-section">Alignment Spectrum</div>

> Every named NPC, plotted by their **true** alignment. Light on the left, dark on the right. Hover to see who.

```dataviewjs
const npcs = dv.pages('"NPCs"').where(p => p.npc_name && p.alignment_true && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy"));
const order = ["Light-V","Light-IV","Light-III","Light-II","Light-I","Gray","Dark-I","Dark-II","Dark-III","Dark-IV","Dark-V"];
const sorted = [...npcs].sort((a,b) => {
  const ai = order.findIndex(o => (a.alignment_true||"").startsWith(o));
  const bi = order.findIndex(o => (b.alignment_true||"").startsWith(o));
  return (ai === -1 ? 999 : ai) - (bi === -1 ? 999 : bi);
});
const pips = sorted.map(p => {
  const a = (p.alignment_true || "").toLowerCase();
  const cls = a.startsWith("light") ? "light" : a.startsWith("dark") ? "dark" : "gray";
  const safe = (p.npc_name || "?").replace(/"/g, "&quot;");
  return `<div class="iron-align-pip ${cls}" title="${safe} — ${p.alignment_true}"></div>`;
}).join("");
dv.paragraph(`<div class="iron-alignment-strip">${pips}</div>`);
```

<div class="iron-section">On the Edge — Active Threads</div>

> Characters whose suppression is failing. Resentment, desperation, or disillusionment ≥ 6.  
> *These are the ones the player will break if pushed.*

```dataviewjs
const npcs = dv.pages('"NPCs"')
  .where(p => p.npc_name && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy") && !p.file.path.includes("_Characters"))
  .where(p => (p.loyalty_resentment ?? 0) >= 6 || (p.fear_desperation ?? 0) >= 6 || (p.idealism_disillusionment ?? 0) >= 6);

if (npcs.length === 0) {
  dv.paragraph('*No characters currently drifting. The world is stable. Suspicious.*');
} else {
  const rows = [...npcs].map(p => {
    const r = p.loyalty_resentment ?? 0;
    const d = p.fear_desperation ?? 0;
    const i = p.idealism_disillusionment ?? 0;
    const peak = Math.max(r, d, i);
    const which = peak === r ? "resentment" : peak === d ? "desperation" : "disillusionment";
    const pct = Math.min(100, peak * 10);
    return [
      p.file.link,
      p.faction || "—",
      `${which} ${peak}/10`,
      `<div class="iron-threat-meter" style="--threat:${pct}%"></div>`
    ];
  });
  dv.table(["NPC", "Faction", "Drift", "Pressure"], rows);
}
```

<div class="iron-section">By Faction</div>

```dataviewjs
const pages = dv.pages('"NPCs"').where(p => p.npc_name && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy") && !p.file.path.includes("_Characters"));
const byFac = {};
for (const p of pages) {
  const f = p.faction || "— Unaligned —";
  (byFac[f] ||= []).push(p);
}
for (const f of Object.keys(byFac).sort()) {
  dv.header(3, `${f}  ·  ${byFac[f].length}`);
  dv.table(
    ["NPC", "Tier", "Role", "Public", "True"],
    [...byFac[f]].sort((a,b) => (b.npc_tier ?? 0) - (a.npc_tier ?? 0)).map(p => [
      p.file.link,
      p.npc_tier ?? "—",
      p.npc_role ?? "—",
      p.alignment_public ?? "—",
      p.alignment_true ?? "—"
    ])
  );
}
```

<div class="iron-section">Recently Stirred</div>

```dataviewjs
const all = dv.pages('"NPCs" or "Factions" or "World" or "_System"')
  .where(p => !p.file.path.includes("_Legacy"))
  .sort(p => p.file.mtime, 'desc')
  .limit(10);
const html = [...all].map(p => {
  const link = p.file.link.toString();
  const folder = p.file.folder.split("/")[0];
  const when = dv.func.dateformat(p.file.mtime, "MMM dd · HH:mm");
  return `<div class="iron-ticker-row"><span class="iron-ticker-time">${when}</span><span style="color:var(--text-muted); font-size:0.85em; min-width:80px;">${folder}</span>${link}</div>`;
}).join("");
dv.paragraph(html);
```

<div class="iron-section">Pending Queue</div>

```dataviewjs
const pending = dv.pages('"NPCs/_Pending"').where(p => p.npc_name);
if (pending.length === 0) {
  dv.paragraph('*The intake is silent. No new submissions.*');
} else {
  dv.table(
    ["NPC", "Submitted By", "Status", "Updated"],
    [...pending].map(p => [
      p.file.link,
      p.submitted_by ?? p.writer_name ?? "—",
      p.status ?? "Pending",
      dv.func.dateformat(p.file.mtime, "MMM dd")
    ])
  );
}
```

<div class="iron-section">Quick Strikes</div>

- [[_System/Writer-Standards|Writer Standards]] — the canonical voice
- [[_System/Writer-Certification/01-Writer-Primer|Writer Primer]] — what every writer must read
- [[_System/NPC-Return-Taxonomy|Return Taxonomy]] — how submissions get sent back
- [[_Templates/NPC-Template-v3|NPC Template v3]] — 41-key frontmatter spec
- [[CLAUDE|CLAUDE.md]] — orientation for any AI session

```dataviewjs
const total = dv.pages('"NPCs" or "Factions" or "World"').where(p => !p.file.path.includes("_Legacy")).length;
const npcs  = dv.pages('"NPCs"').where(p => p.npc_name && !p.file.path.includes("_Pending") && !p.file.path.includes("_Legacy") && !p.file.path.includes("_Characters")).length;
const facs  = dv.pages('"Factions"').where(p => p.faction_name && !p.file.path.includes("Versions")).length;
dv.paragraph(`<div class="iron-footer">${total} entries · ${npcs} souls · ${facs} powers · the world breathes</div>`);
```
