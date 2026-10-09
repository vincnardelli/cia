---
layout: modulo
number: 3
title: Ripetere
sezione: 1
language: R
idea: "La stessa regola applicata a molti casi diventa un ciclo."
hours: 4
concepts_new: [vettori, indicizzazione, operazioni vettoriali, ciclo for, accumulatore]
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
codice:
  - titolo: lezione_4.R
    descr: il codice della lezione
    file: codice/4/lezione_4.R
  - titolo: bmi.R
    descr: lab Classificazione BMI
    file: codice/4/bmi.R
  - titolo: taxi.R
    descr: lab Taxi o Uber
    file: codice/5/taxi.R
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

`clienti[eta < 35]` tiene i clienti nelle posizioni dove il confronto è vero: `"Antonio"` e `"Luca"`. Questa riga, «dammi i nomi di chi ha meno di 35 anni», è già un'analisi dei dati, e nel modulo 5 la riscriveremo con `filter`.

> **Attenzione** Cosa succede con `eta[5]` se il vettore ha tre elementi? R risponde `NA`, «non disponibile», senza errore. Un `NA` che entra in un calcolo lo contamina: `NA + 1` è `NA`, `mean(c(1, NA))` è `NA`. Lo incontreremo spesso dal modulo 5.

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

Il quarto e il quinto passo sono il punto del modulo: la stessa regola, scritta una volta e riusata tante. Il [modulo 4](04-astrarre) riprende da lì e mostra come si scrive una funzione, partendo dall'autovelox del modulo 2.

> **Attenzione** A esattamente 20 km/h (0,333 km in un minuto) il tariffario dice «inferiore a 20» per il tempo e «superiore a 20» per la distanza: i 20 esatti non sono coperti da nessuna delle due. Decidete voi da che parte mandarli, e scrivetelo nei test: è una scelta, non un dettaglio.

## Per approfondire

L'`if` che sta dentro ogni ciclo di oggi è nel [modulo 2](02-decidere). Nel [modulo 4](04-astrarre) la regola scritta nel ciclo prende un nome e diventa una funzione.
