---
layout: settimana
number: 1
title: Partenza
pillar: 1
language: R
idea: "Il computer esegue istruzioni esplicite: prima di scriverle, impariamo a leggere i numeri e a dire al computer cosa calcolare."
hours: 5
dates: []
concepts_new: [variabili, tipi di dato, operatori aritmetici, operatori di confronto, valori logici]
concepts_required: []
explorations: []
slides_pdf:
---

## Perché iniziamo dai numeri e non dal codice

Hans Rosling, medico e statistico svedese, apre *Factfulness* con una frase che vale per tutto il corso: «il mondo non si può capire senza i numeri, ma non si può capire con i numeri soltanto». Il codice che scriveremo serve a far parlare i numeri; capire cosa dicono resta compito nostro.

Prendiamo l'aspettativa di vita. Nel 2007 in Burundi era di 50 anni. Vuol dire che nessuno invecchia? Guardiamo cinque neonati: Pierre vive 1 anno, Liz 36, Jean 57, Ann 72, Sarah 84. La media è (1 + 36 + 57 + 72 + 84) / 5 = 50. Due su cinque superano i 70 anni. In Svezia, stesso anno, l'aspettativa era di 81 anni: 63, 77, 84, 88, 93. Nessuno muore da bambino. La differenza tra i due paesi non è che «tutti gli svedesi vivono 31 anni in più»: è che un burundese su cinque muore nell'infanzia e trascina giù la media. Chi supera l'infanzia in Burundi vive quasi quanto uno svedese. **L'aspettativa di vita è una media**, e una media da sola nasconde la distribuzione.

Secondo esempio, tratto da una tesi triennale di questo corso: il gender pay gap. Nel 2025 quattro testate riportavano quattro numeri diversi (5,6 %, 10,4 %, «non cambia niente», −4,3 % per le laureate). Nessuno mentiva: cambiava la metrica (oraria o annua), chi era incluso, come si aggregava. Nel part-time il gap si riduce o si inverte; nel full-time dei settori professionali aumenta. Con un'aggregazione puoi dire A, con un'altra B: è il **paradosso di Simpson**, e lo ritroveremo quando faremo `group_by` in settimana 4. Corollario: correlazione non è causazione (il sito *spurious correlations* di Tyler Vigen è la collezione più divertente di questo errore).

## La mappa del corso: Software 1.0, 2.0, 3.0

Il problema è sempre lo stesso: lo studente ha preso 21, ha superato l'esame? Ci sono tre modi di farlo risolvere a una macchina.

| | Software 1.0 (dal 1940) | Software 2.0 (dal 2010) | Software 3.0 (dal 2025) |
|---|---|---|---|
| Input | dati strutturati (`voto = 21`) | tanti esempi storici | un prompt in italiano |
| Logica | regole esplicite scritte da noi | regole apprese dai dati | conoscenza pregressa + contesto |
| Esempio | `if(voto >= 18) "Promosso"` | il modello impara la soglia dai voti passati | «Ha preso 21 a Statistica, è promosso?» → ragiona: trentesimi, sufficienza 18, 21 > 18 → sì |
| Pro | controllo totale, prevedibile | affronta problemi complessi | flessibile, accessibile a tutti |
| Contro | rigido | scatola nera, servono dati | non deterministico, allucina |

Questa tabella è il corso intero. Settimane 1–5: scrivi tu le regole (colonna 1). Settimane 6–8: le regole le impara la macchina dai numeri (colonna 2). Settimane 9–12: le impara dai testi e può usare quelle che hai scritto tu (colonna 3). In settimana 12 torneremo su questa stessa tabella con tutto il percorso alle spalle.

> **In aula** abbiamo fatto una demo: un assistente AI ha risolto uno dei lab del corso in dieci secondi, e i test della piattaforma lo hanno bocciato su un caso limite. Il codice era plausibile, elegante e sbagliato. Da questa scena nasce il metodo del corso: *specificare con precisione, verificare con i casi limite*.

## Il patto sull'uso dell'AI

L'AI è **ammessa** e incoraggiata su lab e progetti. Ogni output va **verificato** con i test. Ogni uso va **dichiarato** (nel progetto c'è un registro AI). All'orale si deve saper spiegare ogni riga del proprio codice: quello è il momento senza tecnologia. Non si può superare il corso affidandosi all'AI, ma non si può neanche ignorarla: la sintassi la produce l'assistente, la responsabilità del risultato resta vostra.

