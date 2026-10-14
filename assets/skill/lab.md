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

Il prezzo di vendita è sempre più alto del costo di una pizza: se non lo fosse, ogni pizza venduta aggiungerebbe una perdita e il pareggio non arriverebbe mai. Qui questo caso non si presenta; per gestirlo servirebbe un `if`, che vedremo nel modulo 2.

Scrivi il programma che, dati costi fissi, prezzo e costo unitario, calcola il numero di pizze del pareggio. In R l'arrotondamento per eccesso all'intero si fa con `ceiling(x)`: `ceiling(12.1)` è 13, mentre `ceiling(12)` resta 12.

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
- Una variabile logica si può usare direttamente come condizione: `if(studente)` equivale a `if(studente == TRUE)`.

### Tariffa del parcheggio — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/parcheggio/  
Obiettivo: Calcolare quanto si paga all'uscita di un parcheggio a partire dai minuti di sosta.  
Input: minuti (numero). Output: costo (numero)

Il parcheggio del centro commerciale ha una cassa automatica e la società che lo gestisce ti chiede di riscrivere la regola che calcola l'importo all'uscita, perché quella vecchia sbagliava proprio sui casi che generano reclami.

La sosta è gratuita **fino a 30 minuti**. Oltre i 30 minuti si paga 1,50 euro **per ogni ora o frazione di ora**, contando dal momento dell'ingresso: chi resta 31 minuti paga una frazione della prima ora, cioè 1,50 euro; chi resta 61 minuti è già nella seconda ora e paga 3 euro; chi resta esattamente 60 minuti paga un'ora sola. C'è un **massimo giornaliero** di 12 euro, oltre il quale il contatore si ferma. Il parcheggio chiude la sera, quindi ogni sosta comincia e finisce nella stessa giornata: l'importo non supera mai i 12 euro.

Scrivi il programma che, dati i minuti di sosta, calcola l'importo. In R l'arrotondamento per eccesso all'intero si fa con `ceiling(x)`: `ceiling(12.1)` è 13, mentre `ceiling(12)` resta 12.

Regole:
- Fino a **30 minuti** la sosta è gratuita.
- Oltre i 30 minuti si paga **1,50 € per ogni ora o frazione di ora**, contando dall'ingresso: 31 minuti sono una frazione della prima ora, 61 minuti sono già due ore.
- `ceiling(x)` arrotonda per eccesso all'intero: `ceiling(12.1)` è 13, mentre `ceiling(12)` resta 12. Le ore da pagare sono `ceiling(minuti / 60)`.
- Il **massimo giornaliero** è 12 €. Le soste sono sempre **entro la stessa giornata** (si entra e si esce lo stesso giorno), quindi l'importo non supera mai 12 €.

### Penali sulle fatture — facile, R, AI-on
https://www.vincnardelli.com/cia/lab/penali-fatture/  
Obiettivo: Calcolare il totale di una fattura pagata in ritardo, applicando le penali previste.  
Input: importo (numero); giorni_ritardo (numero). Output: totale (numero)

Nell'ufficio amministrativo di una piccola azienda ti chiedono di automatizzare il calcolo delle **penali per ritardato pagamento** che vanno aggiunte alle fatture dei clienti in ritardo. Le condizioni sono scritte nel contratto standard: entro 10 giorni di ritardo non si applica nulla; da 11 a 30 giorni si aggiunge il 5% dell'importo; da 31 a 60 giorni il 10%; da 61 a 90 giorni il 20%; oltre i 90 giorni si applica il 20% **più un 2% dell'importo per ogni giorno oltre il novantesimo**. La penale però ha un **tetto**: non può mai superare il 50% dell'importo, e una volta arrivata lì smette di crescere.

Il programma riceve l'importo della fattura e i giorni di ritardo e restituisce il totale da pagare (importo più penale), con due decimali. I clienti litigano sempre sui giorni di confine, il decimo, il trentesimo, il novantesimo, e il giorno in cui si tocca il tetto: il tuo codice deve applicare esattamente ciò che dice il contratto.

