---
layout: lab
title: Dove si spende di più per ordine
modulo: 5
order: 4
difficolta: facile
language: R
ai_mode: 'on'
objective: Trovare la città con lo scontrino medio più alto.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: citta_top
  type: testo
  desc: il nome della città
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
regole: |
  - Lo **scontrino medio** (ticket medio) di una città è `mean(TotalAmount)` sui suoi ordini: non il fatturato totale, che premia le città grandi.
  - Raggruppa per `City`, calcola media e numero di ordini, ordina per media decrescente, prendi il primo nome.
  - In RStudio guarda quanto sono vicine le prime tre: la differenza è abbastanza grande da decidere qualcosa?
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(citta_top)
tests:
- inputs: {}
  expected: Milano
  visible: false
  hint: 'Media per città, non somma: con la somma vince la città con più ordini.'
solution: |
  library(dplyr)

  tabella <- data %>%
    group_by(City) %>%
    summarise(ticket = mean(TotalAmount), ordini = n()) %>%
    arrange(desc(ticket))
  citta_top <- tabella$City[1]
  citta_top
solution_after: ''
---

Il negozio online sta scegliendo in quale città fare una campagna con un buono sconto sopra una certa spesa. Serve la città dove i clienti spendono di più **per ordine**: lo scontrino medio (ticket medio), non il fatturato totale, che premia semplicemente le città con più ordini.

Il data frame `data` è già caricato. Raggruppa per città, calcola la media di `TotalAmount` e il numero di ordini, ordina per media decrescente e prendi il nome della prima. In RStudio guarda quanto sono vicine le prime tre: la differenza è abbastanza grande per decidere?
