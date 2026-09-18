---
layout: lab
title: Autovelox
modulo: 2
order: 2
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare la sanzione per eccesso di velocità secondo l'art. 142 del Codice della Strada.
inputs:
- name: velocita
  type: numero
  desc: velocità rilevata, km/h
- name: limite
  type: numero
  desc: limite di velocità, km/h
risultato:
  name: multa
  type: numero
  desc: sanzione in euro
regole: |
  Art. 142 CdS (importi minimi):

  - entro il limite: nessuna sanzione;
  - oltre il limite di **non oltre 10 km/h**: 36 €;
  - di **oltre 10 e non oltre 40 km/h**: 148 €;
  - di **oltre 40 e non oltre 60 km/h**: 370 €;
  - di **oltre 60 km/h**: 500 €.
skeleton: |
  velocita <- 45
  limite <- 50

  # ...
  if(differenza <= 0){
    # ...
  }else if(differenza <= 10){
    # ...
  }else if(differenza <= 40){
    # ...
  }else if(differenza <= 60){
    # ...
  }else{
    # ...
  }

  print(multa)
tests:
- inputs:
    velocita: 45
    limite: 50
  expected: 0
  visible: true
- inputs:
    velocita: 75
    limite: 50
  expected: 148
  visible: true
- inputs:
    velocita: 60
    limite: 50
  expected: 36
  visible: false
  boundary: true
  hint: 'Esattamente 10 km/h oltre il limite è "non oltre 10": quindi 36 €. Il tuo confronto lo include?'
- inputs:
    velocita: 90
    limite: 50
  expected: 148
  visible: false
  boundary: true
  hint: '40 km/h oltre il limite: "non oltre 40" → 148 €.'
- inputs:
    velocita: 110
    limite: 50
  expected: 370
  visible: false
  boundary: true
  hint: '60 km/h oltre: "non oltre 60" → 370 €.'
- inputs:
    velocita: 111
    limite: 50
  expected: 500
  visible: false
  boundary: true
- inputs:
    velocita: 50
    limite: 50
  expected: 0
  visible: false
  boundary: true
  hint: 'Velocità uguale al limite: nessuna sanzione.'
- inputs:
    velocita: 200
    limite: 130
  expected: 500
  visible: false
solution: |
  velocita <- 70
  limite <- 50

  differenza <- velocita - limite

  if(differenza <= 0){
    multa <- 0
  }else if(differenza <= 10){
    multa <- 36
  }else if(differenza <= 40){
    multa <- 148
  }else if(differenza <= 60){
    multa <- 370
  }else{
    multa <- 500
  }
  multa
solution_after: ''
---

Il Comune sta sostituendo il software di un autovelox e ti chiede di riscrivere la parte che calcola la multa. La legge è l'articolo 142 del Codice della Strada, che prevede importi crescenti in base a **di quanto** si supera il limite, e per questo lab si usano gli importi minimi.

Il testo di legge parla di eccessi "non oltre 10 km/h", "oltre 10 e non oltre 40", "oltre 40 e non oltre 60" e "oltre 60". Chi rispetta il limite non paga nulla. Le parole "non oltre" e "oltre" decidono da che parte cade chi va esattamente 10 km/h sopra il limite, e la differenza tra 36 e 148 euro per un automobilista la fa il tuo confronto.

Scrivi il programma che, data la velocità rilevata e il limite del tratto, calcola l'importo della sanzione.
