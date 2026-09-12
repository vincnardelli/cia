---
layout: lab
title: Portafoglio
week: 3
order: 5
level: extra
language: R
ai_mode: 'on'
objective: Calcolare il valore finale di 100 € investiti, dato il vettore dei rendimenti giornalieri.
inputs:
- name: rendimenti
  type: vettore di numeri
  desc: rendimento di ogni giorno in frazione, es. 0.01 = +1%
output:
  name: valore_finale
  type: numero
  desc: valore dei 100 € iniziali alla fine, 2 decimali
skeleton: |
  rendimenti <- c(0.01, -0.02, 0.03)

  # alla fine deve esistere la variabile valore_finale
tests:
- inputs:
    rendimenti:
    - 0.01
    - -0.02
    - 0.03
  expected: 101.95
  visible: true
- inputs:
    rendimenti:
    - 0.1
    - 0.1
  expected: 121.0
  visible: true
- inputs:
    rendimenti:
    - 0.05
  expected: 105.0
  visible: false
  boundary: true
  hint: 'Un solo giorno: il ciclo deve funzionare anche con un vettore di lunghezza 1.'
- inputs:
    rendimenti:
    - 0.2
    - -1
    - 0.5
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Dopo un −100% il valore è zero e resta zero: 0 × 1,5 = 0.'
- inputs:
    rendimenti:
    - 0
    - 0
    - 0
  expected: 100.0
  visible: false
  boundary: true
- inputs:
    rendimenti:
    - -0.5
    - 1
  expected: 100.0
  visible: false
solution: |
  rendimenti <- c(0.01, -0.02, 0.03)

  valore_finale <- 100
  for(i in 1:length(rendimenti)){
    valore_finale <- valore_finale * (1 + rendimenti[i])
  }
  valore_finale <- round(valore_finale, 2)
  valore_finale
solution_after: ''
---

- Si parte da 100 €. Ogni giorno il valore viene moltiplicato per `(1 + rendimento)` di quel giorno.
- Un rendimento di −1 (−100%) azzera il capitale: da lì in poi resta zero.
- Arrotonda a due decimali. Fallo con un ciclo `for`; se conosci `prod()` usalo per controllare.
