---
layout: lab
title: Autovelox come funzione
modulo: 3
order: 3
difficolta: facile
language: R
ai_mode: 'off'
objective: Riscrivere l'autovelox come funzione `multa(velocita, limite)` riutilizzabile, e verificarla con gli stessi casi del modulo 2.
inputs:
- name: velocita
  type: numero
- name: limite
  type: numero
risultato:
  name: multa
  type: numero
  desc: valore restituito dalla funzione
function: multa
regole: |
  - Stesse regole dell'[Autovelox](../autovelox/): 0 / 36 / 148 / 370 / 500 € per le fasce "entro il limite", "non oltre 10", "non oltre 40", "non oltre 60", "oltre 60".
  - Il codice deve **definire** la funzione `multa <- function(velocita, limite){ ... }` che **restituisce** l'importo (ultima espressione o `return()`).
  - La verifica chiama la tua funzione con i valori di ogni caso: non servono assegnazioni di prova.
  - In RStudio, usala su un vettore di veicoli con un ciclo `for` e conta quante multe superano i 100 €.
skeleton: |
  multa <- function(velocita, limite){
    # ...
    if(differenza <= 0){
      # ...
    }else if(differenza <= 10){
      # ...
    }else if(differenza <= 40){
      # ...
    }else if(differenza <= 60){
      # ...
    }else{
      # ...
    }
    # ...
  }

  print(multa(45, 50))
tests:
- inputs:
    velocita: 45
    limite: 50
  expected: 0
  visible: true
- inputs:
    velocita: 75
    limite: 50
  expected: 148
  visible: true
- inputs:
    velocita: 60
    limite: 50
  expected: 36
  visible: false
  boundary: true
- inputs:
    velocita: 90
    limite: 50
  expected: 148
  visible: false
  boundary: true
- inputs:
    velocita: 110
    limite: 50
  expected: 370
  visible: false
  boundary: true
- inputs:
    velocita: 111
    limite: 50
  expected: 500
  visible: false
  boundary: true
- inputs:
    velocita: 50
    limite: 50
  expected: 0
  visible: false
  boundary: true
solution: |
  multa <- function(velocita, limite){
    differenza <- velocita - limite
    if(differenza <= 0){
      importo <- 0
    }else if(differenza <= 10){
      importo <- 36
    }else if(differenza <= 40){
      importo <- 148
    }else if(differenza <= 60){
      importo <- 370
    }else{
      importo <- 500
    }
    return(importo)
  }

  multa(75, 50)
solution_after: ''
---

Il software dell'autovelox scritto nel modulo 2 funziona, ma il Comune ne ha comprati altri dodici, su strade con limiti diversi, e vuole usare **lo stesso codice** per tutti senza copiarlo e incollarlo ogni volta. È il momento di trasformarlo in una **funzione**.

Le regole restano quelle dell'articolo 142: nessuna sanzione entro il limite; 36 € per un eccesso non oltre 10 km/h; 148 € oltre 10 e non oltre 40; 370 € oltre 40 e non oltre 60; 500 € oltre 60. Il tuo codice deve **definire** la funzione `multa(velocita, limite)` che restituisce l'importo. La verifica non assegna variabili: chiama direttamente la tua funzione con i valori di ogni caso.

In RStudio, poi, usala su un vettore di veicoli con un ciclo e conta quante multe superano i 100 euro: è esattamente ciò che vuole il Comune.
