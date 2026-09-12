---
layout: lab
title: Boomer finder
week: 2
order: 1
level: base
language: R
ai_mode: 'off'
objective: Stabilire se una persona è un baby boomer a partire dall'anno di nascita.
inputs:
- name: anno
  type: numero
  desc: anno di nascita
output:
  name: status
  type: testo
  desc: '"Boomer" oppure "Non Boomer"'
skeleton: |
  anno <- 1955

  # alla fine deve esistere la variabile status ("Boomer" o "Non Boomer")
tests:
- inputs:
    anno: 1955
  expected: Boomer
  visible: true
- inputs:
    anno: 2006
  expected: Non Boomer
  visible: true
- inputs:
    anno: 1946
  expected: Boomer
  visible: false
  boundary: true
  hint: 'Il 1946 è compreso: chi è nato quell''anno è boomer. Il tuo confronto usa < oppure <=?'
- inputs:
    anno: 1964
  expected: Boomer
  visible: false
  boundary: true
  hint: Anche il 1964 è compreso. Controlla il confronto sull'estremo superiore.
- inputs:
    anno: 1945
  expected: Non Boomer
  visible: false
  boundary: true
- inputs:
    anno: 1965
  expected: Non Boomer
  visible: false
  boundary: true
solution: |
  anno <- 1955

  if(anno >= 1946 & anno <= 1964){
    status <- "Boomer"
  }else{
    status <- "Non Boomer"
  }
  status
solution_after: ''
---

- È boomer chi è nato **dal 1946 al 1964 compresi**.
- Tutti gli altri sono "Non Boomer".
- Scrivilo in almeno due modi diversi (con due `if`, con `&`, con `%in%`) e controlla che diano lo stesso risultato sui casi al confine.
