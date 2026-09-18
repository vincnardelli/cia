---
layout: lab
title: Sconto e quantità
modulo: 5
order: 3
difficolta: facile
language: R
ai_mode: 'on'
objective: Misurare quanto lo sconto applicato e i pezzi acquistati crescono insieme.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: correlazione
  type: numero
  desc: coefficiente di correlazione, 3 decimali
data_url: dati/ecommerce.csv
data_var: data
tolerance: 0.002
regole: |
  - `cor(x, y)` va da −1 a +1: vicino a +1 le due colonne salgono insieme, vicino a 0 non c'è legame.
  - Calcola la correlazione tra `Discount` e `Quantity` e arrotonda a 3 decimali.
  - In RStudio fai il grafico a dispersione con ggplot2 e poi confronta con la correlazione tra `Discount` e `TotalAmount`: perché è più bassa?
skeleton: |
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(correlazione)
tests:
- inputs: {}
  expected: 0.673
  visible: true
  hint: 'La correlazione è simmetrica, cor(a, b) = cor(b, a): se il numero non torna, hai preso una colonna sbagliata (TotalAmount al posto di Quantity?).'
solution: |
  correlazione <- round(cor(data$Discount, data$Quantity), 3)
  correlazione
solution_after: ''
---

Il responsabile vendite del negozio online sostiene che gli sconti fanno comprare più pezzi. Il responsabile finanza sostiene che gli sconti fanno solo spendere di meno. Prima di litigare, un numero: quanto lo sconto applicato all'ordine e i pezzi acquistati crescono insieme.

Il data frame `data` è già caricato, con lo sconto in percentuale in `Discount` e i pezzi in `Quantity`. Lo strumento è il coefficiente di correlazione, `cor(x, y)`, da −1 a +1. Arrotonda a tre decimali. Poi, in RStudio, calcola anche la correlazione tra sconto e importo dell'ordine: è più bassa, e vale la pena chiedersi perché.
