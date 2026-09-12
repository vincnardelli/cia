---
layout: lab
title: Piano di risparmio
week: 1
order: 4
level: sfida
language: R
ai_mode: 'on'
objective: Calcolare quanto si accumula versando ogni anno una somma fissa su un conto a interesse composto.
inputs:
- name: capitale
  type: numero
  desc: somma iniziale
- name: versamento
  type: numero
  desc: versato alla fine di ogni anno
- name: tasso
  type: numero
  desc: tasso annuo in percentuale
- name: anni
  type: numero
  desc: anni (intero)
output:
  name: montante
  type: numero
  desc: somma finale, 2 decimali
skeleton: |
  capitale <- 1000
  versamento <- 100
  tasso <- 2
  anni <- 3

  # alla fine deve esistere la variabile montante
tests:
- inputs:
    capitale: 1000
    versamento: 100
    tasso: 2
    anni: 3
  expected: 1367.25
  visible: true
- inputs:
    capitale: 0
    versamento: 1200
    tasso: 4
    anni: 10
  expected: 14407.33
  visible: false
- inputs:
    capitale: 1000
    versamento: 100
    tasso: 2
    anni: 0
  expected: 1000.0
  visible: false
  boundary: true
- inputs:
    capitale: 500
    versamento: 0
    tasso: 3
    anni: 5
  expected: 579.64
  visible: false
  boundary: true
- inputs:
    capitale: 1000
    versamento: 100
    tasso: 0
    anni: 4
  expected: 1400.0
  visible: false
  boundary: true
solution: |
  capitale <- 1000
  versamento <- 100
  tasso <- 2
  anni <- 3

  montante <- capitale
  if(anni > 0){
    for(i in 1:anni){
      montante <- montante * (1 + tasso/100) + versamento
    }
  }
  montante <- round(montante, 2)
  montante
solution_after: ''
---

- Ogni anno, nell'ordine: il saldo cresce del tasso, poi si aggiunge il versamento.
- Con zero anni non succede nulla: il montante è il capitale iniziale.
- Non esiste una formula "già vista" nel corso: serve ripetere il passo per ogni anno (o trovare la formula da soli).
