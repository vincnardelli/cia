# Indice dei lab

Per ogni lab: specifica sintetica e URL della pagina (dove ci sono regole complete, esempi e verifica automatica con casi nascosti).

## Settimana 1

### Scontrino — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/scontrino/  
Obiettivo: Calcolare il totale di uno scontrino a partire dal prezzo netto e dalla quantità, con IVA al 22%.  
Input: prezzo_netto (numero); quantita (numero). Output: totale (numero)

- Il totale netto è `prezzo_netto * quantita`.
- L'IVA è il 22% del totale netto: il totale da pagare è il netto più l'IVA.
- Arrotonda il risultato a due decimali con `round(x, 2)`.

### Cambio valuta — extra, R, AI-off
https://www.vincnardelli.com/cbd/lab/cambio-valuta/  
Obiettivo: Convertire un importo in euro in dollari applicando la commissione dello sportello.  
Input: importo_euro (numero); tasso (numero). Output: dollari (numero)

- La commissione è il **maggiore** tra 2 € e l'1% dell'importo.
- Si cambia solo l'importo al netto della commissione: `dollari = (importo - commissione) * tasso`.
- Se l'importo non copre nemmeno la commissione, si ricevono 0 dollari (mai un valore negativo).
- Arrotonda a due decimali.

### Interesse composto — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/interesse-composto/  
Obiettivo: Calcolare il montante di un capitale investito a interesse composto per un certo numero di anni.  
Input: capitale (numero); tasso (numero); anni (numero). Output: montante (numero)

- Ogni anno il capitale cresce del tasso: `montante = capitale * (1 + tasso/100)^anni`.
- Attenzione: il tasso è dato in percentuale (3 significa 3%), non in frazione.
- Arrotonda a due decimali.

### Piano di risparmio — sfida, R, AI-on
https://www.vincnardelli.com/cbd/lab/piano-risparmio/  
Obiettivo: Calcolare quanto si accumula versando ogni anno una somma fissa su un conto a interesse composto.  
Input: capitale (numero); versamento (numero); tasso (numero); anni (numero). Output: montante (numero)

- Ogni anno, nell'ordine: il saldo cresce del tasso, poi si aggiunge il versamento.
- Con zero anni non succede nulla: il montante è il capitale iniziale.
- Non esiste una formula "già vista" nel corso: serve ripetere il passo per ogni anno (o trovare la formula da soli).

## Settimana 2

### Boomer finder — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/boomer/  
Obiettivo: Stabilire se una persona è un baby boomer a partire dall'anno di nascita.  
Input: anno (numero). Output: status (testo)

- È boomer chi è nato **dal 1946 al 1964 compresi**.
- Tutti gli altri sono "Non Boomer".
- Scrivilo in almeno due modi diversi (con due `if`, con `&`, con `%in%`) e controlla che diano lo stesso risultato sui casi al confine.

### Autovelox — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/autovelox/  
Obiettivo: Calcolare la sanzione per eccesso di velocità secondo l'art. 142 del Codice della Strada.  
Input: velocita (numero); limite (numero). Output: multa (numero)

Art. 142 CdS (importi minimi):

- entro il limite: nessuna sanzione;
- oltre il limite di **non oltre 10 km/h**: 36 €;
- di **oltre 10 e non oltre 40 km/h**: 148 €;
- di **oltre 40 e non oltre 60 km/h**: 370 €;
- di **oltre 60 km/h**: 500 €.

### Pricing dei voli — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/pricing-voli/  
Obiettivo: Calcolare il prezzo di un biglietto aereo in base a classe, giorni di anticipo e riempimento dell'aereo.  
Input: seat_type (testo); days_before (numero); load_factor (numero). Output: prezzo_finale (numero)

- **Tariffa base**: Economy 100 €, Premium 180 €, Business 350 €.
- **Anticipo** (`days_before`): oltre 60 giorni −20%; da 31 a 60 −10%; da 15 a 30 0%; da 7 a 14 +20%; da 3 a 6 +40%; da 0 a 2 +70%.
- **Riempimento** (`load_factor`): sotto 0.50 −10%; da 0.50 a 0.70 0%; oltre 0.70 fino a 0.85 +15%; oltre 0.85 +35%.
- **Fee fissa**: 25 € aggiunti alla fine.
- **Stress di mercato**: se `days_before` è 2 o meno **e** `load_factor` supera 0.85, ulteriore +10% (prima della fee).
- I moltiplicatori si applicano in cascata: `base × anticipo × riempimento × stress + 25`.

