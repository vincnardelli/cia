---
layout: modulo
number: 5
title: Delegare
sezione: 1
language: R
idea: "Il codice si può far scrivere all'AI, il problema no: se l'hai capito, deleghi la scrittura e tieni per te la specifica e la verifica."
hours: 3
concepts_new: [specifica prima del codice, skill del corso, modalità della skill, leggere il codice generato, verificare sui casi limite, registro AI]
concepts_required: [if/else, ciclo for, funzioni, test di una funzione]
explorations: []
---

## Quello che abbiamo capito scrivendo codice

Quattro moduli di codice scritto a mano, e quasi mai l'errore era di sintassi. Nell'autovelox era decidere se «non oltre 10» comprende il 10. Nel BMI era il paziente con BMI esattamente 25. Nel taxi era il minuto a 20 km/h esatti; nei due fornitori era capire che il problema non si risolve prodotto per prodotto. Ogni volta il lavoro vero è stato **capire il problema**: cosa entra, cosa esce, cosa succede su ogni confine. Tradurlo in R, una volta capito, era la parte facile.

Ed è proprio la parte che un modello di linguaggio fa bene. Scrive `if`, cicli e funzioni più in fretta di noi e senza errori di battitura. Quello che non può fare è decidere al posto nostro se il 10 è dentro o fuori: se la specifica è ambigua, sceglie una delle due strade con la stessa sicurezza con cui sceglierebbe l'altra. È la demo della prima lezione: la rata del mutuo a tasso zero, sbagliata con sicurezza.

## L'assunto di questo modulo

**Se hai capito il problema, puoi far scrivere il codice all'AI.** Se non l'hai capito, l'AI scrive con la stessa sicurezza la soluzione di un altro problema, e tu non te ne accorgi.

Per questo l'AI arriva adesso e non alla prima lezione: per delegare bisogna saper dire con precisione cosa si vuole e saper controllare il risultato. Sono le due cose che restano a noi, e i moduli 1–4 servivano a impararle.

## Il metodo, in quattro passi

1. **Specifica (tu).** Prima di aprire la chat scrivi input, output, regole e confini. Se non riesci a scriverli, il problema non è ancora capito: nessun prompt lo capirà al posto tuo.
2. **Chiedi (AI).** Dai la specifica, non «fammi l'esercizio». E chiedi prima le domande, poi il codice: l'AI è molto brava a trovare i buchi in un testo.
3. **Leggi (tu).** Ogni riga del codice generato: sai dire cosa fa? Se compare qualcosa che non hai mai visto (`ifelse`, `sapply`, `while`), chiedi di riscriverlo con quello che conosci o fattelo spiegare.
4. **Verifica (tu).** Esegui il codice in RStudio sui casi limite che hai scelto tu, uno per ogni confine. I casi proposti dall'AI aiutano, ma il risultato atteso lo calcoli tu.
{: .steps }

E tieni il **registro AI**: cosa hai chiesto, cosa ti ha dato, cosa hai controllato e cambiato. Non è burocrazia: è il modo per accorgerti di quanto del lavoro è rimasto tuo.

## La skill del corso

Un assistente generico risponde a tutto con la soluzione completa, spesso con costrutti che non conosci. La **skill del corso** è un insieme di istruzioni che lo trasforma in un tutor: conosce il programma fino a questo modulo, scrive nello stile delle lezioni, usa solo i costrutti visti in aula e ti fa sempre trovare i casi limite. Funziona su ChatGPT, Claude e Gemini.

[Come installarla e usarla]({{ site.baseurl }}/skill/){: .btn .btn-primary }

Si usa scrivendo la modalità come prima parola del messaggio:

| scrivi | quando | cosa fa |
|---|---|---|
| `assistito:` + la specifica | hai il problema, non il codice | analizza la specifica e ti fa le domande sui confini, poi propone la struttura e, se vuoi, il codice |
| `tutor:` + il tuo codice | hai una bozza | ti indica **un** problema alla volta, come domanda, con casi da provare; non riscrive il codice |
| `errore:` + il messaggio di R | R si lamenta | traduce l'errore e ti dice dove guardare |
| `spiega:` + un concetto | non ti è chiaro qualcosa | otto righe, un esempio, il rimando alla lezione |
| `shiny:` + le tue funzioni | vuoi un'app | costruisce l'app attorno alle tue funzioni, come il calcolatore BMI |
| `progetto:` + la tua idea | progetto 1 | ti aiuta a trovare un problema e a specificarlo, facendo il compagno che lo deve risolvere |