## Perché programmare e non cliccare

Excel si impara in un pomeriggio, R in qualche settimana. Perché allora un linguaggio? Perché cliccare non lascia traccia: un'analisi fatta a mano non si ripete, non si controlla, non si mette in produzione. Uno script è **riproducibile**: chiunque lo rilegge, lo riesegue, trova l'errore. R è gratuito, open source, ha migliaia di pacchetti e una comunità enorme; è il linguaggio della statistica e della ricerca. Python lo incontreremo dalla settimana 7, quando servirà per il machine learning e per gli LLM.

## Le prime istruzioni

Apriamo RStudio. La console esegue una riga alla volta: scriviamo `1 + 2` e otteniamo `3`. Il computer è una calcolatrice che ricorda. Per farlo ricordare usiamo l'**assegnazione**:

```r
risultato <- 2 * 2
risultato
risultato <- risultato + 3
risultato
```

La freccia `<-` mette a destra il valore e a sinistra il nome. Il nome è una **variabile**: una scatola con un'etichetta. La terza riga si legge «il nuovo `risultato` è il vecchio `risultato` più 3», e vale 7. R accetta anche `=`, ma nel corso usiamo sempre `<-`, come negli script che troverete in piattaforma.

Le variabili hanno un **tipo**. I numeri si scrivono col punto decimale (`3.14`, non `3,14`). Il testo va tra virgolette:

```r
prezzo <- 19.99
nome_cliente <- "Giorgio"
class(prezzo)
class(nome_cliente)
```

`class()` risponde `"numeric"` e `"character"`. I nomi delle variabili sono in italiano, in minuscolo, con il trattino basso per separare le parole; R distingue le maiuscole, quindi `nome_cliente`, `NomeCliente` e `nomecliente` sono tre variabili diverse.

## Aritmetica: lo scontrino

Con quattro operatori (`+ - * /`, più `^` per la potenza) si fa già un lavoro vero. Prendiamo un prezzo netto e calcoliamo IVA e totale:

```r
prezzo_netto <- 100
aliquota_iva <- 0.22

iva <- prezzo_netto * aliquota_iva
totale <- prezzo_netto + iva
totale_arrotondato <- round(totale, 2)

print(paste0("Totale: ", totale_arrotondato, " euro"))
```

`round(x, 2)` arrotonda a due decimali; `paste0` incolla testo e numeri senza spazi; `print` li mostra. Provate a cambiare `prezzo_netto` in `33.33` e rieseguite tutto: è la prima forma di automazione.

> **Attenzione** `round(2.5)` in R dà 2, non 3: quando la cifra è esattamente a metà, R arrotonda al pari (0.5 → 0, 1.5 → 2, 2.5 → 2). Su uno scontrino da 0,005 euro non importa; su un milione di righe di fatturazione sì. È il primo caso limite del corso: si trova solo provando il valore esatto sul confine.

## Confronti: la macchina risponde vero o falso

La terza cosa che il computer sa fare, oltre a ricordare e calcolare, è **confrontare**:

```r
1 == 1
1 == 2
18 > 12
voto <- 21
voto >= 18
```

Le risposte sono `TRUE`, `FALSE`, `TRUE`, `TRUE`. Questi due valori sono un tipo a sé, il tipo **logico**. Gli operatori di confronto sono `==` (uguale), `!=` (diverso), `<`, `>`, `<=`, `>=`. Il risultato di un confronto si può salvare in una variabile come qualunque altro valore:

```r
promosso <- voto >= 18
promosso
```

Questa riga è il seme della prossima settimana: quando avremo un `TRUE` o un `FALSE`, potremo far scegliere al computer cosa fare.

> **Attenzione** `=` e `==` sono due cose diverse: il primo assegna, il secondo confronta. Scrivere `voto = 18` quando volevate chiedere «il voto è 18?» non dà errore: sovrascrive silenziosamente il voto. Seconda trappola: `0.1 + 0.2 == 0.3` è `FALSE`, perché il computer rappresenta i decimali con un'approssimazione. Per confrontare importi in euro si arrotonda prima, oppure si lavora in centesimi.

## Per approfondire

Le guide del sito spiegano come installare R e RStudio e come usare console, script e ambiente. Il lab in piattaforma sull'interesse composto è il primo in cui provate il ciclo *specifica → genera → testa* con l'assistente. La [settimana 2](02-decidere) usa i confronti di oggi per far prendere decisioni al computer.
