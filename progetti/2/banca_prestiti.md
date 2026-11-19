---
layout: page
title: "Insolvenze sul credito al consumo"
permalink: /progetti/2/banca_prestiti/
parent: Progetti
nav_exclude: true
---

# Insolvenze sul credito al consumo

**Settore:** Banca e finanza · **Righe:** 2800 · **Colonne:** 15 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/banca_prestiti.csv){: .btn .btn-primary }

## Il contesto

Una società di credito al consumo concede prestiti personali e finalizzati. Oggi la decisione la prende un regolamento interno scritto anni fa; l'ufficio rischi vuole sapere se dai dati dei prestiti già erogati si possono ricavare regole migliori.

Il dataset contiene i prestiti erogati in un anno, con la situazione del cliente al momento della richiesta e l'esito a ventiquattro mesi. Attenzione: **qui gli insolventi sono il 30%, mentre il tasso di deterioramento del credito al consumo in Italia è il 2,3%** (Banca d'Italia, 2025). Il campione è stato arricchito, altrimenti il problema sarebbe ingestibile con gli strumenti del corso.

## La domanda

Quali richieste conviene rifiutare, o mandare a istruttoria manuale? Ogni insolvenza costa in media quanto venti pratiche buone di margine.

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `eta` | numerica | 20-78 anni | età del richiedente |
| `area` | categorica | nord ovest / nord est / centro / sud e isole | area di residenza |
| `reddito_mensile` | numerica | 700-9.000 € | reddito netto mensile dichiarato |
| `importo_prestito` | numerica | 500-90.000 € | importo erogato |
| `durata_mesi` | numerica | 12-120 | durata del piano di ammortamento |
| `taeg` | numerica | 5-19 % | TAEG applicato |
| `rata_mensile` | numerica | € | rata mensile calcolata su importo, durata e TAEG |
| `incidenza_rata` | numerica | 0-1 | rata mensile divisa per il reddito mensile |
| `ritardi_passati` | numerica | 0-4 | ritardi superiori a 30 giorni su altri crediti negli ultimi due anni |
| `utilizzo_credito` | numerica | 0-100 % | quota di fido e carte già utilizzata |
| `carte_credito` | numerica | 0-15 | numero di linee di credito attive |
| `anni_lavoro` | numerica | 0-40 | anzianità lavorativa presso il datore attuale |
| `tipo_contratto` | categorica | indeterminato / determinato / autonomo | tipo di contratto di lavoro |
| `finalita` | categorica | auto / ristrutturazione / consolidamento debiti / piccola impresa / matrimonio / altro | scopo dichiarato del prestito |
| `insolvente` | **target** | `si` / `no` | il cliente è andato oltre 90 giorni di ritardo entro due anni dall'erogazione |

Le colonne `anni_lavoro`, `utilizzo_credito` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/banca_prestiti.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/banca_prestiti.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **70 %** dei casi, perché i casi con `insolvente` uguale a «si» sono circa il 30 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % o quasi sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
