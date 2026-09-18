---
layout: page
title: Skill
permalink: /skill/
description: Installa la skill del corso nel tuo assistente AI
nav_order: 4
published: false
---

# 🧠 La skill del corso

La **skill** è un insieme di istruzioni e file che insegnano al tuo assistente AI come aiutarti in questo corso: conosce il programma, lo stile del codice, i lab, e soprattutto **non ti dà la soluzione pronta** ma ti fa trovare i casi limite. La stessa skill funziona su {% include icona.html nome="gpt" testo=true %}, {% include icona.html nome="claude" testo=true %} e {% include icona.html nome="gemini" testo=true %}; la installi una volta e poi, dalle pagine dei lab, il bottone *Lavora con l'AI* ti manda nella chat giusta con il prompt pronto.

Quando la skill è attiva, puoi parlarle così:

| scrivi | cosa succede |
|---|---|
| `tutor:` + il tuo codice | ti dice **una** cosa da guardare, come domanda, con casi da provare; mai la soluzione intera |
| `assistito:` + la specifica | analizza l'esercizio, ti fa domande sui casi limite, poi propone la struttura |
| `errore:` + il messaggio di R | ti traduce l'errore e ti dice dove guardare |
| `spiega:` + un concetto | otto righe, un esempio, il rimando al modulo |

Versione skill: **{{ site.skill_version }}** · [SKILL.md]({{ site.baseurl }}/assets/skill/istruzioni.txt) · [programma.md]({{ site.baseurl }}/assets/skill/programma.md) · [stile.md]({{ site.baseurl }}/assets/skill/stile.md) · [lab.md]({{ site.baseurl }}/assets/skill/lab.md)

<div class="tabs" data-tabs>
  <div class="tab is-active" data-tab="gpt">{% include icona.html nome="gpt" testo=true size=20 %}</div>
  <div class="tab" data-tab="claude">{% include icona.html nome="claude" testo=true size=20 %}</div>
  <div class="tab" data-tab="gemini">{% include icona.html nome="gemini" testo=true size=20 %}</div>
</div>

<div class="tab-panel is-active" data-panel="gpt" markdown="1">

<div class="via via--rapida" markdown="1">
<div class="via__k">Via rapida</div>
{% if site.skill_gpt_url != '' %}
Il GPT del corso è già configurato: aprilo e fissalo nella barra laterale. Funziona anche con l'account gratuito.

[Apri "Coding e fondamenti di AI" su ChatGPT]({{ site.skill_gpt_url }}){: .btn .btn-primary }
{% else %}
Il GPT condiviso del corso sarà pubblicato qui all'inizio del corso. Nel frattempo usa la via manuale.
{% endif %}
</div>

<div class="via" markdown="1">
<div class="via__k">Via manuale (Progetto o GPT personale)</div>

<ol class="steps">
<li>Su ChatGPT apri <strong>Progetti → Nuovo progetto</strong> e chiamalo <em>Coding e fondamenti di AI</em>.</li>
<li>In <strong>Istruzioni</strong> incolla il testo della skill: <button class="btn btn-outline btn-sm" data-copy-file="{{ site.baseurl }}/assets/skill/istruzioni.txt">Copia le istruzioni</button></li>
<li>In <strong>File</strong> carica i tre allegati: <a href="{{ site.baseurl }}/assets/skill/programma.md" download>programma.md</a>, <a href="{{ site.baseurl }}/assets/skill/stile.md" download>stile.md</a>, <a href="{{ site.baseurl }}/assets/skill/lab.md" download>lab.md</a>.</li>
<li>Apri una chat dentro il progetto e fai il test qui sotto.</li>
</ol>
</div>
</div>

<div class="tab-panel" data-panel="claude" markdown="1">

