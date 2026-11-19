---
layout: page
title: "Chiusura del conto corrente"
permalink: /progetti/2/banca_conti/
parent: Progetti
nav_exclude: true
---

# Chiusura del conto corrente

**Settore:** Banca e finanza · **Righe:** 3000 · **Colonne:** 15 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/banca_conti.csv){: .btn .btn-primary }

## Il contesto

Una banca retail vuole sapere quali clienti stanno per chiudere il conto, per provare a trattenerli prima che lo facciano. Trattenere un cliente costa molto meno che acquisirne uno nuovo, ma le offerte di retention costano, quindi vanno mandate a chi serve.

Il dataset è una fotografia dei conti a inizio anno, con quello che è successo nei dodici mesi dopo. Attenzione: **qui chiude il 28%, mentre in Italia il tasso di chiusura stimato è il 5-7% l'anno** (ricostruito dalla distribuzione dell'anzianità dei conti pubblicata da Banca d'Italia). Il famoso dataset «Churn Modelling» che si trova in rete usa il 20% ed è anch'esso una convenzione, non un dato.

## La domanda

A quali clienti mandare un'offerta di retention, sapendo che la banca può contattarne circa il 15%?

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `eta` | numerica | 18-90 anni | età dell'intestatario |
| `anzianita_anni` | numerica | 0,1-35 | da quanti anni il cliente ha il conto |
| `tipo_conto` | categorica | tradizionale / online / postale | tipo di conto |
| `prodotti` | numerica | 1-5 | quanti prodotti della banca ha il cliente (conto, carta, fondi, assicurazione…) |
| `saldo_medio` | numerica | 0-120.000 € | giacenza media nell'anno |
| `variazione_saldo_12m` | numerica | −95 / +150 % | variazione percentuale della giacenza nei dodici mesi |
| `operazioni_anno` | numerica | 0-1.200 | numero di operazioni nell'anno |
| `mesi_inattivo` | numerica | 0-12 | mesi consecutivi senza operazioni |
| `reclami_12m` | numerica | 0-4 | reclami presentati nell'anno |
| `costo_annuo` | numerica | 0-400 € | spese annue del conto |
| `mutuo` | categorica | si / no | il cliente ha un mutuo con la banca |
| `carta_credito` | categorica | si / no | il cliente ha una carta di credito |
| `filiale_vicina` | categorica | si / no | c'è una filiale nel comune di residenza |
| `canale_digitale` | categorica | si / no | il cliente usa l'home banking |
| `chiude_conto` | **target** | `si` / `no` | il cliente ha chiuso il conto nei dodici mesi successivi alla fotografia dei dati |

Le colonne `saldo_medio`, `operazioni_anno` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/banca_conti.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/banca_conti.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **72 %** dei casi, perché i casi con `chiude_conto` uguale a «si» sono circa il 28 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
