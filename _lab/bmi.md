---
layout: lab
title: Classificazione BMI
week: 3
order: 1
level: base
language: R
ai_mode: 'off'
objective: Calcolare l'indice di massa corporea di un paziente e classificarlo secondo le fasce del Ministero della Salute.
inputs:
- name: altezza
  type: numero
  desc: in metri
- name: peso
  type: numero
  desc: in kg
output:
  name: classificazione
  type: testo
  desc: una delle sei categorie, scritta esattamente come nella tabella
skeleton: |
  altezza <- 1.73
  peso <- 86

  # alla fine deve esistere la variabile classificazione (testo)
tests:
- inputs:
    altezza: 1.73
    peso: 86
  expected: Sovrappeso
  visible: true
- inputs:
    altezza: 1.81
    peso: 60
  expected: Sottopeso
  visible: true
- inputs:
    altezza: 2
    peso: 100
  expected: Sovrappeso
  visible: false
  boundary: true
  hint: 'BMI esattamente 25: la tabella dice 25 ≤ BMI < 30 → Sovrappeso. Se il tuo codice dice Normopeso, guarda il confronto sulla soglia.'
- inputs:
    altezza: 2
    peso: 74
  expected: Normopeso
  visible: false
  boundary: true
  hint: 'BMI 18,5 esatto: è Normopeso, perché la soglia 18,5 è compresa nel normopeso.'
- inputs:
    altezza: 2
    peso: 120
  expected: Obesità grado I
  visible: false
  boundary: true
- inputs:
    altezza: 2
    peso: 140
  expected: Obesità grado II
  visible: false
  boundary: true
- inputs:
    altezza: 2
    peso: 160
  expected: Obesità grado III
  visible: false
  boundary: true
- inputs:
    altezza: 1.6
    peso: 45
  expected: Sottopeso
  visible: false
solution: |
  altezza <- 1.73
  peso <- 86

  bmi <- peso / altezza^2

  if(bmi < 18.5){
    classificazione <- "Sottopeso"
  }else if(bmi < 25){
    classificazione <- "Normopeso"
  }else if(bmi < 30){
    classificazione <- "Sovrappeso"
  }else if(bmi < 35){
    classificazione <- "Obesità grado I"
  }else if(bmi < 40){
    classificazione <- "Obesità grado II"
  }else{
    classificazione <- "Obesità grado III"
  }
  classificazione
solution_after: ''
---

- `BMI = peso / altezza^2`.
- Sottopeso: BMI < 18,5 · Normopeso: 18,5 ≤ BMI < 25 · Sovrappeso: 25 ≤ BMI < 30 · Obesità grado I: 30 ≤ BMI < 35 · Obesità grado II: 35 ≤ BMI < 40 · Obesità grado III: BMI ≥ 40.
- Le categorie vanno scritte così: `"Sottopeso"`, `"Normopeso"`, `"Sovrappeso"`, `"Obesità grado I"`, `"Obesità grado II"`, `"Obesità grado III"`.
- Poi, in RStudio, applica lo stesso codice a più pazienti con un ciclo `for` (la verifica qui controlla un paziente alla volta).
