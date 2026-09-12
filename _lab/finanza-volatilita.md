---
layout: lab
title: 'Finanza: la volatilità'
week: 5
order: 1
level: base
language: R
ai_mode: 'off'
objective: Calcolare la volatilità (deviazione standard dei rendimenti giornalieri) del titolo Unicredit.
inputs:
- name: returns
  type: data frame
  desc: 'già caricato: finanza.csv (Ferrari, Enel, Intesa, Unicredit, day) con i rendimenti giornalieri del 2023'
output:
  name: volatilita
  type: numero
  desc: deviazione standard dei rendimenti di Unicredit (4 decimali)
data_url: dati/finanza.csv
data_var: returns
tolerance: 0.0002
skeleton: |
  # returns è già caricato

  # alla fine deve esistere la variabile volatilita
tests:
- inputs: {}
  expected: 0.0176
  visible: true
  hint: 'sd() usa n−1 al denominatore: è quella che vogliamo. Non c''è nessun NA, quindi non serve na.rm.'
solution: |
  volatilita <- round(sd(returns$Unicredit), 4)
  volatilita
solution_after: ''
---

- In finanza il rischio di un titolo si misura con la **variabilità** dei suoi rendimenti: `sd()`.
- Calcola `sd(returns$Unicredit)` e arrotonda a 4 decimali.
- In RStudio confronta le quattro azioni: quale ha il rendimento medio più alto? quale il rischio più alto? coincidono?
