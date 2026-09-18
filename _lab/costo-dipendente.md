---
layout: lab
title: Quanto costa un dipendente
modulo: 1
order: 3
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare il costo annuo di un dipendente per l'azienda a partire dal lordo mensile.
inputs:
- name: lordo_mensile
  type: numero
  desc: stipendio lordo mensile in euro
risultato:
  name: costo_annuo
  type: numero
  desc: costo annuo per l'azienda, 2 decimali
regole: |
  - Le mensilità sono **13** (c'è la tredicesima).
  - Sul lordo annuo l'azienda paga contributi pari al **30%**: il costo è il lordo annuo più i contributi.
  - Arrotonda a due decimali.
skeleton: |
  lordo_mensile <- 1800


  print(costo_annuo)
tests:
- inputs:
    lordo_mensile: 1800
  expected: 30420.0
  visible: true
- inputs:
    lordo_mensile: 2500
  expected: 42250.0
  visible: true
- inputs:
    lordo_mensile: 0
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Con lordo zero il costo è zero: se ottieni altro, hai sommato una cifra fissa da qualche parte.'
- inputs:
    lordo_mensile: 1234.56
  expected: 20864.06
  visible: false
  boundary: true
  hint: 'Con i centesimi conta dove arrotondi: alla fine, sul costo annuo, non sul lordo.'
- inputs:
    lordo_mensile: 3100
  expected: 52390.0
  visible: false
solution: |
  lordo_mensile <- 1800

  lordo_annuo <- lordo_mensile * 13
  contributi <- lordo_annuo * 0.30
  costo_annuo <- round(lordo_annuo + contributi, 2)
  costo_annuo
solution_after: ''
---

La titolare di un piccolo studio di consulenza vuole assumere una persona e sta facendo i conti. L'annuncio dice 1.800 euro lordi al mese, ma lei sa che il costo per l'azienda è molto più alto: in Italia le mensilità sono tredici (c'è la tredicesima) e sul lordo annuo l'azienda versa contributi che, per semplificare, contiamo al 30%.

Ti chiede un programma che, dato il lordo mensile, calcoli il costo annuo che sosterrà l'azienda, con due decimali, così da poterlo confrontare con il budget. Lo userà per più candidati, anche con cifre con i centesimi: l'arrotondamento va fatto una volta sola, alla fine.
