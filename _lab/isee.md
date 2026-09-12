---
layout: lab
title: ISEE semplificato
week: 2
order: 8
level: sfida
language: R
ai_mode: 'on'
objective: Calcolare un ISEE semplificato di una famiglia a partire da reddito, patrimonio e numero di componenti.
inputs:
- name: reddito
  type: numero
  desc: reddito familiare annuo
- name: patrimonio
  type: numero
  desc: patrimonio mobiliare e immobiliare
- name: componenti
  type: numero
  desc: persone nel nucleo (intero ≥ 1)
output:
  name: isee
  type: numero
  desc: ISEE, 2 decimali
skeleton: |
  reddito <- 30000
  patrimonio <- 50000
  componenti <- 3

  # alla fine deve esistere la variabile isee
tests:
- inputs:
    reddito: 30000
    patrimonio: 50000
    componenti: 3
  expected: 19607.84
  visible: true
- inputs:
    reddito: 30000
    patrimonio: 0
    componenti: 1
  expected: 30000.0
  visible: false
  boundary: true
- inputs:
    reddito: 30000
    patrimonio: 0
    componenti: 5
  expected: 10526.32
  visible: false
  boundary: true
- inputs:
    reddito: 30000
    patrimonio: 0
    componenti: 6
  expected: 9375.0
  visible: false
  boundary: true
- inputs:
    reddito: 30000
    patrimonio: 0
    componenti: 8
  expected: 7692.31
  visible: false
- inputs:
    reddito: 0
    patrimonio: 100000
    componenti: 2
  expected: 12738.85
  visible: false
solution: |
  reddito <- 30000
  patrimonio <- 50000
  componenti <- 3

  ise <- reddito + 0.2 * patrimonio
  if(componenti == 1){
    scala <- 1
  }else if(componenti == 2){
    scala <- 1.57
  }else if(componenti == 3){
    scala <- 2.04
  }else if(componenti == 4){
    scala <- 2.46
  }else{
    scala <- 2.85 + (componenti - 5) * 0.35
  }
  isee <- round(ise / scala, 2)
  isee
solution_after: ''
---

- L'indicatore della situazione economica è `ISE = reddito + 20% del patrimonio`.
- La scala di equivalenza dipende dai componenti: 1 → 1,00; 2 → 1,57; 3 → 2,04; 4 → 2,46; 5 → 2,85; **oltre 5, +0,35 per ogni componente in più**.
- `ISEE = ISE / scala`, arrotondato a due decimali.
