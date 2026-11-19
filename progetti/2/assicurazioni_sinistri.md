---
layout: page
title: "Sinistri RC auto entro dodici mesi"
permalink: /progetti/2/assicurazioni_sinistri/
parent: Progetti
nav_exclude: true
---

# Sinistri RC auto entro dodici mesi

**Settore:** Assicurazioni · **Righe:** 3000 · **Colonne:** 12 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/assicurazioni_sinistri.csv){: .btn .btn-primary }

## Il contesto

Una compagnia assicurativa vuole capire quali polizze auto porteranno un sinistro nell'anno. Serve per la tariffa, ma anche per decidere a chi proporre la scatola nera.

Il dataset contiene le polizze RC auto in corso a inizio anno e i sinistri denunciati nei dodici mesi successivi. Attenzione: **qui il 27% ha un sinistro, mentre in Italia la frequenza reale è il 5-6,4% per le autovetture** (IVASS, bollettino statistico 2026). Il campione è arricchito.

Una cosa che nel dataset **non c'è**: i chilometri percorsi in un anno. Le compagnie non li conoscono quasi mai, ed è esattamente il motivo per cui esiste la scatola nera.

## La domanda

A chi proporre la scatola nera con uno sconto, sapendo che la compagnia può farlo per il 20% del portafoglio? E prima ancora: le variabili che trovate importanti si possono davvero usare per fare il prezzo?

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `eta_conducente` | numerica | 18-92 anni | età del conducente principale |
| `sesso` | categorica | M / F | sesso del conducente principale |
| `anni_patente` | numerica | 0-60 | da quanti anni ha la patente |
| `zona` | categorica | grande citta / citta media / provincia / area rurale | zona di circolazione prevalente |
| `eta_veicolo` | numerica | 0-30 anni | anni del veicolo (l'età media del parco auto italiano è 13 anni) |
| `potenza_kw` | numerica | 35-230 kW | potenza del veicolo |
| `alimentazione` | categorica | benzina / diesel / ibrida / elettrica | alimentazione del veicolo |
| `classe_cu` | numerica | 1-18 | classe di merito bonus-malus (1 è la migliore; l'87% degli assicurati italiani è in classe 1; chi ha appena preso la patente parte dalla 14, a meno che erediti la classe di un familiare) |
| `uso` | categorica | privato / commerciale | uso dichiarato del veicolo |
| `scatola_nera` | categorica | si / no | il veicolo ha la scatola nera |
| `anni_compagnia` | numerica | 0,1-30 | da quanti anni è cliente della compagnia |
| `sinistro_12m` | **target** | `si` / `no` | l'assicurato ha denunciato almeno un sinistro con colpa nei dodici mesi |

Le colonne `anni_patente`, `potenza_kw` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/assicurazioni_sinistri.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/assicurazioni_sinistri.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **73 %** dei casi, perché i casi con `sinistro_12m` uguale a «si» sono circa il 27 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % o quasi sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
