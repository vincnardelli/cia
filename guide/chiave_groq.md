---
layout: page
title: La chiave API (Groq)
permalink: /guide/chiave_groq
parent: Guide
nav_order: 5
---

# 🔑 La chiave API per gli LLM

Dalla settimana 10 chiamiamo un modello di linguaggio dal codice. Serve una **chiave API personale**: usiamo Groq, che ha un piano gratuito senza carta di credito e non usa i tuoi dati per addestrare modelli.

1. Vai su [console.groq.com](https://console.groq.com) e crea un account (basta l'email).
2. **API Keys → Create API Key**, dai un nome (es. `corso`) e copia la chiave: si vede una sola volta.
3. Su Colab, nel pannello a sinistra apri l'icona della **chiave** (Secrets), aggiungi un segreto chiamato `GROQ_API_KEY` con la tua chiave e attiva "accesso dal notebook".
4. Nel notebook:

```python
from google.colab import userdata
from openai import OpenAI

client = OpenAI(api_key=userdata.get("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

risposta = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "Spiegami in una frase cos'è un caso limite."}])
print(risposta.choices[0].message.content)
```

La chiave è **tua**: non incollarla in chat, non condividerla, non metterla in un file che consegni. Il piano gratuito ha un limite di richieste al giorno più che sufficiente per i lab; se lo superi, aspetta il giorno dopo o cambia `base_url` con un altro fornitore: il codice resta identico, è il punto della lezione.
