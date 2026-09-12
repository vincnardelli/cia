---
layout: lab
title: 'Titanic: sopravvivenza in prima classe'
week: 4
order: 3
level: extra
language: R
ai_mode: 'on'
objective: Qual è la percentuale di sopravvissuti tra i passeggeri di prima classe?
inputs:
- name: titanic
  type: data frame
  desc: 'già caricato: titanic.csv'
output:
  name: perc_prima
  type: numero
  desc: quota di sopravvissuti in prima classe, tra 0 e 1 (3 decimali)
data_url: dati/titanic.csv
data_var: titanic
packages:
- dplyr
tolerance: 0.002
skeleton: |
  library(dplyr)
  # titanic è già caricato

  # alla fine deve esistere la variabile perc_prima (un numero tra 0 e 1)
tests:
- inputs: {}
  expected: 0.63
  visible: true
  hint: 'La percentuale è calcolata *dentro* la classe (denominatore: i passeggeri di prima classe), non sul totale dei sopravvissuti.'
solution: |
  library(dplyr)

  tabella <- titanic %>%
    group_by(Pclass) %>%
    summarise(perc = mean(Survived))
  perc_prima <- round(tabella$perc[tabella$Pclass == 1], 3)
  perc_prima
solution_after: ''
---

- `Survived` vale 1 se sopravvissuto, 0 altrimenti: la **media** di Survived è già la percentuale.
- Raggruppa per `Pclass`, calcola la media per classe, poi estrai il valore della classe 1.
- Confronta con la terza classe: la differenza è il punto della domanda.
