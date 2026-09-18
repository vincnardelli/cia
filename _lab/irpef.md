---
layout: lab
title: IRPEF 2025 vs 2026
modulo: 2
order: 6
difficolta: facile
language: R
ai_mode: 'on'
objective: Calcolare l'IRPEF lorda con gli scaglioni 2025 e con la proposta 2026, e la differenza tra le due.
inputs:
- name: reddito
  type: numero
  desc: reddito complessivo annuo, euro
risultato:
  name: differenza
  type: numero
  desc: IRPEF 2026 − IRPEF 2025, in euro, 2 decimali
regole: |
  Aliquote per scaglione (ogni fascia tassa **solo la parte di reddito che ci cade dentro**):

  | scaglione | 2025 | 2026 (proposta) |
  |---|---|---|
  | fino a 15.000 € | 23% | 20% |
  | da 15.001 a 28.000 € | 23% | 23% |
  | da 28.001 a 50.000 € | 35% | 36% |
  | da 50.001 a 75.000 € | 43% | 40% |
  | da 75.001 a 120.000 € | 43% | 43% |
  | oltre 120.000 € | 43% | 46% |

  - Calcola `imposta_2025` e `imposta_2026`, poi `differenza <- imposta_2026 - imposta_2025` (negativa se il 2026 conviene).
  - Arrotonda la differenza a due decimali.
skeleton: |
  reddito <- 45000

  # ...
  if (reddito <= 15000) {
    # ...
  } else if (reddito <= 28000) {
    # ...
  } else if (reddito <= 50000) {
    # ...
  } else if (reddito <= 75000) {
    # ...
  } else if (reddito <= 120000) {
    # ...
  } else {
    # ...
  }
  # ...
  if (reddito <= 15000) {
    # ...
  } else if (reddito <= 28000) {
    # ...
  } else if (reddito <= 50000) {
    # ...
  } else if (reddito <= 75000) {
    # ...
  } else if (reddito <= 120000) {
    # ...
  } else {
    # ...
  }

  print(differenza)
tests:
- inputs:
    reddito: 45000
  expected: -280.0
  visible: true
- inputs:
    reddito: 10000
  expected: -300.0
  visible: true
- inputs:
    reddito: 15000
  expected: -450.0
  visible: false
  boundary: true
  hint: '15.000 esatti stanno tutti nel primo scaglione: nel 2026 al 20%.'
- inputs:
    reddito: 28000
  expected: -450.0
  visible: false
  boundary: true
  hint: A 28.000 non c'è ancora nessun euro tassato al 35%/36%.
- inputs:
    reddito: 50000
  expected: -230.0
  visible: false
  boundary: true
- inputs:
    reddito: 75000
  expected: -980.0
  visible: false
  boundary: true
- inputs:
    reddito: 120000
  expected: -980.0
  visible: false
  boundary: true
- inputs:
    reddito: 0
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Reddito zero: imposta zero in entrambi gli anni, differenza zero.'
- inputs:
    reddito: 200000
  expected: 1420.0
  visible: false
solution: |
  reddito <- 45000

  # IRPEF 2025
  if (reddito <= 15000) {
    imposta_2025 <- reddito * 0.23
  } else if (reddito <= 28000) {
    imposta_2025 <- 15000 * 0.23 + (reddito - 15000) * 0.23
  } else if (reddito <= 50000) {
    imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (reddito - 28000) * 0.35
  } else if (reddito <= 75000) {
    imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.35 + (reddito - 50000) * 0.43
  } else if (reddito <= 120000) {
    imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.35 +
      (75000 - 50000) * 0.43 + (reddito - 75000) * 0.43
  } else {
    imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.35 +
      (75000 - 50000) * 0.43 + (120000 - 75000) * 0.43 + (reddito - 120000) * 0.43
  }

  aliquota_totale_2025 <- (imposta_2025 / reddito) * 100



  # IRPEF 2026 (PROPOSTA)
  if (reddito <= 15000) {
    imposta_2026 <- reddito * 0.20
  } else if (reddito <= 28000) {
    imposta_2026 <- 15000 * 0.20 + (reddito - 15000) * 0.23
  } else if (reddito <= 50000) {
    imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (reddito - 28000) * 0.36
  } else if (reddito <= 75000) {
    imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.36 + (reddito - 50000) * 0.40
  } else if (reddito <= 120000) {
    imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.36 +
      (75000 - 50000) * 0.40 + (reddito - 75000) * 0.43
  } else {
    imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.36 +
      (75000 - 50000) * 0.40 + (120000 - 75000) * 0.43 + (reddito - 120000) * 0.46
  }


  differenza <- round(imposta_2026 - imposta_2025, 2)
  differenza
solution_after: ''
---

Un commercialista vuole mostrare ai clienti, con un numero, cosa cambierebbe per loro con la **riforma delle aliquote IRPEF** in discussione. Ti chiede un programma che, dato il reddito imponibile annuo, calcoli l'imposta lorda con gli scaglioni del 2025 e con quelli proposti per il 2026, e restituisca la differenza (negativa se con il 2026 si paga meno).

L'IRPEF è **progressiva a scaglioni**: ogni aliquota si applica solo alla parte di reddito che cade in quella fascia, non all'intero reddito. Nel 2025 le fasce sono: fino a 15.000 € al 23%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 35%, oltre 50.000 al 43%. Nella proposta 2026: fino a 15.000 al 20%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 36%, da 50.001 a 75.000 al 40%, da 75.001 a 120.000 al 43%, oltre 120.000 al 46%.

Il commercialista userà il numero per decidere a chi mandare la newsletter, quindi la differenza deve essere esatta al centesimo, e deve tornare anche per chi guadagna esattamente 15.000, 28.000 o 50.000 euro.
