---
layout: lab
title: Sconto fedeltà
modulo: 3
order: 7
difficolta: difficile
language: R
ai_mode: 'on'
objective: 'Scrivere la specifica e il codice di un programma fedeltà: sconto a soglie più bonus tessera, con un tetto massimo.'
inputs:
- name: totale_carrello
  type: numero
- name: tessera
  type: testo
  desc: '"nessuna", "silver" o "gold"'
risultato:
  name: totale_scontato
  type: numero
  desc: importo da pagare, 2 decimali
regole: |
  - Sconto base: 0% sotto i 100 €; 5% da 100 € in su; 10% da 250 € in su.
  - Bonus tessera in punti percentuali: silver +2, gold +7, nessuna +0.
  - Lo sconto complessivo non può superare il 15%.
  - Prima di scrivere codice, scrivi tu la specifica completa (input, output, casi limite) e passala all'assistente in modalità *sviluppo assistito*.
skeleton: |
  totale_carrello <- 80
  tessera <- "nessuna"

  print(totale_scontato)
tests:
- inputs:
    totale_carrello: 80
    tessera: nessuna
  expected: 80.0
  visible: true
- inputs:
    totale_carrello: 300
    tessera: gold
  expected: 255.0
  visible: true
- inputs:
    totale_carrello: 100
    tessera: nessuna
  expected: 95.0
  visible: false
  boundary: true
- inputs:
    totale_carrello: 250
    tessera: silver
  expected: 220.0
  visible: false
  boundary: true
- inputs:
    totale_carrello: 250
    tessera: gold
  expected: 212.5
  visible: false
  boundary: true
- inputs:
    totale_carrello: 99.99
    tessera: gold
  expected: 92.99
  visible: false
  boundary: true
- inputs:
    totale_carrello: 120
    tessera: silver
  expected: 111.6
  visible: false
solution: |
  totale_carrello <- 80
  tessera <- "nessuna"

  if(totale_carrello >= 250){
    sconto <- 10
  }else if(totale_carrello >= 100){
    sconto <- 5
  }else{
    sconto <- 0
  }

  if(tessera == "silver"){
    sconto <- sconto + 2
  }else if(tessera == "gold"){
    sconto <- sconto + 7
  }

  if(sconto > 15){
    sconto <- 15
  }
  totale_scontato <- round(totale_carrello * (1 - sconto/100), 2)
  totale_scontato
solution_after: ''
---

Una catena di negozi di abbigliamento lancia il nuovo programma fedeltà e ti chiede di scrivere il calcolo dello **sconto alla cassa**. La direzione marketing ti ha spiegato le regole a voce, in riunione, e questa è la tua trascrizione.

Lo sconto base dipende da quanto si spende: niente sconto sotto i 100 euro, il 5% da 100 euro in su, il 10% da 250 euro in su. Chi ha la tessera fedeltà ha un **bonus** che si somma in punti percentuali: la tessera silver aggiunge 2 punti, la gold 7, chi non ha tessera non aggiunge nulla. Lo sconto complessivo, base più bonus, **non può in nessun caso superare il 15%**: un cliente gold da 300 euro avrebbe 10 + 7 = 17, ma paga con il 15%.

Il programma riceve la spesa e la tessera ("silver", "gold" o "nessuna") e restituisce il prezzo finale con due decimali. Prima di scrivere codice, scrivi tu la specifica completa, con i casi limite (100 euro esatti, 250 esatti, il tetto del 15%), e passala all'assistente in modalità *aiutami a partire*.
