---
layout: lab
title: Rimborso per il ritardo del treno
modulo: 2
order: 1
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare il rimborso dovuto al passeggero in base ai minuti di ritardo all'arrivo.
inputs:
- name: prezzo
  type: numero
  desc: prezzo del biglietto in euro
- name: ritardo
  type: numero
  desc: minuti di ritardo all'arrivo
risultato:
  name: rimborso
  type: numero
  desc: euro da rimborsare, 2 decimali
regole: |
  - Ritardo **sotto i 60 minuti**: nessun rimborso.
  - Da 60 a 119 minuti: rimborso del **25%** del prezzo.
  - Da **120 minuti in su**: rimborso del **50%**.
  - Arrotonda a due decimali.
skeleton: |
  prezzo <- 50
  ritardo <- 30

  if(...){
    # ...
  }else if(...){
    # ...
  }else{
    # ...
  }

  print(rimborso)
tolerance: 0.001
tests:
- inputs:
    prezzo: 50
    ritardo: 30
  expected: 0
  visible: true
- inputs:
    prezzo: 50
    ritardo: 75
  expected: 12.5
  visible: true
- inputs:
    prezzo: 50
    ritardo: 60
  expected: 12.5
  visible: false
  boundary: true
  hint: '60 minuti esatti: il rimborso scatta ''da 60 in su''. Il tuo confronto usa < o <=?'
- inputs:
    prezzo: 50
    ritardo: 59
  expected: 0
  visible: false
  boundary: true
- inputs:
    prezzo: 50
    ritardo: 120
  expected: 25.0
  visible: false
  boundary: true
  hint: 120 esatti è già la fascia del 50%.
- inputs:
    prezzo: 50
    ritardo: 119
  expected: 12.5
  visible: false
  boundary: true
- inputs:
    prezzo: 89.9
    ritardo: 200
  expected: 44.95
  visible: false
- inputs:
    prezzo: 23.45
    ritardo: 75
  expected: 5.86
  visible: false
  hint: 'Il 25% di 23,45 fa 5,8625: il rimborso va con due decimali. Hai usato round(x, 2)?'
solution: |
  prezzo <- 50
  ritardo <- 30

  if(ritardo < 60){
    rimborso <- 0
  }else if(ritardo < 120){
    rimborso <- round(prezzo * 0.25, 2)
  }else{
    rimborso <- round(prezzo * 0.50, 2)
  }
  rimborso
solution_after: ''
---

Lavori all'assistenza clienti di una compagnia ferroviaria e ogni giorno arrivano richieste di rimborso per ritardo. Le condizioni di trasporto sono chiare: se il treno arriva con un ritardo **sotto i 60 minuti** non è dovuto nulla; **da 60 a 119 minuti** il passeggero ha diritto al 25% del prezzo del biglietto; **da 120 minuti in su** al 50%.

Ti chiedono di automatizzare il calcolo: dati il prezzo del biglietto e i minuti di ritardo, l'importo da rimborsare con due decimali. I passeggeri più agguerriti sono quelli con 59 o 60 minuti di ritardo, e con 119 o 120: sono esattamente i casi su cui il tuo programma deve fare la cosa scritta nelle condizioni.
