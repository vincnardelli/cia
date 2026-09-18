---
layout: modulo
number: 1
title: Partenza
sezione: 1
language: R
idea: "Dalle istruzioni scritte a mano ai prompt: tre modi di far lavorare una macchina, e in tutti il controllo resta a noi."
hours: 4
concepts_new: ["software 1.0, 2.0 e 3.0", linguaggi di programmazione, variabili, tipi di dato, operatori aritmetici, operatori di confronto, valori logici]
concepts_required: []
explorations: []
slides_pdf:
slides:
  - titolo: Lezione 1
    descr: Introduzione
    pdf: slide/lezione_1.pdf
  - titolo: Lezione 2
    descr: Linguaggi e software
    pdf: slide/lezione_2.pdf
---

## Paura, e poche competenze

Sui giornali l'AI arriva soprattutto come una minaccia. Eppure in Italia la usa il 16% delle imprese con almeno 10 addetti, contro il 20% della media europea. Il motivo principale per cui le imprese la scartano: **mancano le competenze** (Banca d'Italia, dati Eurostat).

Chi la usa senza conoscerla sbaglia. A Firenze un avvocato deposita in tribunale sentenze della Cassazione inventate da ChatGPT; in Australia Deloitte consegna al governo un rapporto con studi che non esistono. Si chiama **allucinazione**: un testo che sembra vero ed è inventato. Non è mancato lo strumento, è mancato chi controllasse. E la usiamo tutti: il 94% degli studenti, e tra chi si fida di più il 55% non controlla mai le risposte.

## Cosa resta da fare a noi

Se l'AI sa già fare tutto, cosa resta a noi? Delegare non vuol dire sparire. Del commercialista non vediamo come lavora, giudichiamo il risultato, e se sbaglia la multa arriva a noi. L'AI è un commercialista bravissimo e quasi gratuito, ma senza albo e senza responsabilità. A chi delega restano tre passaggi: **dire cosa fare, controllare il risultato, firmare**. E per controllare bisogna capire.

## Il prezzo della delega

- Negli Stati Uniti, dopo ChatGPT, l'occupazione scende solo per chi ha 22–25 anni e lavora dove l'AI è più usata: assunzioni che non ci sono state (Stanford).
- Per la Banca d'Italia i contabili sono sostituibili, gli specialisti di economia complementari. La differenza non è il titolo di studio: nei primi si applicano procedure, nei secondi si capisce la situazione e si decide.
- In un esperimento con 758 consulenti, l'AI migliora il lavoro dove è brava e lo peggiora dove sbaglia: lì le risposte giuste scendono dall'84,5% al 70,6%. Più fiducia, meno controllo.
- La competenza più richiesta dalle imprese è il pensiero analitico, non l'AI (World Economic Forum).

## Tre modi di far fare qualcosa a una macchina

La risposta è **controllo e pensiero critico**. Una macchina si istruisce in tre modi, le tre epoche del software (1.0, 2.0, 3.0), e in tutti e tre interveniamo due volte: prima diciamo cosa vogliamo, dopo controlliamo e firmiamo.

1. **Dirglielo** (moduli 1–5, R). Scriviamo noi le istruzioni, senza poter essere vaghi, e le proviamo su casi di cui conosciamo la risposta, soprattutto i casi limite. Ogni analisi che riceveremo sarà fatta di codice: chi non sa leggerlo può solo fidarsi.
2. **Mostrarle degli esempi** (moduli 6–8, R poi Python). La regola la trova la macchina, ma nei dati che le diamo, e i dati ingannano. La correlazione: petrolio consumato in Italia e divorzi in Texas scendono insieme per vent'anni, senza nessun legame. La media: in Burundi si viveva in media 50 anni, ma due bambini su cinque superavano i 70 (Hans Rosling, *Factfulness*). L'aggregazione: il divario salariale tra donne e uomini è 5,6%, 10,4% o 39,9% a seconda di cosa si conta, e sono tutti numeri veri. La domanda da fare sempre: su quali dati l'hai provata?
3. **Chiederglielo** (moduli 9–12, Python). Diamo una domanda e gli strumenti per rispondere, poi verifichiamo con i nostri. Un modello di linguaggio fa una cosa sola: prevede quale pezzo di testo viene dopo. Per questo la risposta sembra giusta anche quando è sbagliata. In aula lo proviamo chiedendo a un assistente la rata di un mutuo a tasso zero.

## I linguaggi di programmazione

Quale linguaggio conviene imparare? Secondo l'indice PYPL, che misura quanto si cercano su Google i tutorial di ciascun linguaggio, a settembre 2026 **Python** vale da solo più di metà delle ricerche (52%) ed è in forte crescita dal 2025; **R** è intorno al 4%, in calo dopo il picco di inizio 2026. Nel corso li usiamo entrambi: R per imparare a scrivere le regole e a leggere i dati, Python per l'apprendimento automatico e i modelli di linguaggio.

Attenzione a non confondere il **linguaggio** con l'**IDE** (*integrated development environment*). Il linguaggio è il motore: R, Python. L'IDE è il cruscotto, il programma in cui scriviamo ed eseguiamo il codice: RStudio per R; Colab, Jupyter, VS Code, PyCharm o Spyder per Python. Oggi si aggiunge un cruscotto nuovo, gli **agenti**: Cursor, Google Antigravity, Claude Code non si limitano a suggerire, leggono il progetto, scrivono il codice, lo eseguono e correggono gli errori. Il linguaggio resta il motore, e il controllo resta a noi.

Ma il linguaggio di programmazione più usato dei prossimi anni sarà un altro: **l'inglese** (o l'italiano, se preferite). Con i modelli di linguaggio le istruzioni si danno in lingua naturale.

## Tre epoche del software, un solo esempio

Lo stesso problema, lo studente ha preso 21, ha superato l'esame?, risolto in tre modi.

| | Software 1.0 (dal 1940) | Software 2.0 (dal 2010) | Software 3.0 (dal 2025) |
|---|---|---|---|
| Come | **coding**: istruzioni esplicite | **machine learning**: la regola si impara dai dati | **LLM**: il prompt è il programma |
| Input | dati strutturati (`voto = 21`) | tanti esempi storici (voti, ore di studio…) | una domanda in linguaggio naturale |
| Pro | pieno controllo, prevedibile, facile da correggere | adatto a problemi complessi, migliora con più dati | flessibilissimo, accessibile a chi non programma |
| Contro | rigido, non si adatta a casi non previsti | scatola nera, servono molti dati | non deterministico, allucinazioni, dipende dal prompt |

Nel Software 1.0 la regola la scriviamo noi:

```r
voto <- 21
if (voto >= 18) {
  status <- "Promosso"
} else {
  status <- "Bocciato"
}
```

Nel Software 2.0 un modello guarda lo storico degli studenti e impara a prevedere l'esito. Nel Software 3.0 scriviamo la domanda in italiano, e il modello ragiona: in Italia i voti sono in trentesimi, la sufficienza è 18, 21 è più di 18, quindi l'esame è superato. In tutti e tre i casi la risposta va controllata: sono i tre blocchi del corso.

## Le regole del corso

L'AI nel corso è ammessa e incoraggiata. Ogni risultato va controllato, ogni uso va dichiarato, ogni riga va spiegata. Delegare è comodo, e non è sbagliato. Ma non è gratis: il prezzo è capire come funziona.

Per iniziare installa R e RStudio seguendo le [guide]({{ site.baseurl }}/guide/).{% if site.mostra_lab %} I lab qui sotto sono i primi passi in R: variabili, calcoli e confronti.{% endif %}
