---
layout: lab
title: Taxi o Uber?
week: 3
order: 4
level: extra
language: R
ai_mode: 'off'
objective: Aggiungere al taxi la quota fissa (giorno e ora) e decidere se conviene il taxi o Uber.
inputs:
- name: distanza
  type: vettore di numeri
  desc: km per minuto
- name: giorno
  type: testo
  desc: 'iniziale del giorno: "L","M","M","G","V","S","D"'
- name: ora
  type: numero
  desc: ora di partenza, da 0 a 23
- name: costo_uber
  type: numero
  desc: prezzo proposto da Uber
output:
  name: decisione
  type: testo
  desc: '"Taxi" oppure "Uber"'
skeleton: |
  distanza <- c(1, 0.3, 0.5, 0.8, 0.2)
  giorno <- "D"
  ora <- 12
  costo_uber <- 9

  # alla fine deve esistere la variabile decisione ("Taxi" o "Uber")
tests:
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
    giorno: D
    ora: 12
    costo_uber: 9
  expected: Taxi
  visible: true
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
    giorno: L
    ora: 12
    costo_uber: 9
  expected: Taxi
  visible: true
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
    giorno: L
    ora: 22
    costo_uber: 9
  expected: Uber
  visible: false
  boundary: true
  hint: 'Alle 22 è già tariffa notturna (7 €): il taxi costa più di 9 €?'
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
    giorno: L
    ora: 21
    costo_uber: 9
  expected: Taxi
  visible: false
  boundary: true
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
    giorno: L
    ora: 6
    costo_uber: 9
  expected: Taxi
  visible: false
  boundary: true
  hint: Alle 6 in punto è già tariffa diurna.
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
    giorno: L
    ora: 5
    costo_uber: 9
  expected: Uber
  visible: false
  boundary: true
- inputs:
    distanza:
    - 0.5
    - 0.5
    giorno: M
    ora: 10
    costo_uber: 4.14
  expected: Taxi
  visible: false
  boundary: true
  hint: 'A parità di prezzo la regola dice Taxi: il confronto è < oppure <=?'
- inputs:
    distanza:
    - 0.5
    - 0.5
    giorno: D
    ora: 10
    costo_uber: 6
  expected: Uber
  visible: false
solution: |
  distanza <- c(1, 0.3, 0.5, 0.8, 0.2)
  giorno <- "D"
  ora <- 12
  costo_uber <- 9

  if(ora >= 6 & ora < 22){
    if(giorno == "D"){
      costo <- 5
    }else{
      costo <- 3
    }
  }else{
    costo <- 7
  }

  for(i in 1:length(distanza)){
    velocita <- distanza[i] * 60
    if(velocita < 20){
      costo <- costo + 28/60
    }else{
      costo <- costo + 1.14 * distanza[i]
    }
  }

  if(costo_uber < costo){
    decisione <- "Uber"
  }else{
    decisione <- "Taxi"
  }
  decisione
solution_after: ''
---

- **Quota fissa**: giorni feriali dalle 6 alle 21 (ora < 22) 3 €; domenica ("D") nella stessa fascia 5 €; **notturna** (dalle 22 in poi o prima delle 6, qualsiasi giorno) 7 €.
- **Quota variabile**: come nel lab Taxi (28 €/h sotto i 20 km/h, 1,14 €/km altrimenti).
- Si sceglie "Uber" solo se costa **strettamente meno** del taxi; a parità, "Taxi".
