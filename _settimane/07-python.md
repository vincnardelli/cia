---
layout: settimana
number: 7
title: Python per chi sa R
pillar: 2
language: R → Python
idea: "I concetti sono gli stessi, cambia la sintassi: i test dei lab non sanno in che linguaggio è scritta la soluzione."
hours: 5
dates: []
concepts_new: [Colab, liste, pandas]
concepts_required: [variabili, if/else, ciclo for, funzioni, vettori, data frame, dplyr]
explorations: []
slides_pdf:
---

## L'idea della settimana

Tutto ciò che sapete fare in R (assegnare, decidere, ripetere, scrivere funzioni, filtrare e raggruppare una tabella) esiste identico in Python. Cambiano i simboli: `<-` diventa `=`, le graffe diventano indentazione, `c()` diventa una **lista** `[]`, i vettori partono da 0. Il machine learning moderno e le API degli LLM parlano Python, e da qui in avanti lo useremo in **Google Colab**, che gira nel browser senza installare nulla.

La rimappatura si fa costrutto per costrutto sull'autovelox:

```python
def multa(velocita, limite):
    differenza = velocita - limite
    if differenza <= 0:
        return 0
    elif differenza <= 10:
        return 36
    elif differenza <= 40:
        return 148
    elif differenza <= 60:
        return 370
    else:
        return 500
```

Al posto di dplyr c'è **pandas**: `df[df["Age"] > 50]` è il `filter`, `groupby` è il `group_by`, `.mean()` dopo un `groupby` è il `summarise`. Le pipe diventano catene di metodi con il punto.

## In aula

La tabella di corrispondenza R ↔ Python costruita insieme, la funzione `multa()` riscritta, e le domande sul Titanic della settimana 4 rifatte in pandas: stesse risposte, e lo stesso `NA` (qui `NaN`) che sparisce in silenzio dai confronti.

## In piattaforma

Tutti i lab base del pilastro 1 da far passare in Python **con gli stessi test**: i test sono coppie input → output attesi e non dipendono dal linguaggio. Il lab consigliato è farli tradurre all'assistente e poi verificare: la traduzione automatica sbaglia proprio su `<` e `<=`, e i casi limite lo rivelano una seconda volta. Tabella di corrispondenza completa come riferimento.

## Per approfondire

Le funzioni da tradurre sono nella [settimana 3](03-ripetere-e-astrarre), i verbi dplyr da rimappare nella [settimana 4](04-dati). Nella [settimana 8](08-random-forest) Python serve subito, per scikit-learn.