<div class="via" markdown="1">
<div class="via__k">Progetto (funziona con l'account gratuito)</div>

<ol class="steps">
<li>Su Claude apri <strong>Projects → New project</strong>, nome <em>Coding e fondamenti di AI</em>.</li>
<li>In <strong>Instructions</strong> (o "Set project instructions") incolla la skill: <button class="btn btn-outline btn-sm" data-copy-file="{{ site.baseurl }}/assets/skill/istruzioni.txt">Copia le istruzioni</button></li>
<li>In <strong>Project knowledge</strong> carica <a href="{{ site.baseurl }}/assets/skill/programma.md" download>programma.md</a>, <a href="{{ site.baseurl }}/assets/skill/stile.md" download>stile.md</a>, <a href="{{ site.baseurl }}/assets/skill/lab.md" download>lab.md</a>.</li>
<li>Apri una chat nel progetto e fai il test qui sotto.</li>
</ol>
</div>

<div class="via via--rapida" markdown="1">
<div class="via__k">Skill vera e propria (piani a pagamento)</div>
Scarica la cartella della skill e caricala in **Settings → Capabilities → Skills**: si attiva da sola quando parli di codice o di un lab del corso, senza dover aprire un progetto.

[Scarica cia-skill.zip]({{ site.baseurl }}/assets/skill/cia-skill.zip){: .btn .btn-primary }
</div>
</div>

<div class="tab-panel" data-panel="gemini" markdown="1">

<div class="via via--rapida" markdown="1">
<div class="via__k">Via rapida</div>
{% if site.skill_gem_url != '' %}
La Gem del corso è condivisa: aprila e salvala tra le tue Gem.

[Apri la Gem "Coding e fondamenti di AI"]({{ site.skill_gem_url }}){: .btn .btn-primary }
{% else %}
La Gem condivisa del corso sarà pubblicata qui all'inizio del corso. Nel frattempo usa la via manuale.
{% endif %}
</div>

<div class="via" markdown="1">
<div class="via__k">Via manuale</div>

<ol class="steps">
<li>Su Gemini apri <strong>Gems → Nuova Gem</strong>, nome <em>Coding e fondamenti di AI</em>.</li>
<li>In <strong>Istruzioni</strong> incolla la skill: <button class="btn btn-outline btn-sm" data-copy-file="{{ site.baseurl }}/assets/skill/istruzioni.txt">Copia le istruzioni</button></li>
<li>In <strong>Conoscenza</strong> carica <a href="{{ site.baseurl }}/assets/skill/programma.md" download>programma.md</a>, <a href="{{ site.baseurl }}/assets/skill/stile.md" download>stile.md</a>, <a href="{{ site.baseurl }}/assets/skill/lab.md" download>lab.md</a>.</li>
<li>Salva, apri la Gem e fai il test qui sotto. Nota: Gemini non accetta prompt precompilati dal link, quindi dalle pagine dei lab il bottone <em>copia</em> il prompt e apre la Gem: incollalo tu.</li>
</ol>
</div>
</div>

## ✅ Test di installazione

Incolla questo messaggio nella chat del tuo assistente:

<pre data-test-prompt>tutor: ecco la mia bozza dell'autovelox

velocita <- 60
limite <- 50
differenza <- velocita - limite
if(differenza < 10){
  multa <- 36
}else if(differenza < 40){
  multa <- 148
}else{
  multa <- 500
}
multa</pre>
<button class="btn btn-outline btn-sm" data-copy-el="[data-test-prompt]">Copia il messaggio di prova</button>

La skill è attiva se la risposta ha **tre sezioni** — *Cosa funziona*, *Una cosa da guardare*, *Prova questo* — ti fa **una sola domanda** (probabilmente su cosa succede con esattamente 10 km/h oltre il limite) e **non** ti riscrive il codice. Se invece ti consegna la soluzione corretta, le istruzioni non sono state caricate: ricontrolla il passo 2.

<script>
(function(){
  document.querySelectorAll('[data-tabs] .tab').forEach(t => t.addEventListener('click', () => {
    document.querySelectorAll('[data-tabs] .tab').forEach(x => x.classList.toggle('is-active', x === t));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.toggle('is-active', p.dataset.panel === t.dataset.tab));
  }));
  function copyText(t, btn){ navigator.clipboard.writeText(t).then(()=>{ const o=btn.textContent; btn.textContent='Copiato ✓'; setTimeout(()=>btn.textContent=o,1500); }); }
  document.querySelectorAll('[data-copy-file]').forEach(b => b.addEventListener('click', () => fetch(b.dataset.copyFile).then(r=>r.text()).then(t=>copyText(t,b))));
  document.querySelectorAll('[data-copy-el]').forEach(b => b.addEventListener('click', () => copyText(document.querySelector(b.dataset.copyEl).textContent, b)));
})();
</script>
