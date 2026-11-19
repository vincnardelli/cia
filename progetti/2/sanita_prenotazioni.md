---
layout: page
title: "Visite prenotate e non disdette"
permalink: /progetti/2/sanita_prenotazioni/
parent: Progetti
nav_exclude: true
---

# Visite prenotate e non disdette

**Settore:** Sanità · **Righe:** 3000 · **Colonne:** 13 · [Progetto 2]({{ site.baseurl }}/progetti/2/)

[Scarica il dataset]({{ site.baseurl }}/materiale_progetti/sanita_prenotazioni.csv){: .btn .btn-primary }

## Il contesto

Un'azienda sanitaria perde ogni anno migliaia di ore di ambulatorio per visite prenotate e mai disdette: il posto resta vuoto, e intanto qualcun altro aspetta. L'azienda vuole capire chi rischia di non presentarsi, per mandargli un promemoria mirato o per sovraprenotare quelle fasce.

Il dataset contiene le prenotazioni di un anno di poliambulatorio. Attenzione: **qui gli assenti sono circa il 28%, mentre in Italia la quota reale è intorno al 5%** (Torino 5,1%, un policlinico campano 3,9%). Il campione è stato arricchito per rendere il problema affrontabile.

## La domanda

A chi conviene mandare una telefonata di promemoria, se l'azienda può farne solo per una prenotazione su cinque?

## Le variabili

| variabile | tipo | valori | descrizione |
|---|---|---|---|
| `giorni_attesa` | numerica | 1-365 | giorni fra la prenotazione e la data della visita |
| `assenze_precedenti` | numerica | 0-5 | quante volte quel paziente non si è presentato in passato |
| `eta` | numerica | 16-92 anni | età del paziente |
| `sesso` | categorica | M / F | sesso del paziente |
| `esenzione` | categorica | paga il ticket / esenzione per reddito / esenzione per patologia | posizione rispetto al ticket |
| `ticket_euro` | numerica | 0-36,15 € | quanto paga il paziente (0 se esente) |
| `classe_priorita` | categorica | B (10 giorni) / D (30 giorni) / P (120 giorni) | classe di priorità assegnata dal medico |
| `specialita` | categorica | dermatologia / oculistica / cardiologia / ortopedia / endocrinologia | specialità della visita |
| `promemoria_sms` | categorica | si / no | è stato inviato un SMS di promemoria |
| `residenza` | categorica | stesso comune / stessa provincia / altra regione / estero | residenza del paziente rispetto alla sede |
| `prima_visita` | categorica | si / no | è la prima visita per quel problema |
| `fascia_oraria` | categorica | mattina / pomeriggio | fascia oraria dell'appuntamento |
| `assente` | **target** | `si` / `no` | il paziente non si è presentato alla visita e non l'ha disdetta |

Le colonne `eta`, `residenza` hanno qualche valore mancante (`NA`): decidete voi come trattarlo, e scrivete perché.

## Leggere i dati

In Colab, senza caricare niente:

```python
import pandas as pd

dati = pd.read_csv("https://www.vincnardelli.com/cia/materiale_progetti/sanita_prenotazioni.csv")
```

In R: `dati <- read.csv("https://www.vincnardelli.com/cia/materiale_progetti/sanita_prenotazioni.csv")`.

## Il confronto da battere

Chi risponde sempre «no» indovina circa il **72 %** dei casi, perché i casi con `assente` uguale a «si» sono circa il 28 %. Un albero vale qualcosa solo se fa meglio di così.

> **Attenzione** L'albero senza limiti arriva al 100 % o quasi sul training. Non è bravo: ha imparato a memoria. Il confronto fra training e test è metà del lavoro.

Cosa consegnare, entro quando e come viene valutato: nella [pagina del progetto 2]({{ site.baseurl }}/progetti/2/).
