---
title: Scritto o imparato?
slug: scritto-o-imparato
modulo: 8
question: Cosa cambia tra una regola scritta a mano e un albero che la impara dai dati?
ready: true
altezza: 1200
---

Tre passi sulle 5.000 multe dell'autovelox. In **Scritto a mano** scegli un'auto e guardi quale riga della funzione `multa()` viene eseguita. In **Imparato dai dati** decidi quante multe vede l'albero e premi **▶ Guarda come impara**: per ogni gruppo di multe prova tutte le soglie, misura quanto restano mescolati i due gruppi e taglia dove la curva è più bassa. Alla fine scrive il suo codice, accanto a quello scritto a mano. In **Messi alla prova** lo stesso albero viene provato sulle auto che non ha mai visto.

**Cosa guardare.** Il codice scritto dà sempre la stessa multa, e le soglie le ha decise una persona. L'albero trova le soglie da solo, ma solo dove ha visto abbastanza esempi: con poche multe sbaglia vicino ai confini, e una multa assente dal training non la prevede mai. Sul training ha sempre il 100 %; quanto ha imparato davvero lo dice il test.