Regole:
- entro 10 giorni di ritardo: nessuna penale;
- da 11 a 30 giorni: 5% dell'importo;
- da 31 a 60 giorni: 10%;
- da 61 a 90 giorni: 20%;
- oltre 90 giorni: 20% **più il 2% per ogni giorno oltre il 90°**;
- in ogni caso la penale **non può superare il 50%** dell'importo: raggiunto il tetto, smette di crescere.
- Arrotonda il totale a due decimali.

### IRPEF a confronto con uno scenario ipotetico — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/irpef/  
Obiettivo: Calcolare l'IRPEF lorda con gli scaglioni 2025 e con uno scenario ipotetico di riforma (inventato per l'esercizio), e la differenza tra le due.  
Input: reddito (numero). Output: differenza (numero)

Un commercialista vuole mostrare ai clienti, con un numero, quanto cambierebbe la loro IRPEF con una diversa scala di aliquote. Per l'esercizio usiamo uno **scenario ipotetico**, inventato a scopo didattico: **non è la legge**. Nella realtà la legge di bilancio 2026 ha cambiato una cosa sola, il secondo scaglione (da 28.001 a 50.000 €), sceso dal 35% al 33%.

Ti chiede un programma che, dato il reddito imponibile annuo, calcoli l'imposta lorda con gli scaglioni del 2025 e con quelli dello scenario, e metta in `differenza` l'imposta dello scenario meno quella del 2025: un numero negativo vuol dire che con lo scenario si paga meno.

L'IRPEF è **progressiva a scaglioni**: ogni aliquota si applica solo alla parte di reddito che cade in quella fascia, non all'intero reddito. Nel 2025 le fasce sono: fino a 15.000 € al 23%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 35%, oltre 50.000 al 43%. Nello scenario ipotetico: fino a 15.000 al 20%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 36%, da 50.001 a 75.000 al 40%, da 75.001 a 120.000 al 43%, oltre 120.000 al 46%.

Il commercialista userà il numero per decidere a chi mandare la newsletter, quindi la differenza va arrotondata a due decimali e deve essere esatta al centesimo: anche per un reddito con i centesimi, e per chi guadagna esattamente 15.000, 28.000 o 50.000 euro.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### ISEE semplificato — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/isee/  
Obiettivo: Calcolare un ISEE semplificato di una famiglia a partire da reddito, patrimonio e numero di componenti.  
Input: reddito (numero); patrimonio (numero); componenti (numero). Output: isee (numero)

Il CAF del quartiere è sommerso di richieste per le agevolazioni scolastiche, e ti chiede uno strumento che dia alle famiglie una **stima dell'ISEE** prima dell'appuntamento. È una versione semplificata, ma segue la logica vera dell'indicatore.

Si parte dall'ISE, l'indicatore della situazione economica: il reddito annuo della famiglia più il **20% del patrimonio** (conti, case, risparmi). Poi l'ISE si divide per una **scala di equivalenza** che tiene conto di quante persone vivono di quegli stessi soldi: un componente vale 1,00; due componenti 1,57; tre 2,04; quattro 2,46; cinque 2,85; e per ogni componente oltre il quinto si aggiungono 0,35 alla scala. Il risultato, l'ISEE, va arrotondato a due decimali.

Scrivi il programma che, dati reddito, patrimonio e numero di componenti, calcola l'ISEE. Le famiglie numerose sono quelle che più spesso hanno diritto alle agevolazioni: assicurati che la regola "oltre cinque" torni per sei, sette, otto persone.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

## Modulo 3

### Prodotti sotto scorta — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/sotto-scorta/  
Obiettivo: Contare quanti prodotti del magazzino sono scesi sotto la loro scorta minima e vanno riordinati.  
Input: giacenza (vettore di numeri); soglia (vettore di numeri). Output: da_riordinare (numero)

Il responsabile del magazzino di un negozio di ferramenta ha due elenchi, uno accanto all'altro: per ogni prodotto la **giacenza** (i pezzi sullo scaffale) e la **scorta minima** sotto la quale bisogna riordinare. Ogni lunedì li confronta a mano e conta quanti prodotti vanno riordinati, per sapere quante righe avrà l'ordine al fornitore.

