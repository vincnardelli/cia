---
layout: lab
title: Tariffa del parcheggio
modulo: 2
order: 5
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare quanto si paga all'uscita di un parcheggio a partire dai minuti di sosta.
inputs:
- name: minuti
  type: numero
  desc: minuti di sosta, dall'ingresso all'uscita
risultato:
  name: costo
  type: numero
  desc: euro da pagare
regole: |
  - Fino a **30 minuti** la sosta è gratuita.
  - Oltre i 30 minuti si paga **1,50 € per ogni ora o frazione di ora**, contando dall'ingresso: 31 minuti sono una frazione della prima ora, 61 minuti sono già due ore.
  - Il **massimo giornaliero** è 12 €.
skeleton: |
  minuti <- 20

  if(minuti <= 30){
    # ...
  }else{
    # ...
    if(costo > 12){
      # ...
    }
  }

  print(costo)
tests:
- inputs:
    minuti: 20
  expected: 0
  visible: true
- inputs:
    minuti: 45
  expected: 1.5
  visible: true
- inputs:
    minuti: 150
  expected: 4.5
  visible: true
- inputs:
    minuti: 30
  expected: 0
  visible: false
  boundary: true
  hint: 30 minuti esatti sono ancora gratis ('fino a 30').
- inputs:
    minuti: 31
  expected: 1.5
  visible: false
  boundary: true
- inputs:
    minuti: 60
  expected: 1.5
  visible: false
  boundary: true
  hint: '60 minuti sono un''ora esatta, non due: ceiling(60/60) = 1.'
- inputs:
    minuti: 61
  expected: 3.0
  visible: false
  boundary: true
- inputs:
    minuti: 480
  expected: 12
  visible: false
  boundary: true
  hint: '8 ore fanno esattamente 12 €: il tetto non taglia nulla.'
- inputs:
    minuti: 600
  expected: 12
  visible: false
  hint: 10 ore farebbero 15 €, ma il massimo giornaliero è 12.
solution: |
  minuti <- 45

  if(minuti <= 30){
    costo <- 0
  }else{
    ore <- ceiling(minuti / 60)
    costo <- ore * 1.5
    if(costo > 12){
      costo <- 12
    }
  }
  costo
solution_after: ''
---

Il parcheggio del centro commerciale ha una cassa automatica e la società che lo gestisce ti chiede di riscrivere la regola che calcola l'importo all'uscita, perché quella vecchia sbagliava proprio sui casi che generano reclami.

La sosta è gratuita **fino a 30 minuti**. Oltre i 30 minuti si paga 1,50 euro **per ogni ora o frazione di ora**, contando dal momento dell'ingresso: chi resta 31 minuti paga una frazione della prima ora, cioè 1,50 euro; chi resta 61 minuti è già nella seconda ora e paga 3 euro; chi resta esattamente 60 minuti paga un'ora sola. C'è un **massimo giornaliero** di 12 euro, oltre il quale il contatore si ferma.

Scrivi il programma che, dati i minuti di sosta, calcola l'importo. In R l'arrotondamento per eccesso è `ceiling()`.
