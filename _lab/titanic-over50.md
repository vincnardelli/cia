---
layout: lab
title: 'Titanic: gli over 50'
week: 4
order: 2
level: base
language: R
ai_mode: 'off'
objective: Quante persone con più di 50 anni erano a bordo del Titanic?
inputs:
- name: titanic
  type: data frame
  desc: 'già caricato: titanic.csv (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)'
output:
  name: n_over50
  type: numero
  desc: passeggeri con Age > 50
data_url: dati/titanic.csv
data_var: titanic
packages:
- dplyr
skeleton: |
  library(dplyr)
  # titanic è già caricato

  # alla fine deve esistere la variabile n_over50 (un numero)
tests:
- inputs: {}
  expected: 64
  visible: true
  hint: '177 passeggeri non hanno l''età: filter(Age > 50) li scarta da solo, ma devi saperlo e dirlo.'
solution: |
  library(dplyr)

  risultato <- titanic %>%
    filter(!is.na(Age), Age > 50) %>%
    summarise(n = n())
  n_over50 <- risultato$n
  n_over50
solution_after: ''
---

- Conta i passeggeri con `Age > 50` (età nota).
- Estrai il numero dalla tabella di `summarise()`.
- Poi, in RStudio, continua con le altre domande della settimana: la percentuale di uomini e donne tra gli over 50 (percentuale *rispetto a chi?*).