I due elenchi sono due vettori della stessa lunghezza, nello stesso ordine: il prodotto in posizione 3 ha giacenza `giacenza[3]` e soglia `soglia[3]`. Un prodotto va riordinato se la giacenza è **strettamente sotto** la soglia: chi è esattamente alla soglia è ancora a posto.

Scrivi il programma che conta i prodotti da riordinare scorrendo i vettori con un ciclo e un contatore: parte da 0 e cresce di 1 ogni volta che trovi un prodotto sotto soglia.

Regole:
- I due vettori hanno la stessa lunghezza: il prodotto `i` ha giacenza `giacenza[i]` e soglia `soglia[i]`.
- Un prodotto va riordinato se la giacenza è **strettamente minore** della soglia: alla soglia esatta è ancora a posto.
- Scorri i prodotti con un ciclo `for` e usa un contatore: parte da 0 e cresce di 1 a ogni prodotto sotto soglia.

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

Contali con un ciclo e due contatori, uno per i promotori e uno per i detrattori, che partono da 0 e crescono di 1 a ogni voto della loro fascia.

Regole:
- I clienti con voto **9 o 10** sono *promotori*; quelli con voto **da 0 a 6** sono *detrattori*; 7 e 8 sono *passivi* e non contano.
- `NPS = (promotori − detrattori) / totale intervistati × 100`.
- Arrotonda a un decimale.
- Contali con un ciclo e due contatori, `promotori` e `detrattori`, che partono da 0 e crescono di 1 a ogni voto della loro fascia.

### Provvigioni dell'agente — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/provvigioni/  
Obiettivo: Calcolare le provvigioni annue di un agente di commercio a partire dal venduto di ciascun mese, con scaglioni progressivi.  
Input: vendite (vettore di numeri). Output: provvigioni (numero)

Un'azienda che vende macchine per il caffè ai bar paga i propri agenti a provvigione, con un contratto a **scaglioni progressivi calcolati mese per mese**: sul venduto di ogni mese, il 3% sulla parte fino a 10.000 euro, il 5% sulla parte tra 10.000 e 20.000, l'8% sulla parte oltre i 20.000. È lo stesso meccanismo dell'IRPEF: ogni aliquota si applica solo alla fetta che cade nella sua fascia, non a tutto il venduto.

Un agente con 25.000 euro di venduto in un mese prende quindi 300 sul primo scaglione, 500 sul secondo e 400 sul terzo; uno con 10.000 esatti prende 300 e basta. L'ufficio amministrazione ti passa il vettore del venduto dei dodici mesi di un agente e vuole le provvigioni dell'anno, con due decimali. Si arrotonda una volta sola, il **totale dell'anno**: le provvigioni dei singoli mesi si sommano senza arrotondarle.

Prima di scrivere codice, scrivi tu la specifica con i casi al confine (10.000 esatti, 20.000 esatti, un mese a zero), poi ragiona su come applicare la regola a un mese, e infine ripetila con un ciclo.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

## Modulo 4

### Sconto fedeltà — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/sconto-fedelta/  
Obiettivo: Scrivere la specifica e il codice di un programma fedeltà come funzione `totale_scontato(totale_carrello, tessera)`: sconto a soglie più bonus tessera, con un tetto massimo.  
Input: totale_carrello (numero); tessera (testo). Output: totale_scontato (numero) — funzione `totale_scontato`

Una catena di negozi di abbigliamento lancia il nuovo programma fedeltà e ti chiede di scrivere il calcolo dello **sconto alla cassa**. La direzione marketing ti ha spiegato le regole a voce, in riunione, e questa è la tua trascrizione.

Lo sconto base dipende da quanto si spende: niente sconto sotto i 100 euro, il 5% da 100 euro in su, il 10% da 250 euro in su. Chi ha la tessera fedeltà ha un **bonus** che si somma in punti percentuali: la tessera silver aggiunge 2 punti, la gold 7, chi non ha tessera non aggiunge nulla. Lo sconto complessivo, base più bonus, **non può in nessun caso superare il 15%**: un cliente gold da 300 euro avrebbe 10 + 7 = 17, ma paga con il 15%.

