---
layout: lab
title: Provvigioni dell'agente
modulo: 3
order: 8
difficolta: difficile
language: R
ai_mode: 'on'
objective: Calcolare le provvigioni annue di un agente di commercio a partire dal venduto di ciascun mese, con scaglioni progressivi.
inputs:
- name: vendite
  type: vettore di numeri
  desc: venduto in euro in ciascuno dei 12 mesi
risultato:
  name: provvigioni
  type: numero
  desc: totale annuo in euro, 2 decimali
regole: |
  - In ogni mese: **3%** sul venduto fino a 10.000 €; **5%** sulla parte tra 10.000 e 20.000 €; **8%** sulla parte oltre 20.000 €.
  - Gli scaglioni sono progressivi (come l'IRPEF): ogni aliquota si applica solo alla fetta che cade nella sua fascia.
  - Le provvigioni annue sono la somma dei dodici mesi, arrotondata a due decimali.
skeleton: |
  vendite <- c(8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000)

  print(provvigioni)
tests:
- inputs:
    vendite:
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
    - 8000
  expected: 2880.0
  visible: true
- inputs:
    vendite:
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
    - 15000
  expected: 6600.0
  visible: false
- inputs:
    vendite:
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
    - 10000
  expected: 3600.0
  visible: false
  boundary: true
  hint: '10.000 esatti stanno tutti nel primo scaglione: 300 al mese.'
- inputs:
    vendite:
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
    - 20000
  expected: 9600.0
  visible: false
  boundary: true
  hint: '20.000: 300 sul primo scaglione più 500 sul secondo, niente terzo.'
- inputs:
    vendite:
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
    - 25000
  expected: 14400.0
  visible: false
  boundary: true
- inputs:
    vendite:
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  expected: 0.0
  visible: false
  boundary: true
- inputs:
    vendite:
    - 3000
    - 12000
    - 27000
    - 9999.5
    - 10000.5
    - 0
    - 18000
    - 22000
    - 5000
    - 30000
    - 11000
    - 7000
  expected: 6420.01
  visible: false
solution: |
  vendite <- c(8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000)

  provvigioni <- 0
  for(i in 1:length(vendite)){
    v <- vendite[i]
    if(v <= 10000){
      mese <- v * 0.03
    }else if(v <= 20000){
      mese <- 10000 * 0.03 + (v - 10000) * 0.05
    }else{
      mese <- 10000 * 0.03 + 10000 * 0.05 + (v - 20000) * 0.08
    }
    provvigioni <- provvigioni + mese
  }
  provvigioni <- round(provvigioni, 2)
  provvigioni
solution_after: ''
---

Un'azienda che vende macchine per il caffè ai bar paga i propri agenti a provvigione, con un contratto a **scaglioni progressivi calcolati mese per mese**: sul venduto di ogni mese, il 3% sulla parte fino a 10.000 euro, il 5% sulla parte tra 10.000 e 20.000, l'8% sulla parte oltre i 20.000. È lo stesso meccanismo dell'IRPEF: ogni aliquota si applica solo alla fetta che cade nella sua fascia, non a tutto il venduto.

Un agente con 25.000 euro di venduto in un mese prende quindi 300 sul primo scaglione, 500 sul secondo e 400 sul terzo; uno con 10.000 esatti prende 300 e basta. L'ufficio amministrazione ti passa il vettore del venduto dei dodici mesi di un agente e vuole le provvigioni dell'anno, con due decimali.

Prima di scrivere codice, scrivi tu la specifica con i casi al confine (10.000 esatti, 20.000 esatti, un mese a zero), poi ragiona su come applicare la regola a un mese, e infine ripetila con un ciclo.
