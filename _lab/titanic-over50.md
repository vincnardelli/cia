---
layout: lab
title: 'Titanic: gli over 50'
modulo: 4
order: 2
difficolta: facile
language: R
ai_mode: 'off'
objective: Quante persone con più di 50 anni erano a bordo del Titanic?
inputs:
- name: titanic
  type: data frame
  desc: 'già caricato: titanic.csv (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)'
risultato:
  name: n_over50
  type: numero
  desc: passeggeri con Age > 50
data_url: dati/titanic.csv
data_var: titanic
packages:
- dplyr
regole: |
  - Conta i passeggeri con `Age > 50` (età nota).
  - Estrai il numero dalla tabella di `summarise()`.
  - Poi, in RStudio, continua con le altre domande del modulo: la percentuale di uomini e donne tra gli over 50 (percentuale *rispetto a chi?*).
skeleton: |
  library(dplyr)
  # titanic è già caricato (in RStudio: titanic <- read.csv("titanic.csv"))


  print(n_over50)
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

Il dataset dei passeggeri del Titanic è il classico su cui tutti imparano a leggere una tabella, e per questo lo usiamo. Il data frame `titanic` è già caricato: una riga per passeggero, con le colonne PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.

La prima domanda è semplice: **quante persone con più di 50 anni** erano a bordo? Il conteggio riguarda chi ha l'età nota; 177 passeggeri non ce l'hanno, e vanno lasciati fuori consapevolmente. Il risultato deve essere un numero estratto dalla tabella che ottieni con dplyr.

Poi, in RStudio, continua con le altre domande del modulo: la percentuale di uomini e donne tra gli over 50, chiedendoti sempre "percentuale rispetto a chi?".
