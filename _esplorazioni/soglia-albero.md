---
title: La soglia dell'albero
slug: soglia-albero
published: false
modulo: 6
question: Come fa un albero a scegliere dove tagliare?
ready: true
---

Sposta la soglia e guarda come cambiano i due gruppi e la loro *deviance* (quanto sono "mescolati"). Poi premi **Lascia scegliere all'algoritmo**: proverà tutte le soglie e terrà quella con la deviance più bassa. È esattamente quello che fa `tree()` in R a ogni split, su ogni variabile.

**Cosa guardare.** La deviance è massima quando in ogni gruppo ci sono metà sì e metà no, e vale zero quando i gruppi sono puri. L'albero non "capisce" la regola: la trova perché i punti glielo permettono. Con pochi punti vicino al confine, la soglia trovata può essere diversa da quella vera (es. 10 km/h): è la differenza tra regola scritta e regola appresa vista in aula.
