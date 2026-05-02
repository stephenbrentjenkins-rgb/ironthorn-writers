// ============================================================
// Ironthorn Writer Portal v4.0
// Google Apps Script — HTML Service
// Single page app: Login, Welcome, Primer, Quiz, Sketch, Dossier
// Persistent writer certification via Google Sheets
// ============================================================

var SHEET_ID = '1WO2e70KJ9USmKL3pEvzYzYxzCrxPNnCa7Ux4Q_bWEv4';

var SHEET_HEADERS = [
  'Timestamp', 'Status', 'Priority', 'Writer Name', 'Writer Email',
  'NPC Name', 'NPC Tier', 'Faction', 'District', 'Alignment Public', 'Alignment True',
  'Cunning', 'Loyalty', 'Fear', 'Greed', 'Idealism',
  'Cunning Ambition', 'Cunning Patience', 'Cunning Paranoia',
  'Loyalty Devotion', 'Loyalty Resentment',
  'Fear Desperation', 'Fear Suppression',
  'Greed Appetite', 'Greed Restraint', 'Greed Envy',
  'Idealism Conviction', 'Idealism Disillusionment',
  'Perception Threshold', 'Trust Score',
  'Goal Primary', 'Goal Secondary', 'Goal Hidden',
  'Surface Tell', 'Mid Tell', 'Deep Tell',
  'Tone Sentence', 'What They Did With It',
  'Voice Notes', 'Decision Map Notes',
  'The Sketch (Original Prose)',
  'Tone Cert 2.1', 'Tone Cert 2.2', 'Tone Cert 2.3', 'Tone Cert 2.4', 'Tone Cert 2.5',
  'Tell Verification', 'Decision Map', 'Voice Verification',
  'Writer Declaration', 'AI Prefill Confidence',
  'Lead Writer Notes', 'Return Codes'
];

// ── SERVE THE PAGE ────────────────────────────────────────────

function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Ironthorn — Writer Portal')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// ── WRITER CERTIFICATION ──────────────────────────────────────

function checkWriterCertification(email) {
  if (!email || email.indexOf('@') < 0) {
    return { certified: false, error: 'Please enter a valid email address.' };
  }
  email = email.toLowerCase().trim();
  try {
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var certSheet = getCertSheet(ss);
    var data = certSheet.getDataRange().getValues();
    for (var i = 1; i < data.length; i++) {
      if (data[i][0] && data[i][0].toString().toLowerCase().trim() === email) {
        return {
          certified: true,
          name: data[i][1] || '',
          score: data[i][2] || '',
          date: data[i][3] || ''
        };
      }
    }
    return { certified: false };
  } catch(err) {
    return { certified: false, error: err.toString() };
  }
}

function certifyWriter(email, name, score) {
  if (!email || email.indexOf('@') < 0) { return { success: false, error: 'Invalid email.' }; }
  email = email.toLowerCase().trim();
  try {
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var certSheet = getCertSheet(ss);
    // Check not already certified
    var data = certSheet.getDataRange().getValues();
    for (var i = 1; i < data.length; i++) {
      if (data[i][0] && data[i][0].toString().toLowerCase().trim() === email) {
        return { success: true, alreadyCertified: true };
      }
    }
    certSheet.appendRow([
      email, name || '', score || '', new Date().toISOString(), 'Quiz'
    ]);
    return { success: true };
  } catch(err) {
    return { success: false, error: err.toString() };
  }
}

function getCertSheet(ss) {
  var sheets = ss.getSheets();
  for (var i = 0; i < sheets.length; i++) {
    if (sheets[i].getName() === 'Certified Writers') { return sheets[i]; }
  }
  // Create it
  var sheet = ss.insertSheet('Certified Writers');
  sheet.appendRow(['Email', 'Name', 'Quiz Score', 'Certified Date', 'Method']);
  sheet.setFrozenRows(1);
  var h = sheet.getRange(1, 1, 1, 5);
  h.setBackground('#2c2820');
  h.setFontColor('#c49a2a');
  h.setFontWeight('bold');
  sheet.setColumnWidth(1, 200);
  sheet.setColumnWidth(2, 150);
  return sheet;
}