### Autovelox con punti patente — extra, R, AI-off
https://www.vincnardelli.com/cbd/lab/autovelox-punti/  
Obiettivo: Estendere l'autovelox: oltre alla sanzione, calcolare i punti patente rimasti dopo la decurtazione.  
Input: velocita (numero); limite (numero); punti_iniziali (numero). Output: punti_finali (numero)

- Fasce come nell'Autovelox: entro il limite o non oltre 10 km/h → nessuna decurtazione; oltre 10 e non oltre 40 → 3 punti; oltre 40 e non oltre 60 → 6 punti; oltre 60 → 10 punti.
- I punti non possono scendere sotto zero.

### Bollo auto — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/bollo-auto/  
Obiettivo: Calcolare il bollo auto (regole semplificate) in base alla potenza e alla classe ambientale.  
Input: kw (numero); classe_euro (numero). Output: bollo (numero)

Tariffa per kW (regole semplificate a fini didattici):

| classe Euro | fino a 100 kW | ogni kW oltre i 100 |
|---|---|---|
| 4, 5, 6 | 2,58 € | 3,87 € |
| 3 | 2,70 € | 4,05 € |
| 2 | 2,80 € | 4,20 € |
| 0, 1 | 3,00 € | 4,50 € |

- I primi 100 kW si pagano alla tariffa bassa; **solo** i kW oltre i 100 alla tariffa alta.
- Arrotonda a due decimali.

### IRPEF 2025 vs 2026 — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/irpef/  
Obiettivo: Calcolare l'IRPEF lorda con gli scaglioni 2025 e con la proposta 2026, e la differenza tra le due.  
Input: reddito (numero). Output: differenza (numero)

Aliquote per scaglione (ogni fascia tassa **solo la parte di reddito che ci cade dentro**):

| scaglione | 2025 | 2026 (proposta) |
|---|---|---|
| fino a 15.000 € | 23% | 20% |
| da 15.001 a 28.000 € | 23% | 23% |
| da 28.001 a 50.000 € | 35% | 36% |
| da 50.001 a 75.000 € | 43% | 40% |
| da 75.001 a 120.000 € | 43% | 43% |
| oltre 120.000 € | 43% | 46% |

- Calcola `imposta_2025` e `imposta_2026`, poi `differenza <- imposta_2026 - imposta_2025` (negativa se il 2026 conviene).
- Arrotonda la differenza a due decimali.

### Penali sulle fatture — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/penali-fatture/  
Obiettivo: Calcolare il totale di una fattura pagata in ritardo, applicando le penali previste.  
Input: importo (numero); giorni_ritardo (numero). Output: totale (numero)

- entro 10 giorni di ritardo: nessuna penale;
- da 11 a 30 giorni: 5% dell'importo;
- da 31 a 60 giorni: 10%;
- da 61 a 90 giorni: 20%;
- oltre 90 giorni: 20% **più il 2% per ogni giorno oltre il 90°**.

### ISEE semplificato — sfida, R, AI-on
https://www.vincnardelli.com/cbd/lab/isee/  
Obiettivo: Calcolare un ISEE semplificato di una famiglia a partire da reddito, patrimonio e numero di componenti.  
Input: reddito (numero); patrimonio (numero); componenti (numero). Output: isee (numero)

- L'indicatore della situazione economica è `ISE = reddito + 20% del patrimonio`.
- La scala di equivalenza dipende dai componenti: 1 → 1,00; 2 → 1,57; 3 → 2,04; 4 → 2,46; 5 → 2,85; **oltre 5, +0,35 per ogni componente in più**.
- `ISEE = ISE / scala`, arrotondato a due decimali.

## Settimana 3

### Classificazione BMI — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/bmi/  
Obiettivo: Calcolare l'indice di massa corporea di un paziente e classificarlo secondo le fasce del Ministero della Salute.  
Input: altezza (numero); peso (numero). Output: classificazione (testo)

