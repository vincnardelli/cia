---
layout: modulo
number: 3
title: Ripetere e astrarre
sezione: 1
language: R
idea: "La stessa regola applicata a molti casi diventa un ciclo; incapsulata con un nome diventa una funzione."
hours: 4
concepts_new: [vettori, indicizzazione, operazioni vettoriali, ciclo for, accumulatore, funzioni, test di una funzione, ricorsione, caso base]
concepts_required: [variabili, operatori di confronto, if/else, operatori logici]
explorations: []
slides_pdf:
slides:
  - titolo: Lezione 4
    descr: Classificazione BMI
    pdf: slide/lezione_4.pdf
  - titolo: Lezione 5
    descr: Taxi o Uber, in cinque passi
    pdf: slide/lezione_5.pdf
  - titolo: Lezione 6
    descr: "Funzioni e ricorsione: carnet e spesa e-commerce"
    pdf: slide/lezione_6.pdf
codice:
  - titolo: lezione_4.R
    descr: il codice della lezione
    file: codice/4/lezione_4.R
  - titolo: bmi.R
    descr: lab Classificazione BMI
    file: codice/4/bmi.R
  - titolo: lezione_6.R
    descr: "Lezione 6: argomenti, ritorno e chiamate tra funzioni"
    file: codice/6/lezione_6.R
  - titolo: biglietti_ricorsione.R
    descr: "Lezione 6: biglietti singoli o carnet"
    file: codice/6/biglietti_ricorsione.R
  - titolo: spesa_ecommerce.R
    descr: "Lezione 6: tre prodotti e due e-commerce"
    file: codice/6/spesa_ecommerce.R
---

## Più valori in una variabile sola

Finora ogni variabile conteneva un valore. Un'analisi vera ha cento clienti, non uno. Il **vettore** è una sequenza di valori dello stesso tipo, costruita con `c()` («combine»):

```r
clienti <- c("Antonio", "Luca", "Giorgio")
eta <- c(23, 19, 93)

clienti[3]
eta[2:3]
clienti[c(1, 3)]
```

Le parentesi quadre estraggono per posizione: `clienti[3]` è `"Giorgio"`, `eta[2:3]` sono il secondo e il terzo valore. Si parte da 1, non da 0. Attenzione alla differenza tra `c("Antonio", "Luca", "Giorgio")`, che è un vettore di tre elementi, e `"Antonio, Luca, Giorgio"`, che è un testo solo.

Le operazioni sui vettori lavorano **elemento per elemento**, senza che dobbiamo chiederlo:

```r
eta < 35
eta + 1
eta * 12
```

`eta < 35` restituisce `TRUE FALSE FALSE`: un vettore logico lungo quanto `eta`. E un vettore logico serve a selezionare:

```r
clienti[eta < 35]
eta[eta < 35]
```

`clienti[eta < 35]` tiene i clienti nelle posizioni dove il confronto è vero: `"Antonio"` e `"Luca"`. Questa riga, «dammi i nomi di chi ha meno di 35 anni», è già un'analisi dei dati, e il modulo prossimo la riscriveremo con `filter`.

> **Attenzione** Cosa succede con `eta[5]` se il vettore ha tre elementi? R risponde `NA`, «non disponibile», senza errore. Un `NA` che entra in un calcolo lo contamina: `NA + 1` è `NA`, `mean(c(1, NA))` è `NA`. Lo incontreremo spesso dal modulo 4.

## Il ciclo for: la stessa cosa per ogni elemento

L'operazione elemento per elemento funziona per l'aritmetica e i confronti, non per un `if`: `if` guarda una condizione sola. Per applicare la regola dei pensionati a quattro persone dobbiamo **ripetere**:

```r
nomi <- c("Raffaele", "Giovanni", "Carmela", "Gioele")
eta <- c(89, 6, 45, 102)

for(i in 1:4){
  if(eta[i] > 67){
    print(paste0(nomi[i], " è in pensione"))
  }else{
    print(paste0(nomi[i], " non è in pensione"))
  }
}
```

`for(i in 1:4)` fa girare il blocco quattro volte, con `i` che vale 1, poi 2, 3, 4. Dentro, `eta[i]` e `nomi[i]` sono l'età e il nome della persona corrente. Il corpo del ciclo è esattamente l'`if` del modulo scorso: non abbiamo imparato una regola nuova, l'abbiamo applicata a più casi.

Lo stesso schema serve ogni volta che una regola va applicata a molti casi. Il ciclo non introduce una regola nuova: ripete quella che sapete già scrivere.

Dentro un ciclo serve spesso un **accumulatore**: una variabile che nasce prima del ciclo e cresce a ogni giro. Qui conta le persone in pensione:

```r
quanti <- 0
for(i in 1:length(eta)){
  if(eta[i] > 67){
    quanti <- quanti + 1
  }
}
quanti
```

