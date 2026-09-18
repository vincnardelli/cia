---
layout: modulo
number: 3
title: Ripetere e astrarre
sezione: 1
language: R
idea: "La stessa regola applicata a molti casi diventa un ciclo; incapsulata con un nome diventa una funzione."
hours: 4
published: false
concepts_new: [vettori, indicizzazione, operazioni vettoriali, ciclo for, accumulatore, funzioni, test di una funzione]
concepts_required: [variabili, operatori di confronto, if/else, operatori logici]
explorations: []
slides_pdf:
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

Il lab dei pazienti calcola il BMI (peso / altezza²) di cinque persone e li classifica: sottopeso sotto 18,5; normopeso da 18,5 a 25 escluso; sovrappeso da 25 a 30 escluso; obesità oltre. Il BMI si calcola in un colpo solo, vettorialmente; la classificazione richiede il ciclo:

```r
altezza <- c(1.58, 1.73, 1.81, 1.47, 1.74)
peso <- c(62, 86, 85, 95, 75)

bmi <- peso / altezza^2

sovrappeso <- 0
for(i in 1:5){
  if(bmi[i] < 18.5){
    classificazione <- "Sottopeso"
  }else if(bmi[i] < 25){
    classificazione <- "Normopeso"
  }else if(bmi[i] < 30){
    classificazione <- "Sovrappeso"
  }else{
    classificazione <- "Obesità"
  }
  if(bmi[i] >= 25){
    sovrappeso <- sovrappeso + 1
  }
  print(paste0("Paziente ", i, ": BMI ", round(bmi[i], 1), " - ", classificazione))
}
print(paste0("Pazienti in sovrappeso o oltre: ", sovrappeso))
```

La variabile `sovrappeso` è un **accumulatore**: nasce a zero prima del ciclo e cresce di uno a ogni paziente che supera la soglia. È lo schema di ogni conteggio, somma o totale: inizializza fuori, aggiorna dentro, leggi dopo.

> **Attenzione** Nelle slide dell'edizione precedente la soglia è «18,5 ≤ BMI < 25», ma il codice del docente usava `bmi[i] <= 18.5` e `<= 25`: un paziente con BMI esattamente 25 veniva classificato normopeso invece che sovrappeso. Quel codice è in piattaforma come «codice da testare»: trovate il caso che lo smaschera. I confini 18,5, 25 e 30 sono i test obbligatori.

Lo stesso schema calcola la corsa del taxi: ogni minuto conosciamo i km percorsi; se la velocità (km × 60) è sotto i 20 km/h si paga a tempo (28 euro/ora, cioè 28/60 al minuto), altrimenti a distanza (1,14 euro/km). Il costo è un accumulatore che somma minuto per minuto.

```r
distanza <- c(1, 0.3, 0.5, 0.8, 0.2)
tariffa_minuto <- 28 / 60
tariffa_km <- 1.14

costo <- 0
for(i in 1:5){
  velocita <- distanza[i] * 60
  if(velocita < 20){
    costo <- costo + tariffa_minuto
  }else{
    costo <- costo + tariffa_km * distanza[i]
  }
}
print(paste0("Costo della corsa: ", round(costo, 2), " euro"))
```

A esattamente 20 km/h (0,333 km in un minuto) la tariffa dice «inferiore a 20» per il tempo e «> 20» per la distanza: i 20 esatti non sono coperti da nessuna delle due. Il codice sopra li manda alla tariffa a km. È una scelta, e va scritta nei test.

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

> **Attenzione** `for(i in 1:length(x))` con un vettore vuoto fa girare il ciclo due volte, con `i` uguale a 1 e a 0, perché `1:0` è il vettore `c(1, 0)`. Se non siete sicuri che il vettore abbia almeno un elemento, usate `seq_along(x)`, che con un vettore vuoto non gira affatto.

## Una funzione che nessuno ha scritto

Chiudiamo con una frase da tenere a mente fino al modulo 6. `multa()` è una funzione: entra una velocità e un limite, esce un importo. Le regole dentro le abbiamo scritte noi leggendo il Codice della Strada. Un modello di machine learning è **una funzione che nessuno ha scritto**: entrano dati, esce una previsione, e le regole dentro le ha trovate un algoritmo guardando esempi. La forma è la stessa; cambia chi decide le soglie. Le funzioni `multa()`, `bmi()` e `rata()` di questo modulo torneranno in modulo 11, quando un modello di linguaggio le userà come strumenti.

## Per approfondire

L'`if` che sta dentro ogni ciclo di oggi è nel [modulo 2](02-decidere). Nella [modulo 4](04-dati) i vettori diventano le colonne di una tabella, e il ciclo `for` per selezionare e contare sarà sostituito da un verbo di dplyr.
