---
layout: page
title: "Consegne in ritardo"
permalink: /progetti/2/logistica_consegne/
parent: Progetti
nav_exclude: true
---

# Consegne in ritardo

**Settore:** Logistica · **Righe:** 3000 · **Colonne:** 13 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/logistica_consegne.csv){: .btn .btn-primary }

## Il contesto

Un corriere consegna pacchi per conto di negozi online. Ogni consegna in ritardo costa un contatto all'assistenza, a volte un rimborso, e pesa sulla reputazione del negozio. L'azienda vuole prevedere quali ordini arriveranno in ritardo, per avvisare il cliente prima che se ne accorga da solo.

Il dataset contiene gli ordini di un anno. Attenzione a due cose. **Qui i ritardi sono il 26%, mentre i dati reali vanno dal 5% (Poste, rispetto allo standard del regolatore) al 16% (rispetto alla data promessa al checkout)**: il campione è arricchito. E soprattutto: *in ritardo* qui vuol dire rispetto alla **data promessa al cliente**, e i ritardi dovuti al maltempo sono contati. Chi misura diversamente ottiene numeri diversi, e metà delle differenze fra i report del settore nasce da qui.

## La domanda

Quali ordini segnalare al servizio clienti il giorno stesso della spedizione? L'azienda può gestirne il 15%.

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `ora_ordine` | numerica | 0-23,98 | ora in cui è stato pagato l'ordine, in ore e frazioni di ora: 14,5 vuol dire le 14:30, 9,25 le 9:15 |
| `giorno_ordine` | categorica | lun-dom | giorno della settimana dell'ordine |
| `destinazione` | categorica | nord ovest / nord est / centro / sud / isole | macro-area di destinazione |
| `periodo` | categorica | ordinario / picco | periodo dell'anno (picco = Black Friday e dicembre) |
| `servizio` | categorica | economy / standard / express | servizio scelto dal cliente |
| `corriere` | categorica | Alfa / Beta / Gamma | vettore che effettua la consegna |
| `deposito` | categorica | Milano / Bologna / Roma / Catania | deposito di partenza |
| `peso_kg` | numerica | 0,1-17 kg | peso del collo |
| `transiti_hub` | numerica | 1-5 | quanti hub attraversa il pacco |
| `tentativo_fallito` | categorica | si / no | un primo tentativo di consegna è già fallito |
| `punto_ritiro` | categorica | si / no | consegna in punto di ritirio o locker invece che a domicilio |
| `meteo_avverso` | categorica | si / no | allerta meteo sulla tratta |
| `in_ritardo` | **target** | `si` / `no` | il pacco è arrivato dopo la data promessa al cliente al momento dell'ordine |

Le colonne `peso_kg`, `transiti_hub` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/logistica_consegne.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/logistica_consegne.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **73 %** dei casi, perché i casi con `in_ritardo` uguale a «si» sono circa il 27 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % o quasi sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
