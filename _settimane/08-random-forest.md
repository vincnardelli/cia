---
layout: settimana
number: 8
title: Random forest
pillar: 2
language: Python
idea: "Tanti alberi diversi che votano sbagliano meno di un albero solo."
hours: 5
dates: []
concepts_new: [random forest, cross-validation, importanza delle variabili, scikit-learn]
concepts_required: [albero di classificazione, train/test, overfitting, confusion matrix, pandas, Colab]
explorations: []
slides_pdf:
---

## L'idea della settimana

Un albero solo è instabile: cambiate qualche riga di training e gli split si spostano. La **random forest** ne costruisce centinaia, ognuno su un campione diverso dei dati e delle variabili, e fa decidere alla maggioranza. Il singolo albero può memorizzare il rumore; la media di cento alberi che hanno visto rumori diversi lo cancella. Si perde la leggibilità dell'albero disegnato, si guadagna in accuratezza e stabilità. In cambio della scatola chiusa, la foresta dice quali variabili hanno pesato di più (**importanza delle variabili**).

In **scikit-learn** ogni modello ha la stessa forma, `fit` sul train e `predict` sul test:

```python
from sklearn.ensemble import RandomForestClassifier
foresta = RandomForestClassifier(n_estimators=200, random_state=1)
foresta.fit(X_train, y_train)
previsioni = foresta.predict(X_test)
```

## In aula

La pipeline scikit-learn passo per passo: separare X e y, dividere train e test, addestrare, valutare con la confusion matrix della settimana 6. *Churn* con random forest a confronto con l'albero singolo. Poi ogni gruppo passa il proprio dataset dall'albero del progetto di metà corso alla foresta.

## In piattaforma

**Cross-validation**: invece di un solo split train/test, cinque a rotazione, per non fidarsi di una divisione fortunata. Tuning del numero di alberi e della profondità, curva di apprendimento (quanto migliora il modello con più dati), regressione su *real_estate*. Sfida: un confronto onesto albero vs foresta, con le stesse divisioni e le stesse metriche.

## Per approfondire

L'albero singolo e il perché del train/test sono nella [settimana 6](06-software-2-0). Nella [settimana 9](09-da-testo-a-numeri) la stessa foresta classificherà testi, dopo averli trasformati in numeri.
