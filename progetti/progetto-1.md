---
layout: page
title: Progetto 1 · Inventa un problema
permalink: /progetti/1/
parent: Progetti
nav_order: 1
---

# Progetto 1 · Inventa un problema e risolvilo in R

Nei lab ricevi un problema già scritto e scrivi il codice che lo risolve. Qui fai tutte e due le parti: **inventi il problema**, come se dovessi proporlo come lab ai tuoi compagni, e **scrivi il codice R che lo risolve**.

<div class="patto" markdown="1">
**Conta il problema, non solo la soluzione.** Vengono premiate la **fantasia** nella scelta del problema e la **precisione** con cui lo specifichi: chi lo usa, cosa entra, cosa esce, cosa succede su ogni confine. Un problema originale, definito fino all'ultimo caso e risolto con un codice semplice vale più di un problema banale risolto con un codice complicato.
</div>

<div class="spec">
  <div class="spec__row"><div class="spec__k">Chi</div><div class="spec__v">Individuale</div></div>
  <div class="spec__row"><div class="spec__k">Punti</div><div class="spec__v">9 su 30, con un giudizio unico da 0 a 9</div></div>
  <div class="spec__row"><div class="spec__k">Scadenza</div><div class="spec__v"><strong>Venerdì 23 ottobre 2026, ore 23:59</strong>. Dopo la scadenza il progetto vale 0 punti.</div></div>
  <div class="spec__row"><div class="spec__k">Cosa</div><div class="spec__v">Due file: <code>cognome_nome.R</code> e il registro AI in PDF o Word (<code>cognome_nome_registro_ai.pdf</code> o <code>.docx</code>)</div></div>
  <div class="spec__row"><div class="spec__k">Come</div><div class="spec__v">Per email a <a href="mailto:vincenzo.nardelli@unicatt.it?subject=CIA%20Progetto%201%20-%20Cognome%20Nome">vincenzo.nardelli@unicatt.it</a>, con oggetto <code>CIA Progetto 1 - Cognome Nome</code> e i due file in allegato</div></div>
</div>

## Quale problema

Un problema che incontri **nella vita di tutti i giorni** o che potresti incontrare **nel tuo lavoro futuro**: un'azienda, un ufficio, un ospedale, un negozio, un'associazione, la tua casa. Il punto di partenza è sempre lo stesso: alcuni dati in entrata, delle regole precise, un risultato che serve a decidere qualcosa (un prezzo, una priorità, una rata, un sì o un no).

Qualche idea, per capire la misura giusta:

- **Sanità · triage semplificato.** Da saturazione, frequenza cardiaca e dolore dichiarato (da 0 a 10), il codice di priorità di un paziente al pronto soccorso. Che codice ha chi ha saturazione esattamente 92? E chi ha due parametri gialli e uno verde?
- **Marketing · conviene la campagna?** Da budget, costo per clic e tasso di conversione di tre canali (social, motori di ricerca, email), quante vendite aspettarsi e quale canale ripaga l'investimento. E se il budget non basta per nessun canale?
- **Finanza · quale conto corrente conviene.** Da saldo medio, bonifici e prelievi al mese, il costo annuo di tre conti con canoni e commissioni diverse, e il più conveniente. Cosa succede se due costano uguale?
- **Servizi · prenotazioni di un ristorante.** Con 40 coperti e una quota di clienti che non si presenta, quante prenotazioni accettare per una sera, e quanti clienti restano senza tavolo se vengono tutti.
- **Vita quotidiana · spese tra coinquilini.** Chi ha pagato cosa nel mese, e chi deve quanto a chi per andare in pari.

Puoi partire da uno di questi, ma il problema finale deve essere tuo: con le tue regole, i tuoi numeri, il tuo contesto. Non vale riprendere un lab del corso, né l'esempio completo qui sotto, cambiando i numeri.

## Usa l'AI per trovare l'idea e per specificare il problema

L'AI è **ammessa e incentivata** in tutto il progetto, e in due momenti è particolarmente utile.

