---
layout: lab
title: Il corriere più regolare
modulo: 5
order: 2
difficolta: facile
language: R
ai_mode: 'off'
objective: Trovare il corriere con i tempi di consegna più regolari, cioè con la deviazione standard più bassa.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: corriere_regolare
  type: testo
  desc: il nome del corriere
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
regole: |
  - Regolare non vuol dire veloce: un corriere che consegna sempre in 4 giorni è più prevedibile di uno che va da 1 a 8. La regolarità si misura con `sd(DeliveryDays)`.
  - Per corriere: `group_by(Courier)` e `summarise(media = mean(DeliveryDays), variabilita = sd(DeliveryDays))`.
  - Ordina per variabilità crescente e prendi il primo nome. In RStudio guarda anche la media: il più regolare è anche il più veloce?
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(corriere_regolare)
tests:
- inputs: {}
  expected: DHL
  visible: false
  hint: 'Ordina per sd crescente (arrange senza desc): il più regolare è quello con la deviazione standard più piccola, non più grande.'
solution: |
  library(dplyr)

  tabella <- data %>%
    group_by(Courier) %>%
    summarise(media = mean(DeliveryDays), variabilita = sd(DeliveryDays)) %>%
    arrange(variabilita)
  corriere_regolare <- tabella$Courier[1]
  corriere_regolare
solution_after: ''
---

Il negozio online lavora con quattro corrieri e riceve lamentele sui tempi di consegna. Il responsabile logistica non cerca il corriere più veloce: cerca quello **più regolare**, perché un cliente accetta 4 giorni se glieli hai promessi, non accetta che a volte siano 2 e a volte 8. La regolarità si misura con la deviazione standard dei giorni di consegna, come nella lezione la variabilità di un titolo.

Il data frame `data` è già caricato, con il corriere in `Courier` e i giorni in `DeliveryDays`. Per ogni corriere calcola media e deviazione standard, ordina per deviazione crescente e prendi il primo nome. In RStudio guarda anche la media: il più regolare è anche il più veloce?
