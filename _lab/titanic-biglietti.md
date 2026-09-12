---
layout: lab
title: 'Titanic: biglietti condivisi'
week: 4
order: 4
level: sfida
language: R
ai_mode: 'on'
objective: Quanti biglietti erano associati a più di un passeggero?
inputs:
- name: titanic
  type: data frame
  desc: 'già caricato: titanic.csv'
output:
  name: n_condivisi
  type: numero
  desc: numero di codici Ticket con almeno 2 passeggeri
data_url: dati/titanic.csv
data_var: titanic
packages:
- dplyr
skeleton: |
  library(dplyr)
  # titanic è già caricato

  # alla fine deve esistere la variabile n_condivisi (un numero)
tests:
- inputs: {}
  expected: 134
  visible: false
  hint: 'Stai contando biglietti o passeggeri? Dopo il primo summarise ogni riga è un biglietto: contale con nrow() o n().'
solution: |
  library(dplyr)

  biglietti <- titanic %>%
    group_by(Ticket) %>%
    summarise(n = n()) %>%
    filter(n > 1)
  n_condivisi <- nrow(biglietti)
  n_condivisi
solution_after: ''
---

- Raggruppa per `Ticket`, conta i passeggeri per biglietto, tieni solo i biglietti con più di uno.
- Il risultato è il numero di **biglietti**, non di passeggeri.
- Servono due passaggi di conteggio: uno dentro i gruppi, uno sul risultato.