È lo schema di ogni conteggio, somma o totale: inizializza fuori, aggiorna dentro, leggi dopo. Se l'inizializzazione finisce dentro il ciclo, l'accumulatore riparte da zero a ogni giro e resta solo l'ultimo valore: nessun errore, risultato sbagliato.

## Il lab del BMI: vettori e ciclo insieme

Il lab dei pazienti calcola il BMI (peso / altezza²) di cinque persone e le classifica secondo le fasce del Ministero della Salute: sottopeso sotto 18,5; normopeso da 18,5 a 25 escluso; sovrappeso da 25 a 30 escluso; poi i tre gradi di obesità. Il BMI si calcola in un colpo solo, vettorialmente; la classificazione, che è un `if`, richiede il ciclo:

```r
altezza <- c(1.58, 1.73, 1.81, 1.47, 1.74)
peso <- c(62, 86, 85, 95, 75)

bmi <- peso / altezza^2

sovrappeso <- 0
for(i in 1:length(altezza)){
  if(bmi[i] < 18.5){
    classificazione <- "Sottopeso"
  }else if(bmi[i] < 25){
    classificazione <- "Normopeso"
  }else if(bmi[i] < 30){
    classificazione <- "Sovrappeso"
  }else if(bmi[i] < 35){
    classificazione <- "Obesità grado I"
  }else if(bmi[i] < 40){
    classificazione <- "Obesità grado II"
  }else{
    classificazione <- "Obesità grado III"
  }
  if(bmi[i] >= 25){
    sovrappeso <- sovrappeso + 1
  }
  print(paste0("Paziente ", i, ": BMI ", round(bmi[i], 2), " - ", classificazione))
}
print(paste0("Pazienti in sovrappeso o oltre: ", sovrappeso))
```

Due cose da notare. La prima: `bmi <- peso / altezza^2` calcola i cinque valori senza ciclo, perché aritmetica e confronti lavorano già elemento per elemento; il ciclo serve solo dove c'è un `if`. La seconda: le fasce sono **chiuse a sinistra**, quindi un BMI di esattamente 25 è «Sovrappeso», non «Normopeso». Per questo tutti i confronti sono `<` e nessuno è `<=`.

> **Attenzione** Nel codice dell'edizione precedente le soglie erano scritte con `<=`: un paziente con BMI esattamente 25 finiva in «Normopeso». Il programma gira, non dà errori, e sbaglia solo sui confini. I casi da provare sono sempre quelli: 18,5, 25, 30, 35 e 40 esatti.

> **Attenzione** `for(i in 1:length(x))` con un vettore vuoto fa girare il ciclo due volte, con `i` uguale a 1 e a 0, perché `1:0` è il vettore `c(1, 0)`. Se non siete sicuri che il vettore abbia almeno un elemento, usate `seq_along(x)`, che con un vettore vuoto non gira affatto.

## Il lab del taxi: un passo alla volta

Il secondo lab cresce in cinque passi, e ogni passo aggiunge una regola sola.

1. **La quota variabile.** Il tassametro di Roma non fa pagare solo i chilometri: quando il taxi è fermo nel traffico scatta la tariffa a tempo. Il tracciato è un vettore con i km percorsi in ciascun minuto; per ogni minuto la velocità (km × 60) decide quale tariffa si applica, 32,58 euro l'ora sotto i 20 km/h, 1,33 euro al km sopra. Il costo è un accumulatore che somma minuto per minuto: lo schema del BMI, con una somma al posto di un conteggio.
2. **La quota fissa.** Dipende da giorno e ora: feriale (3,50 €), sabato o festivo (5,00 €), notturna (7,50 €). Sono tre casi, quindi un `if` con due `else if`, e conviene mettere per prima la notte, che vale per tutti i giorni.
3. **La decisione.** Uber costa 9 euro: il programma non stampa più un numero, ma una scelta. Con le tariffe di oggi il taxi perde più spesso di quanto perdesse l'anno scorso.
4. **La funzione.** Ai primi tre passi si cambia corsa modificando le righe in cima e rieseguendo tutto. Al quarto il calcolo prende un nome, `costo_corsa(distanza, giorno, ora)`, e una corsa diventa una riga sola.
5. **Tre corse.** La stessa corsa in tre momenti diversi, domenica a mezzogiorno, mercoledì alle 9 e sabato alle 23: giorni e ore stanno in due vettori, la funzione si chiama dentro un ciclo e un contatore dice in quante corse su tre conviene il taxi.

Il quarto e il quinto passo sono il punto del modulo: la stessa regola, scritta una volta e riusata tante. La prossima sezione mostra come si scrive una funzione, partendo dall'autovelox del modulo 2.

