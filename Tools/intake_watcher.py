"""
Ironthorn NPC Intake Watcher v1.2
===================================
Watches NPCs/_Pending/_Intake/ for new NPC description files.
Uses Claude Code CLI (already installed and authenticated) to process prose.
No pip install required — uses your Max subscription directly.

FIXES in v1.2:
  - README.md excluded from processing
  - Encoding set to utf-8 throughout

USAGE:
  Double-click: start_intake_watcher.bat

DROP FORMAT:
  Name the file after the NPC: Factor-Renne-Saul.md
  Optional header:
    Writer: Jane Smith
    Email: jane@example.com
    Tier: 3
    District: Ledger Row
    ---
    (prose below)
"""

import os
import sys
import time
import json
import re
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path

# ─── PATHS ────────────────────────────────────────────────────────────────────

VAULT_ROOT  = Path(r"C:\Users\steph\Desktop\Game\GameVault")
INTAKE_DIR  = VAULT_ROOT / "NPCs" / "_Pending" / "_Intake"
PENDING_DIR = VAULT_ROOT / "NPCs" / "_Pending"
CHARS_DIR   = VAULT_ROOT / "NPCs" / "_Characters"

POLL_INTERVAL = 5  # seconds

# Files to never process regardless of extension
EXCLUDED_FILENAMES = {
    "readme.md", "readme.txt", "readme",
    "instructions.md", "instructions.txt",
}

CLAUDE_PATHS = [
    r"C:\Users\steph\AppData\Roaming\npm\claude.cmd",
    r"C:\Users\steph\AppData\Roaming\npm\claude",
    r"C:\Program Files\nodejs\claude.cmd",
    r"C:\PROGRA~1\nodejs\claude.cmd",
]

