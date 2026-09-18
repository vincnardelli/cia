# Indice dei lab

Per ogni lab: contesto, input/output e URL della pagina (dove c'è la verifica automatica con casi nascosti). I lab sono 'facili' (regole ed esempi espliciti, struttura del codice già data) o 'difficili' (solo contesto, input e output).

## Modulo 1

### Scontrino — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/scontrino/  
Obiettivo: Calcolare il totale di uno scontrino a partire dal prezzo netto e dalla quantità, con IVA al 22%.  
Input: prezzo_netto (numero); quantita (numero). Output: totale (numero)

Lavori nel piccolo negozio di elettronica di famiglia e il registratore di cassa si è rotto proprio il giorno dei saldi. Tuo zio ti passa un foglio con i prezzi **netti** dei prodotti, cioè senza IVA, e ti chiede di calcolare a mano quanto far pagare a ogni cliente.

Il primo cliente compra tre cavi HDMI da 10 € l'uno. Tu sai che in Italia l'IVA ordinaria è del 22% e che si applica sul totale della merce, non sul singolo pezzo. Il totale va scritto sullo scontrino con due decimali, come su qualsiasi ricevuta.

Scrivi il programma che, dati prezzo netto e quantità, calcola il totale da pagare. Tuo zio lo userà tutto il giorno, quindi deve funzionare anche nei casi strani: un cliente che ci ripensa e compra zero pezzi, o un prezzo con i centesimi.

Regole:
- Il totale netto è `prezzo_netto * quantita`.
- L'IVA è il 22% del totale netto: il totale da pagare è il netto più l'IVA.
- Arrotonda il risultato a due decimali con `round(x, 2)`.

### Spedizione gratis? — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/spedizione-gratis/  
Obiettivo: Dire se un carrello ha diritto alla spedizione gratuita, che scatta da 49,90 € in su.  
Input: totale (numero). Output: gratis (logico)

Il sito di un negozio di articoli sportivi mostra, accanto al carrello, la scritta «spedizione gratuita da 49,90 €». Il reparto marketing vuole aggiungere un messaggio che dica al cliente, mentre riempie il carrello, se ha già diritto alla spedizione gratis o no: è una delle leve più efficaci per far aggiungere un ultimo articolo.

Ti chiedono la regola nella forma più semplice possibile: dato il totale del carrello, un valore vero/falso che il sito userà per mostrare o nascondere il messaggio. Il confine conta: a 49,90 esatti la spedizione è gratuita, a 49,89 no. Non serve nessuna decisione «se…allora»: basta un confronto, e il risultato è direttamente `TRUE` o `FALSE`.

Regole:
- La spedizione è gratuita se il totale è **almeno** 49,90 €.
- Il risultato è un valore logico (`TRUE`/`FALSE`), ottenuto da un confronto: non serve nessun `if`.

### Quanto costa un dipendente — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/costo-dipendente/  
Obiettivo: Calcolare il costo annuo di un dipendente per l'azienda a partire dal lordo mensile.  
Input: lordo_mensile (numero). Output: costo_annuo (numero)

La titolare di un piccolo studio di consulenza vuole assumere una persona e sta facendo i conti. L'annuncio dice 1.800 euro lordi al mese, ma lei sa che il costo per l'azienda è molto più alto: in Italia le mensilità sono tredici (c'è la tredicesima) e sul lordo annuo l'azienda versa contributi che, per semplificare, contiamo al 30%.

Ti chiede un programma che, dato il lordo mensile, calcoli il costo annuo che sosterrà l'azienda, con due decimali, così da poterlo confrontare con il budget. Lo userà per più candidati, anche con cifre con i centesimi: l'arrotondamento va fatto una volta sola, alla fine.

Regole:
- Le mensilità sono **13** (c'è la tredicesima).
- Sul lordo annuo l'azienda paga contributi pari al **30%**: il costo è il lordo annuo più i contributi.
- Arrotonda a due decimali.

### Punto di pareggio — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/punto-pareggio/  
Obiettivo: Quanti pezzi bisogna vendere in un mese per coprire i costi fissi.  
Input: costi_fissi (numero); prezzo (numero); costo_unitario (numero). Output: pezzi (numero)

Due amici vogliono aprire una pizzeria da asporto e devono rispondere alla domanda che ogni banca farà loro: quante pizze dovete vendere al mese per non perderci? I costi fissi mensili (affitto, bollette, stipendi) sono noti. Ogni pizza si vende a un prezzo e costa, in ingredienti e scatola, una cifra fissa: la differenza tra i due è quello che ogni pizza venduta lascia per coprire i costi fissi.

Il numero cercato è quante pizze servono perché la somma di quei contributi copra i costi fissi. Non esistono le mezze pizze, e con una pizza in meno non si è ancora in pareggio: quindi la divisione va sempre arrotondata **per eccesso**, anche quando manca pochissimo. Quando invece la divisione è esatta, non si aggiunge nulla.

Scrivi il programma che, dati costi fissi, prezzo e costo unitario, calcola il numero di pizze del pareggio. In R esiste la funzione `ceiling()`.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### Occupazione dell'hotel — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/occupazione-hotel/  
Obiettivo: Calcolare il tasso di occupazione di un hotel in una notte, in percentuale.  
Input: occupate (numero); totali (numero). Output: tasso (numero)

La direttrice di un hotel di 45 camere guarda ogni mattina un numero solo: il tasso di occupazione della notte appena passata, cioè la percentuale di camere occupate sul totale. È il numero con cui ragiona la catena, con cui si decidono i prezzi del giorno e con cui si confrontano gli hotel tra loro.

Il gestionale glielo mostra, ma vuole ricalcolarlo lei quando arrivano i dati dagli altri hotel del gruppo, che hanno numeri di camere diversi. Scrivi il programma che, date le camere occupate e le camere totali, calcola il tasso in percentuale con un decimale. Una notte con l'hotel pieno deve dare 100, una notte vuota 0.

Regole:
- Il tasso di occupazione è `occupate / totali * 100`.
- Arrotonda a **un** decimale.

## Modulo 2

### Boomer finder — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/boomer/  
Obiettivo: Stabilire se una persona è un baby boomer a partire dall'anno di nascita.  
Input: anno (numero). Output: status (testo)

Un'agenzia di marketing sta preparando una campagna pensata per i *baby boomer*, la generazione nata nel dopoguerra. Per segmentare l'elenco clienti servono regole precise, e la definizione che l'agenzia adotta è quella demografica standard: è boomer chi è nato **dal 1946 al 1964, estremi compresi**.

Ti passano una colonna con l'anno di nascita di ogni cliente e ti chiedono un programma che, dato l'anno, risponda "Boomer" oppure "Non Boomer" (scritti esattamente così, perché poi il testo finisce in un filtro automatico).

Il punto delicato è ai bordi: chi è nato nel 1946 o nel 1964 è dentro. Il capo dell'agenzia è pignolo e vuole che tu lo scriva in almeno due modi diversi, per controllare che diano lo stesso risultato proprio su quegli anni.

Regole:
- È boomer chi è nato **dal 1946 al 1964 compresi**.
- Tutti gli altri sono "Non Boomer".
- Scrivilo in almeno due modi diversi (con due `if`, con `&`, con `%in%`) e controlla che diano lo stesso risultato sui casi al confine.

### Autovelox — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/autovelox/  
Obiettivo: Calcolare la sanzione per eccesso di velocità secondo l'art. 142 del Codice della Strada.  
Input: velocita (numero); limite (numero). Output: multa (numero)

Il Comune sta sostituendo il software di un autovelox e ti chiede di riscrivere la parte che calcola la multa. La legge è l'articolo 142 del Codice della Strada, che prevede importi crescenti in base a **di quanto** si supera il limite, e per questo lab si usano gli importi minimi.

Il testo di legge parla di eccessi "non oltre 10 km/h", "oltre 10 e non oltre 40", "oltre 40 e non oltre 60" e "oltre 60". Chi rispetta il limite non paga nulla. Le parole "non oltre" e "oltre" decidono da che parte cade chi va esattamente 10 km/h sopra il limite, e la differenza tra 36 e 148 euro per un automobilista la fa il tuo confronto.

Scrivi il programma che, data la velocità rilevata e il limite del tratto, calcola l'importo della sanzione.

Regole:
Art. 142 CdS (importi minimi):

- entro il limite: nessuna sanzione;
- oltre il limite di **non oltre 10 km/h**: 36 €;
- di **oltre 10 e non oltre 40 km/h**: 148 €;
- di **oltre 40 e non oltre 60 km/h**: 370 €;
- di **oltre 60 km/h**: 500 €.

### Rimborso per il ritardo del treno — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/rimborso-treno/  
Obiettivo: Calcolare il rimborso dovuto al passeggero in base ai minuti di ritardo all'arrivo.  
Input: prezzo (numero); ritardo (numero). Output: rimborso (numero)

Lavori all'assistenza clienti di una compagnia ferroviaria e ogni giorno arrivano richieste di rimborso per ritardo. Le condizioni di trasporto sono chiare: se il treno arriva con un ritardo **sotto i 60 minuti** non è dovuto nulla; **da 60 a 119 minuti** il passeggero ha diritto al 25% del prezzo del biglietto; **da 120 minuti in su** al 50%.

Ti chiedono di automatizzare il calcolo: dati il prezzo del biglietto e i minuti di ritardo, l'importo da rimborsare con due decimali. I passeggeri più agguerriti sono quelli con 59 o 60 minuti di ritardo, e con 119 o 120: sono esattamente i casi su cui il tuo programma deve fare la cosa scritta nelle condizioni.

Regole:
- Ritardo **sotto i 60 minuti**: nessun rimborso.
- Da 60 a 119 minuti: rimborso del **25%** del prezzo.
- Da **120 minuti in su**: rimborso del **50%**.
- Arrotonda a due decimali.

### Biglietto del museo — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/biglietto-museo/  
Obiettivo: Calcolare il prezzo del biglietto di un museo civico in base a età, tessera studente e giorno.  
Input: eta (numero); studente (logico); prima_domenica (logico). Output: prezzo (numero)

Il museo civico della città ha una tariffa che gli addetti alla biglietteria sanno a memoria ma che il nuovo sito deve calcolare da solo. La **prima domenica del mese** l'ingresso è gratuito per tutti, chiunque sia il visitatore. Negli altri giorni, i bambini **sotto i 6 anni** e le persone **dai 70 anni in su** entrano gratis; **fino ai 18 anni compresi**, oppure con la tessera studente a qualunque età, il biglietto è ridotto a 8 euro; tutti gli altri pagano l'intero, 15 euro.

Scrivi il programma che, dati età, tessera studente (vero/falso) e prima domenica (vero/falso), restituisce il prezzo. L'ordine dei controlli conta: un settantacinquenne con tessera studente entra gratis, non a 8 euro, perché il gratuito viene prima del ridotto.

Regole:
- La **prima domenica del mese** l'ingresso è gratuito per tutti.
- Negli altri giorni: gratis **sotto i 6 anni** e **dai 70 in su**; ridotto a 8 € **fino ai 18 anni compresi** oppure con tessera studente; intero 15 € per tutti gli altri.
- Le condizioni vanno controllate nell'ordine giusto: prima i casi gratuiti, poi i ridotti.

### Tariffa del parcheggio — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/parcheggio/  
Obiettivo: Calcolare quanto si paga all'uscita di un parcheggio a partire dai minuti di sosta.  
Input: minuti (numero). Output: costo (numero)

Il parcheggio del centro commerciale ha una cassa automatica e la società che lo gestisce ti chiede di riscrivere la regola che calcola l'importo all'uscita, perché quella vecchia sbagliava proprio sui casi che generano reclami.

La sosta è gratuita **fino a 30 minuti**. Oltre i 30 minuti si paga 1,50 euro **per ogni ora o frazione di ora**, contando dal momento dell'ingresso: chi resta 31 minuti paga una frazione della prima ora, cioè 1,50 euro; chi resta 61 minuti è già nella seconda ora e paga 3 euro; chi resta esattamente 60 minuti paga un'ora sola. C'è un **massimo giornaliero** di 12 euro, oltre il quale il contatore si ferma.

Scrivi il programma che, dati i minuti di sosta, calcola l'importo. In R l'arrotondamento per eccesso è `ceiling()`.

Regole:
- Fino a **30 minuti** la sosta è gratuita.
- Oltre i 30 minuti si paga **1,50 € per ogni ora o frazione di ora**, contando dall'ingresso: 31 minuti sono una frazione della prima ora, 61 minuti sono già due ore.
- Il **massimo giornaliero** è 12 €.

### IRPEF 2025 vs 2026 — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/irpef/  
Obiettivo: Calcolare l'IRPEF lorda con gli scaglioni 2025 e con la proposta 2026, e la differenza tra le due.  
Input: reddito (numero). Output: differenza (numero)

Un commercialista vuole mostrare ai clienti, con un numero, cosa cambierebbe per loro con la **riforma delle aliquote IRPEF** in discussione. Ti chiede un programma che, dato il reddito imponibile annuo, calcoli l'imposta lorda con gli scaglioni del 2025 e con quelli proposti per il 2026, e restituisca la differenza (negativa se con il 2026 si paga meno).

L'IRPEF è **progressiva a scaglioni**: ogni aliquota si applica solo alla parte di reddito che cade in quella fascia, non all'intero reddito. Nel 2025 le fasce sono: fino a 15.000 € al 23%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 35%, oltre 50.000 al 43%. Nella proposta 2026: fino a 15.000 al 20%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 36%, da 50.001 a 75.000 al 40%, da 75.001 a 120.000 al 43%, oltre 120.000 al 46%.

Il commercialista userà il numero per decidere a chi mandare la newsletter, quindi la differenza deve essere esatta al centesimo, e deve tornare anche per chi guadagna esattamente 15.000, 28.000 o 50.000 euro.

Regole:
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

### Penali sulle fatture — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/penali-fatture/  
Obiettivo: Calcolare il totale di una fattura pagata in ritardo, applicando le penali previste.  
Input: importo (numero); giorni_ritardo (numero). Output: totale (numero)

Nell'ufficio amministrativo di una piccola azienda ti chiedono di automatizzare il calcolo delle **penali per ritardato pagamento** che vanno aggiunte alle fatture dei clienti in ritardo. Le condizioni sono scritte nel contratto standard: entro 10 giorni di ritardo non si applica nulla; da 11 a 30 giorni si aggiunge il 5% dell'importo; da 31 a 60 giorni il 10%; da 61 a 90 giorni il 20%; oltre i 90 giorni si applica il 20% **più un 2% dell'importo per ogni giorno oltre il novantesimo**.

Il programma riceve l'importo della fattura e i giorni di ritardo e restituisce il totale da pagare (importo più penale), con due decimali. I clienti litigano sempre sui giorni di confine, il decimo, il trentesimo, il novantesimo: il tuo codice deve applicare esattamente ciò che dice il contratto.

Regole:
- entro 10 giorni di ritardo: nessuna penale;
- da 11 a 30 giorni: 5% dell'importo;
- da 31 a 60 giorni: 10%;
- da 61 a 90 giorni: 20%;
- oltre 90 giorni: 20% **più il 2% per ogni giorno oltre il 90°**.

### ISEE semplificato — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/isee/  
Obiettivo: Calcolare un ISEE semplificato di una famiglia a partire da reddito, patrimonio e numero di componenti.  
Input: reddito (numero); patrimonio (numero); componenti (numero). Output: isee (numero)

Il CAF del quartiere è sommerso di richieste per le agevolazioni scolastiche, e ti chiede uno strumento che dia alle famiglie una **stima dell'ISEE** prima dell'appuntamento. È una versione semplificata, ma segue la logica vera dell'indicatore.

Si parte dall'ISE, l'indicatore della situazione economica: il reddito annuo della famiglia più il **20% del patrimonio** (conti, case, risparmi). Poi l'ISE si divide per una **scala di equivalenza** che tiene conto di quante persone vivono dei quegli stessi soldi: un componente vale 1,00; due componenti 1,57; tre 2,04; quattro 2,46; cinque 2,85; e per ogni componente oltre il quinto si aggiungono 0,35 alla scala. Il risultato, l'ISEE, va arrotondato a due decimali.

Scrivi il programma che, dati reddito, patrimonio e numero di componenti, calcola l'ISEE. Le famiglie numerose sono quelle che più spesso hanno diritto alle agevolazioni: assicurati che la regola "oltre cinque" torni per sei, sette, otto persone.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### Pricing dei voli — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/pricing-voli/  
Obiettivo: Calcolare il prezzo di un biglietto aereo in base a classe, giorni di anticipo e riempimento dell'aereo.  
Input: seat_type (testo); days_before (numero); load_factor (numero). Output: prezzo_finale (numero)

Una compagnia aerea low cost ti ha assunto come stagista nel team che decide i prezzi dei biglietti. Il prezzo non è mai fisso: parte da una **tariffa base** che dipende dalla classe (Economy 100 €, Premium 180 €, Business 350 €) e viene poi corretta da due fattori.

Il primo è l'**anticipo** con cui si prenota: chi compra con più di 60 giorni di anticipo ha uno sconto del 20%, tra 31 e 60 giorni il 10%, tra 15 e 30 giorni paga il prezzo pieno, tra 7 e 14 giorni paga il 20% in più, tra 3 e 6 giorni il 40% in più, e chi compra negli ultimi due giorni il 70% in più. Il secondo è il **riempimento** dell'aereo (`load_factor`, da 0 a 1): sotto il 50% dei posti venduti sconto del 10%, tra 50% e 70% nessuna correzione, oltre il 70% fino all'85% +15%, oltre l'85% +35%.

A tutto questo si aggiunge una **fee fissa** di 25 € alla fine, e c'è una regola di "stress di mercato": se mancano 2 giorni o meno **e** l'aereo è pieno oltre l'85%, si applica un ulteriore +10% prima della fee. I moltiplicatori si applicano in cascata: base × anticipo × riempimento × stress, poi + 25. Scrivi il programma che calcola il prezzo finale.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

## Modulo 3

### Classificazione BMI — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/bmi/  
Obiettivo: Calcolare l'indice di massa corporea di un paziente e classificarlo secondo le fasce del Ministero della Salute.  
Input: altezza (numero); peso (numero). Output: classificazione (testo)

Uno studio medico vuole aggiungere alla cartella digitale dei pazienti la **classificazione automatica del peso** secondo le fasce del Ministero della Salute. L'indice di massa corporea (BMI) si calcola come peso in kg diviso il quadrato dell'altezza in metri, e in base al valore il paziente rientra in una di sei categorie.

Le fasce sono: Sottopeso sotto 18,5; Normopeso da 18,5 a 25 escluso; Sovrappeso da 25 a 30 escluso; Obesità grado I da 30 a 35 escluso; Obesità grado II da 35 a 40 escluso; Obesità grado III da 40 in su. Il medico userà il testo nella cartella, quindi le sei etichette vanno scritte esattamente così: "Sottopeso", "Normopeso", "Sovrappeso", "Obesità grado I", "Obesità grado II", "Obesità grado III".

Scrivi il programma che, dati altezza e peso, restituisce la categoria. Un paziente con BMI esattamente 25 è sovrappeso, non normopeso: le soglie appartengono alla fascia superiore.

Regole:
- `BMI = peso / altezza^2`.
- Sottopeso: BMI < 18,5 · Normopeso: 18,5 ≤ BMI < 25 · Sovrappeso: 25 ≤ BMI < 30 · Obesità grado I: 30 ≤ BMI < 35 · Obesità grado II: 35 ≤ BMI < 40 · Obesità grado III: BMI ≥ 40.
- Le categorie vanno scritte così: `"Sottopeso"`, `"Normopeso"`, `"Sovrappeso"`, `"Obesità grado I"`, `"Obesità grado II"`, `"Obesità grado III"`.
- Poi, in RStudio, applica lo stesso codice a più pazienti con un ciclo `for` (la verifica qui controlla un paziente alla volta).

### Taxi a Roma — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/taxi/  
Obiettivo: Calcolare il costo di una corsa in taxi a Roma a partire dai km percorsi in ogni minuto.  
Input: distanza (vettore di numeri). Output: costo (numero)

A Roma il tassametro non fa pagare solo i chilometri: quando il taxi è fermo nel traffico, scatta la **tariffa a tempo**. Un'associazione di consumatori ti chiede di ricostruire il costo di una corsa a partire da un tracciato GPS, per verificare gli scontrini dei tassisti.

Il tracciato è un vettore con i **km percorsi in ciascun minuto** della corsa. In ogni minuto il tassametro guarda la velocità di quel minuto (i km del minuto moltiplicati per 60 danno i km/h): se è **sotto i 20 km/h** applica la tariffa oraria, 28 € all'ora, cioè 28/60 € per quel minuto; se è di 20 km/h o più applica la tariffa chilometrica, 1,14 € per ogni km percorso in quel minuto. Il costo della corsa è la somma dei minuti, arrotondata a due decimali.

Scrivi il programma che, dato il vettore delle distanze, calcola il costo. Un taxi fermo per quattro minuti a un semaforo ha velocità zero, ma il tassametro corre lo stesso.

Regole:
- In ogni minuto il tassametro sceglie la tariffa in base alla velocità di quel minuto: `velocita = km * 60` (km/h).
- Velocità **sotto i 20 km/h** → tariffa oraria: 28 €/h, cioè 28/60 € per quel minuto.
- Velocità di 20 km/h o più → tariffa chilometrica: 1,14 € per km percorso in quel minuto.
- Il costo è la somma dei minuti. Arrotonda a due decimali.

### Autovelox come funzione — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/autovelox-funzione/  
Obiettivo: Riscrivere l'autovelox come funzione `multa(velocita, limite)` riutilizzabile, e verificarla con gli stessi casi del modulo 2.  
Input: velocita (numero); limite (numero). Output: multa (numero) — funzione `multa`

Il software dell'autovelox scritto nel modulo 2 funziona, ma il Comune ne ha comprati altri dodici, su strade con limiti diversi, e vuole usare **lo stesso codice** per tutti senza copiarlo e incollarlo ogni volta. È il momento di trasformarlo in una **funzione**.

Le regole restano quelle dell'articolo 142: nessuna sanzione entro il limite; 36 € per un eccesso non oltre 10 km/h; 148 € oltre 10 e non oltre 40; 370 € oltre 40 e non oltre 60; 500 € oltre 60. Il tuo codice deve **definire** la funzione `multa(velocita, limite)` che restituisce l'importo. La verifica non assegna variabili: chiama direttamente la tua funzione con i valori di ogni caso.

In RStudio, poi, usala su un vettore di veicoli con un ciclo e conta quante multe superano i 100 euro: è esattamente ciò che vuole il Comune.

Regole:
- Stesse regole dell'[Autovelox](../autovelox/): 0 / 36 / 148 / 370 / 500 € per le fasce "entro il limite", "non oltre 10", "non oltre 40", "non oltre 60", "oltre 60".
- Il codice deve **definire** la funzione `multa <- function(velocita, limite){ ... }` che **restituisce** l'importo (ultima espressione o `return()`).
- La verifica chiama la tua funzione con i valori di ogni caso: non servono assegnazioni di prova.
- In RStudio, usala su un vettore di veicoli con un ciclo `for` e conta quante multe superano i 100 €.

### Prodotti sotto scorta — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/sotto-scorta/  
Obiettivo: Contare quanti prodotti del magazzino sono scesi sotto la loro scorta minima e vanno riordinati.  
Input: giacenza (vettore di numeri); soglia (vettore di numeri). Output: da_riordinare (numero)

Il responsabile del magazzino di un negozio di ferramenta ha due elenchi, uno accanto all'altro: per ogni prodotto la **giacenza** (i pezzi sullo scaffale) e la **scorta minima** sotto la quale bisogna riordinare. Ogni lunedì li confronta a mano e conta quanti prodotti vanno riordinati, per sapere quante righe avrà l'ordine al fornitore.

I due elenchi sono due vettori della stessa lunghezza, nello stesso ordine: il prodotto in posizione 3 ha giacenza `giacenza[3]` e soglia `soglia[3]`. Un prodotto va riordinato se la giacenza è **strettamente sotto** la soglia: chi è esattamente alla soglia è ancora a posto.

Scrivi il programma che conta i prodotti da riordinare scorrendo i vettori con un ciclo. In RStudio, dopo, prova a ottenere lo stesso numero senza ciclo, con `sum(giacenza < soglia)`: è una riga sola, ma solo dopo aver capito il ciclo.

Regole:
- I due vettori hanno la stessa lunghezza: il prodotto `i` ha giacenza `giacenza[i]` e soglia `soglia[i]`.
- Un prodotto va riordinato se la giacenza è **strettamente minore** della soglia: alla soglia esatta è ancora a posto.
- Scorri i prodotti con un ciclo `for` e conta; poi, in RStudio, prova a farlo senza ciclo con `sum(giacenza < soglia)`.

### Straordinari della settimana — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/straordinari/  
Obiettivo: Calcolare la paga settimanale di un addetto a partire dalle ore lavorate ogni giorno, con la maggiorazione per gli straordinari.  
Input: ore (vettore di numeri); paga_oraria (numero). Output: paga (numero)

Nell'ufficio del personale di un supermercato, ogni fine settimana bisogna calcolare la paga degli addetti a partire dal cartellino: un vettore con le ore lavorate in ciascun giorno. Il contratto dice che in ogni giornata le prime **8 ore** sono ordinarie e si pagano alla paga oraria; le ore **oltre l'ottava** sono straordinario e valgono il 130% della paga oraria.

Il punto che il vecchio foglio Excel sbagliava: il conteggio è **giorno per giorno**. Chi fa 9 ore il lunedì e 7 il martedì ha un'ora di straordinario, non zero, perché le ore non si compensano tra giornate.

Scrivi il programma che, dati il vettore delle ore e la paga oraria, calcola la paga della settimana con due decimali.

Regole:
- In ogni giorno le prime **8 ore** sono ordinarie e si pagano a `paga_oraria`.
- Le ore **oltre l'ottava**, giorno per giorno, sono straordinario e si pagano al **130%** (`paga_oraria * 1.3`).
- La paga è la somma dei giorni. Arrotonda a due decimali.
- Il conteggio è per giorno: 9 ore il lunedì e 7 il martedì fanno un'ora di straordinario, non zero.

### Net Promoter Score — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/nps/  
Obiettivo: Calcolare l'NPS di un servizio a partire dai voti da 0 a 10 dati dai clienti alla domanda «lo consiglieresti?».  
Input: voti (vettore di numeri). Output: nps (numero)

Un'azienda di telefonia manda ai clienti la domanda standard della soddisfazione: «quanto consiglieresti il nostro servizio a un amico, da 0 a 10?». Il numero che il management vuole vedere ogni mese è il **Net Promoter Score**: si contano i *promotori* (chi ha risposto 9 o 10) e i *detrattori* (da 0 a 6), si fa la differenza e la si divide per il numero totale di intervistati, in percentuale. Chi ha risposto 7 o 8 è *passivo*: non conta né in un verso né nell'altro, ma resta nel denominatore.

Ti passano il vettore dei voti e ti chiedono l'NPS con un decimale. Va da −100 (tutti detrattori) a 100 (tutti promotori). Un mese con soli 7 e 8 dà zero: non è un errore, è la definizione.

Contali con un ciclo e due contatori; poi, in RStudio, confronta con `sum(voti >= 9)`.

Regole:
- I clienti con voto **9 o 10** sono *promotori*; quelli con voto **da 0 a 6** sono *detrattori*; 7 e 8 sono *passivi* e non contano.
- `NPS = (promotori − detrattori) / totale intervistati × 100`.
- Arrotonda a un decimale. Contali con un ciclo e due contatori; in RStudio confronta con `sum(voti >= 9)`.

### Sconto fedeltà — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/sconto-fedelta/  
Obiettivo: Scrivere la specifica e il codice di un programma fedeltà: sconto a soglie più bonus tessera, con un tetto massimo.  
Input: totale_carrello (numero); tessera (testo). Output: totale_scontato (numero)

Una catena di negozi di abbigliamento lancia il nuovo programma fedeltà e ti chiede di scrivere il calcolo dello **sconto alla cassa**. La direzione marketing ti ha spiegato le regole a voce, in riunione, e questa è la tua trascrizione.

Lo sconto base dipende da quanto si spende: niente sconto sotto i 100 euro, il 5% da 100 euro in su, il 10% da 250 euro in su. Chi ha la tessera fedeltà ha un **bonus** che si somma in punti percentuali: la tessera silver aggiunge 2 punti, la gold 7, chi non ha tessera non aggiunge nulla. Lo sconto complessivo, base più bonus, **non può in nessun caso superare il 15%**: un cliente gold da 300 euro avrebbe 10 + 7 = 17, ma paga con il 15%.

Il programma riceve la spesa e la tessera ("silver", "gold" o "nessuna") e restituisce il prezzo finale con due decimali. Prima di scrivere codice, scrivi tu la specifica completa, con i casi limite (100 euro esatti, 250 esatti, il tetto del 15%), e passala all'assistente in modalità *aiutami a partire*.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### Provvigioni dell'agente — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/provvigioni/  
Obiettivo: Calcolare le provvigioni annue di un agente di commercio a partire dal venduto di ciascun mese, con scaglioni progressivi.  
Input: vendite (vettore di numeri). Output: provvigioni (numero)

Un'azienda che vende macchine per il caffè ai bar paga i propri agenti a provvigione, con un contratto a **scaglioni progressivi calcolati mese per mese**: sul venduto di ogni mese, il 3% sulla parte fino a 10.000 euro, il 5% sulla parte tra 10.000 e 20.000, l'8% sulla parte oltre i 20.000. È lo stesso meccanismo dell'IRPEF: ogni aliquota si applica solo alla fetta che cade nella sua fascia, non a tutto il venduto.

Un agente con 25.000 euro di venduto in un mese prende quindi 300 sul primo scaglione, 500 sul secondo e 400 sul terzo; uno con 10.000 esatti prende 300 e basta. L'ufficio amministrazione ti passa il vettore del venduto dei dodici mesi di un agente e vuole le provvigioni dell'anno, con due decimali.

Prima di scrivere codice, scrivi tu la specifica con i casi al confine (10.000 esatti, 20.000 esatti, un mese a zero), poi ragiona su come applicare la regola a un mese, e infine ripetila con un ciclo.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

## Modulo 4

### Clienti giovani — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/ecommerce-giovani/  
Obiettivo: Contare gli ordini fatti da clienti con meno di 35 anni nel dataset ecommerce.  
Input: data (data frame). Output: n_giovani (numero)

Il responsabile marketing di un negozio online vuole capire quanto pesano i **clienti giovani** sugli ordini, per decidere se investire in una campagna sui social. Ti passa l'estratto degli ordini dell'anno (`ecommerce.csv`, una riga per ordine, con le colonne CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus) e ti chiede una prima cifra: quanti ordini sono stati fatti da clienti con meno di 35 anni.

Il data frame `data` è già caricato quando premi Verifica (in RStudio lo carichi tu con `read.csv`). C'è una trappola: la colonna `Age` ha dei **valori mancanti**, perché non tutti i clienti hanno indicato l'età. Devi decidere cosa farne e scriverlo nel codice, non lasciarlo al caso. Il risultato deve essere un numero, non una tabella.

Regole:
- Il data frame `data` è già caricato quando premi Verifica (in RStudio: `data <- read.csv("ecommerce.csv")`).
- Conta le righe con `Age < 35`. La colonna `Age` ha valori mancanti: decidi cosa farne e scrivilo nel codice, non lasciarlo al caso.
- Il risultato deve essere un **numero** (non una tabella): da una pipeline dplyr, estrailo con `$n` oppure usa `nrow()` / `sum()`.

### Titanic: gli over 50 — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/titanic-over50/  
Obiettivo: Quante persone con più di 50 anni erano a bordo del Titanic?  
Input: titanic (data frame). Output: n_over50 (numero)

Il dataset dei passeggeri del Titanic è il classico su cui tutti imparano a leggere una tabella, e per questo lo usiamo. Il data frame `titanic` è già caricato: una riga per passeggero, con le colonne PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.

La prima domanda è semplice: **quante persone con più di 50 anni** erano a bordo? Il conteggio riguarda chi ha l'età nota; 177 passeggeri non ce l'hanno, e vanno lasciati fuori consapevolmente. Il risultato deve essere un numero estratto dalla tabella che ottieni con dplyr.

Poi, in RStudio, continua con le altre domande del modulo: la percentuale di uomini e donne tra gli over 50, chiedendoti sempre "percentuale rispetto a chi?".

Regole:
- Conta i passeggeri con `Age > 50` (età nota).
- Estrai il numero dalla tabella di `summarise()`.
- Poi, in RStudio, continua con le altre domande del modulo: la percentuale di uomini e donne tra gli over 50 (percentuale *rispetto a chi?*).

### La categoria che vende di più — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/fatturato-categoria/  
Obiettivo: Trovare la categoria di prodotto con il fatturato più alto.  
Input: data (data frame). Output: categoria_top (testo)

Il direttore commerciale di un negozio online vuole sapere, prima della riunione di budget, quale categoria di prodotto ha generato più fatturato nell'anno. Il data frame `data` è già caricato: una riga per ordine, con la categoria in `ProductCategory` e l'importo in `TotalAmount`.

La domanda vuole un nome, non una tabella: dopo aver sommato il fatturato per categoria e ordinato dal più grande al più piccolo, il risultato è il testo della prima riga. In RStudio guarda anche il secondo e il terzo posto: quanto distacco c'è?

Regole:
- Il fatturato di una categoria è la somma di `TotalAmount` delle sue righe: `group_by(ProductCategory)` e `summarise(fatturato = sum(TotalAmount))`.
- Ordina con `arrange(desc(fatturato))` e prendi la prima riga.
- Il risultato è il **testo** della categoria (una stringa), non la tabella: estrailo con `$ProductCategory[1]`.

### Quanti ordini tornano indietro — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/tasso-reso/  
Obiettivo: Calcolare la quota di ordini resi tra quelli pagati con PayPal.  
Input: data (data frame). Output: tasso_paypal (numero)

Il responsabile logistica di un negozio online sospetta che gli ordini pagati con PayPal vengano resi più spesso, perché il reso è più semplice da avviare. Prima di cambiare le condizioni vuole un numero.

Il data frame `data` è già caricato; la colonna `ReturnStatus` vale 1 se l'ordine è stato reso e 0 altrimenti, quindi la sua media è già la quota di resi. Calcola la quota di resi tra gli ordini pagati con PayPal (`PaymentMethod == "PayPal"`), arrotondata a tre decimali. Poi, in RStudio, confronta i quattro metodi di pagamento: il sospetto regge?

Regole:
- `ReturnStatus` vale 1 se l'ordine è stato reso, 0 altrimenti: la sua **media** è già la quota di resi.
- Tieni solo le righe con `PaymentMethod == "PayPal"` e calcola la media; arrotonda a 3 decimali.
- In RStudio confronta i quattro metodi con `group_by(PaymentMethod)`: il reso dipende da come si paga?

### Le città con più ordini — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/terza-citta/  
Obiettivo: Trovare la terza città per numero di ordini.  
Input: data (data frame). Output: terza (testo)

Il negozio online vuole aprire un punto di ritiro in una terza città, dopo le due dove già c'è. La scelta più semplice è la terza città per numero di ordini. Il data frame `data` è già caricato, con la città di consegna in `City`.

Conta gli ordini per città, ordina dalla più grande alla più piccola e prendi il nome della terza. Attenzione al verso dell'ordinamento: se ordini in senso crescente, la terza riga è una città piccola.

Regole:
- Conta gli ordini per città: `group_by(City)` e `summarise(n = n())`.
- Ordina dalla più grande alla più piccola e prendi la **terza** riga.
- Il risultato è il nome della città (testo).

### La categoria che torna indietro di più — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/categoria-resi/  
Obiettivo: Trovare la categoria di prodotto con il tasso di reso più alto.  
Input: data (data frame). Output: categoria_resi (testo)

Il responsabile qualità del negozio online vuole capire su quale categoria di prodotto concentrare i controlli: quella che viene resa più spesso. Non la categoria con più resi in assoluto, che sarebbe semplicemente quella con più ordini, ma quella con la quota di resi più alta rispetto ai suoi ordini.

Il data frame `data` è già caricato; `ReturnStatus` vale 1 per gli ordini resi. Il risultato è il nome della categoria.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

## Modulo 5

### Segmenti RFM: quanti clienti Gold — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/rfm-gold/  
Obiettivo: Costruire le tre metriche RFM dagli scontrini, assegnare i segmenti con case_when e contare i clienti Gold.  
Input: scontrini (data frame). Output: n_gold (numero)

Il responsabile marketing di una catena di negozi vuole scrivere ai clienti migliori, quelli che il reparto chiama **Gold**: hanno comprato di recente, comprano spesso e spendono molto. Il metodo è l'RFM della lezione: per ogni cliente si calcolano *recency* (giorni dall'ultimo acquisto rispetto all'ultima data del file), *frequency* (numero di righe di scontrino) e *monetary* (totale speso); ogni metrica si trasforma in un punteggio da 1 a 4 con `ntile`, ricordando che per la recency il migliore è chi ha **pochi** giorni; e i segmenti si assegnano con il `case_when` della lezione, nell'ordine: Gold se 4-4-4, Persi se 1-1-1, Fedeli se frequency 4, Attivi se recency 4, Alta spesa se monetary 4, Altri per tutti gli altri.

Il data frame `scontrini` è già caricato (in RStudio: `read.csv("retail_rfm.csv")`); la data va convertita con `as.Date`. La domanda è una sola: quanti clienti sono Gold. Il numero deve uscire dalla tabella, con un `filter` o un `group_by`, non contato a occhio.

Regole:
- Converti la data con `as.Date(scontrini$InvoiceDate)`; la data di riferimento è l'ultima del file (`max`).
- Per cliente: `recency` = giorni tra la data di riferimento e il suo ultimo acquisto, `frequency` = numero di righe, `monetary` = somma di `Total`.
- Punteggi con `ntile(desc(recency), 4)`, `ntile(frequency, 4)`, `ntile(monetary, 4)`; segmento con il `case_when` della lezione, in quell'ordine, con `TRUE ~ "Altri"` alla fine.
- `n_gold` è il numero di clienti con segmento `"Gold"`: dalla tabella, non a occhio.

### Il corriere più regolare — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/corriere-affidabile/  
Obiettivo: Trovare il corriere con i tempi di consegna più regolari, cioè con la deviazione standard più bassa.  
Input: data (data frame). Output: corriere_regolare (testo)

Il negozio online lavora con quattro corrieri e riceve lamentele sui tempi di consegna. Il responsabile logistica non cerca il corriere più veloce: cerca quello **più regolare**, perché un cliente accetta 4 giorni se glieli hai promessi, non accetta che a volte siano 2 e a volte 8. La regolarità si misura con la deviazione standard dei giorni di consegna, come nella lezione la variabilità di un titolo.

Il data frame `data` è già caricato, con il corriere in `Courier` e i giorni in `DeliveryDays`. Per ogni corriere calcola media e deviazione standard, ordina per deviazione crescente e prendi il primo nome. In RStudio guarda anche la media: il più regolare è anche il più veloce?

Regole:
- Regolare non vuol dire veloce: un corriere che consegna sempre in 4 giorni è più prevedibile di uno che va da 1 a 8. La regolarità si misura con `sd(DeliveryDays)`.
- Per corriere: `group_by(Courier)` e `summarise(media = mean(DeliveryDays), variabilita = sd(DeliveryDays))`.
- Ordina per variabilità crescente e prendi il primo nome. In RStudio guarda anche la media: il più regolare è anche il più veloce?

### Sconto e quantità — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/sconto-quantita/  
Obiettivo: Misurare quanto lo sconto applicato e i pezzi acquistati crescono insieme.  
Input: data (data frame). Output: correlazione (numero)

Il responsabile vendite del negozio online sostiene che gli sconti fanno comprare più pezzi. Il responsabile finanza sostiene che gli sconti fanno solo spendere di meno. Prima di litigare, un numero: quanto lo sconto applicato all'ordine e i pezzi acquistati crescono insieme.

Il data frame `data` è già caricato, con lo sconto in percentuale in `Discount` e i pezzi in `Quantity`. Lo strumento è il coefficiente di correlazione, `cor(x, y)`, da −1 a +1. Arrotonda a tre decimali. Poi, in RStudio, calcola anche la correlazione tra sconto e importo dell'ordine: è più bassa, e vale la pena chiedersi perché.

Regole:
- `cor(x, y)` va da −1 a +1: vicino a +1 le due colonne salgono insieme, vicino a 0 non c'è legame.
- Calcola la correlazione tra `Discount` e `Quantity` e arrotonda a 3 decimali.
- In RStudio fai il grafico a dispersione con ggplot2 e poi confronta con la correlazione tra `Discount` e `TotalAmount`: perché è più bassa?

### Dove si spende di più per ordine — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/ticket-medio/  
Obiettivo: Trovare la città con lo scontrino medio più alto.  
Input: data (data frame). Output: citta_top (testo)

Il negozio online sta scegliendo in quale città fare una campagna con un buono sconto sopra una certa spesa. Serve la città dove i clienti spendono di più **per ordine**: lo scontrino medio (ticket medio), non il fatturato totale, che premia semplicemente le città con più ordini.

Il data frame `data` è già caricato. Raggruppa per città, calcola la media di `TotalAmount` e il numero di ordini, ordina per media decrescente e prendi il nome della prima. In RStudio guarda quanto sono vicine le prime tre: la differenza è abbastanza grande per decidere?

Regole:
- Lo **scontrino medio** (ticket medio) di una città è `mean(TotalAmount)` sui suoi ordini: non il fatturato totale, che premia le città grandi.
- Raggruppa per `City`, calcola media e numero di ordini, ordina per media decrescente, prendi il primo nome.
- In RStudio guarda quanto sono vicine le prime tre: la differenza è abbastanza grande da decidere qualcosa?

### Assenze per reparto — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/assenze-reparto/  
Obiettivo: Trovare il reparto con più giorni di assenza per addetto.  
Input: personale (data frame). Output: reparto_assenze (testo)

La direttrice del personale di un'azienda di servizi vuole capire in quale reparto il tema delle assenze pesa di più, per parlarne con il responsabile. Il primo conto che le hanno portato, i giorni di assenza totali per reparto, non la convince: le Vendite risultano prime, ma sono anche il reparto con più persone. Il confronto sensato è **per addetto**: i giorni di assenza di un reparto divisi per il numero di dipendenti di quel reparto.

Il data frame `personale` è già caricato (in RStudio: `read.csv("personale.csv")`): una riga per dipendente, con `reparto` e `giorni_assenza`. Il risultato che vuole è il nome del reparto con più giorni di assenza per addetto.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._
