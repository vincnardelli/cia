---
layout: page
title: Lab
permalink: /lab/
description: Tutti gli esercizi del corso, con verifica automatica
nav_order: 3
published: false
---

# 🧪 Tutti i lab

Ogni lab ha un contesto, un banco di prova nel browser e dei **casi nascosti** sui confini delle regole. Puoi lavorare qui o in RStudio: il codice si scarica e si ricarica come file `.R`.

{% assign moduli = site.moduli | sort: 'number' %}
{% assign labs = site.lab | sort: 'order' | sort: 'modulo' %}

<div class="filtri">
  <select data-filter="modulo"><option value="">tutti i moduli</option>{% for w in moduli %}<option value="{{ w.number }}">Modulo {{ w.number }} · {{ w.title }}</option>{% endfor %}</select>
  <select data-filter="difficolta"><option value="">facili e difficili</option><option value="facile">facili</option><option value="difficile">difficili</option></select>
  <select data-filter="language"><option value="">R e Python</option><option value="R">R</option><option value="Python">Python</option></select>
</div>

<div class="lab-grid" data-lab-grid>
{% for l in labs %}
{% assign lm = moduli | where: 'number', l.modulo | first %}{% unless lm %}{% continue %}{% endunless %}
<div data-modulo="{{ l.modulo }}" data-difficolta="{{ l.difficolta }}" data-language="{{ l.language }}">{% include lab-card.html lab=l %}</div>
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
