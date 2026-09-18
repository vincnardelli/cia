---
layout: modulo
number: 2
title: Decidere
sezione: 1
language: R
idea: "Il computer sceglie un ramo in base a una condizione."
hours: 4
published: false
concepts_new: [if/else, else if, operatori logici, "%in%", if annidati]
concepts_required: [variabili, operatori di confronto, valori logici]
explorations: []
slides_pdf:
---

## Dal confronto alla decisione

Il modulo scorso abbiamo chiesto al computer se `voto >= 18` e lui ha risposto `TRUE`. Oggi usiamo quella risposta per fargli fare qualcosa di diverso a seconda del caso. Il costrutto si chiama `if`, «se»:

```r
voto <- 12

if(voto >= 18){
  status <- "Promosso"
}else{
  status <- "Bocciato"
}
status
```

Si legge così: se la condizione tra parentesi è `TRUE`, esegui il blocco tra le prime graffe; altrimenti (`else`) esegui il secondo. Il blocco `else` è facoltativo, ma quasi sempre lo vogliamo: senza, quando la condizione è falsa la variabile `status` non esiste e il programma prosegue con un buco.

Questa è la colonna «Software 1.0» della tabella di modulo 1: la regola (18 è la sufficienza) la scriviamo noi, esplicitamente, e vale sempre.

## Boomer: tre modi, un caso limite

Un *baby boomer* è chi è nato tra il 1946 e il 1964. Dato un anno di nascita, il programma deve rispondere «Boomer» o «Non Boomer». Ci sono almeno tre modi di scriverlo.

Il primo usa una catena di condizioni:

```r
anno <- 1964

if(anno > 1964){
  status <- "Non Boomer"
}else if(anno < 1946){
  status <- "Non Boomer"
}else{
  status <- "Boomer"
}
status
```

`else if` significa «altrimenti, se»: R prova le condizioni dall'alto verso il basso e si ferma alla prima vera. Il secondo modo mette insieme due condizioni con un **operatore logico**:

```r
if(anno < 1964 & anno > 1946){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
```

`&` è la «e»: entrambe le condizioni devono essere vere. `|` è la «o»: basta una. `!` nega. Il terzo modo chiede se l'anno sta dentro un intervallo:

```r
if(anno %in% 1946:1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
```

`1946:1964` è l'elenco di tutti gli interi da 1946 a 1964 e `%in%` chiede «è uno di questi?».

> **Attenzione** Provate i tre programmi con `anno <- 1964`. Il primo e il terzo dicono «Boomer»; il secondo dice «Non Boomer», perché `<` e `>` sono **stretti** ed escludono gli estremi. La regola dice «tra il 1946 e il 1964» e gli estremi sono inclusi: il secondo programma è sbagliato, e lo è solo su due anni su cento. Nessun test «normale» lo scopre; lo scoprono solo i test sui confini. Da oggi ogni lab ha almeno un test su ogni confine.

> **In aula** abbiamo visto solo `&` e `|`. Esistono anche `&&` e `||`, che lavorano su un valore solo: dentro un `if` danno lo stesso risultato, ma sui vettori del modulo 3 si comportano diversamente. Usate `&` e `|` e non sbaglierete.

## Autovelox: una catena ordinata

L'articolo 142 del Codice della Strada fissa le sanzioni per eccesso di velocità in base a quanto si supera il limite: fino a 10 km/h, 36 euro; oltre 10 e fino a 40, 148 euro; oltre 40 e fino a 60, 370 euro; oltre 60, 500 euro. Il programma riceve velocità e limite e restituisce la multa:

```r
velocita <- 70
limite <- 50

differenza <- velocita - limite

if(differenza <= 0){
  multa <- 0
}else if(differenza <= 10){
  multa <- 36
}else if(differenza <= 40){
  multa <- 148
}else if(differenza <= 60){
  multa <- 370
}else{
  multa <- 500
}
multa
```

Due cose da notare. Primo: calcoliamo `differenza` una volta sola, all'inizio, e poi ragioniamo su quella; un programma leggibile prepara i suoi ingredienti prima di decidere. Secondo: l'ordine dei rami conta. Il ramo `differenza <= 40` viene raggiunto solo se `differenza <= 10` era falso, quindi «<= 40» in quella posizione significa in realtà «tra 10 escluso e 40 incluso». Se invertiste i due rami, chi supera il limite di 5 km/h pagherebbe 148 euro.

