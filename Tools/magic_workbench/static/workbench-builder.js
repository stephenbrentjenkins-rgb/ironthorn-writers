/*
 * Magic Workbench — Practitioner Builder client
 * ==============================================
 * Drives the form's live behavior:
 *   - Slug preview as the name is typed
 *   - Filters faction credentials by tradition
 *   - Suggests cost channel from preferred mapping
 *   - Reference panel updates on tradition select
 *   - Embrace flag enables/disables embrace depth slider
 *   - Magic block dims when "this NPC is a practitioner" is unchecked
 *   - Preview and Submit hit the server endpoints
 *
 * No external dependencies. Vanilla JS. Loaded with defer.
 */

(function () {
  "use strict";

  // Only run on the practitioner page.
  if (!document.getElementById("pb-form")) return;

  let constants = null;

  // ─── Helpers ────────────────────────────────────────────────────

  function $(id) { return document.getElementById(id); }

  function slugify(name) {
    return (name || "")
      .trim()
      .replace(/[^\w\s-]/g, "")
      .replace(/\s+/g, "-")
      .replace(/-+/g, "-")
      .replace(/^-|-$/g, "");
  }

  function setHint(el, text, kind) {
    if (!el) return;
    el.textContent = text;
    el.classList.remove("wb-hint-warn", "wb-hint-error", "wb-hint-good");
    if (kind === "warn") el.classList.add("wb-hint-warn");
    else if (kind === "error") el.classList.add("wb-hint-error");
    else if (kind === "good") el.classList.add("wb-hint-good");
  }

  function collectFormData() {
    const form = $("pb-form");
    const data = {};
    Array.from(form.elements).forEach(function (el) {
      if (!el.name) return;
      if (el.type === "checkbox") {
        data[el.name] = el.checked;
      } else if (el.type === "number" || el.type === "range") {
        data[el.name] = parseInt(el.value, 10);
      } else {
        data[el.name] = el.value;
      }
    });
    return data;
  }

  function renderMessages(targetEl, errors, warnings, success) {
    targetEl.innerHTML = "";
    if (success) {
      const div = document.createElement("div");
      div.className = "wb-msg wb-msg-success";
      div.textContent = success;
      targetEl.appendChild(div);
    }
    (errors || []).forEach(function (msg) {
      const div = document.createElement("div");
      div.className = "wb-msg wb-msg-error";
      div.textContent = msg;
      targetEl.appendChild(div);
    });
    (warnings || []).forEach(function (msg) {
      const div = document.createElement("div");
      div.className = "wb-msg wb-msg-warn";
      div.textContent = msg;
      targetEl.appendChild(div);
    });
  }

  // ─── Slug preview ───────────────────────────────────────────────

  $("pb-npc-name").addEventListener("input", function () {
    const slug = slugify(this.value);
    const hint = $("pb-slug-hint");
    if (!slug) {
      hint.innerHTML = "Slug: <code>—</code>";
    } else {
      hint.innerHTML = "Slug: <code>" + slug + "</code> · file: <code>NPCs/_Pending/" + slug + "/" + slug + ".md</code>";
    }
  });

  // ─── Tradition → faction credential filter ──────────────────────

  function updateCredentialOptions() {
    if (!constants) return;
    const tradition = $("pb-tradition").value;
    const credSelect = $("pb-faction-credential");
    const hint = $("pb-credential-hint");

    credSelect.innerHTML = "";

    if (!tradition) {
      const opt = document.createElement("option");
      opt.value = "";
      opt.textContent = "— select tradition first —";
      credSelect.appendChild(opt);
      hint.textContent = "";
      return;
    }

    const valid = constants.valid_tradition_credential[tradition] || [];
    const placeholder = document.createElement("option");
    placeholder.value = "";
    placeholder.textContent = "— select —";
    credSelect.appendChild(placeholder);

    valid.forEach(function (cred) {
      const opt = document.createElement("option");
      opt.value = cred;
      opt.textContent = cred;
      credSelect.appendChild(opt);
    });

    setHint(hint, "Valid credentials for " + tradition + ": " + valid.join(", "), "good");
  }

  // ─── Tradition → preferred cost channel suggestion ──────────────

  function updateChannelHint() {
    if (!constants) return;
    const tradition = $("pb-tradition").value;
    const channel = $("pb-cost-channel").value;
    const hint = $("pb-channel-hint");

    if (!tradition || !channel) {
      setHint(hint, "", null);
      return;
    }

    const preferred = constants.preferred_channel[tradition];
    if (!preferred) {
      setHint(hint, "", null);
      return;
    }

    if (channel === preferred) {
      setHint(hint, "Preferred channel for " + tradition + ".", "good");
    } else {
      setHint(hint, "Non-preferred: " + tradition + " normally channels through " + preferred + ". Allowed but corrupts faster — justify in writer's notes.", "warn");
    }
  }

  // ─── Tradition → reference panel ────────────────────────────────

  function updateReferencePanel() {
    if (!constants) return;
    const tradition = $("pb-tradition").value;
    const content = $("pb-ref-content");

    if (!tradition) {
      content.innerHTML = '<p class="wb-hint">Select a tradition to see its profile.</p>';
      return;
    }

    const valid = constants.valid_tradition_credential[tradition] || [];
    const preferred = constants.preferred_channel[tradition] || "—";

    // Tradition descriptions — keep them tight; the doc is the canonical source
    const descriptions = {
      "Holy": "Sanctification, blessing, healing in the religious mode, binding of corruption, light as substance.",
      "Unholy": "Curses, profanation, blight, binding of the holy, dark as substance. Shares hidden origin with Holy.",
      "Nature-Plant": "Growth, decay, the bodies of plants. Verdant Circle's urban branch.",
      "Nature-Animal": "Bodies and minds of non-human animals. Verdant Circle's rural branch.",
      "Elemental-Fire": "Fire as workable substance. Military (Dominion) or civilian (Compact).",
      "Elemental-Water": "Water as workable substance. Wells, currents, infrastructure.",
      "Elemental-Air": "Air as workable substance. Currents, voice-carrying, weather edge.",
      "Elemental-Ice": "Ice as workable substance. Cold as material, preservation.",
      "Mental": "Thought, memory, perception, intent. Compact-credentialled; world reads it as invasive.",
      "Time": "Causality, duration, sequence. Rarest tradition. Compact-only credential. Decades to learn.",
    };

    const sanctionInfo = {
      "Holy": "Aureate is sanctioned/dominant. Heretic-class is unsanctioned and rumored.",
      "Unholy": "Crimson Throne is tolerated. Ashen Veil is unsanctioned and hunted.",
      "Mental": "Sanctioned through Compact guild. Disdained by Iron Dominion.",
      "Time": "Sanctioned through Compact only. Extremely rare.",
    };

    content.innerHTML =
      '<div class="wb-ref-section">' +
        '<div class="wb-ref-label">Domain</div>' +
        '<div class="wb-ref-value">' + (descriptions[tradition] || "—") + '</div>' +
      '</div>' +
      '<div class="wb-ref-section">' +
        '<div class="wb-ref-label">Valid credentials</div>' +
        '<ul class="wb-ref-list">' + valid.map(function (v) { return '<li>' + v + '</li>'; }).join("") + '</ul>' +
      '</div>' +
      '<div class="wb-ref-section">' +
        '<div class="wb-ref-label">Preferred cost channel</div>' +
        '<div class="wb-ref-value">' + preferred + '</div>' +
      '</div>' +
      (sanctionInfo[tradition] ? (
        '<div class="wb-ref-section">' +
          '<div class="wb-ref-label">Sanction notes</div>' +
          '<div class="wb-ref-value">' + sanctionInfo[tradition] + '</div>' +
        '</div>'
      ) : "");
  }

  // ─── Slider readouts ────────────────────────────────────────────

  function wireSlider(sliderId, readoutId, extraFn) {
    const slider = $(sliderId);
    const readout = $(readoutId);
    if (!slider || !readout) return;
    function update() {
      readout.textContent = slider.value;
      if (extraFn) extraFn(parseInt(slider.value, 10));
    }
    slider.addEventListener("input", update);
    update();
  }

  // ─── Corruption level hint ──────────────────────────────────────

  function corruptionHint(level) {
    const hint = $("pb-corruption-hint");
    if (!hint) return;
    if (level === 0) setHint(hint, "Clean", "good");
    else if (level <= 3) setHint(hint, "Lightly corrupted", null);
    else if (level <= 7) setHint(hint, "Heavily corrupted — visible in body, mind, or conduct", "warn");
    else setHint(hint, "Approaching embrace decision point", "warn");
  }

  // ─── Practitioner checkbox → magic block enable/disable ─────────

  function updatePractitionerState() {
    const checked = $("pb-magical-practice").checked;
    const block = $("pb-magic-block");
    if (checked) {
      block.classList.remove("wb-collapsed");
      // Re-enable inputs
      block.querySelectorAll("select, input, textarea").forEach(function (el) {
        if (el.id !== "pb-embrace-depth") el.disabled = false;
      });
      // Embrace depth follows the embraced checkbox
      $("pb-embrace-depth").disabled = !$("pb-embraced").checked;
    } else {
      block.classList.add("wb-collapsed");
      block.querySelectorAll("select, input, textarea").forEach(function (el) {
        el.disabled = true;
      });
    }
  }

  // ─── Embrace checkbox → depth slider enable/disable ─────────────

  function updateEmbraceState() {
    const checked = $("pb-embraced").checked;
    $("pb-embrace-depth").disabled = !checked;
    if (!checked) {
      $("pb-embrace-depth").value = 0;
      $("pb-embrace-readout").textContent = "0";
    }
  }

  // ─── Preview ────────────────────────────────────────────────────

  async function doPreview() {
    const data = collectFormData();
    const out = $("pb-validation-out");
    const previewPanel = $("pb-preview-panel");
    const previewOut = $("pb-preview-out");
    const btn = $("pb-preview-btn");

    btn.disabled = true;
    btn.textContent = "Building...";

    try {
      const res = await fetch("/api/practitioner/preview", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const result = await res.json();

      renderMessages(out, result.errors, result.warnings, result.ok ? "Preview ready — see right panel." : null);

      if (result.ok && result.markdown) {
        previewOut.textContent = result.markdown;
        previewPanel.style.display = "block";
      } else {
        previewPanel.style.display = "none";
      }
    } catch (e) {
      renderMessages(out, ["Preview failed: " + e.message], [], null);
    } finally {
      btn.disabled = false;
      btn.textContent = "Preview";
    }
  }

  // ─── Submit ─────────────────────────────────────────────────────

  async function doSubmit() {
    const data = collectFormData();
    const out = $("pb-validation-out");
    const btn = $("pb-submit-btn");

    btn.disabled = true;
    btn.textContent = "Submitting...";

    try {
      const res = await fetch("/api/practitioner/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const result = await res.json();

      if (result.ok) {
        const successMsg = "Submitted. File written to " + result.relative_path + ". The intake watcher will pick it up.";
        renderMessages(out, [], result.warnings, successMsg);
        btn.textContent = "✓ Submitted";
        // Don't re-enable; force a page reload for a fresh form
        setTimeout(function () { btn.textContent = "Submit another"; btn.disabled = false; }, 2000);
      } else {
        renderMessages(out, result.errors, result.warnings, null);
        btn.disabled = false;
        btn.textContent = "Submit to vault";
      }
    } catch (e) {
      renderMessages(out, ["Submit failed: " + e.message], [], null);
      btn.disabled = false;
      btn.textContent = "Submit to vault";
    }
  }

  // ─── Initial load ───────────────────────────────────────────────

  async function init() {
    try {
      const res = await fetch("/api/magic-constants");
      constants = await res.json();
    } catch (e) {
      console.error("Failed to load magic constants:", e);
      return;
    }

    // Wire all event listeners

    $("pb-tradition").addEventListener("change", function () {
      updateCredentialOptions();
      updateChannelHint();
      updateReferencePanel();
    });

    $("pb-cost-channel").addEventListener("change", updateChannelHint);

    $("pb-magical-practice").addEventListener("change", updatePractitionerState);
    $("pb-embraced").addEventListener("change", updateEmbraceState);

    wireSlider("pb-corruption-level", "pb-corruption-readout", corruptionHint);
    wireSlider("pb-embrace-depth", "pb-embrace-readout");
    wireSlider("pb-cunning", "pb-cunning-readout");
    wireSlider("pb-loyalty", "pb-loyalty-readout");
    wireSlider("pb-fear", "pb-fear-readout");
    wireSlider("pb-greed", "pb-greed-readout");
    wireSlider("pb-idealism", "pb-idealism-readout");
    wireSlider("pb-perception", "pb-perception-readout");

    $("pb-preview-btn").addEventListener("click", doPreview);
    $("pb-submit-btn").addEventListener("click", doSubmit);

    // Initial state
    updatePractitionerState();
    updateEmbraceState();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
