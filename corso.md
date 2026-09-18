---
layout: page
title: Corso
permalink: /corso/
description: I dodici moduli del corso, in tre sezioni
nav_order: 2
---

# 📚 Il corso, modulo per modulo

Ogni modulo ha un'idea sola. In aula si vede il nucleo; qui trovi le slide e la lezione per esteso.

{% assign moduli = site.moduli | sort: 'number' %}
{% assign nomi = "Il codice|Come imparano le macchine|LLM e agenti" | split: "|" %}
{% for p in (1..3) %}
{% assign idx = p | minus: 1 %}
{% assign nsez = moduli | where: 'sezione', p | size %}{% if nsez > 0 %}
<h2 class="sezione-h sezione-h--{{ p }}">Sezione {{ p }} · {{ nomi[idx] }}</h2>
<div class="moduli-list">
{% for w in moduli %}{% if w.sezione == p %}
{% assign nlab = site.lab | where: 'modulo', w.number | size %}
<a class="modulo-row modulo-row--p{{ p }}" href="{{ site.baseurl }}{{ w.url }}">
  <div class="modulo-row__n">{{ w.number }}</div>
  <div><div class="modulo-row__t">{{ w.title }}</div><div class="modulo-row__i">{{ w.idea }}</div></div>
  <div><span class="tag tag--lang">{{ w.language }}</span> {% if nlab > 0 %}<span class="tag">{{ nlab }} lab</span>{% endif %}</div>
</a>
{% endif %}{% endfor %}
</div>
{% endif %}
{% endfor %}
