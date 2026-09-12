---
layout: lab
title: Interesse composto
week: 1
order: 3
level: extra
language: R
ai_mode: 'on'
objective: Calcolare il montante di un capitale investito a interesse composto per un certo numero di anni.
inputs:
- name: capitale
  type: numero
  desc: euro investiti
- name: tasso
  type: numero
  desc: tasso annuo in percentuale, es. 3 per il 3%
- name: anni
  type: numero
  desc: anni di investimento (intero)
output:
  name: montante
  type: numero
  desc: capitale finale, arrotondato a 2 decimali
skeleton: |
  capitale <- 1000
  tasso <- 3
  anni <- 2

  # alla fine deve esistere la variabile montante
tests:
- inputs:
    capitale: 1000
    tasso: 3
    anni: 2
  expected: 1060.9
  visible: true
- inputs:
    capitale: 5000
    tasso: 5
    anni: 10
  expected: 8144.47
  visible: true
- inputs:
    capitale: 1000
    tasso: 3
    anni: 0
  expected: 1000.0
  visible: false
  boundary: true
  hint: 'Con zero anni il montante è il capitale iniziale: qualunque numero elevato a 0 fa 1.'
- inputs:
    capitale: 1000
    tasso: 0
    anni: 5
  expected: 1000.0
  visible: false
  boundary: true
  hint: Con tasso zero il capitale non cambia. Hai diviso il tasso per 100 prima di sommarlo a 1?
- inputs:
    capitale: 250.5
    tasso: 1.5
    anni: 7
  expected: 278.02
  visible: false
solution: |
  capitale <- 1000
  tasso <- 3
  anni <- 2

  montante <- round(capitale * (1 + tasso/100)^anni, 2)
  montante
solution_after: ''
---

- Ogni anno il capitale cresce del tasso: `montante = capitale * (1 + tasso/100)^anni`.
- Attenzione: il tasso è dato in percentuale (3 significa 3%), non in frazione.
- Arrotonda a due decimali.
