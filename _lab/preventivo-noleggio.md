---
layout: lab
title: Preventivo del noleggio
modulo: 4
order: 5
difficolta: difficile
language: R
ai_mode: 'on'
objective: Scomporre il preventivo di un noleggio auto in tre funzioni piccole (giorni, chilometri, supplemento per i giovani) e scrivere la funzione principale che le usa.
inputs:
- name: giorni
  type: numero
  desc: giorni di noleggio, almeno 1
- name: km
  type: numero
  desc: chilometri che il cliente prevede di percorrere
- name: eta
  type: numero
  desc: età del conducente in anni compiuti
risultato:
  name: totale
  type: numero
  desc: prezzo del noleggio in euro, 2 decimali
function: preventivo
regole: |
  - Noleggio: 45 € al giorno; da 7 giorni in su (7 compreso) tutti i giorni a 38 €.
  - Chilometri: inclusi 200 km per ogni giorno di noleggio; ogni km oltre gli inclusi costa 0,25 €.
  - Conducente con meno di 25 anni: supplemento di 12 € al giorno; con 25 anni compiuti nessun supplemento.
  - Il preventivo è la somma delle tre voci, 2 decimali.
  - Tre funzioni piccole, una per voce, e `preventivo(giorni, km, eta)` che le chiama.
skeleton: |
  preventivo <- function(giorni, km, eta){

  }
tests:
- inputs:
    giorni: 3
    km: 500
    eta: 30
  expected: 135.0
  visible: true
- inputs:
    giorni: 2
    km: 550
    eta: 22
  expected: 151.5
  visible: true
- inputs:
    giorni: 7
    km: 900
    eta: 40
  expected: 266.0
  visible: false
  boundary: true
  hint: 'Sette giorni esatti hanno già la tariffa settimanale: 7 x 38 €.'
- inputs:
    giorni: 6
    km: 1200
    eta: 50
  expected: 270.0
  visible: false
  boundary: true
  hint: 'Sei giorni includono 6 x 200 = 1200 km: nessun chilometro da pagare.'
- inputs:
    giorni: 4
    km: 300
    eta: 25
  expected: 180.0
  visible: false
  boundary: true
  hint: 'Con 25 anni compiuti il supplemento giovani non si paga.'
- inputs:
    giorni: 1
    km: 350
    eta: 19
  expected: 94.5
  visible: false
  boundary: true
  hint: 'Un giorno solo: 45 € di noleggio, 150 km oltre i 200 inclusi, 12 € di supplemento.'
- inputs:
    giorni: 10
    km: 2600
    eta: 24
  expected: 650.0
  visible: false
- inputs:
    giorni: 8
    km: 1000
    eta: 21
  expected: 400.0
  visible: false
solution: |
  # ---- Le tre voci, una funzione ciascuna ----

  costo_giorni <- function(giorni){
    if(giorni >= 7){
      tariffa <- 38          # tariffa settimanale, su tutti i giorni
    }else{
      tariffa <- 45
    }
    return(giorni * tariffa)
  }

  costo_km <- function(km, giorni){
    inclusi <- 200 * giorni
    if(km > inclusi){
      return((km - inclusi) * 0.25)
    }else{
      return(0)
    }
  }

  supplemento_giovane <- function(eta, giorni){
    if(eta < 25){
      return(12 * giorni)
    }else{
      return(0)
    }
  }

  # ---- La funzione principale: mette insieme le tre voci ----

  preventivo <- function(giorni, km, eta){
    totale <- costo_giorni(giorni) + costo_km(km, giorni) + supplemento_giovane(eta, giorni)
    return(round(totale, 2))
  }

  costo_giorni(7)            # 266
  costo_km(550, 2)           # 37.5
  supplemento_giovane(25, 4) # 0
  preventivo(2, 550, 22)     # 151.5
solution_after: ''
---

Un'agenzia di noleggio auto vuole che il sito mostri subito il **preventivo** a chi indica quanti giorni gli serve l'auto, quanti chilometri pensa di fare e quanti anni ha. Il listino ha tre voci, e il responsabile commerciale le cambia spesso, una alla volta: per questo vuole il codice diviso in **una funzione per voce**, da provare e correggere separatamente, più una funzione principale che le somma.

Le voci sono queste. Il **noleggio** costa 45 euro al giorno; da 7 giorni in su, 7 compreso, scatta la tariffa settimanale e tutti i giorni costano 38 euro. I **chilometri**: sono inclusi 200 km per ogni giorno di noleggio (tre giorni, 600 km inclusi), e ogni chilometro oltre quelli inclusi costa 0,25 euro. Il **supplemento giovani**: se il conducente ha meno di 25 anni si pagano 12 euro in più per ogni giorno; con 25 anni compiuti non si paga.

Scrivi tre funzioni piccole, `costo_giorni(giorni)`, `costo_km(km, giorni)` e `supplemento_giovane(eta, giorni)`, e la funzione principale `preventivo(giorni, km, eta)` che le chiama e restituisce la somma con due decimali. La verifica chiama solo `preventivo()`, ma provala anche voce per voce: ognuna delle tre funzioni deve ricevere come argomenti tutto quello che le serve, giorni compresi.
