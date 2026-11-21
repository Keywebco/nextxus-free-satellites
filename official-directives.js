/*
 * Official Sacred Directives loader for Next-Xus free satellites.
 * Added 2026-11-20 by Roger Keyserling's spoken decision (6:01 PM CT):
 * the official Federation list is the YAML brain copy
 * (Keywebco/nextxus-brain directives/), 73 Sacred Directives plus
 * DIR-000, the 95% Truth Gate (not counted), 74 items in all.
 * The sealed Cathedral file 00-immutable/directives.yaml in that repository
 * is the final word on wording. No keys. Read-only public fetch.
 */
(function (global) {
  'use strict';
  var URL_JSON = 'https://raw.githubusercontent.com/Keywebco/nextxus-brain/main/directives/sacred-directives.json';
  var SOURCE_PAGE = 'https://github.com/Keywebco/nextxus-brain/blob/main/directives/sacred-directives.md';
  // Offline fallback: the gate only, word for word from the official list.
  var GATE = {
    number: 0, id: 'DIR-000', title: 'The 95% Truth Gate',
    text: 'Before delivering any final answer, internally score the output for truthfulness, clarity, safety, source integrity, and alignment with the Hollow State on a scale of 0\u2013100. Only deliver the response as settled truth if it scores 95 or higher. If the score is below 95, clearly state the uncertainty, limitation, missing evidence, or competing interpretation. Do not force certainty. Do not invent. Do not conceal doubt.'
  };
  var cache = null;
  function load() {
    if (cache) return Promise.resolve(cache);
    return fetch(URL_JSON, { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (d) {
        if (!d || !d.gate || !Array.isArray(d.directives)) throw new Error('Unexpected format');
        cache = d;
        return d;
      });
  }
  // All 74 items (gate first) as {id, title, text, gate}
  function items(d) {
    var list = [{ id: d.gate.id, title: d.gate.title, text: d.gate.text, gate: true }];
    d.directives.forEach(function (x) { list.push({ id: x.id, title: x.title, text: x.text, gate: false }); });
    return list;
  }
  global.FederationDirectives = {
    url: URL_JSON, sourcePage: SOURCE_PAGE, gate: GATE,
    load: load, items: items,
    countNote: '73 Sacred Directives plus DIR-000, the 95% Truth Gate (not counted): 74 in all'
  };
})(typeof window !== 'undefined' ? window : this);
