---
layout: modulo
number: 4
title: Dati
sezione: 1
language: R
idea: "Una tabella è un insieme di vettori affiancati; con cinque verbi la interroghiamo senza cicli."
hours: 4
concepts_new: [funzioni che chiamano funzioni, ricorsione, caso base, data frame, read.csv, fattori, valori mancanti, dplyr, pipe, group_by]
concepts_required: [vettori, indicizzazione, ciclo for, funzioni, if/else, operatori logici]
explorations: []
slides_pdf:
slides:
  - titolo: Lezione 6
    descr: Funzioni, Shiny e ricorsione
    pdf: slide/lezione_6.pdf
codice:
  - titolo: lezione_6.R
    descr: funzioni, print e return
    file: codice/6/lezione_6.R
  - titolo: app.R
    descr: la app Shiny del BMI
    file: codice/6/app.R
  - titolo: biglietti.R
    descr: lab 1, biglietti e carnet
    file: codice/6/biglietti.R
  - titolo: fornitori.R
    descr: lab 2, due fornitori
    file: codice/6/fornitori.R
  - titolo: fornitori_sconti.R
    descr: lab 3, con lo sconto
    file: codice/6/fornitori_sconti.R
---

<div id="lezione-6"></div>

## Lezione 6: funzioni e ricorsione

Il percorso parte da [`lezione_6.R`]({{ site.baseurl }}/codice/6/lezione_6.R) e dalla differenza fra **stampare** e **restituire**. Una funzione che fa `print()` mostra un numero e basta: `x <- bmi_stampa(86, 1.73)` lascia `x` vuoto. Una funzione che fa `return()` dà indietro un valore, che si può assegnare, confrontare con un atteso o passare a un'altra funzione. Da qui nascono `bmi(peso, altezza)`, che fa un conto, e `classificazione(valore)`, che prende una decisione: due lavori diversi, due funzioni, e `classificazione(bmi(86, 1.73))` che le mette in fila.

La stessa coppia di funzioni finisce dentro una piccola applicazione web: [`app.R`]({{ site.baseurl }}/codice/6/app.R) usa **Shiny** per mettere due cursori attorno al calcolo. L'interfaccia cambia, la funzione no: se sbaglia a BMI 25 esatto, sbaglia anche con i cursori.

Le [slide della lezione 6]({{ site.baseurl }}/slide/lezione_6.pdf) contengono i testi dei tre laboratori.

Una funzione è **ricorsiva** quando richiama sé stessa. Servono un **caso base**, che restituisce subito il risultato, e una chiamata che si avvicina al caso base. Senza caso base la funzione non si ferma: R risponde «evaluation nested too deeply». Nei tre laboratori le tariffe sono inventate per l'esercizio.

### Primo laboratorio: singoli o carnet

Un biglietto singolo costa **3 €** e copre un viaggio. Un carnet costa **10 €** e copre cinque viaggi. Si possono acquistare più carnet e i biglietti possono avanzare. L'input è il numero intero di viaggi da fare, almeno zero; l'output è il costo minimo per coprirli tutti.

```r
costo_minimo <- function(viaggi){
  if(viaggi <= 0){
    return(0)
  }

  con_singolo <- 3 + costo_minimo(viaggi - 1)
  con_carnet <- 10 + costo_minimo(viaggi - 5)

  return(min(con_singolo, con_carnet))
}
```

Con quattro viaggi si confrontano `3 + costo_minimo(3)`, cioè 12 €, e `10 + costo_minimo(-1)`, cioè 10 €. Il valore negativo significa che il carnet copre anche un viaggio in più: il caso base deve essere `<= 0`. Con sei viaggi il costo minimo è 13 €; con dieci è 20 €.

Il codice commentato e le prove sono in [biglietti.R]({{ site.baseurl }}/codice/6/biglietti.R). La funzione esplora entrambe le alternative e ricalcola alcuni casi: in aula usiamo pochi viaggi per seguire le chiamate.

### Secondo laboratorio: due fornitori

Un ufficio acquisti deve comprare un'unità di ciascun prodotto. Ogni prodotto si può prendere dal fornitore A o dal fornitore B, e ogni fornitore da cui si ordina aggiunge la **sua** spedizione: 8 € per A, 5 € per B. Se non compriamo nulla da un fornitore, non paghiamo la sua spedizione.

