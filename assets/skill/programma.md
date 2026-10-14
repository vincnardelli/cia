# Programma del corso: la parte sul codice

Il corso ha tre sezioni; questa skill copre la prima, *Il codice*, in R, fin dove si è arrivati in aula. Dati, machine learning, Python e modelli di linguaggio arrivano dopo e non fanno parte di questa skill. Il programma è una guida, non una gabbia: se lo studente usa qualcosa che non è qui, chiedigli dove l'ha visto.

## Modulo 1 · Partenza (lezioni 1–2)

Dalle istruzioni scritte a mano ai prompt: tre modi di far lavorare una macchina, e in tutti il controllo resta a noi.

Concetti: software 1.0, 2.0 e 3.0, linguaggi di programmazione, variabili, tipi di dato, operatori aritmetici, operatori di confronto, valori logici.
Pagina: https://www.vincnardelli.com/cia/modulo/01-partenza/

## Modulo 2 · Decidere (lezione 3)

Il computer sceglie un ramo in base a una condizione.

Concetti: if/else, else if, operatori logici, %in%, if annidati.
Pagina: https://www.vincnardelli.com/cia/modulo/02-decidere/
Codice delle lezioni: [lezione_3.R](https://www.vincnardelli.com/cia/codice/3/lezione_3.R) (il codice della lezione) · [boomer.R](https://www.vincnardelli.com/cia/codice/3/boomer.R) (lab Boomer finder) · [autovelox.R](https://www.vincnardelli.com/cia/codice/3/autovelox.R) (lab Autovelox) · [prezzi_voli.R](https://www.vincnardelli.com/cia/codice/3/prezzi_voli.R) (lab Pricing dei voli)

## Modulo 3 · Ripetere (lezioni 4–5)

La stessa regola applicata a molti casi diventa un ciclo.

Concetti: vettori, indicizzazione, operazioni vettoriali, ciclo for, accumulatore.
Pagina: https://www.vincnardelli.com/cia/modulo/03-ripetere/
Codice delle lezioni: [lezione_4.R](https://www.vincnardelli.com/cia/codice/4/lezione_4.R) (il codice della lezione) · [bmi.R](https://www.vincnardelli.com/cia/codice/4/bmi.R) (lab Classificazione BMI) · [taxi.R](https://www.vincnardelli.com/cia/codice/5/taxi.R) (lab Taxi o Uber)

## Modulo 4 · Astrarre (lezioni 6–8)

Una regola che vale per molti casi prende un nome e diventa una funzione; una funzione può chiamarne un'altra, o sé stessa.

Concetti: funzioni, argomenti, valore di ritorno, test di una funzione, funzioni che chiamano funzioni, ricorsione, caso base.
Pagina: https://www.vincnardelli.com/cia/modulo/04-astrarre/
Codice delle lezioni: [lezione_6.R](https://www.vincnardelli.com/cia/codice/6/lezione_6.R) (funzioni, print e return) · [app.R](https://www.vincnardelli.com/cia/codice/6/app.R) (la app Shiny del BMI) · [biglietti.R](https://www.vincnardelli.com/cia/codice/6/biglietti.R) (lab 1, biglietti e carnet) · [fornitori.R](https://www.vincnardelli.com/cia/codice/6/fornitori.R) (lab 2, due fornitori) · [fornitori_sconti.R](https://www.vincnardelli.com/cia/codice/6/fornitori_sconti.R) (lab 3, con lo sconto)

## Ordine dei costrutti

Se lo studente non dice a che punto è, deducilo dal codice che scrive. Ordine di apparizione: calcoli, variabili e tipi di dato → vettori e parentesi quadre → confronti → if/else ed else if → &, |, ! e %in% → if annidati → ciclo for e accumulatore → funzioni con return() → funzioni che chiamano funzioni e funzioni dentro un ciclo → ricorsione con caso base → la prima app Shiny.

Nota: nelle lezioni 1 e 2 non si è scritto codice R; le basi di R (calcoli, `<-`, tipi, vettori, confronti) sono all'inizio della lezione 3.
