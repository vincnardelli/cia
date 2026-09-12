---
layout: home
title: Coding e fondamenti di AI 2026/2027
nav_exclude: false
nav_order: 1
permalink: index.html
seo:
  type: Coding e fondamenti di intelligenza artificiale 2026/2027
  name: Economia e Gestione dei Servizi - Università Cattolica del Sacro Cuore
---

# 💻 Coding e fondamenti di intelligenza artificiale

**Coding e fondamenti di intelligenza artificiale** è un corso facoltativo del Corso di Laurea Triennale in *Economia e Gestione dei Servizi* dell'Università Cattolica del Sacro Cuore (sede di Roma). Sessanta ore in dodici settimane per imparare tre cose collegate da un unico filo: scrivere regole in un linguaggio di programmazione, far imparare le regole a una macchina dai dati, e capire come i modelli di linguaggio gestiscono i testi fino agli agenti che usano il codice che avrai scritto tu.

{% assign settimane = site.settimane | sort: 'number' %}
{% assign oggi = 'now' | date: '%s' | plus: 0 %}
{% assign corrente = nil %}
{% for w in settimane %}{% for d in w.dates %}{% assign ds = d | date: '%s' | plus: 0 %}{% if ds <= oggi %}{% assign corrente = w %}{% endif %}{% endfor %}{% endfor %}
{% if corrente %}
<div class="dove-siamo">
  <span class="dove-siamo__k">Dove siamo</span>
  <span class="dove-siamo__t">Settimana {{ corrente.number }} · {{ corrente.title }}</span>
  <a class="btn btn-primary btn-sm" href="{{ site.baseurl }}{{ corrente.url }}">Apri la lezione</a>
  <a class="btn btn-outline btn-sm" href="{{ site.baseurl }}{{ corrente.url }}#lab">Lab della settimana</a>
</div>
{% endif %}

## 🧭 Tre pilastri

<div class="pilastri">
  <a class="pilastro pilastro--1" href="{{ site.baseurl }}/settimana/01-partenza/">
    <div class="pilastro__n">Pilastro 1 · settimane 1–5 · R</div>
    <div class="pilastro__t">Il codice</div>
    <div class="pilastro__d">Scrivi tu le regole: variabili, decisioni, cicli, funzioni, dati con dplyr. Ogni lab ha dei casi limite nascosti che ti aspettano.</div>
    <div class="pilastro__w">Software 1.0 →</div>
  </a>
  <a class="pilastro pilastro--2" href="{{ site.baseurl }}/settimana/06-software-2-0/">
    <div class="pilastro__n">Pilastro 2 · settimane 6–8 · R → Python</div>
    <div class="pilastro__t">Come imparano le macchine</div>
    <div class="pilastro__d">Le regole le impara un albero dai dati. Poi Python, random forest e la validazione: quanto fidarsi di un modello.</div>
    <div class="pilastro__w">Software 2.0 →</div>
  </a>
  <a class="pilastro pilastro--3" href="{{ site.baseurl }}/settimana/09-da-testo-a-numeri/">
    <div class="pilastro__n">Pilastro 3 · settimane 9–12 · Python</div>
    <div class="pilastro__t">LLM e agenti</div>
    <div class="pilastro__d">Da testo a numeri, il modello di linguaggio, il prompt come programma, e gli agenti che chiamano le funzioni scritte nel pilastro 1.</div>
    <div class="pilastro__w">Software 3.0 →</div>
  </a>
</div>

## 🤖 Come si usa l'AI in questo corso

<div class="patto" markdown="1">
**Ammessa e incoraggiata** su lab e progetti. **Sempre verificata**: ogni codice generato va eseguito e provato sui casi limite, in RStudio o nella pagina del lab. **Sempre dichiarata**: nel progetto si consegna il registro di cosa ha fatto l'AI e cosa hai controllato tu. All'orale devi saper spiegare ogni riga: non si passa il corso affidandosi all'AI.
</div>

Installa la [skill del corso]({{ site.baseurl }}/skill/) nel tuo assistente (ChatGPT, Claude o Gemini): ti aiuta a trovare gli errori senza darti la soluzione. In ogni lab trovi il bottone *Apri nell'assistente*.

## 👩🏻‍💻 Perché seguire il corso?

Seguendo il corso otterrai **CFU aggiuntivi**, utili anche per l'accesso a corsi di laurea magistrale (informati per tempo!). Al di là del valore curricolare, il vero obiettivo è fornirti idee, strumenti e conoscenze pratiche per il tuo futuro professionale: viviamo in una società in cui le decisioni pubbliche e private sono guidate da dati, algoritmi e ormai da modelli di linguaggio, e comprenderne il funzionamento è indispensabile per chiunque voglia avere un ruolo attivo nel lavoro e nella società.

## 👩🏻‍🎓 A chi è rivolto?

A studenti e studentesse di Economia, non a ingegneri informatici o data scientist. Si affrontano temi tecnici, ma sempre legati ad applicazioni concrete: economia e finanza, marketing e startup, sanità e pubblica amministrazione.

## 📘 Come funziona

- **In aula** (5 ore a settimana): il minimo che serve per capire il concetto, quasi tutto scritto a mano.
- **In piattaforma**: le lezioni per esteso, i lab con la **verifica automatica** e i casi limite nascosti, lab extra e sfide, le esplorazioni interattive. Il tuo avanzamento resta nel tuo browser.
- **Progetto di gruppo** a metà corso su un dataset reale.

[Vai al corso]({{ site.baseurl }}/corso/){: .btn .btn-primary } [Tutti i lab]({{ site.baseurl }}/lab/){: .btn .btn-outline } [Guide di installazione]({{ site.baseurl }}/guide/){: .btn .btn-outline }

## 📌 Avvisi

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