- `BMI = peso / altezza^2`.
- Sottopeso: BMI < 18,5 · Normopeso: 18,5 ≤ BMI < 25 · Sovrappeso: 25 ≤ BMI < 30 · Obesità grado I: 30 ≤ BMI < 35 · Obesità grado II: 35 ≤ BMI < 40 · Obesità grado III: BMI ≥ 40.
- Le categorie vanno scritte così: `"Sottopeso"`, `"Normopeso"`, `"Sovrappeso"`, `"Obesità grado I"`, `"Obesità grado II"`, `"Obesità grado III"`.
- Poi, in RStudio, applica lo stesso codice a più pazienti con un ciclo `for` (la verifica qui controlla un paziente alla volta).

### Taxi a Roma — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/taxi/  
Obiettivo: Calcolare il costo di una corsa in taxi a Roma a partire dai km percorsi in ogni minuto.  
Input: distanza (vettore di numeri). Output: costo (numero)

- In ogni minuto il tassametro sceglie la tariffa in base alla velocità di quel minuto: `velocita = km * 60` (km/h).
- Velocità **sotto i 20 km/h** → tariffa oraria: 28 €/h, cioè 28/60 € per quel minuto.
- Velocità di 20 km/h o più → tariffa chilometrica: 1,14 € per km percorso in quel minuto.
- Il costo è la somma dei minuti. Arrotonda a due decimali.

### Autovelox come funzione — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/autovelox-funzione/  
Obiettivo: Riscrivere l'autovelox come funzione `multa(velocita, limite)` riutilizzabile, e verificarla con gli stessi casi della settimana 2.  
Input: velocita (numero); limite (numero). Output: multa (numero) — funzione `multa`

- Stesse regole dell'[Autovelox](../autovelox/): 0 / 36 / 148 / 370 / 500 € per le fasce "entro il limite", "non oltre 10", "non oltre 40", "non oltre 60", "oltre 60".
- Il codice deve **definire** la funzione `multa <- function(velocita, limite){ ... }` che **restituisce** l'importo (ultima espressione o `return()`).
- La verifica chiama la tua funzione con i valori di ogni caso: non servono assegnazioni di prova.
- In RStudio, usala su un vettore di veicoli con un ciclo `for` e conta quante multe superano i 100 €.

### Taxi o Uber? — extra, R, AI-off
https://www.vincnardelli.com/cbd/lab/taxi-uber/  
Obiettivo: Aggiungere al taxi la quota fissa (giorno e ora) e decidere se conviene il taxi o Uber.  
Input: distanza (vettore di numeri); giorno (testo); ora (numero); costo_uber (numero). Output: decisione (testo)

- **Quota fissa**: giorni feriali dalle 6 alle 21 (ora < 22) 3 €; domenica ("D") nella stessa fascia 5 €; **notturna** (dalle 22 in poi o prima delle 6, qualsiasi giorno) 7 €.
- **Quota variabile**: come nel lab Taxi (28 €/h sotto i 20 km/h, 1,14 €/km altrimenti).
- Si sceglie "Uber" solo se costa **strettamente meno** del taxi; a parità, "Taxi".

### Portafoglio — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/portafoglio/  
Obiettivo: Calcolare il valore finale di 100 € investiti, dato il vettore dei rendimenti giornalieri.  
Input: rendimenti (vettore di numeri). Output: valore_finale (numero)

- Si parte da 100 €. Ogni giorno il valore viene moltiplicato per `(1 + rendimento)` di quel giorno.
- Un rendimento di −1 (−100%) azzera il capitale: da lì in poi resta zero.
- Arrotonda a due decimali. Fallo con un ciclo `for`; se conosci `prod()` usalo per controllare.

### Rata del mutuo — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/rata-mutuo/  
Obiettivo: Scrivere la funzione `rata(capitale, tasso, anni)` che calcola la rata mensile di un mutuo a rata costante.  
Input: capitale (numero); tasso (numero); anni (numero). Output: rata (numero) — funzione `rata`

- Tasso mensile `i = tasso/100/12`, numero di rate `n = anni * 12`.
- Formula della rata costante (ammortamento "alla francese"): `rata = capitale * i / (1 - (1 + i)^(-n))`.
- **Se il tasso è zero** la formula divide per zero: in quel caso la rata è semplicemente `capitale / n`.
- Restituisci la rata arrotondata a due decimali.