- **Per trovare l'idea.** Raccontale cosa ti interessa e falle proporre problemi, poi scegli e cambia. Per esempio: *"Studio economia e mi interessa il marketing. Proponimi cinque problemi di lavoro reali che si risolvono con dei dati in entrata e qualche regola, senza bisogno di un dataset."*
- **Per specificare il problema.** Quando hai scritto il testo, chiedile di fare la parte del compagno che deve risolverlo: *"Ecco il testo di un esercizio. Non risolverlo: fammi tutte le domande che faresti perché non è chiaro, e trova i casi in cui due regole si contraddicono o nessuna regola dice cosa fare."* Ogni domanda a cui il tuo testo non risponde è una regola da aggiungere.

## Cosa fare

1. **Scegli la situazione** e decidi chi userebbe il tuo programma: un'infermiera al triage, un responsabile marketing, un consulente in banca, tu stesso.
2. **Scrivi il testo del problema** in testa al file, nei commenti: contesto, dati in entrata, risultato, regole. Deve bastare a chi non ti conosce per risolverlo senza farti domande, quindi ogni soglia ha un valore e ogni caso ha una risposta.
3. **Scrivi il codice** che lo risolve, dentro una o più funzioni, come nella lezione 6.
4. **Provalo sui casi limite**: sotto le funzioni, chiamale con dati diversi e scrivi accanto il risultato atteso. Almeno un caso per ogni confine delle tue regole, più i casi strani (zero, valori negativi, tutto uguale).
5. **Compila il registro AI** e invia i due file.
{: .steps }

<div class="via" markdown="1">
<div class="via__k">Se vuoi · un'app Shiny</div>
Puoi mettere le tue funzioni dentro una piccola app, come il calcolatore BMI della lezione 6: caselle e cursori per i dati in entrata, il risultato che si aggiorna da solo. È una possibilità, non un obbligo: usala se ti diverte e se aiuta a far capire a cosa serve il tuo programma. L'app si aggiunge in fondo allo stesso file `.R`.
</div>

## Un esempio completo

Ecco cosa potrebbe consegnare una studentessa che ha scelto il piano di risparmio: il file `.R`, il registro AI e, facoltativa, l'app. Guarda soprattutto quanto è dettagliato il testo del problema in testa al file: è la parte che pesa di più.

<div class="tabs" data-tabs>
  <div class="tab is-active" data-tab="codice">📄 rossi_giulia.R</div>
  <div class="tab" data-tab="registro">📝 Registro AI</div>
  <div class="tab" data-tab="shiny">✨ Con Shiny (facoltativo)</div>
</div>

<div class="tab-panel is-active" data-panel="codice" markdown="1">

Il file ha tre parti, in quest'ordine: il testo del problema nei commenti, le funzioni, i casi di prova con il risultato atteso. L'ultima funzione, `saldo_finale`, è un controllo: rifà il conto mese per mese con un ciclo, senza la formula, per verificare che il versamento basti davvero.

