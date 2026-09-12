---
layout: lab
title: Autovelox con punti patente
week: 2
order: 4
level: extra
language: R
ai_mode: 'off'
objective: 'Estendere l''autovelox: oltre alla sanzione, calcolare i punti patente rimasti dopo la decurtazione.'
inputs:
- name: velocita
  type: numero
- name: limite
  type: numero
- name: punti_iniziali
  type: numero
  desc: punti sulla patente prima della multa
output:
  name: punti_finali
  type: numero
  desc: punti rimasti (mai sotto zero)
skeleton: |
  velocita <- 75
  limite <- 50
  punti_iniziali <- 20

  # alla fine deve esistere la variabile punti_finali
tests:
- inputs:
    velocita: 75
    limite: 50
    punti_iniziali: 20
  expected: 17
  visible: true
- inputs:
    velocita: 55
    limite: 50
    punti_iniziali: 20
  expected: 20
  visible: true
- inputs:
    velocita: 60
    limite: 50
    punti_iniziali: 20
  expected: 20
  visible: false
  boundary: true
- inputs:
    velocita: 90
    limite: 50
    punti_iniziali: 20
  expected: 17
  visible: false
  boundary: true
- inputs:
    velocita: 120
    limite: 50
    punti_iniziali: 4
  expected: 0
  visible: false
  boundary: true
  hint: Con 4 punti e una decurtazione di 10 il risultato deve essere 0, non −6.
- inputs:
    velocita: 111
    limite: 50
    punti_iniziali: 10
  expected: 0
  visible: false
  boundary: true
solution: |
  velocita <- 75
  limite <- 50
  punti_iniziali <- 20

  differenza <- velocita - limite
  if(differenza <= 10){
    decurtazione <- 0
  }else if(differenza <= 40){
    decurtazione <- 3
  }else if(differenza <= 60){
    decurtazione <- 6
  }else{
    decurtazione <- 10
  }
  punti_finali <- punti_iniziali - decurtazione
  if(punti_finali < 0){
    punti_finali <- 0
  }
  punti_finali
solution_after: ''
---

- Fasce come nell'Autovelox: entro il limite o non oltre 10 km/h → nessuna decurtazione; oltre 10 e non oltre 40 → 3 punti; oltre 40 e non oltre 60 → 6 punti; oltre 60 → 10 punti.
- I punti non possono scendere sotto zero.
