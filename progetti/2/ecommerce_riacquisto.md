---
layout: page
title: "Riacquisto entro 90 giorni"
permalink: /progetti/2/ecommerce_riacquisto/
parent: Progetti
nav_exclude: true
---

# Riacquisto entro 90 giorni

**Settore:** Marketing ed e-commerce · **Righe:** 3000 · **Colonne:** 13 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/ecommerce_riacquisto.csv){: .btn .btn-primary }

## Il contesto

Un negozio online multicategoria ha un budget per inviare buoni sconto, e vuole spenderlo su chi sta per sparire, non su chi comprerebbe comunque. Prima di decidere a chi mandarli, serve capire chi riacquista e chi no.

Il dataset è la base clienti alla fine di un trimestre, con quello che hanno fatto nei 90 giorni dopo. Il 32% di riacquisti è realistico per un negozio multicategoria (il riferimento pubblicato più solido dice che il 32% dei clienti compra una seconda volta entro un anno).

## La domanda

A chi mandare il buono sconto? E soprattutto: il buono va a chi riacquista comunque o a chi è sul punto di andarsene?

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `giorni_ultimo_acquisto` | numerica | 1-540 | giorni trascorsi dall'ultimo ordine (recency) |
| `acquisti_12_mesi` | numerica | 1-40 | ordini fatti nei dodici mesi (frequency) |
| `scontrino_medio` | numerica | € | valore medio dell'ordine (monetary) |
| `categoria_prevalente` | categorica | beauty / abbigliamento / alimentari / arredamento / elettronica | categoria in cui il cliente spende di più |
| `categorie_distinte` | numerica | 1-6 | in quante categorie diverse ha comprato |
| `resi_percentuale` | numerica | 0-60 % | quota di articoli resi |
| `sconto_primo_ordine` | numerica | 0-45 % | sconto applicato al primo ordine |
| `canale_acquisizione` | categorica | ricerca / social / passaparola / pubblicita a pagamento | come è arrivato il cliente |
| `newsletter` | categorica | si / no | iscritto alla newsletter |
| `dispositivo` | categorica | telefono / computer / app | dispositivo usato più spesso |
| `consegna_in_ritardo` | categorica | si / no | l'ultimo ordine è arrivato in ritardo |
| `anni_cliente` | numerica | 0,1-12 | da quanto tempo è cliente |
| `riacquista_90gg` | **target** | `si` / `no` | il cliente ha fatto un altro ordine entro 90 giorni dall'ultimo |

Le colonne `resi_percentuale`, `scontrino_medio` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/ecommerce_riacquisto.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/ecommerce_riacquisto.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **68 %** dei casi, perché i casi con `riacquista_90gg` uguale a «si» sono circa il 32 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
