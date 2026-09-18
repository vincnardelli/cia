---
layout: page
title: Calendario
permalink: /schedule/
description: Le 23 lezioni del corso, con giorno, ora e aula
nav_order: 9
---

# 🗓 Calendario delle lezioni

Il calendario ufficiale, con eventuali variazioni, è sulla [pagina del corso su unicatt.it](https://docenti.unicatt.it/ppd2/it/docenti/80554/vincenzo-nardelli/didattica).

{% assign oggi = 'now' | date: '%Y-%m-%d' %}
{% assign mesi = 'gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre' | split: '|' %}

<table class="calendario">
<thead><tr><th>#</th><th>data</th><th>ora</th><th>aula</th></tr></thead>
<tbody>
{% for l in site.data.lezioni %}
{% assign dstr = l.data | date: '%Y-%m-%d' %}
<tr class="{% if dstr < oggi %}is-past{% elsif dstr == oggi %}is-today{% endif %}">
  <td class="muted">{{ l.n }}</td>
  {% assign mi = l.data | date: '%-m' | minus: 1 %}<td><strong>{{ l.giorno }} {{ l.data | date: '%-d' }} {{ mesi[mi] }}</strong></td>
  <td>{{ l.ora }}</td>
  <td class="muted">{{ l.aula }}</td>
</tr>
{% endfor %}
</tbody>
</table>

Attenzione ai cambi di orario e di aula. Fino al 23 ottobre si fa lezione il **venerdì dalle 9:00 alle 12:00** e il **mercoledì dalle 14:00 alle 16:00**. Il mercoledì si è in aula **12**, tranne il 23 settembre, che è in aula **104**. Dal 2 novembre si fa lezione il **lunedì dalle 11:00 alle 13:00** e il **venerdì dalle 9:00 alle 12:00**, sempre in aula **14**. Tra il 23 ottobre e il 2 novembre non c'è lezione.
