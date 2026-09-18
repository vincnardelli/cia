---
layout: lab
title: Penali sulle fatture
modulo: 2
order: 7
difficolta: facile
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
risultato:
  name: totale
  type: numero
  desc: importo più penale, 2 decimali
regole: |
  - entro 10 giorni di ritardo: nessuna penale;
  - da 11 a 30 giorni: 5% dell'importo;
  - da 31 a 60 giorni: 10%;
  - da 61 a 90 giorni: 20%;
  - oltre 90 giorni: 20% **più il 2% per ogni giorno oltre il 90°**.
skeleton: |
  importo <- 1000
  giorni_ritardo <- 20

  if(giorni_ritardo <= 10){
    # ...
  }else if(giorni_ritardo <= 30){
    # ...
  }else if(giorni_ritardo <= 60){
    # ...
  }else if(giorni_ritardo <= 90){
    # ...
  }else{
    # ...
  }

  print(totale)
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

Nell'ufficio amministrativo di una piccola azienda ti chiedono di automatizzare il calcolo delle **penali per ritardato pagamento** che vanno aggiunte alle fatture dei clienti in ritardo. Le condizioni sono scritte nel contratto standard: entro 10 giorni di ritardo non si applica nulla; da 11 a 30 giorni si aggiunge il 5% dell'importo; da 31 a 60 giorni il 10%; da 61 a 90 giorni il 20%; oltre i 90 giorni si applica il 20% **più un 2% dell'importo per ogni giorno oltre il novantesimo**.

Il programma riceve l'importo della fattura e i giorni di ritardo e restituisce il totale da pagare (importo più penale), con due decimali. I clienti litigano sempre sui giorni di confine, il decimo, il trentesimo, il novantesimo: il tuo codice deve applicare esattamente ciò che dice il contratto.
