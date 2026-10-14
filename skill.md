---
layout: page
title: Skill
permalink: /skill/
description: Installa la skill del corso nel tuo assistente AI
nav_order: 4
---

# 🧠 La skill del corso

La **skill** è un insieme di istruzioni e file che insegnano al tuo assistente AI come aiutarti in questo corso: conosce il programma, lo stile del codice e gli esercizi, e soprattutto **non ti dà la soluzione pronta** ma ti fa trovare i casi limite. La stessa skill funziona su {% include icona.html nome="gpt" testo=true %}, {% include icona.html nome="gemini" testo=true %} e {% include icona.html nome="claude" testo=true %}: la installi una volta e la usi per tutto il corso.{% if site.mostra_lab %} Dalle pagine dei lab, il bottone *Lavora con l'AI* ti manda nella chat giusta con il prompt pronto.{% endif %}

La skill copre la parte del corso sul codice in R: usa solo i costrutti visti a lezione e scrive il codice nello stesso stile.{% assign m5 = site.moduli | where: 'number', 5 | first %}{% if m5 %} Perché e quando usarla, con un esempio dall'inizio alla fine, è spiegato nel [modulo 5, Delegare]({{ site.baseurl }}{{ m5.url }}).{% endif %}

## Come si usa

Scrivi la modalità come prima parola del messaggio:

| scrivi | cosa succede |
|---|---|
| `tutor:` + il tuo codice | ti dice **una** cosa da guardare, come domanda, con casi da provare; mai la soluzione intera |
| `assistito:` + la specifica | analizza il problema, ti fa domande sui casi limite, poi propone la struttura e, se vuoi, il codice |
| `errore:` + il messaggio di R | ti traduce l'errore e ti dice dove guardare |
| `spiega:` + un concetto | otto righe, un esempio, il rimando alla lezione |
| `shiny:` + le tue funzioni | ti aiuta a costruirci attorno un'app Shiny, come il calcolatore BMI della lezione 6 |
| `progetto:` + la tua idea | ti aiuta a trovare un problema e a specificarlo bene, facendo la parte del compagno che lo deve risolvere |

Più sotto trovi un esempio pronto per ognuna.

## Installala

Versione **{{ site.skill_version }}** · file: [istruzioni]({{ site.baseurl }}/assets/skill/istruzioni.txt) · [programma.md]({{ site.baseurl }}/assets/skill/programma.md) · [stile.md]({{ site.baseurl }}/assets/skill/stile.md) · [lab.md]({{ site.baseurl }}/assets/skill/lab.md)

<div class="tabs" data-tabs>
  <div class="tab is-active" data-tab="gpt">{% include icona.html nome="gpt" testo=true size=20 %}</div>
  <div class="tab" data-tab="gemini">{% include icona.html nome="gemini" testo=true size=20 %}</div>
  <div class="tab" data-tab="claude">{% include icona.html nome="claude" testo=true size=20 %}</div>
</div>

<div class="tab-panel is-active" data-panel="gpt" markdown="1">

{% if site.skill_gpt_url != '' %}
<div class="via via--rapida" markdown="1">
<div class="via__k">Via rapida</div>
Il GPT del corso è già configurato: aprilo e fissalo nella barra laterale. Funziona anche con l'account gratuito.

[Apri "Coding e fondamenti di AI" su ChatGPT]({{ site.skill_gpt_url }}){: .btn .btn-primary }
</div>
{% endif %}

<div class="via" markdown="1">
<div class="via__k">Un progetto su ChatGPT (la strada consigliata)</div>

<ol class="steps">
<li>Su ChatGPT apri <strong>Progetti → Nuovo progetto</strong> e chiamalo <em>Coding e fondamenti di AI</em>.</li>
<li>Nelle <strong>istruzioni</strong> del progetto incolla il testo della skill: <button class="btn btn-outline btn-sm" data-copy-file="{{ site.baseurl }}/assets/skill/istruzioni.txt">Copia le istruzioni</button></li>
<li>Nei <strong>file</strong> del progetto carica i tre allegati: <a href="{{ site.baseurl }}/assets/skill/programma.md" download>programma.md</a>, <a href="{{ site.baseurl }}/assets/skill/stile.md" download>stile.md</a>, <a href="{{ site.baseurl }}/assets/skill/lab.md" download>lab.md</a>.</li>
<li>Apri una chat dentro il progetto e fai il test qui sotto.</li>
</ol>
</div>