La modalità `tutor` non ti consegna la soluzione apposta: serve quando vuoi imparare. Quando hai capito e vuoi solo che il codice venga scritto, usa `assistito`, che passa dalla specifica.

## Un esempio dall'inizio alla fine

Un'azienda rimborsa ai dipendenti le trasferte in auto: 0,30 € al km fino a 100 km, 0,20 € per i km oltre i 100, più i pedaggi. C'è un tetto di 150 €.

**Passo 1, la specifica.** Scritta così, sembra completa. Si incolla nella chat con `assistito:` davanti.

**Passo 2, le domande.** La skill non scrive codice: risponde con «Ho capito così» e cinque punti da chiarire. 100 km esatti sono tutti a 0,30? Il tetto vale anche sui pedaggi? Con 0 km si rimborsano solo i pedaggi? Cosa succede con km negativi? A 700 km il rimborso è esattamente 150: si applica il tetto? Ognuna è una regola che mancava. Le risposte (sì; no, il tetto vale solo sui km; sì; dato sbagliato, risultato `NA`; 150 è dentro) sono decisioni tue, non dell'AI.

**Passo 3, il codice.** Con le risposte, il codice nello stile del corso:

```r
rimborso <- function(km, pedaggi){
  if(km < 0){
    return(NA)                              # km negativi: dato sbagliato
  }

  if(km <= 100){
    quota_km <- km * 0.30
  }else{
    quota_km <- 100 * 0.30 + (km - 100) * 0.20
  }

  if(quota_km > 150){
    quota_km <- 150                         # il tetto vale solo sui km
  }

  return(quota_km + pedaggi)
}
```

**Passo 4, la verifica.** Un caso per ogni confine, con il risultato atteso calcolato a mano prima di eseguire:

```r
rimborso(100, 0)    # atteso 30: 100 km esatti, tutti a 0,30
rimborso(101, 0)    # atteso 30.2
rimborso(0, 12)     # atteso 12: solo i pedaggi
rimborso(700, 0)    # atteso 150: esattamente sul tetto
rimborso(800, 10)   # atteso 160: tetto sui km, pedaggi per intero
rimborso(-5, 0)     # atteso NA
```

Il codice l'ha scritto l'AI; le cinque decisioni e i sei casi di prova sono tuoi. Se la specifica avesse detto «tetto di 150 € sul rimborso», senza dire se i pedaggi sono dentro, l'AI avrebbe scelto da sola, e `rimborso(800, 10)` avrebbe dato 150 o 160 a seconda del caso.

## Dove sbaglia l'AI: cosa controllare sempre

- **I confini.** `<` al posto di `<=`, «oltre» letto come «da». È l'errore più frequente e il codice gira lo stesso.
- **I casi che nessuno ha previsto.** Zero, negativi, un vettore vuoto: se la specifica non li nomina, l'AI li tratta a caso.
- **Costrutti fuori dal corso.** `ifelse`, `sapply`, pacchetti mai visti. Non sono sbagliati, ma se non sai leggerli non puoi verificarli.
- **Variabili prese da fuori.** Una funzione che usa una soglia definita fuori invece di riceverla come argomento: funziona finché qualcuno non cambia quella variabile.
- **`print` al posto di `return`.** La funzione sembra funzionare, ma il risultato non si può usare.
- **Numeri dichiarati senza eseguire.** «Il risultato è 42» scritto dall'AI non è un risultato: esegui e guarda.

## Per il progetto 1

Il [progetto 1]({{ site.baseurl }}/progetti/1/) è il posto giusto per mettere in pratica questo modulo: inventare un problema è proprio il passo 1, e la modalità `progetto:` della skill ti aiuta a trovare l'idea e a specificarla. L'AI è ammessa e incoraggiata; il registro AI va consegnato insieme al codice.

## Per approfondire

Le funzioni che farai scrivere all'AI sono quelle del [modulo 4](../04-astrarre/). Nel modulo 6 si passa dai vettori alle tabelle di dati: lo stesso metodo vale anche lì, e diventa ancora più importante, perché con migliaia di righe non si controlla a occhio.
