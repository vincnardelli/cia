---
layout: lab
title: Net Promoter Score
modulo: 3
order: 6
difficolta: facile
language: R
ai_mode: 'on'
objective: Calcolare l'NPS di un servizio a partire dai voti da 0 a 10 dati dai clienti alla domanda «lo consiglieresti?».
inputs:
- name: voti
  type: vettore di numeri
  desc: un voto da 0 a 10 per ogni cliente intervistato
risultato:
  name: nps
  type: numero
  desc: da −100 a 100, un decimale
regole: |
  - I clienti con voto **9 o 10** sono *promotori*; quelli con voto **da 0 a 6** sono *detrattori*; 7 e 8 sono *passivi* e non contano.
  - `NPS = (promotori − detrattori) / totale intervistati × 100`.
  - Arrotonda a un decimale. Contali con un ciclo e due contatori; in RStudio confronta con `sum(voti >= 9)`.
skeleton: |
  voti <- c(10, 9, 8, 7, 6, 10)

  # ...
  for(i in 1:length(voti)){
    if(voti[i] >= 9){
      # ...
    }else if(voti[i] <= 6){
      # ...
    }
  }

  print(nps)
tests:
- inputs:
    voti:
    - 10
    - 9
    - 8
    - 7
    - 6
    - 10
  expected: 33.3
  visible: true
- inputs:
    voti:
    - 9
    - 9
    - 9
  expected: 100.0
  visible: true
- inputs:
    voti:
    - 8
    - 9
  expected: 50.0
  visible: false
  boundary: true
  hint: '8 è passivo, 9 è promotore: (1 − 0) / 2 = 50.'
- inputs:
    voti:
    - 6
    - 7
  expected: -50.0
  visible: false
  boundary: true
  hint: '6 è detrattore, 7 è passivo: (0 − 1) / 2 = −50.'
- inputs:
    voti:
    - 7
    - 8
    - 8
    - 7
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Solo passivi: il denominatore li conta comunque, NPS 0.'
- inputs:
    voti:
    - 6
    - 6
  expected: -100.0
  visible: false
- inputs:
    voti:
    - 10
    - 0
    - 5
    - 9
    - 7
    - 3
    - 8
    - 9
    - 10
    - 2
  expected: 0.0
  visible: false
solution: |
  voti <- c(10, 9, 8, 7, 6, 10)

  promotori <- 0
  detrattori <- 0
  for(i in 1:length(voti)){
    if(voti[i] >= 9){
      promotori <- promotori + 1
    }else if(voti[i] <= 6){
      detrattori <- detrattori + 1
    }
  }
  nps <- round((promotori - detrattori) / length(voti) * 100, 1)
  nps
solution_after: ''
---

Un'azienda di telefonia manda ai clienti la domanda standard della soddisfazione: «quanto consiglieresti il nostro servizio a un amico, da 0 a 10?». Il numero che il management vuole vedere ogni mese è il **Net Promoter Score**: si contano i *promotori* (chi ha risposto 9 o 10) e i *detrattori* (da 0 a 6), si fa la differenza e la si divide per il numero totale di intervistati, in percentuale. Chi ha risposto 7 o 8 è *passivo*: non conta né in un verso né nell'altro, ma resta nel denominatore.

Ti passano il vettore dei voti e ti chiedono l'NPS con un decimale. Va da −100 (tutti detrattori) a 100 (tutti promotori). Un mese con soli 7 e 8 dà zero: non è un errore, è la definizione.

Contali con un ciclo e due contatori; poi, in RStudio, confronta con `sum(voti >= 9)`.
