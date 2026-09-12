---
layout: lab
title: Pricing dei voli
week: 2
order: 3
level: base
language: R
ai_mode: 'off'
objective: Calcolare il prezzo di un biglietto aereo in base a classe, giorni di anticipo e riempimento dell'aereo.
inputs:
- name: seat_type
  type: testo
  desc: '"Economy", "Premium" o "Business"'
- name: days_before
  type: numero
  desc: giorni di anticipo (intero)
- name: load_factor
  type: numero
  desc: riempimento tra 0 e 1
output:
  name: prezzo_finale
  type: numero
  desc: prezzo in euro, 2 decimali
skeleton: |
  seat_type   <- "Economy"
  days_before <- 5
  load_factor <- 0.82

  # alla fine deve esistere la variabile prezzo_finale
tests:
- inputs:
    seat_type: Economy
    days_before: 5
    load_factor: 0.82
  expected: 186.0
  visible: true
- inputs:
    seat_type: Business
    days_before: 90
    load_factor: 0.3
  expected: 277.0
  visible: true
- inputs:
    seat_type: Economy
    days_before: 60
    load_factor: 0.6
  expected: 115.0
  visible: false
  boundary: true
  hint: '60 giorni è "da 31 a 60": sconto del 10%, non del 20%.'
- inputs:
    seat_type: Economy
    days_before: 61
    load_factor: 0.6
  expected: 105.0
  visible: false
  boundary: true
- inputs:
    seat_type: Economy
    days_before: 15
    load_factor: 0.6
  expected: 125.0
  visible: false
  boundary: true
  hint: 15 giorni è ancora nella fascia 0%.
- inputs:
    seat_type: Economy
    days_before: 7
    load_factor: 0.6
  expected: 145.0
  visible: false
  boundary: true
- inputs:
    seat_type: Economy
    days_before: 3
    load_factor: 0.6
  expected: 165.0
  visible: false
  boundary: true
- inputs:
    seat_type: Premium
    days_before: 20
    load_factor: 0.5
  expected: 205.0
  visible: false
  boundary: true
  hint: '0.50 esatto è nella fascia "da 0.50 a 0.70": 0%.'
- inputs:
    seat_type: Premium
    days_before: 20
    load_factor: 0.7
  expected: 205.0
  visible: false
  boundary: true
- inputs:
    seat_type: Premium
    days_before: 20
    load_factor: 0.85
  expected: 232.0
  visible: false
  boundary: true
  hint: 0.85 esatto è ancora +15%; il +35% scatta solo *oltre* 0.85.
- inputs:
    seat_type: Economy
    days_before: 2
    load_factor: 0.86
  expected: 277.45
  visible: false
  boundary: true
  hint: 'Due giorni e aereo quasi pieno: scatta anche lo stress di mercato (+10%).'
- inputs:
    seat_type: Economy
    days_before: 2
    load_factor: 0.85
  expected: 220.5
  visible: false
  boundary: true
  hint: 'A 0.85 esatto lo stress NON scatta: la regola dice "supera 0.85".'
solution: |-
  # ===== INPUT =====
  seat_type   <- "Economy"   # "Economy", "Premium", "Business"
  days_before <- 5           # giorni prima della partenza
  load_factor <- 0.82        # tra 0 e 1

  # ===== BASE FARE PER TIPO POSTO =====
  if (seat_type == "Economy") {
    prezzo <- 100
  } else if (seat_type == "Premium") {
    prezzo <- 180
  } else if (seat_type == "Business") {
    prezzo <- 350
  }

  # ===== MOLTIPLICATORE PER ANTICIPO =====
  moltip_anticipo <- 1
  if (days_before > 60) {
    moltip_anticipo <- 0.80   # -20%
  } else if (days_before >= 31) {
    moltip_anticipo <- 0.90   # -10%
  } else if (days_before >= 15) {
    moltip_anticipo <- 1.00   #  0%
  } else if (days_before >= 7) {
    moltip_anticipo <- 1.20   # +20%
  } else if (days_before >= 3) {
    moltip_anticipo <- 1.40   # +40%
  } else { # 0-2 giorni
    moltip_anticipo <- 1.70   # +70%
  }

  # ===== MOLTIPLICATORE PER RIEMPIMENTO =====
  moltip_riempimento <- 1
  if (load_factor < 0.50) {
    moltip_riempimento <- 0.90   # -10%
  } else if (load_factor <= 0.70) {
    moltip_riempimento <- 1.00   #  0%
  } else if (load_factor <= 0.85) {
    moltip_riempimento <- 1.15   # +15%
  } else { # > 0.85
    moltip_riempimento <- 1.35   # +35%
  }

  # ===== CALCOLO PREZZO =====
  fee_fissa <- 25

  prezzo_dinamico <- prezzo * moltip_anticipo * moltip_riempimento

  # Extra: se last-minute e aereo quasi pieno → +10%
  extra_stress <- 1
  if (days_before <= 2 & load_factor > 0.85) {
    extra_stress <- 1.10
  }

  prezzo_finale <- round((prezzo_dinamico * extra_stress) + fee_fissa, 2)
  prezzo_finale
solution_after: ''
---

- **Tariffa base**: Economy 100 €, Premium 180 €, Business 350 €.
- **Anticipo** (`days_before`): oltre 60 giorni −20%; da 31 a 60 −10%; da 15 a 30 0%; da 7 a 14 +20%; da 3 a 6 +40%; da 0 a 2 +70%.
- **Riempimento** (`load_factor`): sotto 0.50 −10%; da 0.50 a 0.70 0%; oltre 0.70 fino a 0.85 +15%; oltre 0.85 +35%.
- **Fee fissa**: 25 € aggiunti alla fine.
- **Stress di mercato**: se `days_before` è 2 o meno **e** `load_factor` supera 0.85, ulteriore +10% (prima della fee).
- I moltiplicatori si applicano in cascata: `base × anticipo × riempimento × stress + 25`.
