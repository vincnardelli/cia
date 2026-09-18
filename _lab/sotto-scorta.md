---
layout: lab
title: Prodotti sotto scorta
modulo: 3
order: 4
difficolta: facile
language: R
ai_mode: 'off'
objective: Contare quanti prodotti del magazzino sono scesi sotto la loro scorta minima e vanno riordinati.
inputs:
- name: giacenza
  type: vettore di numeri
  desc: pezzi in magazzino, un valore per prodotto
- name: soglia
  type: vettore di numeri
  desc: scorta minima di ciascun prodotto, stesso ordine
risultato:
  name: da_riordinare
  type: numero
  desc: numero di prodotti con giacenza sotto la soglia
regole: |
  - I due vettori hanno la stessa lunghezza: il prodotto `i` ha giacenza `giacenza[i]` e soglia `soglia[i]`.
  - Un prodotto va riordinato se la giacenza è **strettamente minore** della soglia: alla soglia esatta è ancora a posto.
  - Scorri i prodotti con un ciclo `for` e conta; poi, in RStudio, prova a farlo senza ciclo con `sum(giacenza < soglia)`.
skeleton: |
  giacenza <- c(12, 3, 40, 0)
  soglia <- c(10, 5, 20, 2)

  # ...
  for(i in 1:length(giacenza)){
    if(giacenza[i] < soglia[i]){
      # ...
    }
  }

  print(da_riordinare)
tests:
- inputs:
    giacenza:
    - 12
    - 3
    - 40
    - 0
    soglia:
    - 10
    - 5
    - 20
    - 2
  expected: 2
  visible: true
- inputs:
    giacenza:
    - 5
    - 5
    - 5
    soglia:
    - 5
    - 5
    - 5
  expected: 0
  visible: true
- inputs:
    giacenza:
    - 4
    - 5
    - 6
    soglia:
    - 5
    - 5
    - 5
  expected: 1
  visible: false
  boundary: true
  hint: 'Solo il primo è sotto: 5 non è ''sotto 5''.'
- inputs:
    giacenza:
    - 0
    soglia:
    - 1
  expected: 1
  visible: false
  boundary: true
- inputs:
    giacenza:
    - 0
    - 0
    - 0
    soglia:
    - 0
    - 0
    - 0
  expected: 0
  visible: false
  boundary: true
  hint: 'Giacenza zero con soglia zero: non è sotto soglia.'
- inputs:
    giacenza:
    - 100
    - 2
    - 7
    - 30
    - 1
    soglia:
    - 50
    - 3
    - 7
    - 40
    - 5
  expected: 3
  visible: false
solution: |
  giacenza <- c(12, 3, 40, 0)
  soglia <- c(10, 5, 20, 2)

  da_riordinare <- 0
  for(i in 1:length(giacenza)){
    if(giacenza[i] < soglia[i]){
      da_riordinare <- da_riordinare + 1
    }
  }
  da_riordinare
solution_after: ''
---

Il responsabile del magazzino di un negozio di ferramenta ha due elenchi, uno accanto all'altro: per ogni prodotto la **giacenza** (i pezzi sullo scaffale) e la **scorta minima** sotto la quale bisogna riordinare. Ogni lunedì li confronta a mano e conta quanti prodotti vanno riordinati, per sapere quante righe avrà l'ordine al fornitore.

I due elenchi sono due vettori della stessa lunghezza, nello stesso ordine: il prodotto in posizione 3 ha giacenza `giacenza[3]` e soglia `soglia[3]`. Un prodotto va riordinato se la giacenza è **strettamente sotto** la soglia: chi è esattamente alla soglia è ancora a posto.

Scrivi il programma che conta i prodotti da riordinare scorrendo i vettori con un ciclo. In RStudio, dopo, prova a ottenere lo stesso numero senza ciclo, con `sum(giacenza < soglia)`: è una riga sola, ma solo dopo aver capito il ciclo.
