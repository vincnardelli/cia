---
layout: lab
title: La categoria che torna indietro di più
modulo: 4
order: 6
difficolta: difficile
language: R
ai_mode: 'on'
objective: Trovare la categoria di prodotto con il tasso di reso più alto.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: categoria_resi
  type: testo
  desc: il nome della categoria
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
regole: |
  - Per ogni categoria il tasso di reso è la media di `ReturnStatus` (non la somma: le categorie hanno numeri di ordini diversi).
  - Ordina per tasso decrescente e prendi il nome della prima categoria.
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))

  print(categoria_resi)
tests:
- inputs: {}
  expected: Abbigliamento
  visible: false
  hint: 'Media, non somma: con la somma vince semplicemente la categoria con più ordini.'
solution: |
  library(dplyr)

  tabella <- data %>%
    group_by(ProductCategory) %>%
    summarise(tasso = mean(ReturnStatus)) %>%
    arrange(desc(tasso))
  categoria_resi <- tabella$ProductCategory[1]
  categoria_resi
solution_after: ''
---

Il responsabile qualità del negozio online vuole capire su quale categoria di prodotto concentrare i controlli: quella che viene resa più spesso. Non la categoria con più resi in assoluto, che sarebbe semplicemente quella con più ordini, ma quella con la quota di resi più alta rispetto ai suoi ordini.

Il data frame `data` è già caricato; `ReturnStatus` vale 1 per gli ordini resi. Il risultato è il nome della categoria.