// ── AI PREFILL ────────────────────────────────────────────────

function prefillFromProse(prose, npcName, tier, district, writer) {
  if (!prose || prose.length < 20) { return { error: 'Description too short.' }; }
  var apiKey = PropertiesService.getScriptProperties().getProperty('ANTHROPIC_API_KEY');
  if (!apiKey) { return { error: 'ANTHROPIC_API_KEY not set in Script Properties.' }; }

  var systemPrompt =
    'You are an NPC analyst for the Ironthorn dark fantasy RPG.\n' +
    'Read a character description and extract structured data to pre-fill a submission form.\n' +
    'Scoring: 1-3 Low, 4-6 Average, 7-9 High, 10 Masterful.\n' +
    'Tone: tired, not broken. Every NPC made choices and lives with them.\n' +
    'For tells: SPECIFIC OBSERVABLE BEHAVIOURS only.\n' +
    'Respond ONLY with valid JSON. No markdown. No explanation.\n' +
    '{"alignment_public":"Gray","alignment_true":"Gray","alignment_confidence":"High",' +
    '"alignment_note":"reason","tone_sentence":"one sentence",' +
    '"what_they_did_with_it":"concrete action not backstory",' +
    '"faction_inferred":"string","tier_suggested":3,' +
    '"attributes":{' +
    '"cunning":{"value":5,"confidence":"High","note":"reason"},' +
    '"loyalty":{"value":5,"confidence":"High","note":"reason"},' +
    '"fear":{"value":5,"confidence":"High","note":"reason"},' +
    '"greed":{"value":5,"confidence":"High","note":"reason"},' +
    '"idealism":{"value":5,"confidence":"High","note":"reason"},' +
    '"cunning_ambition":{"value":5,"confidence":"High","note":"reason"},' +
    '"cunning_patience":{"value":5,"confidence":"High","note":"reason"},' +
    '"cunning_paranoia":{"value":5,"confidence":"High","note":"reason"},' +
    '"loyalty_devotion":{"value":5,"confidence":"High","note":"reason"},' +
    '"loyalty_resentment":{"value":5,"confidence":"High","note":"reason"},' +
    '"fear_desperation":{"value":5,"confidence":"High","note":"reason"},' +
    '"fear_suppression":{"value":5,"confidence":"High","note":"reason"},' +
    '"greed_appetite":{"value":5,"confidence":"High","note":"reason"},' +
    '"greed_restraint":{"value":5,"confidence":"High","note":"reason"},' +
    '"greed_envy":{"value":5,"confidence":"High","note":"reason"},' +
    '"idealism_conviction":{"value":5,"confidence":"High","note":"reason"},' +
    '"idealism_disillusionment":{"value":5,"confidence":"High","note":"reason"},' +
    '"perception_threshold":{"value":5,"confidence":"High","note":"reason"},' +
    '"trust_score":{"value":5,"confidence":"High","note":"reason"}},' +
    '"tells":{"surface":"string or null","surface_deviation":"string or null",' +
    '"mid":"string or null","mid_state":"string or null",' +
    '"deep":"string or null","deep_note":"string or null"},' +
    '"goals":{"primary_tag":"string","primary_description":"string",' +
    '"secondary_tag":"string or null","hidden_tag":"string or null",' +
    '"hidden_description":"string or null"},' +
    '"voice_notes":"string","decision_map_notes":"string","writer_notes":"string",' +
    '"story_threads":["matching names from: The Auditors Defection, The Energy Source, ' +
    'The Forge and the Building, The Dead-Drop and the Missing Agent, ' +
    'The Debt That Doesnt Clear, Torven in the Confession Chair, ' +
    'The Certificate, What Rynn Saw in the Hollows"]}';

  var userMsg = 'NPC: ' + npcName + ' | Tier: ' + (tier || '?') +
    ' | District: ' + (district || '?') + ' | Writer: ' + (writer || '?') +
    '\n\nCharacter description:\n\n' + prose;

  var resp = UrlFetchApp.fetch('https://api.anthropic.com/v1/messages', {
    method: 'post', contentType: 'application/json',
    headers: { 'x-api-key': apiKey, 'anthropic-version': '2023-06-01' },
    payload: JSON.stringify({
      model: 'claude-sonnet-4-5', max_tokens: 4000,
      system: systemPrompt, messages: [{ role: 'user', content: userMsg }]
    }),
    muteHttpExceptions: true
  });

  var rd = JSON.parse(resp.getContentText());
  if (rd.error) { return { error: rd.error.message || JSON.stringify(rd.error) }; }
  var text = rd.content[0].text.trim().replace(/^```json\n?/, '').replace(/\n?```$/, '');
  var m = text.match(/\{[\s\S]*\}/);
  var parsed = JSON.parse(m ? m[0] : text);
  return { success: true, data: parsed };
}

