---
layout: lab
title: Straordinari della settimana
modulo: 3
order: 5
difficolta: facile
language: R
ai_mode: 'on'
objective: Calcolare la paga settimanale di un addetto a partire dalle ore lavorate ogni giorno, con la maggiorazione per gli straordinari.
inputs:
- name: ore
  type: vettore di numeri
  desc: ore lavorate in ciascun giorno della settimana
- name: paga_oraria
  type: numero
  desc: euro per ora ordinaria
risultato:
  name: paga
  type: numero
  desc: paga della settimana in euro, 2 decimali
regole: |
  - In ogni giorno le prime **8 ore** sono ordinarie e si pagano a `paga_oraria`.
  - Le ore **oltre l'ottava**, giorno per giorno, sono straordinario e si pagano al **130%** (`paga_oraria * 1.3`).
  - La paga è la somma dei giorni. Arrotonda a due decimali.
  - Il conteggio è per giorno: 9 ore il lunedì e 7 il martedì fanno un'ora di straordinario, non zero.
skeleton: |
  ore <- c(8, 8, 8, 8, 8)
  paga_oraria <- 12

  # ...
  for(i in 1:length(ore)){
    if(ore[i] > 8){
      # ...
    }else{
      # ...
    }
    # ...
  }

  print(paga)
tests:
- inputs:
    ore:
    - 8
    - 8
    - 8
    - 8
    - 8
    paga_oraria: 12
  expected: 480.0
  visible: true
- inputs:
    ore:
    - 9
    - 8
    - 10
    - 8
    - 7
    paga_oraria: 12
  expected: 514.8
  visible: true
- inputs:
    ore:
    - 9
    - 7
    paga_oraria: 10
  expected: 163.0
  visible: false
  boundary: true
  hint: 'Le ore si compensano tra giorni? No: 9 e 7 danno un''ora di straordinario e sette ordinarie il secondo giorno.'
- inputs:
    ore:
    - 8.5
    - 8
    - 8
    - 8
    - 8
    paga_oraria: 10
  expected: 406.5
  visible: false
  boundary: true
- inputs:
    ore:
    - 0
    - 0
    - 0
    - 0
    - 0
    paga_oraria: 15
  expected: 0.0
  visible: false
  boundary: true
- inputs:
    ore:
    - 12
    - 12
    - 12
    - 12
    - 12
    paga_oraria: 10
  expected: 660.0
  visible: false
- inputs:
    ore:
    - 6
    - 6
    - 6
    paga_oraria: 11.5
  expected: 207.0
  visible: false
solution: |
  ore <- c(8, 8, 8, 8, 8)
  paga_oraria <- 12

  paga <- 0
  for(i in 1:length(ore)){
    if(ore[i] > 8){
      ordinarie <- 8
      extra <- ore[i] - 8
    }else{
      ordinarie <- ore[i]
      extra <- 0
    }
    paga <- paga + ordinarie * paga_oraria + extra * paga_oraria * 1.3
  }
  paga <- round(paga, 2)
  paga
solution_after: ''
---

Nell'ufficio del personale di un supermercato, ogni fine settimana bisogna calcolare la paga degli addetti a partire dal cartellino: un vettore con le ore lavorate in ciascun giorno. Il contratto dice che in ogni giornata le prime **8 ore** sono ordinarie e si pagano alla paga oraria; le ore **oltre l'ottava** sono straordinario e valgono il 130% della paga oraria.

Il punto che il vecchio foglio Excel sbagliava: il conteggio è **giorno per giorno**. Chi fa 9 ore il lunedì e 7 il martedì ha un'ora di straordinario, non zero, perché le ore non si compensano tra giornate.

Scrivi il programma che, dati il vettore delle ore e la paga oraria, calcola la paga della settimana con due decimali.
