---
layout: lab
title: Classificazione BMI
modulo: 3
order: 1
difficolta: facile
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
risultato:
  name: classificazione
  type: testo
  desc: una delle sei categorie, scritta esattamente come nella tabella
regole: |
  - `BMI = peso / altezza^2`.
  - Sottopeso: BMI < 18,5 · Normopeso: 18,5 ≤ BMI < 25 · Sovrappeso: 25 ≤ BMI < 30 · Obesità grado I: 30 ≤ BMI < 35 · Obesità grado II: 35 ≤ BMI < 40 · Obesità grado III: BMI ≥ 40.
  - Le categorie vanno scritte così: `"Sottopeso"`, `"Normopeso"`, `"Sovrappeso"`, `"Obesità grado I"`, `"Obesità grado II"`, `"Obesità grado III"`.
  - Poi, in RStudio, applica lo stesso codice a più pazienti con un ciclo `for` (la verifica qui controlla un paziente alla volta).
skeleton: |
  altezza <- 1.73
  peso <- 86

  # ...
  if(bmi < 18.5){
    # ...
  }else if(bmi < 25){
    # ...
  }else if(bmi < 30){
    # ...
  }else if(bmi < 35){
    # ...
  }else if(bmi < 40){
    # ...
  }else{
    # ...
  }

  print(classificazione)
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

Uno studio medico vuole aggiungere alla cartella digitale dei pazienti la **classificazione automatica del peso** secondo le fasce del Ministero della Salute. L'indice di massa corporea (BMI) si calcola come peso in kg diviso il quadrato dell'altezza in metri, e in base al valore il paziente rientra in una di sei categorie.

Le fasce sono: Sottopeso sotto 18,5; Normopeso da 18,5 a 25 escluso; Sovrappeso da 25 a 30 escluso; Obesità grado I da 30 a 35 escluso; Obesità grado II da 35 a 40 escluso; Obesità grado III da 40 in su. Il medico userà il testo nella cartella, quindi le sei etichette vanno scritte esattamente così: "Sottopeso", "Normopeso", "Sovrappeso", "Obesità grado I", "Obesità grado II", "Obesità grado III".

Scrivi il programma che, dati altezza e peso, restituisce la categoria. Un paziente con BMI esattamente 25 è sovrappeso, non normopeso: le soglie appartengono alla fascia superiore.