Le casse dei negozi useranno il calcolo migliaia di volte al giorno, quindi va scritto come **funzione**: `totale_scontato(totale_carrello, tessera)` riceve la spesa e la tessera ("silver", "gold" o "nessuna"), in quest'ordine, e con `return()` restituisce il prezzo finale arrotondato a due decimali. Prima di scrivere codice, scrivi tu la specifica completa, con i casi limite (100 euro esatti, 250 esatti, il tetto del 15%), e passala all'assistente in modalità *aiutami a partire*.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### Visite fuori tempo massimo — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/visite-fuori-tempo/  
Obiettivo: Scrivere una funzione che riceve i giorni di attesa delle visite e il tempo massimo previsto, seleziona con le parentesi quadre quelle fuori tempo e restituisce la loro percentuale.  
Input: attese (vettore di numeri); limite (numero). Output: percentuale (numero) — funzione `percentuale_fuori_tempo`

Il Piano nazionale di governo delle liste d'attesa fissa un **tempo massimo** per ogni classe di priorità della ricetta: una visita con priorità B va fatta entro 10 giorni, una D (differibile) entro 30, una P (programmata) entro 120. L'ufficio qualità di un'azienda sanitaria deve dire alla Regione, ogni mese, quale percentuale delle visite prenotate è finita oltre il tempo massimo.

Per ogni classe di priorità l'ufficio estrae dal sistema di prenotazione un vettore con i giorni di attesa di ciascuna visita. Una visita fatta a 30 giorni con un limite di 30 è **in tempo**; a 31 giorni è fuori tempo. La percentuale si dà con un decimale.

Il calcolo va ripetuto per ogni classe e ogni mese, cambiando solo il vettore e il limite: scrivi la funzione `percentuale_fuori_tempo(attese, limite)`, che seleziona le attese fuori tempo con le parentesi quadre e restituisce la percentuale. La verifica chiama la tua funzione con i valori di ogni caso.

Regole:
- Una visita è **in tempo** se l'attesa è minore o uguale al limite: a `limite` giorni esatti è ancora in tempo. È **fuori tempo** se l'attesa è **strettamente maggiore** del limite.
- Dentro la funzione seleziona le attese fuori tempo con le parentesi quadre e un vettore logico: `attese[attese > limite]` tiene solo quelle.
- `length()` di quel vettore dice quante sono; `length(attese)` dice quante sono le visite in tutto.
- La percentuale è `100 * fuori tempo / tutte`, arrotondata a **1 decimale** con `round(..., 1)`.
- Il limite arriva come argomento: la funzione non deve usare variabili scritte fuori, e deve **restituire** il numero con `return()`.

### Promemoria di rinnovo — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/promemoria-rinnovo/  
Obiettivo: Scrivere una funzione che conta a quanti soci con l'abbonamento in scadenza va mandato il promemoria, escludendo chi ha già rinnovato e chi ha chiesto di non essere contattato, con %in% e !.  
Input: in_scadenza (vettore di testi); rinnovati (vettore di testi); non_contattare (vettore di testi). Output: messaggi (numero) — funzione `promemoria`

Una catena di palestre manda ogni mese un messaggio ai soci con l'abbonamento **in scadenza**, per ricordare di rinnovarlo. Il messaggio però non va mandato a tutti: chi ha **già rinnovato** in anticipo si irrita a ricevere il sollecito, e chi ha **negato il consenso** ai messaggi commerciali non può essere contattato, per legge.

Dal gestionale escono tre elenchi di codici tessera: i soci in scadenza questo mese, i soci che hanno già rinnovato (anche in anticipo di mesi, quindi non tutti sono in scadenza) e i soci che non vogliono essere contattati. Il responsabile marketing vuole sapere **quanti messaggi** partiranno, per comprare il pacchetto di SMS giusto.

Scrivi la funzione `promemoria(in_scadenza, rinnovati, non_contattare)` che restituisce quanti soci vanno avvisati, usando `%in%` per sapere se un codice è in un elenco e `!` per tenere quelli che non ci sono. La verifica chiama la tua funzione con gli elenchi di ogni caso.