```r
# ==============================================================
# PROGETTO 1 - Il piano di risparmio                 Rossi Giulia
#
# Contesto
# Allo sportello di una banca arrivano clienti giovani con un
# obiettivo: l'anticipo per una casa, un master, un viaggio. La
# domanda è sempre la stessa: "quanto devo mettere da parte ogni
# mese?". Subito dopo ne arriva una seconda: "ce la posso fare con
# il mio stipendio?". Il programma serve al consulente per
# rispondere a tutte e due in pochi secondi, durante il colloquio.
#
# Input
#   obiettivo         la cifra da raggiungere, in euro (più di 0)
#   gia_risparmiato   quanto il cliente ha già da parte, in euro (0 o più)
#   mesi              entro quanti mesi, un numero intero
#   rendimento        rendimento annuo del conto deposito, in percento
#                     (3 vuol dire 3% all'anno; 0 se è un conto normale)
#   stipendio         stipendio netto mensile, in euro (più di 0)
#
# Output
#   il versamento mensile, in euro, e un giudizio in parole
#
# Regole
#   1. Gli interessi si calcolano ogni mese: il tasso mensile è il
#      rendimento annuo diviso 12. Il versamento si fa a fine mese.
#   2. Quello che è già da parte cresce con gli interessi per tutti
#      i mesi. Se da solo arriva all'obiettivo, il versamento è 0.
#   3. Il versamento si arrotonda per eccesso all'euro intero:
#      meglio un euro in più che arrivare corti.
#   4. Con 0 mesi (o meno) il calcolo non ha senso: il risultato è NA.
#   5. Il giudizio dipende dalla quota dello stipendio che serve:
#        fino al 20% compreso   "sostenibile"
#        fino al 35% compreso   "impegnativo"
#        oltre il 35%           "da rivedere: allunga i tempi o
#                                abbassa l'obiettivo"
#      Se il versamento è 0 il giudizio è "obiettivo già raggiunto".
# ==============================================================


# ---- 1. Le funzioni ---------------------------------------------

versamento_mensile <- function(obiettivo, gia_risparmiato, mesi, rendimento){
  if(mesi < 1){
    return(NA)
  }

  tasso <- rendimento / 100 / 12

  # quanto diventa da solo quello che è già da parte
  gia_cresciuto <- gia_risparmiato * (1 + tasso)^mesi
  mancante <- obiettivo - gia_cresciuto
  if(mancante <= 0){
    return(0)
  }

  if(tasso == 0){
    versamento <- mancante / mesi
  }else{
    versamento <- mancante * tasso / ((1 + tasso)^mesi - 1)
  }
  return(ceiling(versamento))
}

giudizio <- function(versamento, stipendio){
  if(versamento == 0){
    return("obiettivo già raggiunto")
  }
  quota <- versamento / stipendio
  if(quota <= 0.20){
    return("sostenibile")
  }else if(quota <= 0.35){
    return("impegnativo")
  }else{
    return("da rivedere: allunga i tempi o abbassa l'obiettivo")
  }
}

# Controllo indipendente: simula il conto mese per mese con un
# ciclo, senza usare la formula, e dice quanto c'è alla fine.
saldo_finale <- function(gia_risparmiato, versamento, mesi, rendimento){
  tasso <- rendimento / 100 / 12
  saldo <- gia_risparmiato
  for(m in 1:mesi){
    saldo <- saldo * (1 + tasso) + versamento
  }
  return(saldo)
}


# ---- 2. Casi di prova -------------------------------------------

# senza interessi i conti si fanno a mano
versamento_mensile(12000, 0, 24, 0)        # atteso: 500
versamento_mensile(12000, 2000, 20, 0)     # atteso: 500
versamento_mensile(1000, 0, 3, 0)          # atteso: 334 (333,33 per eccesso)

# confini della regola 2
versamento_mensile(5000, 5000, 12, 3)      # atteso: 0 (già raggiunto)
versamento_mensile(10000, 9800, 12, 3)     # atteso: 0 (bastano gli interessi)

# regola 4
versamento_mensile(5000, 0, 0, 3)          # atteso: NA

# con gli interessi il versamento scende sotto 500...
v <- versamento_mensile(12000, 0, 24, 3)
v                                          # atteso: 486
# ...e la simulazione conferma che si arriva all'obiettivo
saldo_finale(0, v, 24, 3) >= 12000         # atteso: TRUE
saldo_finale(0, v - 1, 24, 3) >= 12000     # atteso: FALSE (un euro in meno non basta)

# confini della regola 5, con uno stipendio di 1500 euro
giudizio(300, 1500)                        # atteso: "sostenibile" (20% esatto)
giudizio(301, 1500)                        # atteso: "impegnativo"
giudizio(525, 1500)                        # atteso: "impegnativo" (35% esatto)
giudizio(526, 1500)                        # atteso: "da rivedere: ..."
giudizio(0, 1500)                          # atteso: "obiettivo già raggiunto"
```

</div>

<div class="tab-panel" data-panel="registro" markdown="1">

Un documento PDF o Word, nella forma che preferisci. Contiene gli strumenti usati e, per ogni uso importante, cosa hai chiesto, cosa ti ha dato l'AI e cosa hai fatto tu. Se non hai usato l'AI, scrivilo.

<div class="via" markdown="1">
<div class="via__k">rossi_giulia_registro_ai.pdf</div>

**Registro AI · Progetto 1 · Giulia Rossi**

**Strumenti usati:** ChatGPT (versione gratuita) e Claude.

**1. L'idea.**

- *Cosa ho chiesto:* "Studio economia e vorrei lavorare in banca. Proponimi cinque problemi che un consulente risolve con qualche numero e qualche regola."
- *Cosa mi ha dato:* cinque idee; una era "quanto risparmiare ogni mese per un obiettivo".
- *Cosa ho fatto io:* l'ho scelta e ho aggiunto la seconda domanda, "ce la posso fare con il mio stipendio?", che nella proposta non c'era.