| Prodotto | Fornitore A | Fornitore B |
|---|---:|---:|
| Carta | 20 € | 22 € |
| Penne | 30 € | 32 € |
| Cartucce | 40 € | 38 € |
| *Spedizione* | *8 €* | *5 €* |

Comprare ogni prodotto dove costa meno (carta e penne da A, cartucce da B) costa 88 € più due spedizioni: **101 €**. Comprare tutto da A costa 90 € più 8: **98 €**. Ma il minimo è **97 €**, tutto da B, che su carta e penne costa di più e si fa perdonare con la spedizione. La scelta migliore non si trova prodotto per prodotto.

Il vettore `scelte` descrive le decisioni nello stesso ordine dei prodotti. `c("A", "B")` significa che carta e penne sono già assegnate, mentre manca la scelta delle cartucce. `c()` indica che nessuna scelta è stata ancora presa.

Nel file [fornitori.R]({{ site.baseurl }}/codice/6/fornitori.R) ci sono solo due funzioni. `costo(scelte)` riceve tre scelte complete e calcola il conto. `minimo(scelte)` completa le scelte mancanti:

```r
minimo <- function(scelte){
  if(length(scelte) == length(prodotti)){
    return(costo(scelte))
  }

  con_a <- minimo(c(scelte, "A"))
  con_b <- minimo(c(scelte, "B"))

  return(min(con_a, con_b))
}

minimo(c())  # 97 euro
```

Ogni chiamata aggiunge una scelta, quindi si avvicina al caso base delle tre scelte complete. Le combinazioni sono otto. Ogni chiamata restituisce **un numero**, il costo minimo; non restituisce il vettore dei negozi da cui acquistare.

> **In aula** Le due funzioni leggono `prodotti`, `prezzi_a`, `prezzi_b` e le due spedizioni, definiti all'inizio del file. È una semplificazione per concentrarci sulla ricorsione. I prezzi devono essere positivi, i vettori devono avere la stessa lunghezza e i prodotti devono comparire nello stesso ordine.

Le prove da fare: `costo(c("A", "A", "A"))` deve dare 98, `costo(c("A", "A", "B"))` deve dare 101 e `minimo(c("B"))` deve dare 97. Nell'ultimo caso fissiamo il primo prodotto da B e lasciamo alla funzione le altre due decisioni.

### Terzo laboratorio: lo sconto sopra una soglia

Stesso ordine, una regola in più: ogni fornitore sconta chi supera una soglia di spesa. A toglie **12 €** a chi arriva a **70 €** di prodotti, B toglie **5 €** a chi arriva a **90 €**. Lo sconto si calcola sui prodotti, **prima** della spedizione, e la soglia è compresa: a 70 € esatti lo sconto di A spetta.

Cambia solo `costo()`; `minimo()` resta identica. E cambia la risposta: il minimo diventa **86 €, tutto da A**, contro i 97 € del laboratorio precedente. Una regola in più e il fornitore migliore è un altro.

L'ordine dei passaggi conta: prima si sommano i prodotti, poi si toglie lo sconto, infine si aggiunge la spedizione. E torna il confine: l'ordine `c("B", "A", "A")` lascia ad A esattamente 70 € di prodotti, quindi lo sconto spetta. Scritto con `>` al posto di `>=`, quello stesso ordine costa 105 € invece di 93. Il codice è in [fornitori_sconti.R]({{ site.baseurl }}/codice/6/fornitori_sconti.R).

## La tabella: vettori affiancati

I vettori del modulo scorso avevano un difetto: `clienti` ed `eta` erano due variabili separate, e solo noi sapevamo che il secondo elemento dell'una corrispondeva al secondo dell'altra. Il **data frame** mette i vettori uno accanto all'altro come colonne di una tabella, con una riga per osservazione. È l'oggetto con cui si lavora in R il 90 % del tempo, ed è esattamente ciò che avete sempre chiamato «foglio Excel».

I dati arrivano quasi sempre da un file CSV, testo con le colonne separate da virgole:

```r
library(dplyr)
ecommerce <- read.csv("ecommerce.csv")

str(ecommerce)
summary(ecommerce)
```

