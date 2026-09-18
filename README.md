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

<div class="iscrizione">
  <div><span class="iscrizione__k">Iscrizione al corso</span><span class="iscrizione__t">Compila il questionario di iscrizione prima della prossima lezione.</span></div>
  <a class="btn btn-primary" href="https://forms.gle/H5XrnvV977ZBd44F8" target="_blank" rel="noopener">Compila il questionario</a>
</div>

**Coding e fondamenti di intelligenza artificiale** è un corso facoltativo del Corso di Laurea Triennale in *Economia e Gestione dei Servizi* dell'Università Cattolica del Sacro Cuore (sede di Roma), costruito sui tre modi di far fare qualcosa a una macchina: **dirglielo**, scrivendo le regole in un linguaggio di programmazione; **mostrarle degli esempi**, perché impari le regole dai dati; **chiederglielo**, con un modello di linguaggio fino agli agenti che usano il codice che avrai scritto tu. In tutti e tre il lavoro che resta a te è lo stesso: prima dire con precisione cosa vuoi, dopo controllare il risultato.

{% assign moduli = site.moduli | sort: 'number' %}

## 🧭 Tre sezioni

<div class="sezioni">
{% assign sez_n = "moduli 1–5 · R|moduli 6–8 · R → Python|moduli 9–12 · Python" | split: "|" %}
{% assign sez_t = "Il codice|Come imparano le macchine|LLM e agenti" | split: "|" %}
{% assign sez_d = "Dirglielo. Scrivi tu le regole: variabili, decisioni, cicli, funzioni, dati con dplyr. Poi le provi sui casi limite.|Mostrarle degli esempi. La regola la trova la macchina, nei dati che le dai: alberi, poi Python e random forest. La domanda da fare sempre: su quali dati l'hai provata?|Chiederglielo. Da testo a numeri, il modello di linguaggio che prevede il pezzo di testo successivo, gli agenti che chiamano le funzioni scritte nella sezione 1. La risposta la verifichi con i tuoi strumenti." | split: "|" %}
{% for p in (1..3) %}{% assign i = p | minus: 1 %}{% assign primo = moduli | where: 'sezione', p | first %}
  <{% if primo %}a href="{{ site.baseurl }}{{ primo.url }}"{% else %}div{% endif %} class="sezione sezione--{{ p }}">
    <div class="sezione__n">Sezione {{ p }} · {{ sez_n[i] }}</div>
    <div class="sezione__t">{{ sez_t[i] }}</div>
    <div class="sezione__d">{{ sez_d[i] }}</div>
    <div class="sezione__w">Software {{ p }}.0{% if primo %} →{% else %} · in arrivo{% endif %}</div>
  </{% if primo %}a{% else %}div{% endif %}>
{% endfor %}
</div>

## 🤖 Come si usa l'AI in questo corso

<div class="patto" markdown="1">
**Ammessa e incoraggiata** nel corso. **Sempre verificata**: ogni codice generato va eseguito e provato sui casi limite, in RStudio{% if site.mostra_lab %} o nella pagina del lab{% endif %}. **Sempre dichiarata**: tieni un registro di cosa ha fatto l'AI e di cosa hai controllato tu, e devi saper spiegare ogni riga del tuo codice.
</div>

{% if site.mostra_skill %}
Installa la [skill del corso]({{ site.baseurl }}/skill/) nel tuo assistente ({% include icona.html nome="gpt" testo=true %}, {% include icona.html nome="claude" testo=true %} o {% include icona.html nome="gemini" testo=true %}): ti aiuta a trovare gli errori senza darti la soluzione. In ogni lab trovi il bottone *Lavora con l'AI*.
{% endif %}

## 👩🏻‍💻 Perché seguire il corso?

Seguendo il corso otterrai **CFU aggiuntivi**, utili anche per l'accesso a corsi di laurea magistrale (informati per tempo!). Al di là del valore curricolare, il vero obiettivo è il tuo futuro professionale. L'AI la usiamo già tutti, ma chi la usa senza conoscerla sbaglia, e la competenza più richiesta dalle imprese non è l'AI: è saper ragionare. Delegare a una macchina è comodo, ma a chi delega restano tre cose: dire cosa fare, controllare il risultato, firmare. E per controllare bisogna capire come funziona.

## 👩🏻‍🎓 A chi è rivolto?

A studenti e studentesse di Economia, non a ingegneri informatici o data scientist: non serve saper programmare, si parte da zero. Si affrontano temi tecnici, ma sempre legati ad applicazioni concrete: economia e finanza, marketing e startup, sanità e pubblica amministrazione.

## 📘 Come funziona

- **In aula** (giorni, orari e aule cambiano durante il semestre: controlla il [calendario]({{ site.baseurl }}/schedule/)): il minimo che serve per capire il concetto, quasi tutto scritto a mano.
- **In piattaforma**: le slide e la lezione scritta{% if site.mostra_lab %}, i lab con la **verifica automatica** e i casi limite nascosti, le esplorazioni interattive. Il codice lo scrivi qui o in RStudio: si scarica e si ricarica come file `.R`{% endif %}.

[Vai al corso]({{ site.baseurl }}/corso/){: .btn .btn-primary }{% if site.mostra_lab %} [Tutti i lab]({{ site.baseurl }}/lab/){: .btn .btn-outline }{% endif %} [Guide di installazione]({{ site.baseurl }}/guide/){: .btn .btn-outline }

## 📌 Avvisi

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