**2. Il testo del problema.**

- *Cosa ho chiesto:* ho incollato la prima versione del testo e ho chiesto a Claude di non risolverlo ma di farmi le domande di chi lo deve risolvere.
- *Cosa mi ha dato:* nove domande. Le più utili: "gli interessi si calcolano ogni mese o ogni anno?", "il versamento si arrotonda?", "e se i soldi già da parte bastano?", "20% esatto è sostenibile o impegnativo?".
- *Cosa ho fatto io:* ho aggiunto le regole 1, 3 e 4 e ho scritto "compreso" nelle soglie della regola 5. Rileggendo mi sono accorta di un caso che l'AI non aveva visto: quello che è già da parte può arrivare all'obiettivo solo con gli interessi. È diventato la regola 2.

**3. La formula.**

- *Cosa ho chiesto:* come calcolare il versamento mensile con un rendimento annuo.
- *Cosa mi ha dato:* una formula corretta, ma che con rendimento 0 divide per zero.
- *Cosa ho fatto io:* ho provato a mano 12.000 euro in 24 mesi senza interessi (devono essere 500 al mese), ho visto l'errore e ho aggiunto un `if` per il caso senza interessi.

**4. La verifica.**

- *Cosa ho chiesto:* niente: ho scritto io la funzione `saldo_finale`, che rifà il conto mese per mese con un ciclo.
- *Cosa ho controllato:* che con 486 euro al mese si arrivi a 12.000 e con 485 no. Il conto esatto è 485,77 euro: la prima versione toglieva i decimali e dava 485, che non bastava. Per questo nella regola 3 l'arrotondamento è per eccesso.
</div>

</div>

<div class="tab-panel" data-panel="shiny" markdown="1">

Solo se vuoi. Queste righe si aggiungono in fondo allo stesso file, dopo i casi di prova: le funzioni sono le stesse, l'app cambia solo chi passa i numeri. Per avviarla, seleziona tutto il file ed eseguilo (<kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>).

```r
# ---- 3. L'app (facoltativa) ---------------------------------------
# Le funzioni sono le stesse: l'app cambia solo chi passa i numeri.

library(shiny)

ui <- fluidPage(
  titlePanel("Piano di risparmio"),
  sidebarLayout(
    sidebarPanel(
      numericInput("obiettivo", "Obiettivo (euro)", value = 12000, min = 0, step = 500),
      numericInput("gia", "Già risparmiato (euro)", value = 0, min = 0, step = 500),
      sliderInput("mesi", "Entro quanti mesi", min = 1, max = 120, value = 24),
      sliderInput("rendimento", "Rendimento annuo (%)", min = 0, max = 6, value = 3, step = 0.5),
      numericInput("stipendio", "Stipendio netto mensile (euro)", value = 1500, min = 1, step = 100)
    ),
    mainPanel(
      h2(textOutput("versamento")),
      h3(textOutput("giudizio"))
    )
  )
)

server <- function(input, output){
  output$versamento <- renderText({
    v <- versamento_mensile(input$obiettivo, input$gia, input$mesi, input$rendimento)
    paste("Da versare ogni mese:", v, "euro")
  })
  output$giudizio <- renderText({
    v <- versamento_mensile(input$obiettivo, input$gia, input$mesi, input$rendimento)
    giudizio(v, input$stipendio)
  })
}

shinyApp(ui = ui, server = server)
```

Con i valori di partenza l'app mostra *Da versare ogni mese: 486 euro* e *impegnativo*. Abbassando lo stipendio a 1.000 euro il giudizio diventa *da rivedere*.

</div>

## Come viene valutato

Il progetto riceve un **giudizio unico da 0 a 9**. Conta il progetto nel suo insieme, e soprattutto il problema: quanto è originale e vicino alla realtà, quanto è specificato bene, cioè se chiunque potrebbe risolverlo senza farti domande. Poi se il codice lo risolve davvero anche sui confini e se i casi di prova lo dimostrano.

<script>
(function(){
  document.querySelectorAll('[data-tabs] .tab').forEach(t => t.addEventListener('click', () => {
    document.querySelectorAll('[data-tabs] .tab').forEach(x => x.classList.toggle('is-active', x === t));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.toggle('is-active', p.dataset.panel === t.dataset.tab));
  }));
})();
</script>
