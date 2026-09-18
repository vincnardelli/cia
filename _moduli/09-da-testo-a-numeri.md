---
layout: modulo
number: 9
title: Da testo a numeri
sezione: 3
language: Python
idea: "Una macchina non legge: conta parole, poi impara a rappresentare un testo come un punto nello spazio."
hours: 4
published: false
concepts_new: [bag of words, TF-IDF, tokenizzazione, embeddings, similarità coseno]
concepts_required: [vettori, pandas, random forest, correlazione]
explorations: [tokenizzatore]
slides_pdf:
---

## L'idea del modulo

Tutto quello che abbiamo fatto finora funziona su numeri. Una recensione, un reclamo, una descrizione di prodotto sono testo, e per farli entrare in una foresta vanno tradotti in numeri. Il modo più semplice è il **bag of words**: una colonna per ogni parola del vocabolario, e in ogni cella quante volte compare. **TF-IDF** pesa di più le parole rare e informative e di meno quelle che stanno ovunque. Funziona, ma «ottimo prodotto» e «prodotto eccellente» restano due vettori quasi senza nulla in comune.

Il passo successivo è il cuore della sezione 3. Prima la **tokenizzazione**: un modello di linguaggio non lavora su parole ma su pezzi di parola (sub-token), e «incredibilmente» diventa tre o quattro pezzi. Poi gli **embeddings**: un modello addestrato su miliardi di frasi trasforma un testo in un vettore di qualche centinaio di numeri, in cui testi con lo stesso significato finiscono vicini. La vicinanza si misura con la **similarità coseno**, cugina della correlazione del modulo 5.

```python
from sklearn.metrics.pairwise import cosine_similarity
simili = cosine_similarity(embedding_recensione, embeddings_tutte)
```

## In aula

Lab *recensioni simili*: data una recensione, trovare le cinque più vicine nel dataset testuale del proprio settore. Poi classificazione delle recensioni (positiva/negativa) con la random forest del modulo 8 addestrata sugli embeddings: la foresta non sa che sono testi.

## In piattaforma

Esplorazione interattiva del tokenizzatore: si scrive una frase e si vede in quanti pezzi viene spezzata, in italiano e in inglese. Ricerca semantica su descrizioni prodotto. Sfida: «stesso significato, parole diverse», il caso in cui il bag of words fallisce e gli embeddings no.

## Per approfondire

La foresta che classifica gli embeddings è nel [modulo 8](08-random-forest). Nella [modulo 10](10-modello-di-linguaggio) il modello che produce gli embeddings genera anche testo, un token alla volta.
