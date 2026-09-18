---
layout: lab
title: Biglietto del museo
modulo: 2
order: 4
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare il prezzo del biglietto di un museo civico in base a età, tessera studente e giorno.
inputs:
- name: eta
  type: numero
  desc: anni del visitatore
- name: studente
  type: logico
  desc: TRUE se ha la tessera studente
- name: prima_domenica
  type: logico
  desc: TRUE se è la prima domenica del mese
risultato:
  name: prezzo
  type: numero
  desc: 0, 8 oppure 15
regole: |
  - La **prima domenica del mese** l'ingresso è gratuito per tutti.
  - Negli altri giorni: gratis **sotto i 6 anni** e **dai 70 in su**; ridotto a 8 € **fino ai 18 anni compresi** oppure con tessera studente; intero 15 € per tutti gli altri.
  - Le condizioni vanno controllate nell'ordine giusto: prima i casi gratuiti, poi i ridotti.
skeleton: |
  eta <- 30
  studente <- FALSE
  prima_domenica <- FALSE

  if(prima_domenica){
    # ...
  }else if(eta < 6 | eta >= 70){
    # ...
  }else if(eta <= 18 | studente){
    # ...
  }else{
    # ...
  }

  print(prezzo)
tests:
- inputs:
    eta: 30
    studente: false
    prima_domenica: false
  expected: 15
  visible: true
- inputs:
    eta: 16
    studente: false
    prima_domenica: false
  expected: 8
  visible: true
- inputs:
    eta: 25
    studente: true
    prima_domenica: false
  expected: 8
  visible: true
- inputs:
    eta: 5
    studente: false
    prima_domenica: false
  expected: 0
  visible: false
  boundary: true
- inputs:
    eta: 6
    studente: false
    prima_domenica: false
  expected: 8
  visible: false
  boundary: true
  hint: '6 anni: non è più ''sotto i 6'', quindi paga il ridotto.'
- inputs:
    eta: 18
    studente: false
    prima_domenica: false
  expected: 8
  visible: false
  boundary: true
  hint: '18 anni compresi: ridotto.'
- inputs:
    eta: 19
    studente: false
    prima_domenica: false
  expected: 15
  visible: false
  boundary: true
- inputs:
    eta: 70
    studente: false
    prima_domenica: false
  expected: 0
  visible: false
  boundary: true
  hint: 'Dai 70 in su è gratis: 70 compreso.'
- inputs:
    eta: 69
    studente: false
    prima_domenica: false
  expected: 15
  visible: false
  boundary: true
- inputs:
    eta: 40
    studente: false
    prima_domenica: true
  expected: 0
  visible: false
- inputs:
    eta: 75
    studente: true
    prima_domenica: false
  expected: 0
  visible: false
  hint: 'Over 70 con tessera studente: vince il gratis, perché lo controlli prima.'
solution: |
  eta <- 30
  studente <- FALSE
  prima_domenica <- FALSE

  if(prima_domenica){
    prezzo <- 0
  }else if(eta < 6 | eta >= 70){
    prezzo <- 0
  }else if(eta <= 18 | studente){
    prezzo <- 8
  }else{
    prezzo <- 15
  }
  prezzo
solution_after: ''
---

Il museo civico della città ha una tariffa che gli addetti alla biglietteria sanno a memoria ma che il nuovo sito deve calcolare da solo. La **prima domenica del mese** l'ingresso è gratuito per tutti, chiunque sia il visitatore. Negli altri giorni, i bambini **sotto i 6 anni** e le persone **dai 70 anni in su** entrano gratis; **fino ai 18 anni compresi**, oppure con la tessera studente a qualunque età, il biglietto è ridotto a 8 euro; tutti gli altri pagano l'intero, 15 euro.

Scrivi il programma che, dati età, tessera studente (vero/falso) e prima domenica (vero/falso), restituisce il prezzo. L'ordine dei controlli conta: un settantacinquenne con tessera studente entra gratis, non a 8 euro, perché il gratuito viene prima del ridotto.
