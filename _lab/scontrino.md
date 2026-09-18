---
layout: lab
title: Scontrino
modulo: 1
order: 1
difficolta: facile
language: R
ai_mode: 'off'
objective: Calcolare il totale di uno scontrino a partire dal prezzo netto e dalla quantità, con IVA al 22%.
inputs:
- name: prezzo_netto
  type: numero
  desc: prezzo unitario senza IVA, in euro
- name: quantita
  type: numero
  desc: pezzi acquistati
risultato:
  name: totale
  type: numero
  desc: totale da pagare, arrotondato a 2 decimali
regole: |
  - Il totale netto è `prezzo_netto * quantita`.
  - L'IVA è il 22% del totale netto: il totale da pagare è il netto più l'IVA.
  - Arrotonda il risultato a due decimali con `round(x, 2)`.
skeleton: |
  prezzo_netto <- 10
  quantita <- 3


  print(totale)
tests:
- inputs:
    prezzo_netto: 10
    quantita: 3
  expected: 36.6
  visible: true
- inputs:
    prezzo_netto: 19.9
    quantita: 1
  expected: 24.28
  visible: true
- inputs:
    prezzo_netto: 10
    quantita: 0
  expected: 0.0
  visible: false
  boundary: true
  hint: 'Con zero pezzi il totale deve essere 0: il tuo codice lo gestisce senza bisogno di un caso speciale?'
- inputs:
    prezzo_netto: 0.99
    quantita: 7
  expected: 8.45
  visible: false
  boundary: true
  hint: 'Con i centesimi l''arrotondamento conta: hai usato round(x, 2) sul totale finale, non sul prezzo unitario?'
- inputs:
    prezzo_netto: 1234.5
    quantita: 2
  expected: 3012.18
  visible: false
solution: |
  prezzo_netto <- 10
  quantita <- 3

  netto <- prezzo_netto * quantita
  iva <- netto * 0.22
  totale <- round(netto + iva, 2)
  totale
solution_after: ''
---

Lavori nel piccolo negozio di elettronica di famiglia e il registratore di cassa si è rotto proprio il giorno dei saldi. Tuo zio ti passa un foglio con i prezzi **netti** dei prodotti, cioè senza IVA, e ti chiede di calcolare a mano quanto far pagare a ogni cliente.

Il primo cliente compra tre cavi HDMI da 10 € l'uno. Tu sai che in Italia l'IVA ordinaria è del 22% e che si applica sul totale della merce, non sul singolo pezzo. Il totale va scritto sullo scontrino con due decimali, come su qualsiasi ricevuta.

Scrivi il programma che, dati prezzo netto e quantità, calcola il totale da pagare. Tuo zio lo userà tutto il giorno, quindi deve funzionare anche nei casi strani: un cliente che ci ripensa e compra zero pezzi, o un prezzo con i centesimi.
