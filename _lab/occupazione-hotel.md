---
layout: lab
title: Occupazione dell'hotel
modulo: 1
order: 5
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare il tasso di occupazione di un hotel in una notte, in percentuale.
inputs:
- name: occupate
  type: numero
  desc: camere occupate
- name: totali
  type: numero
  desc: camere dell'hotel
risultato:
  name: tasso
  type: numero
  desc: percentuale con un decimale
regole: |
  - Il tasso di occupazione è `occupate / totali * 100`.
  - Arrotonda a **un** decimale.
skeleton: |
  occupate <- 80
  totali <- 100


  print(tasso)
tests:
- inputs:
    occupate: 80
    totali: 100
  expected: 80.0
  visible: true
- inputs:
    occupate: 37
    totali: 45
  expected: 82.2
  visible: true
- inputs:
    occupate: 0
    totali: 45
  expected: 0.0
  visible: false
  boundary: true
- inputs:
    occupate: 45
    totali: 45
  expected: 100.0
  visible: false
  boundary: true
  hint: 'Hotel pieno: 100, non 100.0 con decimali strani né 1.'
- inputs:
    occupate: 13
    totali: 120
  expected: 10.8
  visible: false
solution: |
  occupate <- 80
  totali <- 100

  tasso <- round(occupate / totali * 100, 1)
  tasso
solution_after: ''
---

La direttrice di un hotel di 45 camere guarda ogni mattina un numero solo: il tasso di occupazione della notte appena passata, cioè la percentuale di camere occupate sul totale. È il numero con cui ragiona la catena, con cui si decidono i prezzi del giorno e con cui si confrontano gli hotel tra loro.

Il gestionale glielo mostra, ma vuole ricalcolarlo lei quando arrivano i dati dagli altri hotel del gruppo, che hanno numeri di camere diversi. Scrivi il programma che, date le camere occupate e le camere totali, calcola il tasso in percentuale con un decimale. Una notte con l'hotel pieno deve dare 100, una notte vuota 0.