> **Attenzione** A esattamente 20 km/h (0,333 km in un minuto) il tariffario dice «inferiore a 20» per il tempo e «superiore a 20» per la distanza: i 20 esatti non sono coperti da nessuna delle due. Decidete voi da che parte mandarli, e scrivetelo nei test: è una scelta, non un dettaglio.

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

<div id="lezione-6"></div>

## Lezione 6: funzioni e ricorsione

Il percorso parte da `lezione_6.R`: una funzione riceve un argomento, restituisce un risultato con `return()` e può chiamare un'altra funzione. `totale_ordine(30)` chiama `spedizione(30)` e restituisce 38. Per un ordine vuoto entrambe restituiscono zero. Il risultato si può assegnare a una variabile, confrontare con un valore atteso o usare in un altro calcolo.

Le [slide della lezione 6]({{ site.baseurl }}/slide/lezione_6.pdf) accompagnano i due laboratori. È disponibile anche la [versione modificabile delle slide]({{ site.baseurl }}/slide/lezione_6.pptx).

Una funzione è **ricorsiva** quando richiama sé stessa. Servono un **caso base**, che restituisce subito il risultato, e una chiamata che si avvicina al caso base. Nei due laboratori le tariffe sono inventate per l'esercizio.

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

Il codice commentato e le prove sono in [biglietti_ricorsione.R]({{ site.baseurl }}/codice/6/biglietti_ricorsione.R). La funzione esplora entrambe le alternative e ricalcola alcuni casi: in aula usiamo pochi viaggi per seguire le chiamate.

### Secondo laboratorio: tre prodotti, due e-commerce

Un ufficio deve acquistare un'unità di ciascun prodotto. Ogni prodotto si può comprare dal negozio A oppure dal negozio B. Ogni negozio usato aggiunge **8 € di spedizione fissa**, senza soglie. Se non compriamo nulla da un negozio, non paghiamo la sua spedizione.

| Prodotto | Negozio A | Negozio B |
|---|---:|---:|
| Carta | 20 € | 22 € |
| Penne | 30 € | 32 € |
| Cartucce | 40 € | 38 € |

Comprare ogni prodotto al prezzo più basso costa 88 € più due spedizioni: **104 €**. Comprare tutto da A costa 90 € più una spedizione: **98 €**.

Il vettore `scelte` descrive le decisioni nello stesso ordine dei prodotti. `c("A", "B")` significa che carta e penne sono già assegnate, mentre manca la scelta delle cartucce. `c()` indica che nessuna scelta è stata ancora presa.

Nel file [spesa_ecommerce.R]({{ site.baseurl }}/codice/6/spesa_ecommerce.R) ci sono solo due funzioni. `costo(scelte)` riceve tre scelte complete e calcola il conto. `minimo(scelte)` completa le scelte mancanti:

```r
minimo <- function(scelte){
  if(length(scelte) == length(prodotti)){
    return(costo(scelte))
  }

  con_a <- minimo(c(scelte, "A"))
  con_b <- minimo(c(scelte, "B"))

  return(min(con_a, con_b))
}

minimo(c())  # 98 euro
```

Ogni chiamata aggiunge una scelta, quindi si avvicina al caso base delle tre scelte complete. Le combinazioni sono otto. Ogni chiamata restituisce **un numero**, il costo minimo; non restituisce il vettore dei negozi da cui acquistare.

> **In aula** Le due funzioni leggono `prodotti`, `prezzi_a` e `prezzi_b`, definiti all'inizio del file. È una semplificazione per concentrarci sulla ricorsione. I prezzi devono essere positivi, i vettori devono avere la stessa lunghezza e i prodotti devono comparire nello stesso ordine.

Le prove da fare: `costo(c("A", "A", "A"))` deve dare 98, `costo(c("A", "A", "B"))` deve dare 104 e `minimo(c("B"))` deve dare 100. Nell'ultimo caso fissiamo il primo prodotto da B e lasciamo alla funzione le altre due decisioni.

## Una funzione che nessuno ha scritto

Chiudiamo con una frase da tenere a mente fino al modulo 6. `multa()` è una funzione: entra una velocità e un limite, esce un importo. Le regole dentro le abbiamo scritte noi leggendo il Codice della Strada. Un modello di machine learning è **una funzione che nessuno ha scritto**: entrano dati, esce una previsione, e le regole dentro le ha trovate un algoritmo guardando esempi. La forma è la stessa; cambia chi decide le soglie. Le funzioni `multa()`, `bmi()` e `rata()` di questo modulo torneranno in modulo 11, quando un modello di linguaggio le userà come strumenti.

## Per approfondire

L'`if` che sta dentro ogni ciclo di oggi è nel [modulo 2](02-decidere). Nella [modulo 4](04-dati) i vettori diventano le colonne di una tabella, e il ciclo `for` per selezionare e contare sarà sostituito da un verbo di dplyr.
