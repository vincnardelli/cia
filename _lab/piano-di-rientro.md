---
layout: lab
title: Piano di rientro
modulo: 4
order: 6
difficolta: facile
language: R
ai_mode: 'off'
objective: Scrivere una funzione ricorsiva che conta quante rate mensili servono per saldare un debito, con il caso base quando il debito è finito.
inputs:
- name: debito
  type: numero
  desc: euro ancora da pagare, zero o più
- name: rata
  type: numero
  desc: euro pagati ogni mese, più di zero
risultato:
  name: rate
  type: numero
  desc: numero di rate mensili necessarie
function: numero_rate
regole: |
  - **Caso base**: se il debito è **minore o uguale a zero** non c'è più niente da pagare, e le rate che restano sono **0**. Con 1000 € e rate da 300 € il debito passa da 100 a -200: non vale mai zero esatto, e il caso base deve fermarlo lo stesso.
  - **Passo**: altrimenti si paga una rata adesso, e le rate sono **una più** quelle che servono per il debito che resta (`debito - rata`), calcolate richiamando la funzione stessa.
  - L'ultima rata può essere più piccola delle altre (paga solo il residuo), ma conta come una rata.
  - Niente ciclo: la funzione chiama sé stessa. Entrambi i rami restituiscono il numero con `return()`.
skeleton: |
  numero_rate <- function(debito, rata){
    # caso base: il debito è finito?
    # ...

    # passo: una rata adesso, più le rate per il debito che resta
    # ...
  }

  # prova: deve dare 4
  print(numero_rate(1000, 250))
tests:
- inputs:
    debito: 1000
    rata: 250
  expected: 4
  visible: true
- inputs:
    debito: 1000
    rata: 300
  expected: 4
  visible: true
- inputs:
    debito: 0
    rata: 100
  expected: 0
  visible: false
  boundary: true
  hint: 'Nessun debito, nessuna rata: è il caso base, la funzione deve restituire 0 subito.'
- inputs:
    debito: 50
    rata: 200
  expected: 1
  visible: false
  boundary: true
  hint: 'Il debito è più piccolo della rata: basta una rata sola, dopo il debito è sotto zero.'
- inputs:
    debito: 1200
    rata: 100
  expected: 12
  visible: false
  boundary: true
  hint: 'Dopo dodici rate il debito è zero esatto: zero è già il caso base, la tredicesima rata non serve.'
- inputs:
    debito: 2450.5
    rata: 175
  expected: 15
  visible: false
  hint: 'Quattordici rate da 175 € fanno 2450 €: resta 0,50 €, che è la quindicesima rata.'
- inputs:
    debito: 999.99
    rata: 1000
  expected: 1
  visible: false
solution: |
  numero_rate <- function(debito, rata){
    # caso base: il debito è finito (anche sotto zero, se l'ultima rata era più grande)
    if(debito <= 0){
      return(0)
    }

    # passo: pago una rata e conto le rate per il debito che resta
    return(1 + numero_rate(debito - rata, rata))
  }

  numero_rate(1000, 250)   # 4
  numero_rate(1000, 300)   # 4: 300, 300, 300 e poi 100
  numero_rate(0, 100)      # 0: il caso base
solution_after: ''
---

Un condomino è rimasto indietro con le spese condominiali e l'amministratore gli propone un **piano di rientro**: il debito arretrato si paga a rate mensili di importo fisso, scelto dal condomino in base a quanto può permettersi, senza interessi. L'ultima rata paga solo quello che resta, quindi può essere più piccola delle altre.

L'amministratore deve scrivere nella delibera **quante rate** servono. Con 1.000 euro di debito e rate da 250 ne servono 4; con rate da 300 ne servono comunque 4 (300, 300, 300 e infine 100). Con un debito di zero non serve nessuna rata.

Scrivi la funzione **ricorsiva** `numero_rate(debito, rata)`: se il debito è finito restituisce 0, altrimenti conta una rata e richiama sé stessa sul debito che resta. Attenzione al caso base: deve fermare la funzione anche quando il debito scende sotto zero. La verifica chiama la tua funzione con i valori di ogni caso.
