---
layout: page
title: Lab
permalink: /lab/
description: Tutti gli esercizi del corso, con verifica automatica
nav_order: 3
---

# 🧪 Tutti i lab

Ogni lab ha una specifica, un banco di prova nel browser e dei **casi nascosti** sui confini delle regole. Il tuo avanzamento è salvato in questo browser.

{% assign settimane = site.settimane | sort: 'number' %}
{% assign labs = site.lab | sort: 'order' | sort: 'week' %}
<div class="avanzamento">
{% for p in (1..3) %}
{% assign slugs = "" %}
{% for l in labs %}{% if l.level == 'base' %}{% assign w = settimane | where: 'number', l.week | first %}{% if w.pillar == p %}{% assign s = l.url | split: '/' | last %}{% assign slugs = slugs | append: s | append: "," %}{% endif %}{% endif %}{% endfor %}
<div class="avanzamento__p avanzamento__p--{{ p }}" data-progress-pillar="{{ p }}" data-slugs="{{ slugs }}">
  <div class="avanzamento__k">Pilastro {{ p }}</div>
  <div class="bar"><span></span></div>
  <div class="avanzamento__n"></div>
</div>
{% endfor %}
</div>
<p><button class="btn btn-outline btn-sm" onclick="CBD.exportProgress()">Esporta il mio avanzamento (JSON)</button> <span class="muted">da allegare al progetto</span></p>

<div class="filtri">
  <select data-filter="week"><option value="">tutte le settimane</option>{% for w in settimane %}<option value="{{ w.number }}">Settimana {{ w.number }} · {{ w.title }}</option>{% endfor %}</select>
  <select data-filter="level"><option value="">tutti i livelli</option><option value="base">base</option><option value="extra">extra</option><option value="sfida">sfida</option></select>
  <select data-filter="language"><option value="">R e Python</option><option value="R">R</option><option value="Python">Python</option></select>
</div>

<div class="lab-grid" data-lab-grid>
{% for l in labs %}
<div data-week="{{ l.week }}" data-level="{{ l.level }}" data-language="{{ l.language }}">{% include lab-card.html lab=l %}</div>
{% endfor %}
</div>

<script>
(function(){
  const sel = document.querySelectorAll('[data-filter]');
  function apply(){
    const f = {}; sel.forEach(s => f[s.dataset.filter] = s.value);
    document.querySelectorAll('[data-lab-grid] > div').forEach(d => {
      d.style.display = Object.keys(f).every(k => !f[k] || d.dataset[k] === f[k]) ? '' : 'none';
    });
  }
  sel.forEach(s => s.addEventListener('change', apply));
})();
</script>
