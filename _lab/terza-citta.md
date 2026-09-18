---
layout: lab
title: Le città con più ordini
modulo: 4
order: 5
difficolta: facile
language: R
ai_mode: 'on'
objective: Trovare la terza città per numero di ordini.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: terza
  type: testo
  desc: il nome della terza città in classifica
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
regole: |
  - Conta gli ordini per città: `group_by(City)` e `summarise(n = n())`.
  - Ordina dalla più grande alla più piccola e prendi la **terza** riga.
  - Il risultato è il nome della città (testo).
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(terza)
tests:
- inputs: {}
  expected: Torino
  visible: false
  hint: 'Terza riga dopo l''ordinamento decrescente: tabella$City[3]. Se ordini in senso crescente prendi la terzultima.'
solution: |
  library(dplyr)

  classifica <- data %>%
    group_by(City) %>%
    summarise(n = n()) %>%
    arrange(desc(n))
  terza <- classifica$City[3]
  terza
solution_after: ''
---

Il negozio online vuole aprire un punto di ritiro in una terza città, dopo le due dove già c'è. La scelta più semplice è la terza città per numero di ordini. Il data frame `data` è già caricato, con la città di consegna in `City`.

Conta gli ordini per città, ordina dalla più grande alla più piccola e prendi il nome della terza. Attenzione al verso dell'ordinamento: se ordini in senso crescente, la terza riga è una città piccola.