def find_claude():
    for p in CLAUDE_PATHS:
        if Path(p).exists():
            return p
    result = subprocess.run(["where", "claude"], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip().split("\n")[0].strip()
    return None

# ─── STORY THREAD DETECTION ───────────────────────────────────────────────────

STORY_THREADS = [
    {"name": "The Auditor's Defection",             "keywords": ["vesh","compact","auditor","ledger","defect","spy","registry","saul"]},
    {"name": "The Energy Source",                   "keywords": ["dael","veil","resurrection","energy","ashen","physician","vorell","ritual"]},
    {"name": "The Forge and the Building",          "keywords": ["ord","forge","ashgate","lane","building","veil","tipping"]},
    {"name": "The Dead-Drop and the Missing Agent", "keywords": ["rynn","ashav","petrov","seld","hollows","missing","compact","dead-drop"]},
    {"name": "The Debt That Doesn't Clear",         "keywords": ["maren","voss","drael","ember","debt","relic","smuggl"]},
    {"name": "Torven in the Confession Chair",      "keywords": ["torven","ashcroft","aldric","covenant","throne","penitent","sanctum"]},
    {"name": "The Certificate",                     "keywords": ["sevin","certificate","offered","throne","wound","market","tolerance"]},
    {"name": "What Rynn Saw in the Hollows",        "keywords": ["void","eternum","hollows","rynn","guttered"]},
]

def detect_threads(text):
    t = text.lower()
    return [th["name"] for th in STORY_THREADS if any(k in t for k in th["keywords"])]

# ─── FILE PARSING ─────────────────────────────────────────────────────────────

def parse_intake_file(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    meta = {"writer": "", "email": "", "tier": "", "district": ""}
    prose = content

    if content.startswith(("Writer:", "Email:", "Tier:", "District:", "Name:")):
        parts = content.split("---", 1)
        if len(parts) == 2:
            header, prose = parts[0].strip(), parts[1].strip()
            for line in header.splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    k = key.strip().lower()
                    if k in meta:
                        meta[k] = val.strip()

    return meta, prose.strip()

# ─── CLAUDE CODE CALL ─────────────────────────────────────────────────────────

def call_claude_code(npc_name, meta, prose, claude_path):
    prompt = f"""You are an NPC analyst for the Ironthorn dark fantasy RPG.
Read this character description and extract structured data.

NPC Name: {npc_name}
Tier hint: {meta.get('tier') or 'unknown'}
District hint: {meta.get('district') or 'unknown'}
Writer: {meta.get('writer') or 'unknown'}

Character description:
{prose}

Respond ONLY with a JSON object. No markdown, no explanation, just the JSON.

Use this exact structure:
{{
  "alignment_public": "e.g. Gray, Dark-II, Light-I",
  "alignment_true": "string",
  "alignment_confidence": "High or Medium or Low",
  "alignment_note": "why you inferred this",
  "tone_sentence": "one sentence, tired-not-broken vocabulary",
  "what_they_did_with_it": "concrete response to backstory, not the backstory itself",
  "faction_inferred": "string",
  "tier_suggested": 3,
  "attributes": {{
    "cunning":                  {{"value": 5, "confidence": "High", "note": "reason"}},
    "loyalty":                  {{"value": 5, "confidence": "High", "note": "reason"}},
    "fear":                     {{"value": 5, "confidence": "High", "note": "reason"}},
    "greed":                    {{"value": 5, "confidence": "High", "note": "reason"}},
    "idealism":                 {{"value": 5, "confidence": "High", "note": "reason"}},
    "cunning_ambition":         {{"value": 5, "confidence": "High", "note": "reason"}},
    "cunning_patience":         {{"value": 5, "confidence": "High", "note": "reason"}},
    "cunning_paranoia":         {{"value": 5, "confidence": "High", "note": "reason"}},
    "loyalty_devotion":         {{"value": 5, "confidence": "High", "note": "reason"}},
    "loyalty_resentment":       {{"value": 5, "confidence": "High", "note": "reason"}},
    "fear_desperation":         {{"value": 5, "confidence": "High", "note": "reason"}},
    "fear_suppression":         {{"value": 5, "confidence": "High", "note": "reason"}},
    "greed_appetite":           {{"value": 5, "confidence": "High", "note": "reason"}},
    "greed_restraint":          {{"value": 5, "confidence": "High", "note": "reason"}},
    "greed_envy":               {{"value": 5, "confidence": "High", "note": "reason"}},
    "idealism_conviction":      {{"value": 5, "confidence": "High", "note": "reason"}},
    "idealism_disillusionment": {{"value": 5, "confidence": "High", "note": "reason"}},
    "perception_threshold":     {{"value": 5, "confidence": "High", "note": "reason"}},
    "trust_score":              {{"value": 5, "confidence": "High", "note": "reason"}}
  }},
  "tells": {{
    "surface": "specific observable baseline behaviour or null",
    "surface_deviation": "what deviation signals or null",
    "mid": "specific observable shift at Perception 5-6 or null",
    "mid_state": "internal state that triggers it or null",
    "deep": "micro-signal at Perception 7+ or null",
    "deep_note": "additional context or null"
  }},
  "goals": {{
    "primary_tag": "single word e.g. freedom, order, power, truth",
    "primary_description": "string",
    "secondary_tag": "string or null",
    "secondary_description": "string or null",
    "hidden_tag": "string or null",
    "hidden_description": "string or null"
  }},
  "voice_notes": "vocabulary constraints, what they would NOT say",
  "decision_map_notes": "how this NPC reacts to a caught lie",
  "writer_notes": "open questions, gaps, things the writer needs to decide"
}}

Scoring: 1-3 Naive/Low, 4-6 Aware/Average, 7-9 Calculating/High, 10 Masterful
Tells: SPECIFIC OBSERVABLE BEHAVIOURS only — things a director gives to an actor, not emotions."""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(prompt)
        prompt_file = f.name

    try:
        result = subprocess.run(
            [claude_path, "--print", "--no-conversation", f"$(cat {prompt_file})"],
            capture_output=True, text=True, timeout=120, shell=False
        )
        if result.returncode != 0 or not result.stdout.strip():
            result = subprocess.run(
                [claude_path, "--print"],
                input=prompt, capture_output=True, text=True, timeout=120
            )

        output = result.stdout.strip()
        if not output:
            raise ValueError(f"Claude returned empty output. stderr: {result.stderr[:500]}")

        output = re.sub(r'^```json\s*', '', output, flags=re.MULTILINE)
        output = re.sub(r'\s*```\s*$', '', output, flags=re.MULTILINE)
        match = re.search(r'\{[\s\S]*\}', output)
        if match:
            return json.loads(match.group(0))
        else:
            raise ValueError(f"No JSON found in output: {output[:500]}")
    finally:
        os.unlink(prompt_file)

# ─── OUTPUT BUILDERS ──────────────────────────────────────────────────────────

def build_submission_form(npc_name, meta, d, threads, today):
    a = d.get("attributes", {})
    tier = meta.get("tier") or d.get("tier_suggested") or "—"
    writer = meta.get("writer") or "FILL IN"
    email = meta.get("email") or "FILL IN"
    district = meta.get("district") or d.get("faction_inferred") or "FILL IN"

    def sv(key):
        s = a.get(key, {})
        return f"{s.get('value','?')} [{s.get('confidence','?')} -- {s.get('note','?')}]"

    tells = d.get("tells", {})
    goals = d.get("goals", {})
    threads_str = "\n".join(f"  - {t}" for t in threads) if threads else "  None detected"

    return f"""---
doc_type: "Writer Certification"
module: 4
title: "NPC Submission Form -- PRE-FILLED BY INTAKE WATCHER v1.2"
npc_name: "{npc_name}"
generated: "{today}"
writer: "{writer}"
---

# NPC Submission Form -- {npc_name}
## Pre-filled by Intake Watcher v1.2 -- Review all fields before submitting

> [!warning] Pre-fill -- review everything
> LOW confidence stats are guesses. You know this character better than the operation does.

---

## Section 1 -- Writer and submission details

**Writer name:** {writer}
**Writer email:** {email}
**Quiz score:** FILL IN
**NPC name:** {npc_name}
**NPC tier:** {tier}
**Faction:** {d.get('faction_inferred', 'FILL IN')}
**District:** {district}
**Date submitted:** {today}
**Submission type:** New NPC
**Intake watcher:** Yes -- {today}

---

## Section 2 -- Tone certification

**2.1 -- Tone sentence:**
{d.get('tone_sentence', 'FILL IN')}
[Alignment confidence: {d.get('alignment_confidence','?')} -- {d.get('alignment_note','')}]

**2.2 -- What they did with it:**
{d.get('what_they_did_with_it', 'FILL IN')}

**2.3 -- Most dramatic dialogue line:**
FILL IN -- paste from your NPC file

**2.4 -- Can it be cut to half?**
FILL IN

**2.5 -- Monologues inner state?**
FILL IN -- Yes/No

---

## Section 3 -- Flags

liar_mark_active: false
debt_flag_active: false
trust_score: {sv('trust_score')}
leverage_held: false
secrets_known: []
faction_alert_sent: false

All flags at default -- no active flags at submission.

---

## Section 4 -- Tell verification

**Surface tell (Perception 0):**
{tells.get('surface') or 'FILL IN -- one thing this NPC always does in conversation'}
Deviation signals: {tells.get('surface_deviation') or 'FILL IN'}
Active in all scenes: FILL IN

**Mid tell (Perception 5-6):**
{tells.get('mid') or 'FILL IN -- specific shift from baseline'}
Fires when: {tells.get('mid_state') or 'FILL IN'}
Suppression score: {a.get('fear_suppression',{}).get('value','?')}

**Deep tell (Perception 7+):**
{tells.get('deep') or 'FILL IN -- also fires on lie-catch'}
Fires on lie-catch: Yes (required)
Bracketed stage direction: FILL IN -- [Perception 7+: ...]

Tell consistency check: FILL IN

---

## Section 5 -- Decision map (Tier 3+)

Alignment -- Public: {d.get('alignment_public','?')} / True: {d.get('alignment_true','?')}
{d.get('decision_map_notes', 'FILL IN')}

Cunning: {a.get('cunning',{}).get('value','?')} / Ambition: {a.get('cunning_ambition',{}).get('value','?')} / Patience: {a.get('cunning_patience',{}).get('value','?')} / Paranoia: {a.get('cunning_paranoia',{}).get('value','?')}

5.1 -- Survival check: FILL IN
5.2 -- Leverage check: FILL IN
5.3 -- Alignment filter: FILL IN
5.4 -- Cunning filter: FILL IN
5.5 -- Faction filter: FILL IN
5.6 -- In-world response line: FILL IN
5.7 -- Specific to this character: FILL IN

---

## Section 6 -- Voice

{d.get('voice_notes', 'FILL IN')}

6.1 -- Test dialogue lines (do NOT use in file):
Line 1: FILL IN
Line 2: FILL IN
Line 3: FILL IN

6.2 -- Vocabulary constraints: FILL IN
6.3 -- High-pressure dialogue: FILL IN
6.4 -- Simpler under pressure: FILL IN
6.5 -- Silence as stage direction: FILL IN

---

## Section 7 -- Cross-NPC connections

7.1 -- Connected NPCs: FILL IN
7.2 -- Perception vs suppression: FILL IN
7.3 -- NPC-NPC tell scenes: FILL IN
7.4 -- Shared goal tags:
  Primary: {goals.get('primary_tag','?')} / Hidden: {goals.get('hidden_tag') or 'none inferred'}

---

## Detected story thread connections

{threads_str}

---

## Section 8 -- Hidden agenda (Tier 4+)

{goals.get('hidden_description') or 'FILL IN -- not strongly implied in prose'}

8.2 -- Recontextualises interactions: FILL IN
8.3 -- In dialogue without earning: FILL IN
8.4 -- Exact reveal trigger: FILL IN

---

## Attribute pre-fill (review all)

| Attribute | Score | Confidence | Note |
|-----------|-------|------------|------|
| Cunning | {a.get('cunning',{}).get('value','?')} | {a.get('cunning',{}).get('confidence','?')} | {a.get('cunning',{}).get('note','?')} |
| Loyalty | {a.get('loyalty',{}).get('value','?')} | {a.get('loyalty',{}).get('confidence','?')} | {a.get('loyalty',{}).get('note','?')} |
| Fear | {a.get('fear',{}).get('value','?')} | {a.get('fear',{}).get('confidence','?')} | {a.get('fear',{}).get('note','?')} |
| Greed | {a.get('greed',{}).get('value','?')} | {a.get('greed',{}).get('confidence','?')} | {a.get('greed',{}).get('note','?')} |
| Idealism | {a.get('idealism',{}).get('value','?')} | {a.get('idealism',{}).get('confidence','?')} | {a.get('idealism',{}).get('note','?')} |
| Cunning -- Ambition | {a.get('cunning_ambition',{}).get('value','?')} | {a.get('cunning_ambition',{}).get('confidence','?')} | {a.get('cunning_ambition',{}).get('note','?')} |
| Cunning -- Patience | {a.get('cunning_patience',{}).get('value','?')} | {a.get('cunning_patience',{}).get('confidence','?')} | {a.get('cunning_patience',{}).get('note','?')} |
| Cunning -- Paranoia | {a.get('cunning_paranoia',{}).get('value','?')} | {a.get('cunning_paranoia',{}).get('confidence','?')} | {a.get('cunning_paranoia',{}).get('note','?')} |
| Loyalty -- Devotion | {a.get('loyalty_devotion',{}).get('value','?')} | {a.get('loyalty_devotion',{}).get('confidence','?')} | {a.get('loyalty_devotion',{}).get('note','?')} |
| Loyalty -- Resentment | {a.get('loyalty_resentment',{}).get('value','?')} | {a.get('loyalty_resentment',{}).get('confidence','?')} | {a.get('loyalty_resentment',{}).get('note','?')} |
| Fear -- Desperation | {a.get('fear_desperation',{}).get('value','?')} | {a.get('fear_desperation',{}).get('confidence','?')} | {a.get('fear_desperation',{}).get('note','?')} |
| Fear -- Suppression | {a.get('fear_suppression',{}).get('value','?')} | {a.get('fear_suppression',{}).get('confidence','?')} | {a.get('fear_suppression',{}).get('note','?')} |
| Greed -- Appetite | {a.get('greed_appetite',{}).get('value','?')} | {a.get('greed_appetite',{}).get('confidence','?')} | {a.get('greed_appetite',{}).get('note','?')} |
| Greed -- Restraint | {a.get('greed_restraint',{}).get('value','?')} | {a.get('greed_restraint',{}).get('confidence','?')} | {a.get('greed_restraint',{}).get('note','?')} |
| Greed -- Envy | {a.get('greed_envy',{}).get('value','?')} | {a.get('greed_envy',{}).get('confidence','?')} | {a.get('greed_envy',{}).get('note','?')} |
| Idealism -- Conviction | {a.get('idealism_conviction',{}).get('value','?')} | {a.get('idealism_conviction',{}).get('confidence','?')} | {a.get('idealism_conviction',{}).get('note','?')} |
| Idealism -- Disillusionment | {a.get('idealism_disillusionment',{}).get('value','?')} | {a.get('idealism_disillusionment',{}).get('confidence','?')} | {a.get('idealism_disillusionment',{}).get('note','?')} |
| Perception threshold | {a.get('perception_threshold',{}).get('value','?')} | {a.get('perception_threshold',{}).get('confidence','?')} | {a.get('perception_threshold',{}).get('note','?')} |
| Trust score | {a.get('trust_score',{}).get('value','?')} | {a.get('trust_score',{}).get('confidence','?')} | {a.get('trust_score',{}).get('note','?')} |

---

## Writer notes from intake watcher

{d.get('writer_notes', '')}

---

## Section 10 -- Writer declaration

**Writer signature:** FILL IN
**Date:** FILL IN

---

## Lead writer review *(lead writer only)*

Review date: -- / Tone: -- / Flags: -- / Tells: -- / Decision map: -- / Voice: -- / Overall: --
"""

def build_origin_story(npc_name, meta, prose, today):
    writer = meta.get("writer") or "Unknown"
    return f"""---
doc_type: "NPC Origin Story"
npc_name: "{npc_name}"
writer: "{writer}"
date: "{today}"
location: "NPCs/_Characters/{npc_name}/Notes/"
---

# {npc_name} -- Origin Story

*Written by {writer} / {today}*

---

{prose}

---

*Original prose submitted to Ironthorn NPC Intake Watcher on {today}. Preserved without modification.*
"""

def build_intake_doc(npc_name, meta, threads, today):
    writer = meta.get("writer") or "FILL IN"
    return f"""---
doc_type: "Submission Intake"
npc_name: "{npc_name}"
writer: "{writer}"
date: "{today}"
---

# Submission Intake -- {npc_name}

**Writer:** {writer}
**Email:** {meta.get('email') or 'FILL IN'}
**NPC:** {npc_name}
**Tier:** {meta.get('tier') or 'FILL IN'}
**District:** {meta.get('district') or 'FILL IN'}
**Date:** {today}
**Intake watcher:** Yes -- processed {today}

**Files included:**
- [x] NPC description (processed by intake watcher)
- [ ] NPC file (build from NPC-Template-v3.md)
- [x] Submission Form (pre-filled)
- [x] Origin Story (saved to Notes/)

**Detected story threads:**
{chr(10).join('- ' + t for t in threads) if threads else '- None detected'}

**Next steps:**
1. Build full NPC file using NPC-Template-v3.md
2. Review and complete the pre-filled submission form
3. Email stephenbrentjenkins@gmail.com
   Subject: [NPC SUBMISSION] {npc_name} -- {writer} -- {today}
"""

# ─── PROCESS ONE FILE ─────────────────────────────────────────────────────────

def process_file(filepath, claude_path):
    path = Path(filepath)
    npc_name = path.stem
    today = date.today().strftime("%Y-%m-%d")

    print(f"\n{'='*50}")
    print(f"Processing: {npc_name}")
    print(f"{'='*50}")

    meta, prose = parse_intake_file(filepath)
    if not prose or len(prose) < 30:
        print(f"  ERROR: Too little prose -- skipping")
        return False

    print(f"  Prose: {len(prose)} characters")
    print(f"  Writer: {meta.get('writer') or 'not specified'}")

    threads = detect_threads(prose + " " + meta.get("district",""))
    if threads:
        print(f"  Story threads: {', '.join(threads)}")
    else:
        print(f"  No story thread connections detected")

    print(f"  Calling Claude Code...")
    try:
        d = call_claude_code(npc_name, meta, prose, claude_path)
        print(f"  Alignment: {d.get('alignment_public')} / {d.get('alignment_true')} ({d.get('alignment_confidence')})")
        print(f"  Tone: {d.get('tone_sentence','')[:80]}...")
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

    pending_folder = PENDING_DIR / npc_name
    pending_folder.mkdir(exist_ok=True)
    char_folder = CHARS_DIR / npc_name
    for sub in ["Versions", "Submissions", "Dialogue", "Notes"]:
        (char_folder / sub).mkdir(parents=True, exist_ok=True)

    (pending_folder / f"{npc_name}_Submission-Form.md").write_text(
        build_submission_form(npc_name, meta, d, threads, today), encoding="utf-8")
    (pending_folder / f"{npc_name}_Submission-Intake.md").write_text(
        build_intake_doc(npc_name, meta, threads, today), encoding="utf-8")
    (char_folder / "Notes" / f"{npc_name}_Origin-Story.md").write_text(
        build_origin_story(npc_name, meta, prose, today), encoding="utf-8")

    print(f"  Output: {pending_folder}")
    print(f"  Origin: {char_folder / 'Notes'}")

    done_dir = INTAKE_DIR / "_Done"
    done_dir.mkdir(exist_ok=True)
    shutil.move(str(filepath), str(done_dir / path.name))
    print(f"  Moved to _Intake/_Done/")
    print(f"  DONE: {npc_name}")
    return True

# ─── WATCHER LOOP ─────────────────────────────────────────────────────────────

def watch():
    claude_path = find_claude()
    if not claude_path:
        print("ERROR: Claude Code CLI not found.")
        print("Run: npm install -g @anthropic-ai/claude-code")
        input("Press Enter to exit...")
        return

    print("=" * 50)
    print("  Ironthorn NPC Intake Watcher v1.2")
    print(f"  Claude: {claude_path}")
    print(f"  Watching: {INTAKE_DIR}")
    print(f"  Poll: every {POLL_INTERVAL}s")
    print("  Drop .txt or .md files named after the NPC")
    print("  Ctrl+C to stop")
    print("=" * 50)

    seen = set()
    while True:
        try:
            for fname in os.listdir(INTAKE_DIR):
                # Skip hidden files, underscore-prefixed folders/files
                if fname.startswith(".") or fname.startswith("_"):
                    continue
                # Skip README and instruction files
                if fname.lower() in EXCLUDED_FILENAMES:
                    continue
                # Only process .md and .txt
                if not (fname.endswith(".md") or fname.endswith(".txt")):
                    continue
                fpath = INTAKE_DIR / fname
                if str(fpath) in seen:
                    continue
                time.sleep(1)
                if not fpath.exists():
                    continue
                seen.add(str(fpath))
                try:
                    process_file(fpath, claude_path)
                except Exception as e:
                    print(f"  ERROR: {e}")
            time.sleep(POLL_INTERVAL)
        except KeyboardInterrupt:
            print("\nWatcher stopped.")
            break

if __name__ == "__main__":
    watch()
