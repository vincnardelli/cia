---
layout: modulo
number: 4
title: Astrarre
sezione: 1
language: R
idea: "Una regola che vale per molti casi prende un nome e diventa una funzione; una funzione può chiamarne un'altra, o sé stessa."
hours: 4
concepts_new: [funzioni, argomenti, valore di ritorno, test di una funzione, funzioni che chiamano funzioni, ricorsione, caso base]
concepts_required: [vettori, indicizzazione, ciclo for, if/else, operatori logici]
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

## La funzione: dare un nome a una regola

L'autovelox del modulo 2 funziona, ma per usarlo con un'altra velocità dovete modificare la prima riga e rieseguire tutto. Se il calcolo servisse in dieci punti diversi di un programma, lo copiereste dieci volte. La **funzione** incapsula il calcolo sotto un nome:

```r
multa <- function(velocita, limite){
  differenza <- velocita - limite
  if(differenza <= 0){
    importo <- 0
  }else if(differenza <= 10){
    importo <- 36
  }else if(differenza <= 40){
    importo <- 148
  }else if(differenza <= 60){
    importo <- 370
  }else{
    importo <- 500
  }
  return(importo)
}

multa(70, 50)
multa(45, 50)
multa(60, 50)
```

`function(velocita, limite)` dichiara gli **argomenti**, i dati che la funzione riceve. Il corpo è identico a prima. `return(importo)` è il **valore di ritorno**, quello che esce. Le tre chiamate in fondo restituiscono 148, 0 e 36. Notate che i test del modulo 2 sono diventati tre righe: chiamare la funzione con gli input del test e confrontare con l'atteso. Da qui in poi **testare una funzione** significa esattamente questo:

```r
multa(60, 50) == 36
multa(110, 50) == 370
multa(111, 50) == 500
```

Tutti `TRUE`: la funzione passa i test. Le variabili create dentro la funzione (`differenza`, `importo`) vivono solo lì dentro: fuori non esistono, e non disturbano il resto del programma.

Con lo stesso schema scriviamo `bmi(peso, altezza)` e `nps(voti)`, che riceve un vettore e restituisce un numero solo: una funzione può contenere un ciclo, e chi la chiama non deve saperlo.

> **In aula** abbiamo scritto solo funzioni con `return()` esplicito. R restituisce anche l'ultimo valore calcolato se `return` manca, ma scriverlo rende chiaro cosa esce. Un'altra cosa che in aula non si è vista: gli argomenti possono avere un valore predefinito, `function(velocita, limite = 50)`, e allora `multa(70)` funziona.

## Una funzione che nessuno ha scritto

Chiudiamo con una frase da tenere a mente fino al modulo 6. `multa()` è una funzione: entra una velocità e un limite, esce un importo. Le regole dentro le abbiamo scritte noi leggendo il Codice della Strada. Un modello di machine learning è **una funzione che nessuno ha scritto**: entrano dati, esce una previsione, e le regole dentro le ha trovate un algoritmo guardando esempi. La forma è la stessa; cambia chi decide le soglie. Le funzioni `multa()`, `bmi()` e `rata()` di questo modulo torneranno nel modulo 12, quando un modello di linguaggio le userà come strumenti.

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

## Per approfondire

Il ciclo che queste funzioni sostituiscono è nel [modulo 3](03-ripetere). Nel [modulo 5](05-dati) i vettori diventano le colonne di una tabella, e il ciclo `for` per selezionare e contare sarà sostituito da un verbo di dplyr.
