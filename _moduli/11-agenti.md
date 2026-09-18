---
layout: modulo
number: 11
title: Agenti
sezione: 3
language: Python
idea: "L'LLM ragiona, il codice calcola: un agente è un modello che decide quale funzione chiamare, la esegue e rilegge il risultato."
hours: 4
published: false
concepts_new: [tool use, ciclo dell'agente, RAG, agenti negli IDE, rischi dell'AI]
concepts_required: [funzioni, API, prompt come programma, output JSON, embeddings, pandas]
explorations: []
slides_pdf:
---

## L'idea del modulo

Chiedete a un LLM «sono passato a 95 in un tratto a 50, quanto pago?». Senza strumenti risponde con un numero plausibile, spesso sbagliato. Con il **tool use** gli descriviamo la funzione `multa(velocita, limite)` del modulo 3: il modello capisce che serve, la chiama con gli argomenti giusti, riceve 370 e lo mette nella frase. L'LLM ha fatto la parte che sa fare (capire la domanda, scegliere lo strumento), il codice ha fatto la sua (calcolare esattamente). Se la funzione ha un bug, l'agente lo eredita e lo ripete con sicurezza: gli strumenti vanno testati come i lab.

Il **ciclo dell'agente** sta in venti righe: osserva la richiesta, decide quale strumento chiamare, esegue, rilegge il risultato, ripete finché non ha finito.

```python
while True:
    risposta = chiedi_al_modello(messaggi, strumenti)
    if risposta.tool_calls is None:
        break
    for chiamata in risposta.tool_calls:
        risultato = esegui(chiamata)
        messaggi.append(risultato)
```

## In aula

`multa()`, `bmi()` e `rata()` esposte come tool, e la stessa domanda con e senza strumenti per vedere l'allucinazione. Il ciclo scritto a mano. L'agente in VS Code con Copilot che risolve un lab del corso, con i test della piattaforma a giudicare se ha ragione: l'agente è uno studente in più e vale la stessa regola di verifica. Un'ora su bias, privacy, allucinazioni in produzione e AI Act per chi lavorerà in azienda.

## In piattaforma

Un agente che risponde a domande di business su un dataset chiamando funzioni pandas («quanti clienti in churn nel segmento X?»). **RAG minimo**: embeddings delle lezioni del corso (modulo 9), recupero dei paragrafi più vicini alla domanda, risposta: in venti righe costruite il tutor che avete usato tutto il semestre. Un agente che traduce un lab intero da R a Python. Sfida: valutare un agente con una batteria di casi, esattamente come si valutavano i lab.

## Per approfondire

Le funzioni che diventano strumenti sono nel [modulo 3](03-ripetere-e-astrarre); la chiamata API e il JSON nel [modulo 10](10-modello-di-linguaggio). Il [modulo 12](12-chiusura) chiude il cerchio.
