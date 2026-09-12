/* risolvi-con-ai.js — pannello "Lavora con l'assistente" (pagine lab e settimana).
   Compone il prompt: [istruzioni compatte se la skill non è installata] + modalità + specifica del lab (+ bozza).
   Le istruzioni compatte vengono da /assets/skill/compatta.json, generato dalla cartella skill/.          */
(function () {
  const panels = document.querySelectorAll('.ai-panel[data-ai-context]');
  if (!panels.length) return;
  const cfg = window.CBD_CONFIG || { baseurl: '' };
  let compatta = null;
  const loaded = fetch(cfg.baseurl + '/assets/skill/compatta.json').then(r => r.json()).then(j => { compatta = j; }).catch(() => { compatta = null; });

  const pageUrl = location.origin + location.pathname;
  const lab = document.querySelector('.lab[data-lab]');

  function labBlock() {
    const title = lab.closest('body').querySelector('.lab__title').firstChild.textContent.trim();
    const inputs = JSON.parse(lab.querySelector('[data-lab-inputs]').textContent || '[]');
    const tests = JSON.parse(lab.querySelector('[data-lab-tests]').textContent || '[]').filter(t => t.visible);
    const objective = JSON.parse(lab.querySelector('[data-lab-spec]').textContent || '""');
    const rules = lab.querySelector('[data-lab-rules]').value.trim();
    const out = lab.dataset.output;
    const week = lab.closest('body').querySelector('.ai-panel[data-week]').dataset.week;
    const lang = lab.dataset.language;
    let s = `**Lab: ${title}** (settimana ${week}, ${lang}) — ${pageUrl}\n`;
    s += `Obiettivo: ${objective}\n`;
    s += `Input: ` + inputs.map(i => `${i.name} (${i.type}${i.desc ? ', ' + i.desc : ''})`).join('; ') + `\n`;
    s += `Output: ${out}` + (lab.dataset.function ? ` — da scrivere come funzione ${lab.dataset.function}` : '') + `\n`;
    s += `Regole:\n${rules}\n`;
    if (tests.length) s += `Esempi:\n` + tests.map(t => Object.entries(t.inputs).map(([k, v]) => `${k}=${JSON.stringify(v)}`).join(', ') + ` → ${out}=${JSON.stringify(t.expected)}`).join('\n') + '\n';
    return s;
  }

  function compose(panel) {
    const ctx = panel.dataset.aiContext;
    const mode = (panel.querySelector('input[name="ai-mode"]:checked') || {}).value || 'spiega';
    const skill = panel.querySelector('[data-ai-skill]').checked;
    const parts = [];
    if (!skill && compatta) {
      parts.push(`### Istruzioni per questa conversazione\n${compatta.comuni.trim()}\n\n**Modalità ${mode.toUpperCase()}**\n${(compatta[mode] || compatta.spiega || '').trim()}\n\n---\n`);
    }
    if (ctx === 'lab') {
      parts.push(`${mode}: ${lab.closest('body').querySelector('.lab__title').firstChild.textContent.trim()}\n\n` + labBlock());
      const code = (document.querySelector('[data-editor]') || {}).value || '';
      const skeleton = (lab.querySelector('[data-lab-skeleton]') || {}).value || '';
      if (mode === 'tutor') parts.push(`\nLa mia bozza:\n\`\`\`${lab.dataset.language.toLowerCase()}\n${code.trim() || '(non ho ancora scritto nulla: chiedimi di iniziare dalla struttura)'}\n\`\`\`\n`);
      if (mode === 'assistito') parts.push(`\nNon ho ancora scritto codice. Parti dal passo 1 (analisi), senza codice.\n`);
      if (mode === 'traduci') parts.push(`\nIl mio codice in R, da tradurre in Python mantenendo gli stessi risultati sugli esempi:\n\`\`\`r\n${code.trim() || skeleton}\n\`\`\`\n`);
    } else {
      const title = panel.dataset.title, week = panel.dataset.week;
      const text = (panel.querySelector('.ai-panel__lezione') || {}).value || '';
      parts.push(`spiega: ripasso della settimana ${week} — ${title} (${pageUrl})\n\nEcco il testo della lezione. Fammi tre domande per verificare se l'ho capita, una alla volta, e correggimi quando sbaglio.\n\n${text.slice(0, 6000)}\n`);
    }
    parts.push(`\n_Nota per l'assistente: sto seguendo il corso "Coding e fondamenti di intelligenza artificiale"; le regole complete per aiutarmi sono su ${cfg.siteurl || ''}/skill/ (skill v${cfg.skillVersion || ''})._`);
    return parts.join('\n');
  }

  function openIn(provider, text) {
    const q = encodeURIComponent(text);
    if (provider === 'gpt') { window.open((cfg.gptUrl || 'https://chatgpt.com/') + (cfg.gptUrl && cfg.gptUrl.includes('?') ? '&' : '?') + 'q=' + q, '_blank'); return true; }
    if (provider === 'claude') { window.open('https://claude.ai/new?q=' + q, '_blank'); return true; }
    if (provider === 'gemini') { copy(text); window.open(cfg.gemUrl || 'https://gemini.google.com/app', '_blank'); return true; }
    copy(text); return false;
  }
  function copy(text) { try { navigator.clipboard.writeText(text); } catch (e) { const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); } }
  function flash(btn, msg) { const o = btn.textContent; btn.textContent = msg; setTimeout(() => btn.textContent = o, 1600); }

  panels.forEach(panel => {
    const provSel = panel.querySelector('[data-ai-provider]');
    const skillCb = panel.querySelector('[data-ai-skill]');
    const preview = panel.querySelector('[data-ai-preview]');
    const openBtn = panel.querySelector('[data-ai-open]');
    const copyBtn = panel.querySelector('[data-ai-copy]');
    const st = CBD.ai(); provSel.value = st.provider || 'gpt'; skillCb.checked = !!st.skill;

    function labelOpen() {
      const p = provSel.value;
      openBtn.textContent = p === 'gpt' ? 'Apri in ChatGPT' : p === 'claude' ? 'Apri in Claude' : p === 'gemini' ? 'Copia e apri Gemini' : 'Copia il prompt';
      const lenNote = skillCb.checked ? '' : ' (istruzioni incluse)';
      copyBtn.textContent = 'Copia il prompt' + lenNote;
    }
    function refresh() { if (preview) preview.textContent = compose(panel); labelOpen(); }
    provSel.addEventListener('change', () => { CBD.setAi({ provider: provSel.value }); refresh(); });
    skillCb.addEventListener('change', () => { CBD.setAi({ skill: skillCb.checked }); refresh(); });
    panel.querySelectorAll('input[name="ai-mode"]').forEach(r => r.addEventListener('change', refresh));
    const ed = document.querySelector('[data-editor]'); if (ed) ed.addEventListener('input', () => { if (preview && preview.closest('details').open) refresh(); });
    preview && preview.closest('details').addEventListener('toggle', refresh);
    openBtn.addEventListener('click', () => { const t = compose(panel); if (!openIn(provSel.value, t)) flash(openBtn, 'Copiato ✓'); });
    copyBtn.addEventListener('click', () => { copy(compose(panel)); flash(copyBtn, 'Copiato ✓'); });
    loaded.then(refresh); labelOpen();
  });
})();
