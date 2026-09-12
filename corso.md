---
layout: page
title: Corso
permalink: /corso/
description: Le dodici settimane del corso, in tre pilastri
nav_order: 2
---

# 📚 Il corso, settimana per settimana

Ogni settimana ha un'idea sola. In aula si vede il nucleo; qui trovi la lezione per esteso, i lab con la verifica e le esplorazioni.

{% assign settimane = site.settimane | sort: 'number' %}
{% assign nomi = "Il codice|Come imparano le macchine|LLM e agenti" | split: "|" %}
{% for p in (1..3) %}
{% assign idx = p | minus: 1 %}
<h2 class="pillar-h pillar-h--{{ p }}">Pilastro {{ p }} · {{ nomi[idx] }}</h2>
<div class="settimane-list">
{% for w in settimane %}{% if w.pillar == p %}
{% assign nlab = site.lab | where: 'week', w.number | size %}
<a class="settimana-row settimana-row--p{{ p }}" href="{{ site.baseurl }}{{ w.url }}">
  <div class="settimana-row__n">{{ w.number }}</div>
  <div><div class="settimana-row__t">{{ w.title }}</div><div class="settimana-row__i">{{ w.idea }}</div></div>
  <div><span class="tag tag--lang">{{ w.language }}</span> {% if nlab > 0 %}<span class="tag">{{ nlab }} lab</span>{% endif %}</div>
</a>
{% endif %}{% endfor %}
</div>
{% endfor %}
