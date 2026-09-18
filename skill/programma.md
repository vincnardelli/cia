# Programma del corso

Tre sezioni, dodici moduli, due lezioni da due ore a settimana (lunedì e venerdì, dal 14 settembre al 11 dicembre 2026). Il programma è una guida, non una gabbia: il modulo in cui si è arrivati in aula può differire.

## Sezione 1 — Il codice (R)

| mod. | titolo | idea | concetti introdotti | pagina |
|---|---|---|---|---|
| 1 | Partenza | Una macchina si istruisce in tre modi: dirglielo, mostrarle degli esempi, chiederglielo. In tutti e tre, a noi resta dire cosa vogliamo e controllare il risultato. | software 1.0, 2.0 e 3.0, linguaggi di programmazione, variabili, tipi di dato, operatori aritmetici, operatori di confronto, valori logici | https://www.vincnardelli.com/cia/modulo/01-partenza/ |
| 2 | Decidere | Il computer sceglie un ramo in base a una condizione. | if/else, else if, operatori logici, %in%, if annidati | https://www.vincnardelli.com/cia/modulo/02-decidere/ |
| 3 | Ripetere e astrarre | La stessa regola applicata a molti casi diventa un ciclo; incapsulata con un nome diventa una funzione. | vettori, indicizzazione, operazioni vettoriali, ciclo for, accumulatore, funzioni, test di una funzione | https://www.vincnardelli.com/cia/modulo/03-ripetere-e-astrarre/ |
| 4 | Dati | Una tabella è un insieme di vettori affiancati; con cinque verbi la interroghiamo senza cicli. | data frame, read.csv, fattori, valori mancanti, dplyr, pipe, group_by | https://www.vincnardelli.com/cia/modulo/04-dati/ |
| 5 | Leggere i dati | Una tabella si riassume con pochi numeri e pochi grafici; saperli leggere è più difficile che calcolarli. | media e mediana, quantili, deviazione standard, correlazione, ggplot2, case_when, ntile | https://www.vincnardelli.com/cia/modulo/05-leggere-i-dati/ |

## Sezione 2 — Come imparano le macchine (R → Python)

| mod. | titolo | idea | concetti introdotti | pagina |
|---|---|---|---|---|
| 6 | Software 2.0 | Le regole dell'autovelox non le scriviamo più noi: le trova un albero guardando gli esempi. | albero di classificazione, train/test, overfitting, confusion matrix, accuracy, deviance | https://www.vincnardelli.com/cia/modulo/06-software-2-0/ |
| 7 | Python per chi sa R | I concetti sono gli stessi, cambia la sintassi: i test dei lab non sanno in che linguaggio è scritta la soluzione. | Colab, liste, pandas | https://www.vincnardelli.com/cia/modulo/07-python/ |
| 8 | Random forest | Tanti alberi diversi che votano sbagliano meno di un albero solo. | random forest, cross-validation, importanza delle variabili, scikit-learn | https://www.vincnardelli.com/cia/modulo/08-random-forest/ |

## Sezione 3 — LLM e agenti (Python)

| mod. | titolo | idea | concetti introdotti | pagina |
|---|---|---|---|---|
| 9 | Da testo a numeri | Una macchina non legge: conta parole, poi impara a rappresentare un testo come un punto nello spazio. | bag of words, TF-IDF, tokenizzazione, embeddings, similarità coseno | https://www.vincnardelli.com/cia/modulo/09-da-testo-a-numeri/ |
| 10 | Il modello di linguaggio | Un LLM prevede il prossimo token; il prompt è il programma che gli diamo. | prossimo token, temperatura, allucinazioni, API, prompt come programma, output JSON | https://www.vincnardelli.com/cia/modulo/10-modello-di-linguaggio/ |
| 11 | Agenti | L'LLM ragiona, il codice calcola: un agente è un modello che decide quale funzione chiamare, la esegue e rilegge il risultato. | tool use, ciclo dell'agente, RAG, agenti negli IDE, rischi dell'AI | https://www.vincnardelli.com/cia/modulo/11-agenti/ |
| 12 | Chiusura | La tabella 1.0 / 2.0 / 3.0 della prima lezione, riletta con tutto il percorso alle spalle. |  | https://www.vincnardelli.com/cia/modulo/12-chiusura/ |

## Ordine dei costrutti

Se lo studente non dice a che punto è, deducilo dal codice che scrive. Ordine di apparizione: variabili e operatori → if/else → operatori logici e %in% → vettori e indicizzazione → ciclo for → funzioni → data frame e dplyr → ggplot2 → alberi (R) → Python e pandas → random forest → testi ed embeddings → API LLM → agenti.