Il file degli ordini ha una riga per ordine e queste colonne: `CustomerID`, `OrderID`, `OrderDate`, `Age`, `Gender`, `Membership`, `ProductCategory`, `ProductName`, `UnitPrice`, `Quantity`, `TotalAmount`, `PaymentMethod`, `City`, `ReturnStatus`. `str()` mostra la struttura: quante righe, quante colonne e il **tipo** di ogni colonna (`int`, `num`, `chr`). `summary()` mostra per ogni colonna numerica minimo, quartili, media, massimo e, se ci sono, quanti `NA`.

Una colonna si estrae con il dollaro e si comporta come un vettore normale:

```r
ecommerce$Age
mean(ecommerce$Age)
mean(ecommerce$Age, na.rm = TRUE)
```

La prima media è `NA`: basta un valore mancante e la media non esiste. `na.rm = TRUE` dice «rimuovi gli NA e calcola sul resto». È la prima decisione che i dati vi impongono e va presa consapevolmente, non lasciata al caso.

Le colonne di testo che rappresentano categorie (sesso, città, tipo di abbonamento) vanno convertite in **fattori**, così `summary()` le conta invece di ignorarle:

```r
ecommerce$Gender <- as.factor(ecommerce$Gender)
ecommerce$ProductCategory <- as.factor(ecommerce$ProductCategory)
summary(ecommerce)
```

## Selezionare righe e colonne alla vecchia maniera

Con le parentesi quadre del modulo scorso, su un data frame si indica `[righe, colonne]`:

```r
ecommerce[, c("CustomerID", "Age")]
ecommerce[ecommerce$Age < 35 & !is.na(ecommerce$Age), ]
ecommerce[ecommerce$Age < 35 & !is.na(ecommerce$Age), c("CustomerID", "Age")]
```

Funziona, ma la terza riga è già illeggibile. `is.na()` chiede «è mancante?» e `!` lo nega: senza quel pezzo le righe con età mancante entrerebbero come righe di `NA`. Il pacchetto **dplyr** esiste per rendere leggibili queste operazioni.

## I cinque verbi di dplyr

dplyr offre pochi verbi, ognuno con un compito solo. Tutti ricevono un data frame come primo argomento e restituiscono un data frame.

```r
select(ecommerce, CustomerID, Age)
filter(ecommerce, Age < 35)
mutate(ecommerce, gruppo_eta = ifelse(Age < 35, "Giovane", "Adulto"))
summarise(ecommerce, eta_media = mean(Age, na.rm = TRUE), n = n())
```

- `select` sceglie le **colonne**;
- `filter` sceglie le **righe** che soddisfano una condizione, come `clienti[eta < 35]` del modulo scorso;
- `mutate` crea una **colonna nuova** calcolata dalle altre; `ifelse(condizione, se_vero, se_falso)` è l'`if` del modulo 2 applicato a tutta una colonna in un colpo;
- `summarise` riduce la tabella a **una riga** di statistiche; `n()` conta le righe.

Il quinto verbo, `group_by`, non fa nulla da solo: divide la tabella in gruppi, così che il `summarise` successivo produca una riga per gruppo invece che una sola.

## La pipe: un verbo per riga

Per applicare più verbi in sequenza si potrebbero annidare: `filter(select(ecommerce, CustomerID, Age), Age < 35)`. Si legge dall'interno verso l'esterno, e con quattro verbi diventa un rebus. L'operatore **pipe** `%>%` risolve: prende ciò che sta a sinistra e lo passa come primo argomento a ciò che sta a destra.

```r
ecommerce %>%
  select(CustomerID, Age) %>%
  filter(!is.na(Age)) %>%
  mutate(gruppo_eta = ifelse(Age < 35, "Giovane", "Adulto")) %>%
  group_by(gruppo_eta) %>%
  summarise(n = n())
```

Si legge dall'alto in basso come una ricetta: prendi gli ordini, tieni due colonne, scarta le età mancanti, aggiungi il gruppo, raggruppa, conta. Nel corso scriviamo sempre così: un verbo per riga, la pipe in fondo alla riga.

Un uso tipico sull'ecommerce: fatturato e ordini per categoria, e la quota di resi per metodo di pagamento.

