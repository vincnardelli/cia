/* verifica.js — logica della pagina lab: editor, esecuzione, test, diagnosi a regole, stato.
   L'esecuzione vera è delegata al runner (runner-webr.js) che espone window.CBDRunner
   con:  ready (Promise), run(code) -> {output, error}, evalTests(code, tests, opts) -> [{obtained, error}]   */
(function () {
  const root = document.querySelector('.lab[data-lab]');
  if (!root) return;

  const slug = root.dataset.lab;
  const outputVar = root.dataset.output;
  const tolerance = parseFloat(root.dataset.tolerance || '0.01');
  const tests = JSON.parse(root.querySelector('[data-lab-tests]').textContent || '[]');
  const inputs = JSON.parse(root.querySelector('[data-lab-inputs]').textContent || '[]');
  const editor = root.querySelector('[data-editor]');
  const consoleEl = root.querySelector('[data-console]');
  const results = root.querySelector('[data-results]');
  const summary = root.querySelector('[data-results-summary]');
  const body = root.querySelector('[data-results-body]');
  const hintEl = root.querySelector('[data-hint]');
  const statusEl = root.querySelector('[data-lab-status]');
  const solution = root.querySelector('[data-solution]');
  const skeleton = root.querySelector('[data-lab-skeleton]').value;

  /* ── editor: ripristino contenuto, tab, salvataggio ── */
  const saved = CBD.code(slug);
  if (saved) editor.value = saved;
  editor.addEventListener('input', () => CBD.setCode(slug, editor.value));
  editor.addEventListener('keydown', e => {
    if (e.key === 'Tab') { e.preventDefault(); const s = editor.selectionStart; editor.setRangeText('  ', s, editor.selectionEnd, 'end'); }
  });
  root.querySelector('[data-reset]').addEventListener('click', () => { if (confirm('Ripristino lo scheletro iniziale? Il tuo codice andrà perso.')) { editor.value = skeleton; CBD.setCode(slug, skeleton); } });

  /* ── stato iniziale ── */
  let attempts = (CBD.progress()[slug] || {}).attempts || 0;
  paintStatus();
  maybeUnlockSolution();

  function paintStatus() {
    const p = CBD.progress()[slug];
    if (!p) { statusEl.textContent = 'non iniziato'; statusEl.classList.remove('is-done'); return; }
    if (p.done) { statusEl.textContent = 'superato'; statusEl.classList.add('is-done'); }
    else { statusEl.textContent = p.passed + '/' + p.total + ' test'; statusEl.classList.remove('is-done'); }
  }
  function maybeUnlockSolution() {
    if (!solution) return;
    const p = CBD.progress()[slug] || {};
    const after = root.dataset.solutionAfter;
    const dateOk = after && new Date(after) < new Date();
    if (p.done || (root.dataset.level === 'base' && dateOk)) solution.hidden = false;
  }

  /* ── esegui ── */
  root.querySelector('[data-run]').addEventListener('click', async () => {
    showConsole('… eseguo');
    try {
      await CBDRunner.ready;
      const r = await CBDRunner.run(editor.value);
      showConsole(r.error ? r.error : (r.output || '(nessun output: usa print() per vedere un valore)'), !!r.error);
    } catch (e) { showConsole('Errore del runtime: ' + e, true); }
  });
  function showConsole(txt, isErr) { consoleEl.hidden = false; consoleEl.textContent = txt; consoleEl.classList.toggle('is-error', !!isErr); }

  /* ── verifica ── */
  root.querySelector('[data-verify]').addEventListener('click', async () => {
    results.hidden = false; summary.textContent = '… eseguo i test'; summary.className = 'results__summary'; body.innerHTML = ''; hintEl.hidden = true;
    let out;
    try {
      await CBDRunner.ready;
      out = await CBDRunner.evalTests(editor.value, tests, { outputVar, fn: root.dataset.function || null, inputs: inputs.map(i => i.name) });
    } catch (e) { summary.textContent = 'Errore del runtime: ' + e; summary.classList.add('is-ko'); return; }
    attempts++;
    const rows = tests.map((t, i) => {
      const o = out[i] || {};
      const ok = !o.error && compare(t.expected, o.obtained);
      return { t, o, ok, i };
    });
    const passed = rows.filter(r => r.ok).length;
    renderRows(rows);
    summary.textContent = passed === tests.length ? `Tutti i ${tests.length} casi superati.` : `${passed} casi su ${tests.length} superati.`;
    summary.classList.add(passed === tests.length ? 'is-ok' : 'is-ko');
    CBD.setProgress(slug, { passed, total: tests.length, done: passed === tests.length, attempts });
    paintStatus(); maybeUnlockSolution();
    if (passed < tests.length) showHint(diagnose(rows));
  });

  function compare(expected, obtained) {
    if (obtained === null || obtained === undefined) return false;
    if (typeof expected === 'number') { const n = parseFloat(String(obtained).replace(',', '.')); return isFinite(n) && Math.abs(n - expected) <= tolerance; }
    if (typeof expected === 'boolean') return String(obtained).toUpperCase() === String(expected).toUpperCase();
    return String(obtained).trim().toLowerCase() === String(expected).trim().toLowerCase();
  }

  function renderRows(rows) {
    body.innerHTML = rows.map(({ t, o, ok, i }) => {
      const cells = inputs.map(inp => `<td>${fmt(t.inputs[inp.name])}</td>`).join('');
      const exp = (t.visible || ok) ? fmt(t.expected) : `<span class="hidden-val">nascosto</span>`;
      const got = o.error ? `<span class="hidden-val">errore</span>` : fmt(o.obtained);
      return `<tr class="${ok ? 'is-ok' : 'is-ko'}"><td>${i + 1}${t.boundary ? ' <span title="caso al confine">⚑</span>' : ''}</td>${cells}<td>${exp}</td><td>${got}</td><td>${ok ? '✓' : '✗'}</td></tr>`;
    }).join('');
  }
  function fmt(v) { if (v === null || v === undefined) return '—'; if (typeof v === 'number') return String(Math.round(v * 1000) / 1000); return String(v); }

  /* ── diagnosi a regole (livelli 1 e 2) ── */
  function diagnose(rows) {
    const failed = rows.filter(r => !r.ok);
    const msgs = [];
    const errRow = failed.find(r => r.o.error);
    if (errRow) {
      const e = String(errRow.o.error);
      if (/non trovato|not found|object '.*' not found/i.test(e) && e.includes(outputVar)) {
        msgs.push(`Il test cerca la variabile <code>${outputVar}</code> e non la trova: alla fine del tuo codice deve esistere con quel nome esatto.`);
      } else if (/unexpected|inatteso|parse|Errore di sintassi|unexpected '\}'|unexpected end/i.test(e)) {
        msgs.push('C\'è un errore di sintassi: controlla parentesi tonde e graffe aperte e chiuse, e le virgolette. Il messaggio di R dice dove si è fermato: <code>' + escape(e).slice(0, 160) + '</code>');
      } else {
        msgs.push('Il codice si ferma con un errore: <code>' + escape(e).slice(0, 200) + '</code>. Leggi il messaggio: quale riga nomina?');
      }
      return msgs;
    }
    const boundaryFail = failed.filter(r => r.t.boundary);
    const nonBoundaryFail = failed.filter(r => !r.t.boundary);
    const boundaryAll = rows.filter(r => r.t.boundary);
    if (boundaryFail.length > 0 && nonBoundaryFail.length === 0 && boundaryAll.length > 0) {
      msgs.push('Il tuo codice funziona <em>dentro</em> gli intervalli ma sbaglia esattamente sui bordi. Ogni soglia è compresa o esclusa? Rileggi le regole: "fino a", "non oltre", "da … a" dicono se il valore sul confine sta di qua o di là (<code>&lt;</code> oppure <code>&lt;=</code>).');
    }
    const sameOut = {};
    failed.forEach(r => { const k = String(r.o.obtained); sameOut[k] = (sameOut[k] || 0) + 1; });
    const dup = Object.entries(sameOut).find(([k, n]) => n >= 2 && k !== 'null' && k !== 'undefined');
    if (dup) msgs.push(`Più casi diversi producono lo stesso risultato sbagliato (<code>${escape(dup[0])}</code>): probabilmente finiscono tutti nello stesso ramo. Quale condizione li cattura prima del dovuto?`);
    if (failed.every(r => r.o.obtained === null || r.o.obtained === undefined)) {
      msgs.push(`Nessun caso produce <code>${outputVar}</code>: controlla che la variabile venga assegnata in <em>tutti</em> i rami (anche nell'<code>else</code>).`);
    }
    // livello 1: suggerimenti dei singoli test, sbloccati progressivamente con i tentativi
    const withHint = failed.filter(r => r.t.hint).slice(0, Math.max(1, attempts - 1));
    withHint.forEach(r => msgs.push(`<strong>Caso ${r.i + 1}</strong> — ${r.t.hint}`));
    if (msgs.length === 0) msgs.push('Qualche caso non passa. Prova a eseguire il codice con gli input del caso fallito e guarda che valore ottieni.');
    if (attempts >= 3) msgs.push('<span class="muted">Se sei bloccato: incolla codice e casi falliti nel tuo assistente in modalità <strong>Tutor</strong>.</span>');
    return msgs;
  }
  function showHint(msgs) { hintEl.hidden = false; hintEl.innerHTML = '<div class="hint__k">Suggerimento</div>' + msgs.map(m => `<p>${m}</p>`).join(''); }
  function escape(s) { return String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c])); }
})();