// ── SUBMISSION ────────────────────────────────────────────────

function submitNPC(payload) {
  try {
    ensureSheetHeaders();
    var sheet = SpreadsheetApp.openById(SHEET_ID).getSheets()[0];
    var d = payload.data || {};
    var a = d.attributes || {};
    var t = d.tells || {};
    var g = d.goals || {};
    function av(k) { return (a[k] || {}).value || ''; }

    sheet.appendRow([
      new Date().toISOString(), 'New', '',
      payload.writerName || '', payload.writerEmail || '',
      payload.npcName || '', payload.npcTier || d.tier_suggested || '',
      d.faction_inferred || payload.faction || '', payload.district || '',
      d.alignment_public || '', d.alignment_true || '',
      av('cunning'), av('loyalty'), av('fear'), av('greed'), av('idealism'),
      av('cunning_ambition'), av('cunning_patience'), av('cunning_paranoia'),
      av('loyalty_devotion'), av('loyalty_resentment'),
      av('fear_desperation'), av('fear_suppression'),
      av('greed_appetite'), av('greed_restraint'), av('greed_envy'),
      av('idealism_conviction'), av('idealism_disillusionment'),
      av('perception_threshold'), av('trust_score') || 5,
      g.primary_tag || '', g.secondary_tag || '', g.hidden_tag || '',
      t.surface || '', t.mid || '', t.deep || '',
      d.tone_sentence || '', d.what_they_did_with_it || '',
      d.voice_notes || '', d.decision_map_notes || '',
      payload.prose || '',
      payload.tone_21 || '', payload.tone_22 || '', payload.tone_23 || '',
      payload.tone_24 || '', payload.tone_25 || '',
      payload.tell_verification || '', payload.decision_map || '',
      payload.voice_verification || '', payload.writer_declaration || '',
      payload.ai_confidence || '', '', ''
    ]);
    sheet.getRange(sheet.getLastRow(), 2).setBackground('#fff2cc');
    return { success: true };
  } catch(err) { return { error: err.toString() }; }
}

// ── SHEET SETUP ───────────────────────────────────────────────

function ensureSheetHeaders() {
  var sheet = SpreadsheetApp.openById(SHEET_ID).getSheets()[0];
  if (sheet.getLastRow() > 0) { return; }
  sheet.appendRow(SHEET_HEADERS);
  sheet.setFrozenRows(1);
  var h = sheet.getRange(1, 1, 1, SHEET_HEADERS.length);
  h.setBackground('#2c2820'); h.setFontColor('#c49a2a'); h.setFontWeight('bold');
  sheet.setName('Submissions');
  sheet.setColumnWidth(1, 160); sheet.setColumnWidth(4, 140);
  sheet.setColumnWidth(5, 200); sheet.setColumnWidth(6, 160);
  sheet.setColumnWidth(40, 300);
  sheet.getRange(2, 2, 1000, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList(['New','Under Review','Approved','Returned','Priority'], true).build());
}

function setupSheet() { ensureSheetHeaders(); Logger.log('Done.'); }