Regole:
- Un socio riceve il promemoria se è in `in_scadenza`, **non** è in `rinnovati` **e** **non** è in `non_contattare`. Basta essere in uno dei due elenchi per essere escluso.
- `in_scadenza %in% rinnovati` dà un `TRUE` per ogni socio che ha già rinnovato; `!` rovescia i `TRUE` in `FALSE` e viceversa.
- Gli elenchi `rinnovati` e `non_contattare` possono contenere anche codici che non sono in scadenza: non contano.
- Puoi selezionare i soci da avvisare con le parentesi quadre e contarli con `length()`, oppure scorrere `in_scadenza` con un ciclo `for` e un contatore.
- La funzione restituisce il numero con `return()`.

### Rimborso della trasferta — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/rimborso-trasferta/  
Obiettivo: Scrivere una funzione che calcola il rimborso di una nota spese di trasferta, escludendo le spese non rimborsabili, con un massimo per ogni pasto e un tetto per giorno.  
Input: categorie (vettore di testi); importi (vettore di numeri); giorni (numero). Output: rimborso (numero) — funzione `rimborso_trasferta`

L'ufficio amministrazione di una società di consulenza rimborsa ai dipendenti le spese delle trasferte di lavoro. Ogni nota spese arriva come due elenchi della stessa lunghezza, uno accanto all'altro: la **categoria** di ciascuna spesa ("treno", "aereo", "taxi", "hotel", "pasto", "minibar"…) e il suo **importo** in euro, più la durata della trasferta in giorni.

Il regolamento aziendale dice tre cose. Le spese della categoria "minibar", "alcolici" e "multa" **non si rimborsano mai**. Un "pasto" si rimborsa **fino a 30 euro**: un pranzo da 42 euro vale 30, uno da 30 esatti o meno vale quello che è costato; il limite è per ogni singolo pasto, non sul totale dei pasti. Tutte le altre spese si rimborsano per intero. Infine c'è un **tetto complessivo di 150 euro per ogni giorno** di trasferta: se le spese rimborsabili lo superano, si rimborsa il tetto; se ci arrivano esatte, si rimborsano tutte.

Scrivi la funzione `rimborso_trasferta(categorie, importi, giorni)` che restituisce gli euro da rimborsare, con due decimali. Ti serve `%in%` per riconoscere le categorie escluse e `!` per tenere le altre. Prima di scrivere codice, scrivi tu la specifica con i casi al confine: un pasto da 30 euro esatti, una nota fatta solo di spese escluse, una nota che arriva esattamente al tetto.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### Preventivo del noleggio — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/preventivo-noleggio/  
Obiettivo: Scomporre il preventivo di un noleggio auto in tre funzioni piccole (giorni, chilometri, supplemento per i giovani) e scrivere la funzione principale che le usa.  
Input: giorni (numero); km (numero); eta (numero). Output: totale (numero) — funzione `preventivo`

Un'agenzia di noleggio auto vuole che il sito mostri subito il **preventivo** a chi indica quanti giorni gli serve l'auto, quanti chilometri pensa di fare e quanti anni ha. Il listino ha tre voci, e il responsabile commerciale le cambia spesso, una alla volta: per questo vuole il codice diviso in **una funzione per voce**, da provare e correggere separatamente, più una funzione principale che le somma.

Le voci sono queste. Il **noleggio** costa 45 euro al giorno; da 7 giorni in su, 7 compreso, scatta la tariffa settimanale e tutti i giorni costano 38 euro. I **chilometri**: sono inclusi 200 km per ogni giorno di noleggio (tre giorni, 600 km inclusi), e ogni chilometro oltre quelli inclusi costa 0,25 euro. Il **supplemento giovani**: se il conducente ha meno di 25 anni si pagano 12 euro in più per ogni giorno; con 25 anni compiuti non si paga.

Scrivi tre funzioni piccole, `costo_giorni(giorni)`, `costo_km(km, giorni)` e `supplemento_giovane(eta, giorni)`, e la funzione principale `preventivo(giorni, km, eta)` che le chiama e restituisce la somma con due decimali. La verifica chiama solo `preventivo()`, ma provala anche voce per voce: ognuna delle tre funzioni deve ricevere come argomenti tutto quello che le serve, giorni compresi.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._

