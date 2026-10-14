---
layout: lab
title: Progetti da finanziare
modulo: 4
order: 7
difficolta: difficile
language: R
ai_mode: 'on'
objective: Scegliere quali progetti finanziare con un budget fisso per raggiungere più persone possibile, provando tutte le combinazioni con una funzione ricorsiva.
inputs:
- name: budget
  type: numero
  desc: fondi disponibili, in migliaia di euro
- name: costi
  type: vettore di numeri
  desc: costo di ciascun progetto, in migliaia di euro
- name: persone
  type: vettore di numeri
  desc: persone raggiunte da ciascun progetto, stesso ordine di costi
risultato:
  name: raggiunte
  type: numero
  desc: il numero massimo di persone raggiungibili restando nel budget
function: persone_massime
regole: |
  - Ogni progetto si finanzia per intero o non si finanzia.
  - Una combinazione è ammessa se la somma dei costi dei progetti scelti è minore o uguale al budget (il budget può avanzare).
  - Il risultato è il massimo di persone raggiunte fra le combinazioni ammesse; 0 se nessun progetto entra nel budget.
  - Le combinazioni si costruiscono con una funzione ricorsiva che aggiunge una scelta alla volta (TRUE = finanziato, FALSE = no), caso base quando le scelte sono tante quanti i progetti.
  - `max(a, b)` restituisce il più grande fra a e b.
skeleton: |
  persone_massime <- function(budget, costi, persone){

  }
tests:
- inputs:
    budget: 100
    costi:
    - 70
    - 50
    - 40
    persone:
    - 400
    - 260
    - 230
  expected: 490
  visible: true
- inputs:
    budget: 120
    costi:
    - 30
    - 45
    - 60
    - 25
    persone:
    - 90
    - 160
    - 150
    - 70
  expected: 320
  visible: true
- inputs:
    budget: 100
    costi:
    - 60
    - 40
    - 55
    persone:
    - 300
    - 200
    - 280
  expected: 500
  visible: false
  boundary: true
  hint: 'I primi due progetti costano 60 + 40 = 100, esattamente il budget: la combinazione è ammessa.'
- inputs:
    budget: 50
    costi:
    - 80
    persone:
    - 500
  expected: 0
  visible: false
  boundary: true
  hint: 'Un solo progetto, che costa più del budget: non si finanzia nulla, 0 persone.'
- inputs:
    budget: 80
    costi:
    - 80
    persone:
    - 500
  expected: 500
  visible: false
  boundary: true
  hint: 'Un solo progetto, che costa esattamente il budget: si finanzia.'
- inputs:
    budget: 500
    costi:
    - 100
    - 120
    - 90
    persone:
    - 400
    - 380
    - 350
  expected: 1130
  visible: false
  boundary: true
  hint: 'Il budget basta per tutti i progetti: si finanziano tutti e tre.'
- inputs:
    budget: 200
    costi:
    - 45
    - 30
    - 80
    - 65
    - 50
    persone:
    - 250
    - 120
    - 420
    - 330
    - 260
  expected: 1010
  visible: false
  hint: 'La combinazione migliore è 80 + 65 + 50 = 195: prendere i progetti nell''ordine in cui arrivano finché entrano porta a 790 persone.'
solution: |
  # ---- Prima funzione: quante persone raggiunge una scelta completa ----
  # scelte è un vettore di TRUE/FALSE, uno per progetto

  valuta <- function(scelte, budget, costi, persone){
    spesa <- sum(costi[scelte])           # solo i progetti finanziati
    if(spesa <= budget){
      return(sum(persone[scelte]))
    }else{
      return(0)                           # fuori budget: non vale
    }
  }

  # ---- Seconda funzione: prova tutte le combinazioni ----

  migliore <- function(scelte, budget, costi, persone){
    if(length(scelte) == length(costi)){
      return(valuta(scelte, budget, costi, persone))   # caso base: ho deciso tutto
    }

    con_progetto <- migliore(c(scelte, TRUE), budget, costi, persone)     # il prossimo lo finanzio
    senza_progetto <- migliore(c(scelte, FALSE), budget, costi, persone)  # ... oppure no

    return(max(con_progetto, senza_progetto))
  }

  # ---- La funzione principale: parte da nessuna scelta ----

  persone_massime <- function(budget, costi, persone){
    return(migliore(c(), budget, costi, persone))
  }

  persone_massime(100, c(70, 50, 40), c(400, 260, 230))   # 490
solution_after: ''
---

La fondazione di una banca locale ha un bando per progetti sociali sul territorio: doposcuola, assistenza agli anziani, corsi di lingua per stranieri. Ogni progetto arrivato in commissione ha un **costo** (in migliaia di euro) e una stima delle **persone** che raggiungerà. Un progetto si finanzia per intero o non si finanzia: non esistono mezzi progetti. La somma dei costi dei progetti scelti deve stare **dentro il budget**, che può anche avanzare; se i costi arrivano esattamente al budget, la combinazione va bene.

La commissione vuole sapere qual è il **numero massimo di persone** che si possono raggiungere con il budget disponibile. Scegliere a occhio non funziona: con 100 mila euro e tre progetti da 70, 50 e 40 mila, il più grande (400 persone) lascia fuori gli altri due, mentre 50 + 40 ne raggiungono 490. Se nessun progetto entra nel budget, la risposta è 0.

Scrivi la funzione `persone_massime(budget, costi, persone)`. Lo schema è quello dei due fornitori: una funzione `valuta(scelte, budget, costi, persone)` che riceve un vettore di `TRUE`/`FALSE`, uno per progetto, e restituisce le persone raggiunte (0 se la spesa supera il budget); una funzione ricorsiva `migliore(scelte, budget, costi, persone)` che aggiunge una scelta alla volta, una volta `TRUE` e una volta `FALSE`, con il caso base quando le scelte sono tante quanti i progetti, e tiene il risultato più grande con `max(a, b)`, che restituisce il maggiore fra due numeri; infine `persone_massime` che chiama `migliore` partendo da `c()`, nessuna scelta fatta. Ricorda che `costi[scelte]` con un vettore logico tiene solo i progetti finanziati.
