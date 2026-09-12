---
layout: lab
title: Scontrino
week: 1
order: 1
level: base
language: R
ai_mode: 'off'
objective: Calcolare il totale di uno scontrino a partire dal prezzo netto e dalla quantità, con IVA al 22%.
inputs:
- name: prezzo_netto
  type: numero
  desc: prezzo unitario senza IVA, in euro
- name: quantita
  type: numero
  desc: pezzi acquistati
output:
  name: totale
  type: numero
  desc: totale da pagare, arrotondato a 2 decimali
skeleton: |
  prezzo_netto <- 10
  quantita <- 3

  # calcola il totale con IVA al 22%: alla fine deve esistere la variabile totale
tests:
- inputs:
    prezzo_netto: 10
    quantita: 3
  expected: 36.6
  visible: true
- inputs:
    prezzo_netto: 19.9
    quantita: 1
  expected: 24.28
  visible: true
- inputs:
    prezzo_netto: 10
    quantita: 0
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Con zero pezzi il totale deve essere 0: il tuo codice lo gestisce senza bisogno di un caso speciale?'
- inputs:
    prezzo_netto: 0.99
    quantita: 7
  expected: 8.45
  visible: false
  boundary: true
  hint: 'Con i centesimi l''arrotondamento conta: hai usato round(x, 2) sul totale finale, non sul prezzo unitario?'
- inputs:
    prezzo_netto: 1234.5
    quantita: 2
  expected: 3012.18
  visible: false
solution: |
  prezzo_netto <- 10
  quantita <- 3

  netto <- prezzo_netto * quantita
  iva <- netto * 0.22
  totale <- round(netto + iva, 2)
  totale
solution_after: ''
---

- Il totale netto è `prezzo_netto * quantita`.
- L'IVA è il 22% del totale netto: il totale da pagare è il netto più l'IVA.
- Arrotonda il risultato a due decimali con `round(x, 2)`.
