---
layout: settimana
number: 4
title: Dati
pillar: 1
language: R
idea: "Una tabella è un insieme di vettori affiancati; con cinque verbi la interroghiamo senza cicli."
hours: 5
dates: []
concepts_new: [data frame, read.csv, fattori, valori mancanti, dplyr, pipe, group_by]
concepts_required: [vettori, indicizzazione, if/else, operatori logici, operatori di confronto]
explorations: []
slides_pdf:
---

## La tabella: vettori affiancati

I vettori della settimana scorsa avevano un difetto: `clienti` ed `eta` erano due variabili separate, e solo noi sapevamo che il secondo elemento dell'una corrispondeva al secondo dell'altra. Il **data frame** mette i vettori uno accanto all'altro come colonne di una tabella, con una riga per osservazione. È l'oggetto con cui si lavora in R il 90 % del tempo, ed è esattamente ciò che avete sempre chiamato «foglio Excel».

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

Con le parentesi quadre della settimana scorsa, su un data frame si indica `[righe, colonne]`:

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
- `filter` sceglie le **righe** che soddisfano una condizione, come `clienti[eta < 35]` della settimana scorsa;
- `mutate` crea una **colonna nuova** calcolata dalle altre; `ifelse(condizione, se_vero, se_falso)` è l'`if` della settimana 2 applicato a tutta una colonna in un colpo;
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

Il `mutate` dopo il `summarise` calcola la quota di ogni gruppo sul totale dei gruppi: `sum(n)` è la somma delle righe della tabella riassunta, cioè tutti gli over 50. È il paradosso di Simpson della settimana 1 visto dal lato del codice: cambiare cosa sta al denominatore cambia la risposta.

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

> **Attenzione** Dopo un `group_by` con due variabili, `summarise` toglie **solo l'ultimo** raggruppamento: la tabella risultante è ancora raggruppata per `Pclass`. Un `mutate(percentuale = n / sum(n))` a quel punto calcola le quote **dentro ogni classe**, non sul totale. Se volete il totale generale, aggiungete `ungroup()` prima del `mutate`, oppure scrivete `summarise(..., .groups = "drop")`. È l'errore più comune di tutto il pilastro 1 e i test della piattaforma lo intercettano.

> **In aula** abbiamo risposto alla metà delle domande sul Titanic. Le altre (biglietto minimo, medio e massimo per classe e sesso; se i sopravvissuti hanno pagato di più; il ruolo della dimensione della famiglia e del porto d'imbarco) usano esattamente gli stessi cinque verbi e sono in piattaforma con la verifica automatica. La verifica funziona come per il codice delle settimane scorse: il test è «il numero di over 50 è N», e se il vostro numero è diverso il suggerimento vi dice dove guardare.

## Per approfondire

L'indicizzazione con vettori logici è nella [settimana 3](03-ripetere-e-astrarre); `ifelse` è la versione vettoriale dell'`if` della [settimana 2](02-decidere). Nella [settimana 5](05-leggere-i-dati) le statistiche dentro `summarise` (media, mediana, deviazione standard) diventano il centro, e impareremo a disegnarle con ggplot2.
