---
layout: lab
title: Quanti ordini tornano indietro
modulo: 4
order: 4
difficolta: facile
language: R
ai_mode: 'on'
objective: Calcolare la quota di ordini resi tra quelli pagati con PayPal.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)'
risultato:
  name: tasso_paypal
  type: numero
  desc: quota tra 0 e 1, 3 decimali
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
tolerance: 0.002
regole: |
  - `ReturnStatus` vale 1 se l'ordine è stato reso, 0 altrimenti: la sua **media** è già la quota di resi.
  - Tieni solo le righe con `PaymentMethod == "PayPal"` e calcola la media; arrotonda a 3 decimali.
  - In RStudio confronta i quattro metodi con `group_by(PaymentMethod)`: il reso dipende da come si paga?
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(tasso_paypal)
tests:
- inputs: {}
  expected: 0.33
  visible: true
  hint: 'Il denominatore sono gli ordini PayPal, non tutti gli ordini: filtra prima di fare la media.'
solution: |
  library(dplyr)

  paypal <- data %>%
    filter(PaymentMethod == "PayPal")
  tasso_paypal <- round(mean(paypal$ReturnStatus), 3)
  tasso_paypal
solution_after: ''
---

Il responsabile logistica di un negozio online sospetta che gli ordini pagati con PayPal vengano resi più spesso, perché il reso è più semplice da avviare. Prima di cambiare le condizioni vuole un numero.

Il data frame `data` è già caricato; la colonna `ReturnStatus` vale 1 se l'ordine è stato reso e 0 altrimenti, quindi la sua media è già la quota di resi. Calcola la quota di resi tra gli ordini pagati con PayPal (`PaymentMethod == "PayPal"`), arrotondata a tre decimali. Poi, in RStudio, confronta i quattro metodi di pagamento: il sospetto regge?
