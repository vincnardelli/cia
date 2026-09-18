---
layout: page
title: Google Colab in cinque minuti
permalink: /guide/colab
parent: Guide
nav_order: 4
published: false
---

# 🐍 Google Colab in cinque minuti

Dalla modulo 7 il corso passa a Python, e Python lo usiamo su **Google Colab**: un notebook nel browser, nessuna installazione, basta un account Google.

1. Vai su [colab.research.google.com](https://colab.research.google.com) e accedi con l'account Google.
2. **File → Nuovo notebook**. Si apre una pagina con una cella vuota.
3. Scrivi `print("ciao")` nella cella e premi **Shift+Invio**: la cella viene eseguita e l'output compare sotto.
4. Ogni cella è un pezzo di codice; le variabili restano in memoria tra una cella e l'altra finché non chiudi (o Colab non "riavvia il runtime" dopo un po' di inattività: allora ri-esegui dall'inizio con *Runtime → Esegui tutto*).
5. Il notebook si salva da solo su Google Drive, nella cartella *Colab Notebooks*.

Per caricare un file CSV: icona cartella a sinistra → *Carica*. Poi `pd.read_csv("nome.csv")`. Attenzione: i file caricati spariscono quando il runtime si riavvia; per i dataset del corso usa direttamente l'URL della pagina *Lab*.

L'assistente Gemini integrato in Colab funziona come qualunque altro assistente: valgono le stesse regole del [patto d'uso]({{ site.baseurl }}/guide/patto_ai).
