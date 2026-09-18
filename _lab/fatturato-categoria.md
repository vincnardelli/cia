---
layout: lab
title: La categoria che vende di più
modulo: 4
order: 3
difficolta: facile
language: R
ai_mode: 'off'
objective: Trovare la categoria di prodotto con il fatturato più alto.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: categoria_top
  type: testo
  desc: il nome della categoria, come scritto nel file
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
regole: |
  - Il fatturato di una categoria è la somma di `TotalAmount` delle sue righe: `group_by(ProductCategory)` e `summarise(fatturato = sum(TotalAmount))`.
  - Ordina con `arrange(desc(fatturato))` e prendi la prima riga.
  - Il risultato è il **testo** della categoria (una stringa), non la tabella: estrailo con `$ProductCategory[1]`.
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(categoria_top)
tests:
- inputs: {}
  expected: Elettronica
  visible: false
  hint: 'Vuoi il nome della categoria, non il suo fatturato: dopo arrange, la prima riga della colonna ProductCategory.'
solution: |
  library(dplyr)

  tabella <- data %>%
    group_by(ProductCategory) %>%
    summarise(fatturato = sum(TotalAmount)) %>%
    arrange(desc(fatturato))
  categoria_top <- tabella$ProductCategory[1]
  categoria_top
solution_after: ''
---

Il direttore commerciale di un negozio online vuole sapere, prima della riunione di budget, quale categoria di prodotto ha generato più fatturato nell'anno. Il data frame `data` è già caricato: una riga per ordine, con la categoria in `ProductCategory` e l'importo in `TotalAmount`.

La domanda vuole un nome, non una tabella: dopo aver sommato il fatturato per categoria e ordinato dal più grande al più piccolo, il risultato è il testo della prima riga. In RStudio guarda anche il secondo e il terzo posto: quanto distacco c'è?