```r
ecommerce %>%
  group_by(ProductCategory) %>%
  summarise(ordini = n(), fatturato = sum(TotalAmount)) %>%
  arrange(desc(fatturato))

ecommerce %>%
  group_by(PaymentMethod) %>%
  summarise(quota_resi = mean(ReturnStatus))
```

`ReturnStatus` vale 0 o 1: la media di una colonna 0/1 è la **proporzione** di 1. È un trucco che useremo continuamente. `arrange(desc(...))` ordina dal più grande.

## Titanic: quando il caso limite è nei dati

Il secondo dataset è l'elenco dei passeggeri del Titanic: `PassengerId`, `Survived` (0/1), `Pclass`, `Name`, `Sex`, `Age`, `SibSp` (fratelli e coniugi a bordo), `Parch` (genitori e figli), `Ticket`, `Fare`, `Cabin`, `Embarked` (porto: C, Q, S). Prima domanda: quante persone oltre i 50 anni erano a bordo?

```r
titanic <- read.csv("titanic.csv")
titanic$Sex <- as.factor(titanic$Sex)
titanic$Pclass <- as.factor(titanic$Pclass)

titanic %>%
  filter(Age > 50) %>%
  summarise(n = n())
```

> **Attenzione** `filter(Age > 50)` scarta **in silenzio** le 177 righe con età mancante, perché `NA > 50` non è né vero né falso e `filter` tiene solo i `TRUE`. Il conteggio è giusto per «over 50 tra chi ha l'età nota», ma se poi calcolate «percentuale di over 50 sul totale» dividendo per 891 passeggeri, il denominatore è sbagliato. Scrivete sempre esplicitamente `filter(!is.na(Age))` e decidete voi il denominatore.

Seconda domanda: tra gli over 50, che percentuale sono uomini e donne?

```r
titanic %>%
  filter(!is.na(Age), Age > 50) %>%
  group_by(Sex) %>%
  summarise(n = n()) %>%
  mutate(percentuale = n / sum(n))
```

Il `mutate` dopo il `summarise` calcola la quota di ogni gruppo sul totale dei gruppi: `sum(n)` è la somma delle righe della tabella riassunta, cioè tutti gli over 50. È il paradosso di Simpson del modulo 1 visto dal lato del codice: cambiare cosa sta al denominatore cambia la risposta.

Terza domanda, la più tipica: è sopravvissuta una quota maggiore in prima o in terza classe?

```r
titanic %>%
  group_by(Pclass) %>%
  summarise(quota_sopravvissuti = mean(Survived))

titanic %>%
  group_by(Pclass, Sex) %>%
  summarise(quota_sopravvissuti = mean(Survived), n = n())
```

Il secondo comando raggruppa per due variabili e produce una riga per ogni combinazione classe × sesso. Guardando la seconda tabella si scopre che dentro ogni classe le donne sopravvivono molto più degli uomini: l'aggregazione per sola classe nascondeva la variabile che conta di più.

> **Attenzione** Dopo un `group_by` con due variabili, `summarise` toglie **solo l'ultimo** raggruppamento: la tabella risultante è ancora raggruppata per `Pclass`. Un `mutate(percentuale = n / sum(n))` a quel punto calcola le quote **dentro ogni classe**, non sul totale. Se volete il totale generale, aggiungete `ungroup()` prima del `mutate`, oppure scrivete `summarise(..., .groups = "drop")`. È l'errore più comune di tutto la sezione 1 e i test della piattaforma lo intercettano.

> **In aula** abbiamo risposto alla metà delle domande sul Titanic. Le altre (biglietto minimo, medio e massimo per classe e sesso; se i sopravvissuti hanno pagato di più; il ruolo della dimensione della famiglia e del porto d'imbarco) usano esattamente gli stessi cinque verbi e sono in piattaforma con la verifica automatica. La verifica funziona come per il codice dei moduli scorse: il test è «il numero di over 50 è N», e se il vostro numero è diverso il suggerimento vi dice dove guardare.

## Per approfondire

L'indicizzazione con vettori logici è nel [modulo 3](03-ripetere-e-astrarre); `ifelse` è la versione vettoriale dell'`if` del [modulo 2](02-decidere). Nella [modulo 5](05-leggere-i-dati) le statistiche dentro `summarise` (media, mediana, deviazione standard) diventano il centro, e impareremo a disegnarle con ggplot2.
