---
layout: lab
title: Spedizione gratis?
modulo: 1
order: 2
difficolta: facile
language: R
ai_mode: 'off'
objective: Dire se un carrello ha diritto alla spedizione gratuita, che scatta da 49,90 € in su.
inputs:
- name: totale
  type: numero
  desc: valore del carrello in euro
risultato:
  name: gratis
  type: logico
  desc: TRUE se la spedizione è gratuita, FALSE altrimenti
regole: |
  - La spedizione è gratuita se il totale è **almeno** 49,90 €.
  - Il risultato è un valore logico (`TRUE`/`FALSE`), ottenuto da un confronto: non serve nessun `if`.
skeleton: |
  totale <- 60


  print(gratis)
tests:
- inputs:
    totale: 60
  expected: true
  visible: true
- inputs:
    totale: 20
  expected: false
  visible: true
- inputs:
    totale: 49.9
  expected: true
  visible: false
  boundary: true
  hint: '49,90 esatti: il testo dice ''da 49,90 in su'', quindi è compreso. Il confronto giusto è >=, non >.'
- inputs:
    totale: 49.89
  expected: false
  visible: false
  boundary: true
- inputs:
    totale: 0
  expected: false
  visible: false
solution: |
  totale <- 60

  gratis <- totale >= 49.90
  gratis
solution_after: ''
---

Il sito di un negozio di articoli sportivi mostra, accanto al carrello, la scritta «spedizione gratuita da 49,90 €». Il reparto marketing vuole aggiungere un messaggio che dica al cliente, mentre riempie il carrello, se ha già diritto alla spedizione gratis o no: è una delle leve più efficaci per far aggiungere un ultimo articolo.

Ti chiedono la regola nella forma più semplice possibile: dato il totale del carrello, un valore vero/falso che il sito userà per mostrare o nascondere il messaggio. Il confine conta: a 49,90 esatti la spedizione è gratuita, a 49,89 no. Non serve nessuna decisione «se…allora»: basta un confronto, e il risultato è direttamente `TRUE` o `FALSE`.
