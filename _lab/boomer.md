---
layout: lab
title: Boomer finder
modulo: 2
order: 1
difficolta: facile
language: R
ai_mode: 'off'
objective: Stabilire se una persona è un baby boomer a partire dall'anno di nascita.
inputs:
- name: anno
  type: numero
  desc: anno di nascita
risultato:
  name: status
  type: testo
  desc: '"Boomer" oppure "Non Boomer"'
regole: |
  - È boomer chi è nato **dal 1946 al 1964 compresi**.
  - Tutti gli altri sono "Non Boomer".
  - Scrivilo in almeno due modi diversi (con due `if`, con `&`, con `%in%`) e controlla che diano lo stesso risultato sui casi al confine.
skeleton: |
  anno <- 1955

  if(anno >= 1946 & anno <= 1964){
    # ...
  }else{
    # ...
  }

  print(status)
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

Un'agenzia di marketing sta preparando una campagna pensata per i *baby boomer*, la generazione nata nel dopoguerra. Per segmentare l'elenco clienti servono regole precise, e la definizione che l'agenzia adotta è quella demografica standard: è boomer chi è nato **dal 1946 al 1964, estremi compresi**.

Ti passano una colonna con l'anno di nascita di ogni cliente e ti chiedono un programma che, dato l'anno, risponda "Boomer" oppure "Non Boomer" (scritti esattamente così, perché poi il testo finisce in un filtro automatico).

Il punto delicato è ai bordi: chi è nato nel 1946 o nel 1964 è dentro. Il capo dell'agenzia è pignolo e vuole che tu lo scriva in almeno due modi diversi, per controllare che diano lo stesso risultato proprio su quegli anni.
