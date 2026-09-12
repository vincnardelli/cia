---
layout: lab
title: Penali sulle fatture
week: 2
order: 7
level: extra
language: R
ai_mode: 'on'
objective: Calcolare il totale di una fattura pagata in ritardo, applicando le penali previste.
inputs:
- name: importo
  type: numero
  desc: importo della fattura
- name: giorni_ritardo
  type: numero
  desc: giorni di ritardo (intero, 0 se puntuale)
output:
  name: totale
  type: numero
  desc: importo più penale, 2 decimali
skeleton: |
  importo <- 1000
  giorni_ritardo <- 20

  # alla fine deve esistere la variabile totale
tests:
- inputs:
    importo: 1000
    giorni_ritardo: 20
  expected: 1050.0
  visible: true
- inputs:
    importo: 1000
    giorni_ritardo: 0
  expected: 1000.0
  visible: true
- inputs:
    importo: 1000
    giorni_ritardo: 10
  expected: 1000.0
  visible: false
  boundary: true
  hint: '10 giorni è ancora "entro 10": nessuna penale.'
- inputs:
    importo: 1000
    giorni_ritardo: 11
  expected: 1050.0
  visible: false
  boundary: true
- inputs:
    importo: 1000
    giorni_ritardo: 30
  expected: 1050.0
  visible: false
  boundary: true
- inputs:
    importo: 1000
    giorni_ritardo: 31
  expected: 1100.0
  visible: false
  boundary: true
- inputs:
    importo: 1000
    giorni_ritardo: 60
  expected: 1100.0
  visible: false
  boundary: true
- inputs:
    importo: 1000
    giorni_ritardo: 90
  expected: 1200.0
  visible: false
  boundary: true
  hint: 'A 90 giorni la penale è il 20% secco: il 2% al giorno parte dal 91°.'
- inputs:
    importo: 1000
    giorni_ritardo: 91
  expected: 1220.0
  visible: false
  boundary: true
  hint: '91 giorni: 20% + 2% × 1 giorno = 22%.'
- inputs:
    importo: 250
    giorni_ritardo: 100
  expected: 350.0
  visible: false
solution: |
  importo <- 1000
  giorni_ritardo <- 20

  if(giorni_ritardo <= 10){
    penale <- 0
  }else if(giorni_ritardo <= 30){
    penale <- 0.05
  }else if(giorni_ritardo <= 60){
    penale <- 0.10
  }else if(giorni_ritardo <= 90){
    penale <- 0.20
  }else{
    penale <- 0.20 + 0.02 * (giorni_ritardo - 90)
  }
  totale <- round(importo * (1 + penale), 2)
  totale
solution_after: ''
---

- entro 10 giorni di ritardo: nessuna penale;
- da 11 a 30 giorni: 5% dell'importo;
- da 31 a 60 giorni: 10%;
- da 61 a 90 giorni: 20%;
- oltre 90 giorni: 20% **più il 2% per ogni giorno oltre il 90°**.
