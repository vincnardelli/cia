/* cbd-storage.js — stato personale nel browser (nessun backend)
   chiavi: cbd.progress  {slug: {passed, total, done, attempts, updated}}
           cbd.code.<slug>  testo dell'editor
           cbd.ai  {provider, skill}                                         */
(function () {
  function read(key, fallback) { try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch (e) { return fallback; } }
  function write(key, val) { try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {} }

  const CBD = {
    progress() { return read('cbd.progress', {}); },
    setProgress(slug, data) { const p = CBD.progress(); p[slug] = Object.assign({}, p[slug] || {}, data, { updated: Date.now() }); write('cbd.progress', p); CBD.paintStatuses(); },
    code(slug) { try { return localStorage.getItem('cbd.code.' + slug); } catch (e) { return null; } },
    setCode(slug, txt) { try { localStorage.setItem('cbd.code.' + slug, txt); } catch (e) {} },
    ai() { return read('cbd.ai', { provider: 'gpt', skill: false }); },
    setAi(data) { write('cbd.ai', Object.assign(CBD.ai(), data)); },
    /* colora le schede lab e i contatori presenti nella pagina */
    paintStatuses() {
      const p = CBD.progress();
      document.querySelectorAll('[data-status-for]').forEach(el => {
        const s = p[el.getAttribute('data-status-for')];
        el.classList.remove('is-progress', 'is-done');
        const t = el.querySelector('.status-text');
        if (!s) { if (t) t.textContent = 'non iniziato'; return; }
        if (s.done) { el.classList.add('is-done'); if (t) t.textContent = 'superato'; }
        else { el.classList.add('is-progress'); if (t) t.textContent = (s.passed || 0) + '/' + (s.total || '?') + ' test'; }
      });
      document.querySelectorAll('[data-progress-pillar]').forEach(el => {
        const slugs = (el.getAttribute('data-slugs') || '').split(',').filter(Boolean);
        const done = slugs.filter(s => p[s] && p[s].done).length;
        const bar = el.querySelector('.bar span'); if (bar) bar.style.width = (slugs.length ? 100 * done / slugs.length : 0) + '%';
        const n = el.querySelector('.avanzamento__n'); if (n) n.textContent = done + ' su ' + slugs.length + ' lab base superati';
      });
    },
    exportProgress() {
      const blob = new Blob([JSON.stringify({ exported: new Date().toISOString(), progress: CBD.progress() }, null, 2)], { type: 'application/json' });
      const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'cbd-avanzamento.json'; a.click();
    }
  };
  window.CBD = CBD;
  document.addEventListener('DOMContentLoaded', CBD.paintStatuses);
})();
