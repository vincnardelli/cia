---
layout: lab
title: Punto di pareggio
modulo: 1
order: 4
difficolta: difficile
language: R
ai_mode: 'on'
objective: Quanti pezzi bisogna vendere in un mese per coprire i costi fissi.
inputs:
- name: costi_fissi
  type: numero
  desc: costi fissi mensili in euro
- name: prezzo
  type: numero
  desc: prezzo di vendita di un pezzo
- name: costo_unitario
  type: numero
  desc: costo variabile di un pezzo
risultato:
  name: pezzi
  type: numero
  desc: pezzi da vendere, intero
regole: |
  - Ogni pezzo venduto contribuisce ai costi fissi per `prezzo - costo_unitario` (il **margine di contribuzione**).
  - I pezzi da vendere sono `costi_fissi / margine`, arrotondati **per eccesso** con `ceiling()`: non si vende mezzo pezzo, e con uno in meno non si è ancora in pareggio.
skeleton: |
  costi_fissi <- 3000
  prezzo <- 8
  costo_unitario <- 3

  print(pezzi)
tests:
- inputs:
    costi_fissi: 3000
    prezzo: 8
    costo_unitario: 3
  expected: 600
  visible: true
- inputs:
    costi_fissi: 3000
    prezzo: 8.5
    costo_unitario: 3
  expected: 546
  visible: true
- inputs:
    costi_fissi: 1000
    prezzo: 12
    costo_unitario: 2
  expected: 100
  visible: false
  boundary: true
  hint: '1000 / 10 fa esattamente 100: ceiling() non deve aggiungere nulla quando la divisione è esatta.'
- inputs:
    costi_fissi: 999
    prezzo: 10
    costo_unitario: 0
  expected: 100
  visible: false
  boundary: true
  hint: '99,9 pezzi: con 99 non si è in pareggio, ne servono 100. round() darebbe 100 per caso, ma con 99,4 sbaglierebbe: usa ceiling().'
- inputs:
    costi_fissi: 5000
    prezzo: 25
    costo_unitario: 19.5
  expected: 910
  visible: false
solution: |
  costi_fissi <- 3000
  prezzo <- 8
  costo_unitario <- 3

  margine <- prezzo - costo_unitario
  pezzi <- ceiling(costi_fissi / margine)
  pezzi
solution_after: ''
---

Due amici vogliono aprire una pizzeria da asporto e devono rispondere alla domanda che ogni banca farà loro: quante pizze dovete vendere al mese per non perderci? I costi fissi mensili (affitto, bollette, stipendi) sono noti. Ogni pizza si vende a un prezzo e costa, in ingredienti e scatola, una cifra fissa: la differenza tra i due è quello che ogni pizza venduta lascia per coprire i costi fissi.

Il numero cercato è quante pizze servono perché la somma di quei contributi copra i costi fissi. Non esistono le mezze pizze, e con una pizza in meno non si è ancora in pareggio: quindi la divisione va sempre arrotondata **per eccesso**, anche quando manca pochissimo. Quando invece la divisione è esatta, non si aggiunge nulla.

Scrivi il programma che, dati costi fissi, prezzo e costo unitario, calcola il numero di pizze del pareggio. In R esiste la funzione `ceiling()`.
