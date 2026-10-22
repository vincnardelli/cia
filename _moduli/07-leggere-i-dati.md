---
layout: modulo
number: 7
title: Leggere i dati
sezione: 2
language: R
idea: "Una tabella si riassume con pochi numeri e pochi grafici; saperli leggere è più difficile che calcolarli."
hours: 3
concepts_new: [frequenze, istogramma, media e mediana, quartili, boxplot, deviazione standard, skewness, curtosi, correlazione, ggplot2]
concepts_required: [data frame, dplyr, pipe, group_by]
explorations: []
slides_pdf:
slides:
  - titolo: Lezione 9
    descr: Analisi Catalogo Prodotti
    pdf: slide/lezione_9.pdf
codice:
  - titolo: lezione_9.R
    descr: tutti i grafici e gli indicatori
    file: codice/9/lezione_9.R
dati:
  - titolo: business_intelligence.csv
    descr: 80 prodotti di un catalogo
    file: dati/business_intelligence.csv
  - titolo: domanda_giornaliera.csv
    descr: un anno di vendite di due prodotti
    file: dati/domanda_giornaliera.csv
  - titolo: recensioni.csv
    descr: 400 recensioni di due cuffie
    file: dati/recensioni.csv
---

## Il catalogo

Il file `business_intelligence.csv` descrive 80 prodotti di un'azienda in cinque categorie (Abbigliamento, Alimentari, Casa, Elettronica, Sport): prezzo, unità vendute, fatturato, valutazione dei clienti, numero di recensioni, tasso di reso, margine, giorni di giacenza in magazzino, costo di magazzino e ritardo del fornitore. Una riga per prodotto. Il percorso del modulo è sempre lo stesso: una variabile alla volta, poi due gruppi a confronto, poi due variabili insieme.

```r
library(dplyr)
library(ggplot2)

vendite <- read.csv("business_intelligence.csv")
summary(vendite)
```

## Dalla tabella all'istogramma

Il primo riassunto di una colonna numerica è una **tabella di frequenza**: si divide il fatturato in fasce e si conta quanti prodotti cadono in ognuna. La frequenza relativa è *f*ᵢ = *n*ᵢ / *N*.

```r
vendite %>%
  mutate(fascia = cut(fatturato, breaks = c(0, 50000, 100000, 150000, 200000, Inf))) %>%
  count(fascia) %>%
  mutate(freq_rel = n / sum(n))
```

L'**istogramma** è la stessa tabella disegnata: ogni barra è una fascia, la sua altezza è il conteggio. Con fasce più strette (25.000 € invece di 50.000) si vede meglio la forma, e ogni barra fine sta dentro una delle fasce larghe. Messo accanto al grafico «prodotto per prodotto», l'istogramma è quello che si ottiene facendo cadere tutti i punti sull'asse verticale.

## Cinque numeri e il boxplot

Sopra l'istogramma si possono segnare sei valori: minimo, primo quartile, mediana, media, terzo quartile, massimo. Per il fatturato sono 8.004, 73.949, 118.351, 116.047, 144.688 e 301.599 €.

- La **media** è x̄ = Σ xᵢ / N.
- La **mediana** è il valore che sta a metà una volta ordinati i dati; i **quartili** lasciano sotto di sé un quarto e tre quarti dei prodotti. R li calcola con `quantile()`.

Il **boxplot** è l'istogramma visto dall'alto. La scatola va da Q1 a Q3 e contiene metà dei prodotti; la sua larghezza è l'IQR = Q3 − Q1. I baffi arrivano fino all'ultimo valore entro Q1 − 1,5 · IQR e Q3 + 1,5 · IQR; oltre ci sono i punti isolati.

```r
ggplot(vendite, aes(x = fatturato)) +
  geom_boxplot()
```

## Variabilità

La **deviazione standard** misura quanto i valori si allontanano dalla media:

> s = √( Σ (xᵢ − x̄)² / (N − 1) )

È quello che calcola `sd()`. Per il fatturato è 55.817 €. Elettronica e Sport hanno medie vicine (135.410 e 121.602 €) ma deviazioni standard molto diverse (70.730 e 40.457 €): nell'elettronica convivono prodotti che vendono pochissimo e prodotti che vendono moltissimo. In finanza la stessa misura si chiama rischio.

## Confronto tra categorie

Un grafico a colonne con il fatturato medio per categoria dice chi vende di più in media, ma nasconde tutto il resto. I boxplot affiancati mostrano, sulla stessa scala, mediana, dispersione e prodotti anomali di ogni categoria: è lo stesso confronto con molte più informazioni.

```r
ggplot(vendite, aes(x = categoria, y = fatturato)) +
  geom_boxplot()
```

## Forma: skewness e curtosi

La **skewness** dice se la distribuzione è simmetrica o ha una coda lunga da un lato:

> SK = N / ((N − 1)(N − 2)) · Σ ((xᵢ − x̄) / s)³

Positiva vuol dire coda a destra, con la media sopra la mediana: il prezzo ha skewness 2,68, media 150 € e mediana 61 €.

La **curtosi** dice quanto sono frequenti i valori estremi rispetto a quello che farebbe pensare la deviazione standard:

> K = [ Σ (xᵢ − x̄)⁴ / N ] / [ Σ (xᵢ − x̄)² / N ]² − 3

In aula l'abbiamo vista su quattro domande di business:

| domanda | dati | cosa dice la curtosi |
|---|---|---|
| Dove tagliare il costo di magazzino? | `costo_magazzino`, `giorni_giacenza` | costo con K = 8,79: 10 prodotti su 80 fanno il 63 % del costo, e il grafico di Pareto li mostra |
| Quante scorte tenere? | `domanda_giornaliera.csv` | pasta e smartphone hanno media 100 e dev. std. 20, ma lo smartphone ha K = 20,3: supera 140 pezzi in 14 giorni contro 6, e arriva a 228 |
| Che tempi di consegna promettere? | `ritardo_fornitore_giorni` | media 2,4 giorni, ma il 95° percentile è 17,1: la media non basta per una promessa al cliente |
| Il prodotto piace? | `recensioni.csv` | due cuffie con media 3,5 stelle: una con K = 1,52, l'altra polarizzata con K = −1,54 e il 29,5 % di recensioni a una stella |

## Due variabili: correlazione

Il grafico di dispersione mette un punto per prodotto. La **correlazione** va da −1 a 1:

> Corr(X, Y) = Cov(X, Y) / √( Var(X) · Var(Y) )

Unità vendute e numero di recensioni hanno r = 0,93; valutazione e tasso di reso r = −0,90; valutazione e fatturato appena 0,26. La matrice di dispersione (`GGally::ggpairs`) e `corrplot` mostrano tutte le coppie insieme.

```r
cor(vendite$numero_recensioni, vendite$unita_vendute)
corrplot::corrplot(cor(vendite[, c("prezzo", "unita_vendute", "numero_recensioni",
                                   "fatturato", "valutazione_clienti", "tasso_reso")]))
```

## Per approfondire

I verbi di dplyr usati per preparare ogni grafico sono nel [modulo 6](../06-dati/). Nel [modulo 8](../08-software-2-0/) una macchina impara da sola le regole, a partire da tabelle come queste.
