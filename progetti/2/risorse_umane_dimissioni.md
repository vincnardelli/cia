---
layout: page
title: "Dimissioni volontarie entro dodici mesi"
permalink: /progetti/2/risorse_umane_dimissioni/
parent: Progetti
nav_exclude: true
---

# Dimissioni volontarie entro dodici mesi

**Settore:** Risorse umane · **Righe:** 2800 · **Colonne:** 18 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/risorse_umane_dimissioni.csv){: .btn .btn-primary }

## Il contesto

Un'azienda con qualche migliaio di dipendenti vuole capire chi sta per andarsene. Sostituire una persona costa fra sei mesi e un anno di retribuzione, fra selezione, formazione e produttività persa, e l'azienda vorrebbe intervenire prima, con un colloquio, una revisione retributiva o un cambio di mansione.

Il dataset è una fotografia del personale a inizio anno con le uscite dei dodici mesi successivi. Attenzione: **qui si dimette il 28%, mentre in Italia il tasso reale è intorno al 10%**. Il campione è arricchito. Da sapere anche che il dataset HR più diffuso in rete (quello IBM) è dichiarato dai suoi autori come **«fictional data set created by IBM data scientists»**: un dataset sintetico insegna quello che credeva chi l'ha generato, e vale anche per questo.

## La domanda

Con chi fare un colloquio di retention nei prossimi tre mesi? L'ufficio del personale può gestirne circa il 10%.

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `eta` | numerica | 19-66 anni | età del dipendente |
| `sesso` | categorica | M / F | sesso del dipendente |
| `anzianita_anni` | numerica | 0,1-35 | anni di servizio in azienda |
| `inquadramento` | categorica | operaio / impiegato / quadro / dirigente | inquadramento contrattuale |
| `area` | categorica | nord ovest / nord est / centro / sud | sede di lavoro |
| `ral_euro` | numerica | € | retribuzione annua lorda |
| `contratto` | categorica | indeterminato / determinato | tipo di contratto |
| `soddisfazione` | numerica | 1-5 | punteggio medio dell'indagine interna di clima |
| `disoccupazione_locale` | numerica | 2-20 % | tasso di disoccupazione della provincia della sede |
| `straordinari_settimanali` | numerica | 0-14 ore | ore di straordinario medie a settimana |
| `pendolarismo_minuti` | numerica | 2-120 | minuti di tragitto casa-lavoro, solo andata |
| `mesi_da_promozione` | numerica | 0-180 | mesi trascorsi dall'ultima promozione |
| `figli` | numerica | 0-4 | figli a carico |
| `formazione_giorni` | numerica | 0-15 | giorni di formazione nell'anno |
| `lavoro_agile` | categorica | si / no | lavora da remoto almeno un giorno a settimana |
| `codice_sede` | categorica | S01-S06 | codice della sede di lavoro |
| `ferie_residue` | numerica | 0-32 | giorni di ferie non goduti a fine anno |
| `dimissioni_12m` | **target** | `si` / `no` | il dipendente si è dimesso volontariamente nei dodici mesi successivi |

Le colonne `soddisfazione`, `pendolarismo_minuti` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/risorse_umane_dimissioni.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/risorse_umane_dimissioni.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **73 %** dei casi, perché i casi con `dimissioni_12m` uguale a «si» sono circa il 27 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
