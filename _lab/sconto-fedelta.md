---
layout: lab
title: Sconto fedeltà
week: 3
order: 7
level: sfida
language: R
ai_mode: 'on'
objective: 'Scrivere la specifica e il codice di un programma fedeltà: sconto a soglie più bonus tessera, con un tetto massimo.'
inputs:
- name: totale_carrello
  type: numero
- name: tessera
  type: testo
  desc: '"nessuna", "silver" o "gold"'
output:
  name: totale_scontato
  type: numero
  desc: importo da pagare, 2 decimali
skeleton: |
  totale_carrello <- 80
  tessera <- "nessuna"

  # alla fine deve esistere la variabile totale_scontato
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

- Sconto base: 0% sotto i 100 €; 5% da 100 € in su; 10% da 250 € in su.
- Bonus tessera in punti percentuali: silver +2, gold +7, nessuna +0.
- Lo sconto complessivo non può superare il 15%.
- Prima di scrivere codice, scrivi tu la specifica completa (input, output, casi limite) e passala all'assistente in modalità *sviluppo assistito*.