<div class="via via--rapida" markdown="1">
<div class="via__k">In alternativa: la Skill di ChatGPT (solo se nel tuo account, in Plugin, c'è la scheda Skill)</div>

<ol class="steps">
<li>Scarica la skill: <a class="btn btn-outline btn-sm" href="{{ site.baseurl }}/assets/skill/cia-skill.zip" download>cia-skill.zip</a></li>
<li>Su ChatGPT apri <strong>Plugin</strong> nella barra laterale, poi la scheda <strong>Skill</strong>.</li>
<li>Premi <strong>+</strong>, scegli <strong>Carica dal tuo computer</strong> e trascina lo zip: tra le skill installate compare <em>coding fondamenti ai</em>.</li>
<li>Apri una chat nuova e fai il test qui sotto: la skill si attiva da sola quando scrivi <code>tutor:</code>, <code>assistito:</code> e le altre modalità.</li>
</ol>
</div>
</div>

<div class="tab-panel" data-panel="gemini" markdown="1">

{% if site.skill_gem_url != '' %}
<div class="via via--rapida" markdown="1">
<div class="via__k">Via rapida</div>
La Gem del corso è condivisa: aprila e salvala tra le tue Gem.

[Apri la Gem "Coding e fondamenti di AI"]({{ site.skill_gem_url }}){: .btn .btn-primary }
</div>
{% endif %}

<div class="via" markdown="1">
<div class="via__k">{% if site.skill_gem_url != '' %}In alternativa: una tua Gem{% else %}Una Gem su Gemini (funziona con l'account gratuito){% endif %}</div>

<ol class="steps">
<li>Su Gemini apri <strong>Gem → Nuova Gem</strong> e chiamala <em>Coding e fondamenti di AI</em>.</li>
<li>Nelle <strong>istruzioni</strong> incolla la skill: <button class="btn btn-outline btn-sm" data-copy-file="{{ site.baseurl }}/assets/skill/istruzioni.txt">Copia le istruzioni</button></li>
<li>In <strong>Conoscenza</strong> carica <a href="{{ site.baseurl }}/assets/skill/programma.md" download>programma.md</a>, <a href="{{ site.baseurl }}/assets/skill/stile.md" download>stile.md</a>, <a href="{{ site.baseurl }}/assets/skill/lab.md" download>lab.md</a>.</li>
<li>Salva, apri la Gem e fai il test qui sotto.</li>
</ol>
</div>
</div>

<div class="tab-panel" data-panel="claude" markdown="1">

<div class="via" markdown="1">
<div class="via__k">Un progetto su Claude (funziona con l'account gratuito)</div>

<ol class="steps">
<li>Su Claude apri <strong>Projects → New project</strong> e chiamalo <em>Coding e fondamenti di AI</em>.</li>
<li>Nelle <strong>istruzioni</strong> del progetto incolla la skill: <button class="btn btn-outline btn-sm" data-copy-file="{{ site.baseurl }}/assets/skill/istruzioni.txt">Copia le istruzioni</button></li>
<li>In <strong>Project knowledge</strong> carica <a href="{{ site.baseurl }}/assets/skill/programma.md" download>programma.md</a>, <a href="{{ site.baseurl }}/assets/skill/stile.md" download>stile.md</a>, <a href="{{ site.baseurl }}/assets/skill/lab.md" download>lab.md</a>.</li>
<li>Apri una chat nel progetto e fai il test qui sotto.</li>
</ol>
</div>

<div class="via via--rapida" markdown="1">
<div class="via__k">Skill vera e propria (piani a pagamento)</div>
Scarica la cartella della skill e caricala tra le **Skills** nelle impostazioni di Claude: si attiva da sola quando parli di codice o di un esercizio del corso, senza dover aprire un progetto.

[Scarica cia-skill.zip]({{ site.baseurl }}/assets/skill/cia-skill.zip){: .btn .btn-primary }
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

La skill è attiva se la risposta ha **tre sezioni** (*Cosa funziona*, *Una cosa da guardare*, *Prova questo*), ti fa **una sola domanda**, probabilmente su cosa succede con esattamente 10 km/h oltre il limite, e **non** ti riscrive il codice. Se invece ti consegna la soluzione corretta, le istruzioni non sono state caricate: ricontrolla il passo 2.

## 💬 Un esempio per ogni modalità

Copia un esempio, incollalo nella chat e guarda come risponde. Poi rifallo con il tuo codice o il tuo problema.

### `tutor:` hai scritto una bozza e qualcosa non torna

<pre data-esempio="tutor">tutor: devo contare quanti clienti hanno speso più di 100 euro, ma mi viene sempre 0 o 1

spese <- c(120, 80, 150, 100, 95)
for(i in 1:length(spese)){
  quanti <- 0
  if(spese[i] > 100){
    quanti <- quanti + 1
  }
}
quanti</pre>
<button class="btn btn-outline btn-sm" data-copy-el='[data-esempio="tutor"]'>Copia</button>

Cosa aspettarti: una domanda su dove parte il contatore, non il codice corretto.

### `assistito:` hai il problema, non ancora il codice

<pre data-esempio="assistito">assistito: una palestra costa 40 euro al mese. Gli studenti hanno lo sconto del 25%, chi ha più di 65 anni del 30%. Gli sconti non si sommano. Input: eta (numero) e studente (TRUE o FALSE). Output: la quota mensile da pagare.</pre>
<button class="btn btn-outline btn-sm" data-copy-el='[data-esempio="assistito"]'>Copia</button>

Cosa aspettarti: «Ho capito così» e qualche domanda sui confini (65 anni esatti? uno studente di 70 anni quale sconto ha?), nessun codice finché non rispondi.

### `errore:` R ti ha risposto con un messaggio rosso

<pre data-esempio="errore">errore: Error in if (eta[i] > 67) { : missing value where TRUE/FALSE needed

eta <- c(89, 6, 45)
for(i in 1:4){
  if(eta[i] > 67){
    print("In pensione")
  }
}</pre>
<button class="btn btn-outline btn-sm" data-copy-el='[data-esempio="errore"]'>Copia</button>

Cosa aspettarti: il messaggio tradotto, la riga da guardare (quanti elementi ha `eta`, quante volte gira il ciclo?) e una sola cosa da provare.

### `spiega:` un concetto non ti è chiaro

<pre data-esempio="spiega">spiega: che differenza c'è tra print e return dentro una funzione?</pre>
<button class="btn btn-outline btn-sm" data-copy-el='[data-esempio="spiega"]'>Copia</button>

Cosa aspettarti: poche righe, un esempio nello stile della lezione 6 e una domanda per vedere se hai capito.

### `shiny:` vuoi un'app attorno alla tua funzione

<pre data-esempio="shiny">shiny: vorrei un'app per questa funzione, con una casella per il prezzo e una scelta sì/no per lo studente

prezzo_finale <- function(prezzo, studente){
  if(studente){
    return(prezzo * 0.75)
  }else{
    return(prezzo)
  }
}</pre>
<button class="btn btn-outline btn-sm" data-copy-el='[data-esempio="shiny"]'>Copia</button>

Cosa aspettarti: prima una verifica della funzione sui casi limite, poi l'app con `ui`, `server` e `shinyApp`, come in `app.R` della lezione 6.

### `progetto:` cerchi un'idea per il progetto 1, o vuoi metterla alla prova

<pre data-esempio="progetto">progetto: vorrei lavorare nel marketing di un'azienda di cosmetici. Proponimi quattro problemi reali che potrei risolvere in R con quello che abbiamo fatto a lezione, ognuno con i dati in entrata, le regole e il risultato.</pre>
<button class="btn btn-outline btn-sm" data-copy-el='[data-esempio="progetto"]'>Copia</button>

Quando hai scelto e scritto il tuo problema, rimandalo con `progetto:` e chiedi: *«Non risolverlo: fai il compagno che lo deve risolvere e dimmi cosa non è chiaro.»* Ogni domanda a cui il tuo testo non risponde è una regola da aggiungere. Dettagli sul progetto: [Progetto 1]({{ site.baseurl }}/progetti/1/).

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
