---
layout: page
title: "Riammissioni ospedaliere entro 30 giorni"
permalink: /progetti/2/sanita_riammissioni/
parent: Progetti
nav_exclude: true
---

# Riammissioni ospedaliere entro 30 giorni

**Settore:** Sanità · **Righe:** 2800 · **Colonne:** 14 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/sanita_riammissioni.csv){: .btn .btn-primary }

## Il contesto

Un reparto di medicina interna vuole capire quali pazienti rischiano di tornare in ospedale poco dopo essere stati dimessi. Una riammissione a breve distanza costa al sistema sanitario e spesso segnala una dimissione affrettata o una presa in carico incompleta sul territorio.

Il dataset contiene le dimissioni di un anno: dati del ricovero, condizioni cliniche e destinazione dopo la dimissione. Attenzione a una cosa: **la quota di riammessi in questi dati è circa il 28%, mentre negli studi italiani è il 10-14%**. Il campione è stato arricchito apposta, altrimenti un modello che risponde sempre «no» sarebbe difficile da battere. È una scelta di chi ha preparato i dati, non un fatto del mondo.

## La domanda

Quali pazienti conviene seguire con una telefonata o una visita a domicilio nei dieci giorni dopo la dimissione? Il reparto può permettersi di seguirne circa un quinto.

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `eta` | numerica | 40-99 anni | età del paziente alla dimissione |
| `sesso` | categorica | M / F | sesso del paziente |
| `giorni_degenza` | numerica | 1-60 | durata del ricovero in giorni |
| `ricoveri_12_mesi` | numerica | 0-6 | altri ricoveri nei dodici mesi precedenti |
| `accessi_ps_6_mesi` | numerica | 0-4 | accessi al pronto soccorso nei sei mesi precedenti |
| `indice_comorbidita` | numerica | 0-14 | indice di Charlson: quante e quanto gravi le patologie croniche |
| `emoglobina_dimissione` | numerica | 7,5-16,5 g/dL | emoglobina rilevata alla dimissione |
| `farmaci_dimissione` | numerica | 0-15 | numero di farmaci prescritti alla dimissione |
| `destinazione_dimissione` | categorica | casa / assistenza domiciliare / struttura riabilitativa | dove va il paziente dopo la dimissione |
| `diagnosi_principale` | categorica | scompenso cardiaco / BPCO / diabete / infezione / altro | motivo principale del ricovero |
| `vive_solo` | categorica | si / no | il paziente vive da solo |
| `reparto` | categorica | A / B / C / D | reparto che ha dimesso |
| `giorno_dimissione` | categorica | lun-sab | giorno della settimana della dimissione |
| `riammesso_30gg` | **target** | `si` / `no` | il paziente è tornato in ospedale entro 30 giorni dalla dimissione |

Le colonne `emoglobina_dimissione`, `indice_comorbidita` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/sanita_riammissioni.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/sanita_riammissioni.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **71 %** dei casi, perché i casi con `riammesso_30gg` uguale a «si» sono circa il 29 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % o quasi sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
