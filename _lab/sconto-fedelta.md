---
layout: lab
title: Sconto fedeltà
modulo: 4
order: 1
difficolta: difficile
language: R
ai_mode: 'on'
objective: 'Scrivere la specifica e il codice di un programma fedeltà come funzione `totale_scontato(totale_carrello, tessera)`: sconto a soglie più bonus tessera, con un tetto massimo.'
inputs:
- name: totale_carrello
  type: numero
  desc: spesa in euro, prima dello sconto
- name: tessera
  type: testo
  desc: '"nessuna", "silver" o "gold"'
risultato:
  name: totale_scontato
  type: numero
  desc: importo da pagare, 2 decimali
function: totale_scontato
regole: |
  - Sconto base: 0% sotto i 100 €; 5% da 100 € in su; 10% da 250 € in su.
  - Bonus tessera in punti percentuali: silver +2, gold +7, nessuna +0.
  - Lo sconto complessivo non può superare il 15%.
  - Il prezzo finale è arrotondato a due decimali.
  - Il codice deve **definire** la funzione `totale_scontato <- function(totale_carrello, tessera){ ... }` che **restituisce** il prezzo finale con `return()`. La verifica chiama la tua funzione con i valori di ogni caso.
  - Prima di scrivere codice, scrivi tu la specifica completa (input, output, casi limite) e passala all'assistente in modalità *aiutami a partire*.
skeleton: |
  totale_scontato <- function(totale_carrello, tessera){
    # ...
    return(...)
  }

  print(totale_scontato(80, "nessuna"))
tolerance: 0.001
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
- inputs:
    totale_carrello: 300
    tessera: nessuna
  expected: 270.0
  visible: false
- inputs:
    totale_carrello: 249.99
    tessera: silver
  expected: 232.49
  visible: false
  boundary: true
- inputs:
    totale_carrello: 133.33
    tessera: silver
  expected: 124.0
  visible: false
  hint: '133,33 con il 7% di sconto fa 123,9969: il prezzo finale va con due decimali. Hai usato round(x, 2)?'
solution: |
  totale_scontato <- function(totale_carrello, tessera){
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
    totale <- round(totale_carrello * (1 - sconto/100), 2)
    return(totale)
  }

  print(totale_scontato(80, "nessuna"))
solution_after: ''
---

Una catena di negozi di abbigliamento lancia il nuovo programma fedeltà e ti chiede di scrivere il calcolo dello **sconto alla cassa**. La direzione marketing ti ha spiegato le regole a voce, in riunione, e questa è la tua trascrizione.

Lo sconto base dipende da quanto si spende: niente sconto sotto i 100 euro, il 5% da 100 euro in su, il 10% da 250 euro in su. Chi ha la tessera fedeltà ha un **bonus** che si somma in punti percentuali: la tessera silver aggiunge 2 punti, la gold 7, chi non ha tessera non aggiunge nulla. Lo sconto complessivo, base più bonus, **non può in nessun caso superare il 15%**: un cliente gold da 300 euro avrebbe 10 + 7 = 17, ma paga con il 15%.

Le casse dei negozi useranno il calcolo migliaia di volte al giorno, quindi va scritto come **funzione**: `totale_scontato(totale_carrello, tessera)` riceve la spesa e la tessera ("silver", "gold" o "nessuna"), in quest'ordine, e con `return()` restituisce il prezzo finale arrotondato a due decimali. Prima di scrivere codice, scrivi tu la specifica completa, con i casi limite (100 euro esatti, 250 esatti, il tetto del 15%), e passala all'assistente in modalità *aiutami a partire*.
