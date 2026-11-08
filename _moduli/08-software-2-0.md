---
layout: modulo
number: 8
title: Software 2.0
sezione: 2
language: Python
idea: "Le regole dell'autovelox non le scriviamo più noi: le trova un albero guardando gli esempi."
hours: 4
concepts_new: [Python, Colab, pandas, scikit-learn, albero di classificazione, training e test, accuracy]
concepts_required: [if/else, funzioni, ciclo for, data frame, dplyr]
explorations: [scritto-o-imparato]
slides_pdf:
slides:
  - titolo: Lezione 11
    descr: L'autovelox appreso, il primo albero
    pdf: slide/lezione_11.pdf
codice:
  - titolo: lezione_11.ipynb
    descr: il codice della lezione, in Colab
    file: codice/11/lezione_11.ipynb
  - titolo: lab_multe.ipynb
    descr: lab, le multe imparate
    file: codice/11/lab_multe.ipynb
dati:
  - titolo: autovelox.csv
    descr: 5.000 auto davanti all'autovelox
    file: dati/autovelox.csv
---

{% assign img = site.baseurl | append: "/assets/images/moduli/08/" %}

## L'idea del modulo

Nel [modulo 2](../02-decidere/) abbiamo letto l'articolo 142 e tradotto «non oltre 10 km/h» in `differenza <= 10`. In questo modulo facciamo il contrario: diamo a un algoritmo **5.000 multe già emesse** (velocità, limite, importo) e gli chiediamo di trovare le soglie da solo. È il primo modello di machine learning del corso, ed è anche il momento in cui passiamo da R a **Python**.

| Scritto a mano (Software 1.0) | Imparato dai dati (Software 2.0) |
|---|---|
| regola + dati → risposte | dati + risposte → regola |
| una persona legge la legge e scrive gli `if` | l'algoritmo guarda esempi già classificati |
| deterministico: stessa auto, stessa multa | è bravo quanto gli esempi che ha visto |

Un modello di machine learning è *una funzione che nessuno ha scritto*.

## Colab e Python

I notebook di questo modulo si aprono in **Google Colab** con il pulsante qui sopra: niente da installare, il codice gira sui computer di Google e i dati si leggono dal sito. Si esegue una cella con **Shift + Invio**, dall'alto in basso; per tenere le modifiche, *File → Salva una copia in Drive*.

I concetti sono quelli di R, cambia la sintassi:

| R | Python |
|---|---|
| `x <- 5` | `x = 5` |
| `c(120, 80, 45)` | `[120, 80, 45]` (una lista) |
| `x[1]` | `x[0]`: si conta da 0 |
| `function(a) { ... }` | `def f(a):` e il corpo rientrato di quattro spazi |
| `else if` | `elif` |
| `library(dplyr)`, `read.csv()` | `import pandas as pd`, `pd.read_csv()` |
| `df$x`, `filter(df, x > 5)` | `df["x"]`, `df[df["x"] > 5]` |
| `group_by(g) %>% summarise(mean(x))` | `df.groupby("g")["x"].mean()` |

La funzione `multa()` del modulo 2, in Python:

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

## L'albero impara le soglie

Un **albero di classificazione** prova tutte le soglie possibili sulla differenza tra velocità e limite, sceglie quella che separa meglio le multe, e ripete su ognuno dei due gruppi. In scikit-learn ogni modello si usa allo stesso modo: si crea, si allena con `fit`, si usa con `predict`.

```python
from sklearn.tree import DecisionTreeClassifier

X = autovelox[["Differenza"]]     # quello che sappiamo di ogni auto
y = autovelox["Multa"]            # quello che vogliamo prevedere

albero = DecisionTreeClassifier(random_state=1)
albero.fit(X, y)
```

![L'albero allenato su tutte le multe]({{ img }}albero.png)

![Le soglie della legge e quelle dell'albero]({{ img }}soglie_tutte.png)

Le soglie che trova sono 0,5 · 10,5 · 40,5 · 60,5: sulle differenze intere, «≤ 10,5» vuol dire «≤ 10». Sono le soglie dell'articolo 142, e nessuno gliele ha dette. Sulle 5.000 auto l'albero dà la stessa multa della legge nel 100 % dei casi.

## Training e test

Quel 100 % però è sulle stesse multe da cui l'albero ha imparato: è un esame con le stesse domande dell'esercitazione. Per sapere se un modello ha imparato davvero si dividono i dati in due parti: il **training**, da cui impara, e il **test**, tenuto da parte solo per misurare quanto sbaglia.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=30, random_state=1)
albero_30 = DecisionTreeClassifier(random_state=1).fit(X_train, y_train)
albero_30.score(X_train, y_train), albero_30.score(X_test, y_test)    # (1.0, 0.926)
```

![Le 30 multe di training e le soglie dell'albero]({{ img }}soglie_30.png)

Con 30 multe l'albero ha il 100 % sul training e il 92,6 % sul test: le soglie diventano −3,5 · 12 · 40 · 65. Gli errori stanno tutti vicino ai confini:

![Le auto del test indovinate e sbagliate]({{ img }}errori_30.png)

| Auto | Differenza | Multa vera | Prevista |
|---:|---|---|---|
| 182 | da −3 a 0 km/h | 0 € | 36 € |
| 89 | 11 e 12 km/h | 148 € | 36 € |
| 96 | da 61 a 65 km/h | 500 € | 370 € |

Lontano dalle soglie non sbaglia mai: dove ha visto pochi esempi, indovina.

![Accuracy sul test al crescere delle multe di training]({{ img }}curva.png)

Con 10 multe l'albero indovina in media il 79 % delle auto nuove, con 100 il 98 %, da 500 in su il 100 %. Sul training è sempre il 100 %: per questo non dice niente.

## Il lab

`lab_multe.ipynb` contiene sei domande, più due extra, da fare in aula e correggere insieme. Si comincia con pandas sulle multe (quante da 500 €, la differenza media per importo). Poi la funzione e l'albero sulla stessa auto, e alberi allenati su 100 e su 30 multe. Infine il caso in cui nel training manca una multa intera. Prima di eseguire una cella si scrive il risultato che ci si aspetta.

## Per approfondire

L'autovelox scritto a mano è nel [modulo 2](../02-decidere/); la frase «una funzione che nessuno ha scritto» chiude il [modulo 4](../04-astrarre/). L'esplorazione **Scritto o imparato?** fa vedere l'albero che prova le soglie una per una, e come cambia con il numero di esempi.
