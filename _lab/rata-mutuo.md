---
layout: lab
title: Rata del mutuo
week: 3
order: 6
level: extra
language: R
ai_mode: 'on'
objective: Scrivere la funzione `rata(capitale, tasso, anni)` che calcola la rata mensile di un mutuo a rata costante.
inputs:
- name: capitale
  type: numero
  desc: importo del mutuo
- name: tasso
  type: numero
  desc: tasso annuo in percentuale, es. 4 per il 4%
- name: anni
  type: numero
  desc: durata in anni
output:
  name: rata
  type: numero
  desc: rata mensile, 2 decimali
function: rata
skeleton: |
  rata <- function(capitale, tasso, anni){
    # calcola e restituisci la rata mensile

  }

  # prova: rata(150000, 4, 25)
tests:
- inputs:
    capitale: 150000
    tasso: 4
    anni: 25
  expected: 791.76
  visible: true
- inputs:
    capitale: 10000
    tasso: 6
    anni: 1
  expected: 860.66
  visible: true
- inputs:
    capitale: 12000
    tasso: 0
    anni: 1
  expected: 1000.0
  visible: false
  boundary: true
  hint: 'Tasso zero: la formula dà NaN (0/0). Serve un caso a parte: capitale diviso numero di rate.'
- inputs:
    capitale: 100000
    tasso: 0.5
    anni: 30
  expected: 299.19
  visible: false
- inputs:
    capitale: 5000
    tasso: 12
    anni: 2
  expected: 235.37
  visible: false
solution: |
  rata <- function(capitale, tasso, anni){
    n <- anni * 12
    if(tasso == 0){
      importo <- capitale / n
    }else{
      i <- tasso / 100 / 12
      importo <- capitale * i / (1 - (1 + i)^(-n))
    }
    return(round(importo, 2))
  }

  rata(150000, 4, 25)
solution_after: ''
---

- Tasso mensile `i = tasso/100/12`, numero di rate `n = anni * 12`.
- Formula della rata costante (ammortamento "alla francese"): `rata = capitale * i / (1 - (1 + i)^(-n))`.
- **Se il tasso è zero** la formula divide per zero: in quel caso la rata è semplicemente `capitale / n`.
- Restituisci la rata arrotondata a due decimali.