### Piano di rientro — facile, R, AI-off
https://www.vincnardelli.com/cia/lab/piano-di-rientro/  
Obiettivo: Scrivere una funzione ricorsiva che conta quante rate mensili servono per saldare un debito, con il caso base quando il debito è finito.  
Input: debito (numero); rata (numero). Output: rate (numero) — funzione `numero_rate`

Un condomino è rimasto indietro con le spese condominiali e l'amministratore gli propone un **piano di rientro**: il debito arretrato si paga a rate mensili di importo fisso, scelto dal condomino in base a quanto può permettersi, senza interessi. L'ultima rata paga solo quello che resta, quindi può essere più piccola delle altre.

L'amministratore deve scrivere nella delibera **quante rate** servono. Con 1.000 euro di debito e rate da 250 ne servono 4; con rate da 300 ne servono comunque 4 (300, 300, 300 e infine 100). Con un debito di zero non serve nessuna rata.

Scrivi la funzione **ricorsiva** `numero_rate(debito, rata)`: se il debito è finito restituisce 0, altrimenti conta una rata e richiama sé stessa sul debito che resta. Attenzione al caso base: deve fermare la funzione anche quando il debito scende sotto zero. La verifica chiama la tua funzione con i valori di ogni caso.

Regole:
- **Caso base**: se il debito è **minore o uguale a zero** non c'è più niente da pagare, e le rate che restano sono **0**. Con 1000 € e rate da 300 € il debito passa da 100 a -200: non vale mai zero esatto, e il caso base deve fermarlo lo stesso.
- **Passo**: altrimenti si paga una rata adesso, e le rate sono **una più** quelle che servono per il debito che resta (`debito - rata`), calcolate richiamando la funzione stessa.
- L'ultima rata può essere più piccola delle altre (paga solo il residuo), ma conta come una rata.
- Niente ciclo: la funzione chiama sé stessa. Entrambi i rami restituiscono il numero con `return()`.

### Progetti da finanziare — difficile, R, AI-on
https://www.vincnardelli.com/cia/lab/progetti-da-finanziare/  
Obiettivo: Scegliere quali progetti finanziare con un budget fisso per raggiungere più persone possibile, provando tutte le combinazioni con una funzione ricorsiva.  
Input: budget (numero); costi (vettore di numeri); persone (vettore di numeri). Output: raggiunte (numero) — funzione `persone_massime`

La fondazione di una banca locale ha un bando per progetti sociali sul territorio: doposcuola, assistenza agli anziani, corsi di lingua per stranieri. Ogni progetto arrivato in commissione ha un **costo** (in migliaia di euro) e una stima delle **persone** che raggiungerà. Un progetto si finanzia per intero o non si finanzia: non esistono mezzi progetti. La somma dei costi dei progetti scelti deve stare **dentro il budget**, che può anche avanzare; se i costi arrivano esattamente al budget, la combinazione va bene.

La commissione vuole sapere qual è il **numero massimo di persone** che si possono raggiungere con il budget disponibile. Scegliere a occhio non funziona: con 100 mila euro e tre progetti da 70, 50 e 40 mila, il più grande (400 persone) lascia fuori gli altri due, mentre 50 + 40 ne raggiungono 490. Se nessun progetto entra nel budget, la risposta è 0.

Scrivi la funzione `persone_massime(budget, costi, persone)`. Lo schema è quello dei due fornitori: una funzione `valuta(scelte, budget, costi, persone)` che riceve un vettore di `TRUE`/`FALSE`, uno per progetto, e restituisce le persone raggiunte (0 se la spesa supera il budget); una funzione ricorsiva `migliore(scelte, budget, costi, persone)` che aggiunge una scelta alla volta, una volta `TRUE` e una volta `FALSE`, con il caso base quando le scelte sono tante quanti i progetti, e tiene il risultato più grande con `max(a, b)`, che restituisce il maggiore fra due numeri; infine `persone_massime` che chiama `migliore` partendo da `c()`, nessuna scelta fatta. Ricorda che `costi[scelte]` con un vettore logico tiene solo i progetti finanziati.

_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._
