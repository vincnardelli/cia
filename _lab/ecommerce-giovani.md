---
layout: lab
title: Clienti giovani
modulo: 4
order: 1
difficolta: facile
language: R
ai_mode: 'off'
objective: Contare gli ordini fatti da clienti con meno di 35 anni nel dataset ecommerce.
inputs:
- name: data
  type: data frame
  desc: 'già caricato: il file ecommerce.csv (colonne CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus)'
risultato:
  name: n_giovani
  type: numero
  desc: numero di righe con Age < 35
data_url: dati/ecommerce.csv
data_var: data
packages:
- dplyr
regole: |
  - Il data frame `data` è già caricato quando premi Verifica (in RStudio: `data <- read.csv("ecommerce.csv")`).
  - Conta le righe con `Age < 35`. La colonna `Age` ha valori mancanti: decidi cosa farne e scrivilo nel codice, non lasciarlo al caso.
  - Il risultato deve essere un **numero** (non una tabella): da una pipeline dplyr, estrailo con `$n` oppure usa `nrow()` / `sum()`.
skeleton: |
  library(dplyr)
  # data è già caricato (in RStudio: data <- read.csv("ecommerce.csv"))


  print(n_giovani)
tests:
- inputs: {}
  expected: 3523
  visible: true
  hint: 'Ricorda: gli NA in Age non sono né < 35 né >= 35. Con filter() spariscono in silenzio; con sum(data$Age < 35) restituiscono NA se non usi na.rm = TRUE.'
solution: |
  library(dplyr)

  n_giovani <- data %>%
    filter(!is.na(Age), Age < 35) %>%
    summarise(n = n())
  n_giovani <- n_giovani$n
  n_giovani
solution_after: ''
---

Il responsabile marketing di un negozio online vuole capire quanto pesano i **clienti giovani** sugli ordini, per decidere se investire in una campagna sui social. Ti passa l'estratto degli ordini dell'anno (`ecommerce.csv`, una riga per ordine, con le colonne CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus) e ti chiede una prima cifra: quanti ordini sono stati fatti da clienti con meno di 35 anni.

Il data frame `data` è già caricato quando premi Verifica (in RStudio lo carichi tu con `read.csv`). C'è una trappola: la colonna `Age` ha dei **valori mancanti**, perché non tutti i clienti hanno indicato l'età. Devi decidere cosa farne e scriverlo nel codice, non lasciarlo al caso. Il risultato deve essere un numero, non una tabella.
