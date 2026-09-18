---
layout: lab
title: 'Segmenti RFM: quanti clienti Gold'
modulo: 5
order: 1
difficolta: facile
language: R
ai_mode: 'off'
objective: Costruire le tre metriche RFM dagli scontrini, assegnare i segmenti con case_when e contare i clienti Gold.
inputs:
- name: scontrini
  type: data frame
  desc: 'già caricato: retail_rfm.csv (CustomerID, InvoiceDate, Quantity, UnitPrice, Total), una riga per riga di scontrino'
risultato:
  name: n_gold
  type: numero
  desc: numero di clienti nel segmento Gold
data_url: dati/retail_rfm.csv
data_var: scontrini
packages:
- dplyr
regole: |
  - Converti la data con `as.Date(scontrini$InvoiceDate)`; la data di riferimento è l'ultima del file (`max`).
  - Per cliente: `recency` = giorni tra la data di riferimento e il suo ultimo acquisto, `frequency` = numero di righe, `monetary` = somma di `Total`.
  - Punteggi con `ntile(desc(recency), 4)`, `ntile(frequency, 4)`, `ntile(monetary, 4)`; segmento con il `case_when` della lezione, in quell'ordine, con `TRUE ~ "Altri"` alla fine.
  - `n_gold` è il numero di clienti con segmento `"Gold"`: dalla tabella, non a occhio.
skeleton: |
  library(dplyr)
  # scontrini è già caricato (in RStudio: scontrini <- read.csv("retail_rfm.csv"))


  print(n_gold)
tests:
- inputs: {}
  expected: 157
  visible: false
  hint: Gold è 4-4-4 su tutti e tre i punteggi, e va controllato per primo nel case_when. Se ottieni un numero diverso, guarda se hai usato desc() sulla recency.
solution: |
  library(dplyr)

  scontrini$InvoiceDate <- as.Date(scontrini$InvoiceDate)
  data_riferimento <- max(scontrini$InvoiceDate)

  rfm <- scontrini %>%
    group_by(CustomerID) %>%
    summarise(recency = as.numeric(data_riferimento - max(InvoiceDate)),
              frequency = n(),
              monetary = sum(Total)) %>%
    mutate(r_score = ntile(desc(recency), 4),
           f_score = ntile(frequency, 4),
           m_score = ntile(monetary, 4)) %>%
    mutate(segmento = case_when(
      r_score == 4 & f_score == 4 & m_score == 4 ~ "Gold",
      r_score == 1 & f_score == 1 & m_score == 1 ~ "Persi",
      f_score == 4 ~ "Fedeli",
      r_score == 4 ~ "Attivi",
      m_score == 4 ~ "Alta spesa",
      TRUE ~ "Altri"
    ))

  gold <- rfm %>%
    filter(segmento == "Gold")
  n_gold <- nrow(gold)
  n_gold
solution_after: ''
---

Il responsabile marketing di una catena di negozi vuole scrivere ai clienti migliori, quelli che il reparto chiama **Gold**: hanno comprato di recente, comprano spesso e spendono molto. Il metodo è l'RFM della lezione: per ogni cliente si calcolano *recency* (giorni dall'ultimo acquisto rispetto all'ultima data del file), *frequency* (numero di righe di scontrino) e *monetary* (totale speso); ogni metrica si trasforma in un punteggio da 1 a 4 con `ntile`, ricordando che per la recency il migliore è chi ha **pochi** giorni; e i segmenti si assegnano con il `case_when` della lezione, nell'ordine: Gold se 4-4-4, Persi se 1-1-1, Fedeli se frequency 4, Attivi se recency 4, Alta spesa se monetary 4, Altri per tutti gli altri.

Il data frame `scontrini` è già caricato (in RStudio: `read.csv("retail_rfm.csv")`); la data va convertita con `as.Date`. La domanda è una sola: quanti clienti sono Gold. Il numero deve uscire dalla tabella, con un `filter` o un `group_by`, non contato a occhio.
