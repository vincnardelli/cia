---
layout: settimana
number: 10
title: Il modello di linguaggio
pillar: 3
language: Python
idea: "Un LLM prevede il prossimo token; il prompt è il programma che gli diamo."
hours: 5
dates: []
concepts_new: [prossimo token, temperatura, allucinazioni, API, prompt come programma, output JSON]
concepts_required: [tokenizzazione, embeddings, funzioni, random forest, Colab]
explorations: [temperatura]
slides_pdf:
---

## L'idea della settimana

Un modello di linguaggio fa una cosa sola: dato un testo, assegna una probabilità a ogni possibile **prossimo token** e ne sceglie uno. Ripetuto mille volte, produce una risposta. La **temperatura** regola quanto la scelta è prudente (sempre il token più probabile) o creativa (anche quelli improbabili). Il **contesto** è tutto ciò che il modello vede prima di rispondere; ciò che non c'è nel contesto e non c'è nel suo addestramento, lo inventa con la stessa sicurezza: sono le **allucinazioni**, la colonna «contro» del Software 3.0 nella tabella di settimana 1.

Si usa via **API**: una funzione che riceve messaggi e restituisce testo. Il **prompt è un programma**: un system prompt che fissa il ruolo e le regole, qualche esempio, e la richiesta di un **output JSON** per poter leggere la risposta con il codice invece che a occhio. Con il client OpenAI-compatibile, cambiare provider è cambiare `base_url`:

```python
from openai import OpenAI
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=chiave_groq)
```

## In aula

Prima chiamata API da Colab con la chiave Groq personale (gratuita, creata nella guida). Lab *classificare reclami con l'LLM*: lo stesso dataset testuale della settimana 9, classificato con un prompt invece che con la foresta, e confronto onesto su accuracy, costo per riga e spiegabilità. La foresta non spiega ma non inventa; l'LLM spiega ma può inventare.

## In piattaforma

Esplorazione interattiva della temperatura: la distribuzione del prossimo token che si appiattisce o si concentra. Estrazione strutturata da testo libero (fatture, annunci immobiliari) verso un data frame pandas, con il JSON come contratto. Sfida: far sbagliare l'LLM sui casi limite dell'IRPEF della settimana 2 e documentare perché sbaglia proprio lì.

## Per approfondire

I token e gli embeddings sono nella [settimana 9](09-da-testo-a-numeri). Nella [settimana 11](11-agenti) l'LLM smette di rispondere e basta: chiama le funzioni che avete scritto in settimana 3.
