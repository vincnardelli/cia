---
layout: lab
title: Taxi a Roma
week: 3
order: 2
level: base
language: R
ai_mode: 'off'
objective: Calcolare il costo di una corsa in taxi a Roma a partire dai km percorsi in ogni minuto.
inputs:
- name: distanza
  type: vettore di numeri
  desc: km percorsi in ciascun minuto della corsa
output:
  name: costo
  type: numero
  desc: costo totale in euro, 2 decimali
skeleton: |
  distanza <- c(1, 0.3, 0.5, 0.8, 0.2)

  # alla fine deve esistere la variabile costo
tests:
- inputs:
    distanza:
    - 1
    - 0.3
    - 0.5
    - 0.8
    - 0.2
  expected: 3.56
  visible: true
- inputs:
    distanza:
    - 0.5
    - 0.5
    - 0.5
  expected: 1.71
  visible: true
- inputs:
    distanza:
    - 0.1
  expected: 0.47
  visible: false
  boundary: true
  hint: 'Un solo minuto a 6 km/h: costa un sessantesimo della tariffa oraria.'
- inputs:
    distanza:
    - 0.35
    - 0.3
  expected: 0.87
  visible: false
  boundary: true
  hint: '21 km/h e 18 km/h: il primo minuto è a km, il secondo a tempo.'
- inputs:
    distanza:
    - 0
    - 0
    - 0
    - 0
  expected: 1.87
  visible: false
  boundary: true
  hint: 'Taxi fermo per quattro minuti: la velocità è zero, ma il tassametro corre a tempo.'
- inputs:
    distanza:
    - 2
    - 1.5
    - 1.2
  expected: 5.36
  visible: false
solution: |
  distanza <- c(1, 0.3, 0.5, 0.8, 0.2)

  tariffa_min <- 28/60
  tariffa_km <- 1.14
  costo <- 0

  for(i in 1:length(distanza)){
    velocita <- distanza[i] * 60
    if(velocita < 20){
      costo <- costo + tariffa_min
    }else{
      costo <- costo + tariffa_km * distanza[i]
    }
  }
  costo <- round(costo, 2)
  costo
solution_after: ''
---

- In ogni minuto il tassametro sceglie la tariffa in base alla velocità di quel minuto: `velocita = km * 60` (km/h).
- Velocità **sotto i 20 km/h** → tariffa oraria: 28 €/h, cioè 28/60 € per quel minuto.
- Velocità di 20 km/h o più → tariffa chilometrica: 1,14 € per km percorso in quel minuto.
- Il costo è la somma dei minuti. Arrotonda a due decimali.
