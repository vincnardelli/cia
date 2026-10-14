---
layout: lab
title: Rimborso della trasferta
modulo: 4
order: 4
difficolta: difficile
language: R
ai_mode: 'on'
objective: Scrivere una funzione che calcola il rimborso di una nota spese di trasferta, escludendo le spese non rimborsabili, con un massimo per ogni pasto e un tetto per giorno.
inputs:
- name: categorie
  type: vettore di testi
  desc: categoria di ciascuna spesa della nota, per esempio "treno", "hotel", "pasto", "minibar"
- name: importi
  type: vettore di numeri
  desc: importo in euro di ciascuna spesa, stesso ordine di categorie
- name: giorni
  type: numero
  desc: durata della trasferta in giorni
risultato:
  name: rimborso
  type: numero
  desc: euro rimborsati al dipendente, 2 decimali
function: rimborso_trasferta
regole: |
  - Spese mai rimborsate: categorie "minibar", "alcolici", "multa".
  - "pasto": rimborsato fino a 30 € per pasto; la parte sopra i 30 € resta al dipendente.
  - Ogni altra categoria è rimborsata per intero.
  - Il rimborso complessivo non supera 150 € per ogni giorno di trasferta.
  - Arrotondare a 2 decimali.
skeleton: |
  rimborso_trasferta <- function(categorie, importi, giorni){

  }
tests:
- inputs:
    categorie:
    - treno
    - hotel
    - pasto
    - minibar
    importi:
    - 49.9
    - 95
    - 24.5
    - 12
    giorni: 1
  expected: 150.0
  visible: true
- inputs:
    categorie:
    - treno
    - pasto
    - pasto
    - taxi
    - alcolici
    importi:
    - 35.5
    - 42
    - 18.4
    - 22
    - 15
    giorni: 2
  expected: 105.9
  visible: true
- inputs:
    categorie:
    - pasto
    importi:
    - 30
    giorni: 1
  expected: 30.0
  visible: false
  boundary: true
  hint: 'Un pasto da 30 € esatti è rimborsato per intero.'
- inputs:
    categorie:
    - minibar
    - multa
    - alcolici
    importi:
    - 8.5
    - 42
    - 19
    giorni: 1
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Tutte le spese sono fra quelle mai rimborsate: il rimborso è zero.'
- inputs:
    categorie:
    - hotel
    - hotel
    - treno
    - pasto
    importi:
    - 110
    - 110
    - 52
    - 28
    giorni: 2
  expected: 300.0
  visible: false
  boundary: true
  hint: 'Le spese rimborsabili fanno 300 €, esattamente il tetto di due giorni: si rimborsano tutte.'
- inputs:
    categorie:
    - aereo
    - hotel
    - hotel
    - hotel
    - pasto
    - pasto
    - pasto
    - taxi
    - minibar
    importi:
    - 180
    - 130
    - 130
    - 130
    - 55
    - 26
    - 31
    - 40
    - 22
    giorni: 3
  expected: 450.0
  visible: false
  hint: 'Rimborsabile 696 € (i pasti valgono 30 + 26 + 30), ma il tetto di tre giorni è 450 €.'
- inputs:
    categorie:
    - treno
    - pasto
    - pasto
    - pasto
    - pasto
    - hotel
    - taxi
    importi:
    - 64.8
    - 45
    - 33.9
    - 12.5
    - 29.99
    - 89
    - 17.6
    giorni: 2
  expected: 273.89
  visible: false
  hint: 'I pasti da 45 € e da 33,90 € valgono 30 € ciascuno: il tetto è per pasto, non sul totale dei pasti.'
solution: |
  rimborso_trasferta <- function(categorie, importi, giorni){
    mai_rimborsate <- c("minibar", "alcolici", "multa")

    totale <- 0
    for(i in 1:length(importi)){
      if(!(categorie[i] %in% mai_rimborsate)){
        if(categorie[i] == "pasto" & importi[i] > 30){
          totale <- totale + 30            # oltre i 30 euro paga il dipendente
        }else{
          totale <- totale + importi[i]
        }
      }
    }

    # il tetto dipende dalla durata della trasferta
    tetto <- 150 * giorni
    if(totale > tetto){
      totale <- tetto
    }

    return(round(totale, 2))
  }

  rimborso_trasferta(c("treno", "hotel", "pasto", "minibar"), c(49.9, 95, 24.5, 12), 1)   # 150
solution_after: ''
---

L'ufficio amministrazione di una società di consulenza rimborsa ai dipendenti le spese delle trasferte di lavoro. Ogni nota spese arriva come due elenchi della stessa lunghezza, uno accanto all'altro: la **categoria** di ciascuna spesa ("treno", "aereo", "taxi", "hotel", "pasto", "minibar"…) e il suo **importo** in euro, più la durata della trasferta in giorni.

Il regolamento aziendale dice tre cose. Le spese della categoria "minibar", "alcolici" e "multa" **non si rimborsano mai**. Un "pasto" si rimborsa **fino a 30 euro**: un pranzo da 42 euro vale 30, uno da 30 esatti o meno vale quello che è costato; il limite è per ogni singolo pasto, non sul totale dei pasti. Tutte le altre spese si rimborsano per intero. Infine c'è un **tetto complessivo di 150 euro per ogni giorno** di trasferta: se le spese rimborsabili lo superano, si rimborsa il tetto; se ci arrivano esatte, si rimborsano tutte.

Scrivi la funzione `rimborso_trasferta(categorie, importi, giorni)` che restituisce gli euro da rimborsare, con due decimali. Ti serve `%in%` per riconoscere le categorie escluse e `!` per tenere le altre. Prima di scrivere codice, scrivi tu la specifica con i casi al confine: un pasto da 30 euro esatti, una nota fatta solo di spese escluse, una nota che arriva esattamente al tetto.
