---
layout: page
title: Esplorazioni
permalink: /esplorazioni/
description: Pagine interattive per capire i concetti chiave
nav_order: 5
---

# 🔬 Esplorazioni

Pagine interattive, una per concetto: si gioca con un controllo e si guarda cosa succede. Ognuna risponde a una domanda sola.

<div class="espl-grid">
{% for e in site.esplorazioni %}
<a class="espl-card" href="{{ site.baseurl }}{{ e.url }}">
  <div class="espl-card__title">{{ e.title }}</div>
  <div class="espl-card__q">{{ e.question }}</div>
  <div class="muted">settimana {{ e.week }}{% unless e.ready %} · in arrivo{% endunless %}</div>
</a>
{% endfor %}
</div>
