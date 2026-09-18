---
layout: lab
title: ISEE semplificato
modulo: 2
order: 8
difficolta: difficile
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
risultato:
  name: isee
  type: numero
  desc: ISEE, 2 decimali
regole: |
  - L'indicatore della situazione economica è `ISE = reddito + 20% del patrimonio`.
  - La scala di equivalenza dipende dai componenti: 1 → 1,00; 2 → 1,57; 3 → 2,04; 4 → 2,46; 5 → 2,85; **oltre 5, +0,35 per ogni componente in più**.
  - `ISEE = ISE / scala`, arrotondato a due decimali.
skeleton: |
  reddito <- 30000
  patrimonio <- 50000
  componenti <- 3

  print(isee)
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

Il CAF del quartiere è sommerso di richieste per le agevolazioni scolastiche, e ti chiede uno strumento che dia alle famiglie una **stima dell'ISEE** prima dell'appuntamento. È una versione semplificata, ma segue la logica vera dell'indicatore.

Si parte dall'ISE, l'indicatore della situazione economica: il reddito annuo della famiglia più il **20% del patrimonio** (conti, case, risparmi). Poi l'ISE si divide per una **scala di equivalenza** che tiene conto di quante persone vivono dei quegli stessi soldi: un componente vale 1,00; due componenti 1,57; tre 2,04; quattro 2,46; cinque 2,85; e per ogni componente oltre il quinto si aggiungono 0,35 alla scala. Il risultato, l'ISEE, va arrotondato a due decimali.

Scrivi il programma che, dati reddito, patrimonio e numero di componenti, calcola l'ISEE. Le famiglie numerose sono quelle che più spesso hanno diritto alle agevolazioni: assicurati che la regola "oltre cinque" torni per sei, sette, otto persone.
