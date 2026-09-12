---
layout: lab
title: 'Finanza: due banche'
week: 5
order: 2
level: extra
language: R
ai_mode: 'on'
objective: Misurare quanto i rendimenti di Intesa e Unicredit si muovono insieme.
inputs:
- name: returns
  type: data frame
  desc: 'già caricato: finanza.csv'
output:
  name: correlazione
  type: numero
  desc: coefficiente di correlazione tra Intesa e Unicredit (3 decimali)
data_url: dati/finanza.csv
data_var: returns
tolerance: 0.002
skeleton: |
  # returns è già caricato

  # alla fine deve esistere la variabile correlazione
tests:
- inputs: {}
  expected: 0.807
  visible: true
  hint: 'La correlazione è simmetrica: cor(Intesa, Unicredit) = cor(Unicredit, Intesa). Se ottieni un numero diverso, forse hai preso una colonna sbagliata.'
solution: |
  correlazione <- round(cor(returns$Intesa, returns$Unicredit), 3)
  correlazione
solution_after: ''
---

- `cor(x, y)` misura quanto due serie salgono e scendono insieme: da −1 a +1.
- Calcola la correlazione tra `Intesa` e `Unicredit` e arrotonda a 3 decimali.
- Poi in RStudio fai il grafico a dispersione con ggplot2 e confronta con la coppia Ferrari–Enel.
