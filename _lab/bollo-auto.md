---
layout: lab
title: Bollo auto
week: 2
order: 5
level: extra
language: R
ai_mode: 'on'
objective: Calcolare il bollo auto (regole semplificate) in base alla potenza e alla classe ambientale.
inputs:
- name: kw
  type: numero
  desc: potenza in kW
- name: classe_euro
  type: numero
  desc: classe Euro da 0 a 6
output:
  name: bollo
  type: numero
  desc: importo in euro, 2 decimali
skeleton: |
  kw <- 85
  classe_euro <- 6

  # alla fine deve esistere la variabile bollo
tests:
- inputs:
    kw: 85
    classe_euro: 6
  expected: 219.3
  visible: true
- inputs:
    kw: 140
    classe_euro: 4
  expected: 412.8
  visible: true
- inputs:
    kw: 100
    classe_euro: 5
  expected: 258.0
  visible: false
  boundary: true
  hint: '100 kW esatti: tutti alla tariffa bassa, nessun kW oltre.'
- inputs:
    kw: 101
    classe_euro: 5
  expected: 261.87
  visible: false
  boundary: true
  hint: '101 kW: 100 alla tariffa bassa e 1 solo alla tariffa alta, non 101 alla tariffa alta.'
- inputs:
    kw: 100
    classe_euro: 3
  expected: 270.0
  visible: false
  boundary: true
- inputs:
    kw: 120
    classe_euro: 0
  expected: 390.0
  visible: false
- inputs:
    kw: 120
    classe_euro: 1
  expected: 390.0
  visible: false
  boundary: true
- inputs:
    kw: 120
    classe_euro: 2
  expected: 364.0
  visible: false
solution: |
  kw <- 85
  classe_euro <- 6

  if(classe_euro >= 4){
    bassa <- 2.58
    alta <- 3.87
  }else if(classe_euro == 3){
    bassa <- 2.70
    alta <- 4.05
  }else if(classe_euro == 2){
    bassa <- 2.80
    alta <- 4.20
  }else{
    bassa <- 3.00
    alta <- 4.50
  }

  if(kw <= 100){
    bollo <- kw * bassa
  }else{
    bollo <- 100 * bassa + (kw - 100) * alta
  }
  bollo <- round(bollo, 2)
  bollo
solution_after: ''
---

Tariffa per kW (regole semplificate a fini didattici):

| classe Euro | fino a 100 kW | ogni kW oltre i 100 |
|---|---|---|
| 4, 5, 6 | 2,58 € | 3,87 € |
| 3 | 2,70 € | 4,05 € |
| 2 | 2,80 € | 4,20 € |
| 0, 1 | 3,00 € | 4,50 € |

- I primi 100 kW si pagano alla tariffa bassa; **solo** i kW oltre i 100 alla tariffa alta.
- Arrotonda a due decimali.
