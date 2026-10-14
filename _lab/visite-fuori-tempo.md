---
layout: lab
title: Visite fuori tempo massimo
modulo: 4
order: 2
difficolta: facile
language: R
ai_mode: 'off'
objective: Scrivere una funzione che riceve i giorni di attesa delle visite e il tempo massimo previsto, seleziona con le parentesi quadre quelle fuori tempo e restituisce la loro percentuale.
inputs:
- name: attese
  type: vettore di numeri
  desc: giorni di attesa di ciascuna visita prenotata
- name: limite
  type: numero
  desc: tempo massimo di attesa in giorni previsto per quella classe di priorità
risultato:
  name: percentuale
  type: numero
  desc: percentuale di visite fuori tempo massimo, 1 decimale
function: percentuale_fuori_tempo
regole: |
  - Una visita è **in tempo** se l'attesa è minore o uguale al limite: a `limite` giorni esatti è ancora in tempo. È **fuori tempo** se l'attesa è **strettamente maggiore** del limite.
  - Dentro la funzione seleziona le attese fuori tempo con le parentesi quadre e un vettore logico: `attese[attese > limite]` tiene solo quelle.
  - `length()` di quel vettore dice quante sono; `length(attese)` dice quante sono le visite in tutto.
  - La percentuale è `100 * fuori tempo / tutte`, arrotondata a **1 decimale** con `round(..., 1)`.
  - Il limite arriva come argomento: la funzione non deve usare variabili scritte fuori, e deve **restituire** il numero con `return()`.
skeleton: |
  percentuale_fuori_tempo <- function(attese, limite){
    # 1. tieni solo le attese fuori tempo, con le parentesi quadre
    # ...

    # 2. quante sono, e quante sono le visite in tutto?
    # ...

    # 3. restituisci la percentuale con un decimale
    # ...
  }

  # prova: deve dare 50
  print(percentuale_fuori_tempo(c(12, 35, 28, 40), 30))
tests:
- inputs:
    attese:
    - 12
    - 35
    - 28
    - 40
    limite: 30
  expected: 50.0
  visible: true
- inputs:
    attese:
    - 5
    - 8
    - 10
    - 3
    - 15
    limite: 10
  expected: 20.0
  visible: true
- inputs:
    attese:
    - 30
    - 30
    - 30
    limite: 30
  expected: 0.0
  visible: false
  boundary: true
  hint: '30 giorni esatti con un limite di 30 sono ancora in tempo: nessuna visita è fuori tempo.'
- inputs:
    attese:
    - 61
    limite: 60
  expected: 100.0
  visible: false
  boundary: true
  hint: 'Una sola visita, un giorno oltre il limite: è fuori tempo il 100% delle visite.'
- inputs:
    attese:
    - 10
    - 20
    - 30
    limite: 120
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Nessuna attesa supera 120 giorni: la selezione resta vuota e la sua lunghezza è 0.'
- inputs:
    attese:
    - 4
    - 2
    - 3
    - 5
    - 1
    - 3
    limite: 3
  expected: 33.3
  visible: false
  hint: 'Due visite su sei sono fuori tempo: 33,333… va arrotondato a un decimale.'
- inputs:
    attese:
    - 45
    - 70
    - 59
    - 61
    - 60
    - 90
    - 12
    limite: 60
  expected: 42.9
  visible: false
solution: |
  percentuale_fuori_tempo <- function(attese, limite){
    # le parentesi quadre con un vettore logico tengono solo le attese oltre il limite
    fuori_tempo <- attese[attese > limite]

    # quante sono fuori tempo, su quante visite in tutto
    percentuale <- 100 * length(fuori_tempo) / length(attese)

    return(round(percentuale, 1))
  }

  percentuale_fuori_tempo(c(12, 35, 28, 40), 30)   # 50
  percentuale_fuori_tempo(c(30, 30, 30), 30)       # 0: 30 giorni esatti sono in tempo
solution_after: ''
---

Il Piano nazionale di governo delle liste d'attesa fissa un **tempo massimo** per ogni classe di priorità della ricetta: una visita con priorità B va fatta entro 10 giorni, una D (differibile) entro 30, una P (programmata) entro 120. L'ufficio qualità di un'azienda sanitaria deve dire alla Regione, ogni mese, quale percentuale delle visite prenotate è finita oltre il tempo massimo.

Per ogni classe di priorità l'ufficio estrae dal sistema di prenotazione un vettore con i giorni di attesa di ciascuna visita. Una visita fatta a 30 giorni con un limite di 30 è **in tempo**; a 31 giorni è fuori tempo. La percentuale si dà con un decimale.

Il calcolo va ripetuto per ogni classe e ogni mese, cambiando solo il vettore e il limite: scrivi la funzione `percentuale_fuori_tempo(attese, limite)`, che seleziona le attese fuori tempo con le parentesi quadre e restituisce la percentuale. La verifica chiama la tua funzione con i valori di ogni caso.
