---
layout: modulo
number: 8
title: Imparare con gli alberi
sezione: 2
language: Python
idea: "Le regole dell'autovelox non le scriviamo più noi: le trova un albero guardando gli esempi."
hours: 5
concepts_new: [Python, Colab, pandas, scikit-learn, albero di classificazione, training e test, accuracy, overfitting, tabella di confusione]
concepts_required: [if/else, funzioni, ciclo for, data frame, dplyr]
explorations: [scritto-o-imparato]
slides_pdf:
slides:
  - titolo: Lezione 11
    descr: L'autovelox appreso, il primo albero
    pdf: slide/lezione_11.pdf
  - titolo: Lezione 12
    descr: Training e test, multe e seggiolini
    pdf: slide/lezione_12.pdf
codice:
  - titolo: lezione_11.ipynb
    descr: il codice della lezione 11, in Colab
    file: codice/11/lezione_11.ipynb
  - titolo: lezione_12.ipynb
    descr: il codice della lezione 12, in Colab
    file: codice/12/lezione_12.ipynb
  - titolo: lab_seggiolini.ipynb
    descr: lab, vendite alte o basse?
    file: codice/12/lab_seggiolini.ipynb
dati:
  - titolo: autovelox.csv
    descr: 5.000 auto davanti all'autovelox
    file: dati/autovelox.csv
  - titolo: seggiolini.csv
    descr: 400 negozi di seggiolini per auto
    file: dati/seggiolini.csv
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

Quel 100 % però è sulle stesse multe da cui l'albero ha imparato: è un esame con le stesse domande dell'esercitazione. Uno studente che ha imparato a memoria le soluzioni prende il massimo, ma non sappiamo se ha capito. Un modello si costruisce per usarlo su **casi nuovi**, e per sapere se funzionerà bisogna metterlo alla prova su esempi che non ha mai visto.

Per questo i dati si dividono in due parti, **prima** di cominciare:

- il **training** (di solito il 70–80 %), da cui il modello impara;
- il **test**, tenuto da parte e mai toccato mentre il modello impara, solo per misurare quanto sbaglia.

L'**accuracy** è la quota di risposte giuste. Quella sul training è sempre ottimista; quella che conta è sul test.

### Le multe con pochi esempi

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

### I seggiolini per auto

Il secondo esempio è più vicino a un problema di business. Il file `seggiolini.csv` descrive **400 negozi** che vendono seggiolini per auto (dati del libro *An Introduction to Statistical Learning*):

| Colonna | Cosa contiene |
|---|---|
| `negozio` | identificativo del negozio, da 1 a 400 |
| `vendite` | seggiolini venduti, in migliaia |
| `prezzo` | prezzo del seggiolino nel negozio |
| `prezzo_concorrenza` | prezzo del concorrente nella stessa zona |
| `pubblicita` | budget di pubblicità locale, in migliaia di dollari |
| `scaffale` | posizione sullo scaffale: cattivo, medio, buono |
| `reddito` | reddito medio della zona, in migliaia di dollari |
| `popolazione` | abitanti della zona, in migliaia |
| `eta` | età media della popolazione della zona |
| `istruzione` | anni di studio medi della zona |
| `citta` | il negozio è in città: si, no |
| `usa` | il negozio è negli Stati Uniti: si, no |

**Domanda:** guardando prezzo e pubblicità, sappiamo dire in anticipo quali negozi avranno **vendite alte**, cioè più di 8.000 pezzi? Qui non c'è una regola esatta come per le multe: due negozi con lo stesso prezzo e la stessa pubblicità possono vendere in modo diverso.

```python
seggiolini["vendite_alte"] = (seggiolini["vendite"] > 8).astype(int)

X = seggiolini[["prezzo", "pubblicita"]]
y = seggiolini["vendite_alte"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

albero_2 = DecisionTreeClassifier(max_depth=2, random_state=1).fit(X_train, y_train)
```

Il primo confronto è con il modello più stupido: dire sempre «vendite basse». Sul test indovina il **58,3 %** dei negozi, e un modello vale qualcosa solo se fa meglio.

![L'albero dei seggiolini, profondità 2]({{ img }}seggiolini_albero.png)

![Le zone dell'albero su prezzo e pubblicità]({{ img }}seggiolini_zone.png)

Con poca pubblicità (fino a 6,5) servono prezzi bassissimi (fino a 90,5); con più pubblicità basta un prezzo non troppo alto (fino a 136). L'albero ha il 76,8 % sul training e il **67,5 %** sul test.

### La tabella di confusione

L'accuracy dice *quanto* sbaglia il modello; la **tabella di confusione** dice *come*. Per ogni negozio del test incrocia la classe vera con quella prevista, come `table()` in R:

```python
pd.crosstab(y_test, albero_2.predict(X_test), rownames=["vere"], colnames=["previste"])
```

| | previste basse | previste alte |
|---|---:|---:|
| **vere basse** | 49 | 21 |
| **vere alte** | 18 | 32 |

Le risposte giuste sono 49 + 32 = 81 su 120. I 21 negozi con vendite basse dati per alti sono delusioni; i 18 con vendite alte non riconosciuti sono occasioni perse. I due errori non costano uguale.

### Più profondo non vuol dire migliore

Lasciato crescere senza limiti, l'albero dei seggiolini fa 103 foglie: due o tre negozi per foglia. Sul training arriva al 96,4 %, sul test scende al 60,8 %, appena sopra chi dice sempre «basse». Ha imparato a memoria il training, compresi i casi strani che nei negozi nuovi non si ripetono: è l'**overfitting**.

![Accuracy sul training e sul test al crescere della profondità]({{ img }}seggiolini_profondita.png)

Il training sale sempre; il test arriva al 67,5 % con profondità 2 e 3 e poi scende. È il test a dirci dove fermarci.

## Il lab

`lab_seggiolini.ipynb` contiene sei domande, più una extra, da fare in aula e correggere insieme:
- quanti negozi hanno vendite alte, e il reddito medio delle loro zone;
- un albero di profondità 3;
- la posizione sullo scaffale come variabile in più (il test sale al 73,3 %), con la sua tabella di confusione;
- la previsione per un negozio nuovo;
- la profondità migliore.

Prima di eseguire una cella si scrive il risultato che ci si aspetta.

## Per approfondire

L'autovelox scritto a mano è nel [modulo 2](../02-decidere/); la frase «una funzione che nessuno ha scritto» chiude il [modulo 4](../04-astrarre/). L'esplorazione **Scritto o imparato?** fa vedere l'albero che prova le soglie una per una, e come cambia con il numero di esempi.