I test che il programma deve superare, oltre ai casi normali, sono esattamente i confini: 60 con limite 50 (esattamente +10) deve dare 36; 90 (+40) deve dare 148; 110 (+60) deve dare 370; 111 deve dare 500; 45 deve dare 0.

> **Attenzione** «Non oltre 10 km/h» significa che 10 è incluso nel primo scaglione. Se scrivete `differenza < 10`, il caso 60/50 restituisce 148 invece di 36. La legge è scritta con «non oltre» e «oltre»: tradurre queste parole in `<=` e `<` è il vero lavoro, e l'assistente AI sbaglia spesso proprio qui.

## Condizioni annidate e moltiplicatori

Un `if` può stare dentro un altro `if`. Il taxi a Roma applica una quota fissa che dipende da due cose: l'ora (notturna dalle 22 alle 6) e, se è giorno, se è festivo:

```r
giorno <- "D"
ora <- 12

if(ora >= 6 & ora < 22){
  if(giorno == "D"){
    quota_fissa <- 5
  }else{
    quota_fissa <- 3
  }
}else{
  quota_fissa <- 7
}
quota_fissa
```

Quando le regole si accumulano, conviene non calcolare il risultato dentro ogni ramo ma calcolare un **moltiplicatore** e applicarlo alla fine. È quello che fa il pricing dei voli: prezzo base per tipo di posto (Economy 100, Premium 180, Business 350), uno sconto o un rincaro in base ai giorni di anticipo, un altro in base al riempimento dell'aereo, una fee fissa di 25 euro, e un extra del 10 % se mancano al massimo 2 giorni e l'aereo è pieno oltre l'85 %:

```r
posto <- "Economy"
giorni_anticipo <- 5
riempimento <- 0.82

if(posto == "Economy"){
  prezzo_base <- 100
}else if(posto == "Premium"){
  prezzo_base <- 180
}else{
  prezzo_base <- 350
}

if(giorni_anticipo > 60){
  moltiplicatore_anticipo <- 0.80
}else if(giorni_anticipo >= 31){
  moltiplicatore_anticipo <- 0.90
}else if(giorni_anticipo >= 15){
  moltiplicatore_anticipo <- 1.00
}else if(giorni_anticipo >= 7){
  moltiplicatore_anticipo <- 1.20
}else if(giorni_anticipo >= 3){
  moltiplicatore_anticipo <- 1.40
}else{
  moltiplicatore_anticipo <- 1.70
}

if(riempimento < 0.50){
  moltiplicatore_riempimento <- 0.90
}else if(riempimento <= 0.70){
  moltiplicatore_riempimento <- 1.00
}else if(riempimento <= 0.85){
  moltiplicatore_riempimento <- 1.15
}else{
  moltiplicatore_riempimento <- 1.35
}

extra_stress <- 1
if(giorni_anticipo <= 2 & riempimento > 0.85){
  extra_stress <- 1.10
}

prezzo_finale <- prezzo_base * moltiplicatore_anticipo * moltiplicatore_riempimento * extra_stress + 25
print(paste0("Prezzo: ", round(prezzo_finale, 2), " euro"))
```

Ogni blocco decide una cosa sola; l'ultima riga mette insieme. Se domani cambia lo sconto per l'anticipo, si tocca un solo blocco. La variabile `extra_stress` parte da 1 (nessun effetto) e cambia solo nel caso speciale: è un modo pulito per scrivere un `if` senza `else`.

> **Attenzione** Nelle regole dei voli c'è scritto «31–60 giorni → −10 %» e «> 60 → −20 %». Con 60 giorni esatti il primo `if` (`> 60`) è falso e si scende a `>= 31`: −10 %. Con 61, −20 %. Le tabelle scritte a parole lasciano sempre un dubbio sui confini: quando la specifica è ambigua, la si chiarisce **prima** di scrivere il codice e si mette il valore esatto nei test.

## Come si lavora con l'assistente

Da questo modulo i lab in piattaforma si chiudono con «fallo tradurre in Python e verifica con gli stessi test». Il ciclo è sempre lo stesso: scrivete la specifica (obiettivo, input, output, regole), fate generare il codice, costruite i test sui confini, scoprite dove sbaglia. Il lab sull'IRPEF, con gli scaglioni marginali a 15.000 e 28.000 euro esatti, è quello in cui gli assistenti sbagliano più spesso.

## Per approfondire

I confronti e i valori logici sono nel [modulo 1](01-partenza). Nella [modulo 3](03-ripetere-e-astrarre) applicheremo lo stesso `if` a molti valori in una volta con il ciclo `for`, e trasformeremo l'autovelox in una funzione riutilizzabile.
