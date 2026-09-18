---
layout: modulo
number: 6
title: Software 2.0
sezione: 2
language: R
idea: "Le regole dell'autovelox non le scriviamo più noi: le trova un albero guardando gli esempi."
hours: 4
published: false
concepts_new: [albero di classificazione, train/test, overfitting, confusion matrix, accuracy, deviance]
concepts_required: [if/else, funzioni, data frame, dplyr, media e mediana]
explorations: [soglia-albero]
slides_pdf:
---

## L'idea del modulo

In modulo 2 abbiamo letto l'articolo 142 e tradotto «non oltre 10 km/h» in `differenza <= 10`. Questo modulo diamo a un algoritmo un file di multe già emesse (velocità, limite, importo) e gli chiediamo di trovare da solo le soglie. L'**albero di classificazione** fa esattamente questo: prova tutti i possibili split di una variabile, sceglie quello che rende i due gruppi più omogenei (la *deviance* scende), e ripete. Gli split che trova sull'autovelox sono 0, 10, 40 e 60: gli stessi confini che abbiamo sofferto a mano. È la colonna «Software 2.0» della tabella di modulo 1: stessa forma di `multa()`, ma una funzione che nessuno ha scritto.

```r
library(tree)
albero <- tree(as.factor(Multa) ~ Differenza, data = autovelox)
plot(albero)
text(albero, pretty = 0)
```

## In aula

Autovelox → albero, e lettura dell'output di `tree` (nodi, split, deviance, foglie). Poi un albero lasciato crescere senza limiti che memorizza i dati di *training* e sbaglia su quelli nuovi: è l'**overfitting**, e l'unico modo di vederlo è tenere da parte un insieme di **test** su cui il modello non ha mai imparato. Sul dataset *churn* costruiamo l'albero sul train, lo valutiamo sul test con la **confusion matrix** (veri positivi, falsi positivi, ...) e scopriamo perché l'**accuracy** inganna quando il 90 % dei clienti non abbandona: un modello che dice sempre «resta» ha il 90 % di accuracy e zero utilità.

## In piattaforma

Un'esplorazione interattiva in cui si sposta la soglia dello split a mano e si vede la deviance scendere fino al minimo. Alberi su *Carseats* e un albero di regressione su *real_estate* (target continuo: la foglia predice una media, non una classe). Deviance e gradi di libertà spiegati sull'output di R.

## Per approfondire

L'autovelox scritto a mano è nel [modulo 2](02-decidere); la frase «una funzione che nessuno ha scritto» chiude il [modulo 3](03-ripetere-e-astrarre). Nella [modulo 7](07-python) cambiamo linguaggio prima di far crescere una foresta di alberi.