### Sconto fedeltà — sfida, R, AI-on
https://www.vincnardelli.com/cbd/lab/sconto-fedelta/  
Obiettivo: Scrivere la specifica e il codice di un programma fedeltà: sconto a soglie più bonus tessera, con un tetto massimo.  
Input: totale_carrello (numero); tessera (testo). Output: totale_scontato (numero)

- Sconto base: 0% sotto i 100 €; 5% da 100 € in su; 10% da 250 € in su.
- Bonus tessera in punti percentuali: silver +2, gold +7, nessuna +0.
- Lo sconto complessivo non può superare il 15%.
- Prima di scrivere codice, scrivi tu la specifica completa (input, output, casi limite) e passala all'assistente in modalità *sviluppo assistito*.

## Settimana 4

### Clienti giovani — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/ecommerce-giovani/  
Obiettivo: Contare gli ordini fatti da clienti con meno di 35 anni nel dataset ecommerce.  
Input: data (data frame). Output: n_giovani (numero)

- Il data frame `data` è già caricato quando premi Verifica (in RStudio: `data <- read.csv("ecommerce.csv")`).
- Conta le righe con `Age < 35`. La colonna `Age` ha valori mancanti: decidi cosa farne e scrivilo nel codice, non lasciarlo al caso.
- Il risultato deve essere un **numero** (non una tabella): da una pipeline dplyr, estrailo con `$n` oppure usa `nrow()` / `sum()`.

### Titanic: gli over 50 — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/titanic-over50/  
Obiettivo: Quante persone con più di 50 anni erano a bordo del Titanic?  
Input: titanic (data frame). Output: n_over50 (numero)

- Conta i passeggeri con `Age > 50` (età nota).
- Estrai il numero dalla tabella di `summarise()`.
- Poi, in RStudio, continua con le altre domande della settimana: la percentuale di uomini e donne tra gli over 50 (percentuale *rispetto a chi?*).

### Titanic: sopravvivenza in prima classe — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/titanic-prima-classe/  
Obiettivo: Qual è la percentuale di sopravvissuti tra i passeggeri di prima classe?  
Input: titanic (data frame). Output: perc_prima (numero)

- `Survived` vale 1 se sopravvissuto, 0 altrimenti: la **media** di Survived è già la percentuale.
- Raggruppa per `Pclass`, calcola la media per classe, poi estrai il valore della classe 1.
- Confronta con la terza classe: la differenza è il punto della domanda.

### Titanic: biglietti condivisi — sfida, R, AI-on
https://www.vincnardelli.com/cbd/lab/titanic-biglietti/  
Obiettivo: Quanti biglietti erano associati a più di un passeggero?  
Input: titanic (data frame). Output: n_condivisi (numero)

- Raggruppa per `Ticket`, conta i passeggeri per biglietto, tieni solo i biglietti con più di uno.
- Il risultato è il numero di **biglietti**, non di passeggeri.
- Servono due passaggi di conteggio: uno dentro i gruppi, uno sul risultato.

## Settimana 5

### Finanza: la volatilità — base, R, AI-off
https://www.vincnardelli.com/cbd/lab/finanza-volatilita/  
Obiettivo: Calcolare la volatilità (deviazione standard dei rendimenti giornalieri) del titolo Unicredit.  
Input: returns (data frame). Output: volatilita (numero)

- In finanza il rischio di un titolo si misura con la **variabilità** dei suoi rendimenti: `sd()`.
- Calcola `sd(returns$Unicredit)` e arrotonda a 4 decimali.
- In RStudio confronta le quattro azioni: quale ha il rendimento medio più alto? quale il rischio più alto? coincidono?

### Finanza: due banche — extra, R, AI-on
https://www.vincnardelli.com/cbd/lab/finanza-correlazione/  
Obiettivo: Misurare quanto i rendimenti di Intesa e Unicredit si muovono insieme.  
Input: returns (data frame). Output: correlazione (numero)

- `cor(x, y)` misura quanto due serie salgono e scendono insieme: da −1 a +1.
- Calcola la correlazione tra `Intesa` e `Unicredit` e arrotonda a 3 decimali.
- Poi in RStudio fai il grafico a dispersione con ggplot2 e confronta con la coppia Ferrari–Enel.
