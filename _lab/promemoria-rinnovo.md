---
layout: lab
title: Promemoria di rinnovo
modulo: 4
order: 3
difficolta: facile
language: R
ai_mode: 'off'
objective: Scrivere una funzione che conta a quanti soci con l'abbonamento in scadenza va mandato il promemoria, escludendo chi ha già rinnovato e chi ha chiesto di non essere contattato, con %in% e !.
inputs:
- name: in_scadenza
  type: vettore di testi
  desc: codici tessera dei soci con l'abbonamento in scadenza questo mese
- name: rinnovati
  type: vettore di testi
  desc: codici tessera di chi ha già rinnovato
- name: non_contattare
  type: vettore di testi
  desc: codici tessera di chi ha negato il consenso ai messaggi
risultato:
  name: messaggi
  type: numero
  desc: quanti promemoria mandare
function: promemoria
regole: |
  - Un socio riceve il promemoria se è in `in_scadenza`, **non** è in `rinnovati` **e** **non** è in `non_contattare`. Basta essere in uno dei due elenchi per essere escluso.
  - `in_scadenza %in% rinnovati` dà un `TRUE` per ogni socio che ha già rinnovato; `!` rovescia i `TRUE` in `FALSE` e viceversa.
  - Gli elenchi `rinnovati` e `non_contattare` possono contenere anche codici che non sono in scadenza: non contano.
  - Puoi selezionare i soci da avvisare con le parentesi quadre e contarli con `length()`, oppure scorrere `in_scadenza` con un ciclo `for` e un contatore.
  - La funzione restituisce il numero con `return()`.
skeleton: |
  promemoria <- function(in_scadenza, rinnovati, non_contattare){
    # chi ha già rinnovato? chi non vuole messaggi?
    # ...

    # tieni solo i soci che non sono in nessuno dei due elenchi
    # ...

    # restituisci quanti sono
    # ...
  }

  # prova: deve dare 2
  print(promemoria(c("T01", "T02", "T03", "T04"), c("T02"), c("T04")))
tests:
- inputs:
    in_scadenza:
    - T01
    - T02
    - T03
    - T04
    rinnovati:
    - T02
    non_contattare:
    - T04
  expected: 2
  visible: true
- inputs:
    in_scadenza:
    - T10
    - T11
    - T12
    rinnovati:
    - T10
    - T11
    - T12
    non_contattare:
    - T99
  expected: 0
  visible: true
- inputs:
    in_scadenza:
    - T05
    rinnovati:
    - T01
    non_contattare:
    - T02
  expected: 1
  visible: false
  boundary: true
  hint: 'Un solo socio in scadenza, che non è in nessuno dei due elenchi: riceve il promemoria.'
- inputs:
    in_scadenza:
    - T01
    - T02
    rinnovati:
    - T03
    non_contattare:
    - T01
    - T02
  expected: 0
  visible: false
  boundary: true
  hint: 'Nessuno ha rinnovato, ma tutti hanno negato il consenso: nessun messaggio.'
- inputs:
    in_scadenza:
    - T01
    - T02
    - T03
    - T04
    - T05
    - T06
    rinnovati:
    - T03
    - T08
    - T09
    non_contattare:
    - T05
    - T03
  expected: 4
  visible: false
  hint: 'T03 è in tutti e due gli elenchi, T05 solo in non_contattare: sono esclusi entrambi. Basta un elenco per essere escluso.'
- inputs:
    in_scadenza:
    - A101
    - A102
    - A103
    - A104
    - A105
    - A106
    - A107
    rinnovati:
    - A102
    - A106
    non_contattare:
    - A107
  expected: 4
  visible: false
- inputs:
    in_scadenza:
    - B01
    - B02
    - B03
    rinnovati:
    - B07
    - B08
    non_contattare:
    - B09
  expected: 3
  visible: false
  hint: 'Nessuno dei soci in scadenza compare negli altri due elenchi: vanno avvisati tutti e tre.'
solution: |
  promemoria <- function(in_scadenza, rinnovati, non_contattare){
    # TRUE per chi va escluso, in ciascuno dei due elenchi
    ha_rinnovato <- in_scadenza %in% rinnovati
    senza_consenso <- in_scadenza %in% non_contattare

    # si avvisa chi NON ha rinnovato E NON ha negato il consenso
    da_avvisare <- in_scadenza[!ha_rinnovato & !senza_consenso]

    return(length(da_avvisare))
  }

  promemoria(c("T01", "T02", "T03", "T04"), c("T02"), c("T04"))   # 2
solution_after: ''
---

Una catena di palestre manda ogni mese un messaggio ai soci con l'abbonamento **in scadenza**, per ricordare di rinnovarlo. Il messaggio però non va mandato a tutti: chi ha **già rinnovato** in anticipo si irrita a ricevere il sollecito, e chi ha **negato il consenso** ai messaggi commerciali non può essere contattato, per legge.

Dal gestionale escono tre elenchi di codici tessera: i soci in scadenza questo mese, i soci che hanno già rinnovato (anche in anticipo di mesi, quindi non tutti sono in scadenza) e i soci che non vogliono essere contattati. Il responsabile marketing vuole sapere **quanti messaggi** partiranno, per comprare il pacchetto di SMS giusto.

Scrivi la funzione `promemoria(in_scadenza, rinnovati, non_contattare)` che restituisce quanti soci vanno avvisati, usando `%in%` per sapere se un codice è in un elenco e `!` per tenere quelli che non ci sono. La verifica chiama la tua funzione con gli elenchi di ogni caso.
