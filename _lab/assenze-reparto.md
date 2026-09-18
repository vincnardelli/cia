---
layout: lab
title: Assenze per reparto
modulo: 5
order: 5
difficolta: difficile
language: R
ai_mode: 'on'
objective: Trovare il reparto con più giorni di assenza per addetto.
inputs:
- name: personale
  type: data frame
  desc: 'già caricato: personale.csv (id, reparto, ruolo, sede, anno_assunzione, stipendio_lordo, giorni_assenza, part_time), una riga per dipendente'
risultato:
  name: reparto_assenze
  type: testo
  desc: il nome del reparto
data_url: dati/personale.csv
data_var: personale
packages:
- dplyr
regole: |
  - Il confronto giusto è **per addetto**: giorni di assenza totali del reparto diviso il numero di dipendenti del reparto (cioè la media di `giorni_assenza`).
  - Raggruppa per `reparto`, calcola la media, ordina in senso decrescente, prendi il primo nome.
skeleton: |
  library(dplyr)
  # personale è già caricato (in RStudio: personale <- read.csv("personale.csv"))

  print(reparto_assenze)
tests:
- inputs: {}
  expected: Logistica
  visible: false
  hint: 'Per addetto, non totale: Vendite ha più assenze in tutto perché ha più persone. La media di giorni_assenza per reparto è il numero giusto.'
solution: |
  library(dplyr)

  tabella <- personale %>%
    group_by(reparto) %>%
    summarise(addetti = n(), per_addetto = mean(giorni_assenza)) %>%
    arrange(desc(per_addetto))
  reparto_assenze <- tabella$reparto[1]
  reparto_assenze
solution_after: ''
---

La direttrice del personale di un'azienda di servizi vuole capire in quale reparto il tema delle assenze pesa di più, per parlarne con il responsabile. Il primo conto che le hanno portato, i giorni di assenza totali per reparto, non la convince: le Vendite risultano prime, ma sono anche il reparto con più persone. Il confronto sensato è **per addetto**: i giorni di assenza di un reparto divisi per il numero di dipendenti di quel reparto.

Il data frame `personale` è già caricato (in RStudio: `read.csv("personale.csv")`): una riga per dipendente, con `reparto` e `giorni_assenza`. Il risultato che vuole è il nome del reparto con più giorni di assenza per addetto.
