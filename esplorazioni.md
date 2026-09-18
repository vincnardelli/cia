---
layout: page
title: Esplorazioni
permalink: /esplorazioni/
description: Pagine interattive per capire i concetti chiave
nav_order: 5
published: false
---

# 🔬 Esplorazioni

Pagine interattive, una per concetto: si gioca con un controllo e si guarda cosa succede. Ognuna risponde a una domanda sola.

{% if site.esplorazioni.size == 0 %}
<div class="via"><div class="via__k">In arrivo</div>Le esplorazioni vengono pubblicate insieme ai moduli a cui si riferiscono.</div>
{% endif %}

<div class="espl-grid">
{% for e in site.esplorazioni %}
<a class="espl-card" href="{{ site.baseurl }}{{ e.url }}">
  <div class="espl-card__title">{{ e.title }}</div>
  <div class="espl-card__q">{{ e.question }}</div>
  <div class="muted">modulo {{ e.modulo }}{% unless e.ready %} · in arrivo{% endunless %}</div>
</a>
{% endfor %}
</div>
