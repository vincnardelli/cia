---
layout: page
title: Progetto 2 · Analizza un dataset
permalink: /progetti/2/
parent: Progetti
nav_order: 2
---

# Progetto 2 · Analizza un dataset

<div class="patto" markdown="1">
**Il progetto si fa in aula.** La maggior parte del lavoro va svolta durante le lezioni, con il vostro gruppo: per questo è **necessaria la presenza a tutte le lezioni fino alla consegna**, venerdì 20, lunedì 23 e venerdì 27 novembre.
</div>

{% include iscrizione-progetto.html %}

Un'azienda ha un problema e un archivio di casi passati: prestiti già erogati, pazienti già dimessi, ordini già consegnati. Vuole sapere se dai dati si può ricavare una regola per decidere meglio. Il vostro gruppo riceve uno di questi archivi e risponde alla domanda con un **albero di classificazione**, verificato su dati che non ha mai visto, come nelle lezioni 11 e 12.

<div class="patto" markdown="1">
**Conta la risposta alla domanda, non l'albero più complicato.** Un albero di poche domande, scelto guardando il test e letto nel contesto dell'azienda, vale più di un modello che sul training prende il 100 %.
</div>

<div class="spec">
  <div class="spec__row"><div class="spec__k">Chi</div><div class="spec__v">In gruppi di 3–5 persone, formati a caso tra chi si iscrive al <a href="https://forms.gle/Dr9wGw2miBk5UfZh6" target="_blank" rel="noopener">modulo di iscrizione</a> entro <strong>venerdì 20 novembre 2026, ore 9:00</strong></div></div>
  <div class="spec__row"><div class="spec__k">Punti</div><div class="spec__v">3 su 30, con un giudizio unico da 0 a 3, lo stesso per tutti i componenti del gruppo</div></div>
  <div class="spec__row"><div class="spec__k">Scadenza</div><div class="spec__v"><strong>Domenica 29 novembre 2026, ore 23:59</strong>. Dopo la scadenza il progetto vale 0 punti.</div></div>
  <div class="spec__row"><div class="spec__k">Cosa</div><div class="spec__v">Due file: il notebook <code>gruppo_N.ipynb</code> (oppure <code>gruppo_N.R</code> se lavorate in R) e il registro AI del gruppo in PDF o Word (<code>gruppo_N_registro_ai.pdf</code> o <code>.docx</code>)</div></div>
  <div class="spec__row"><div class="spec__k">Come</div><div class="spec__v">Una sola email per gruppo a <a href="mailto:vincenzo.nardelli@unicatt.it?subject=CIA%20Progetto%202%20-%20Gruppo%20N">vincenzo.nardelli@unicatt.it</a>, mandata da un componente con gli altri in copia, oggetto <code>CIA Progetto 2 - Gruppo N</code> e i due file in allegato (non link)</div></div>
</div>

## I gruppi e i dataset

L'iscrizione è parte del progetto: **chi non si iscrive entro venerdì 20 novembre alle 9:00 non partecipa**: il progetto 2 vale 0 punti. Dopo la chiusura delle iscrizioni formo i gruppi a caso e a ogni gruppo assegno, sempre a caso, uno degli otto dataset. L'elenco dei gruppi arriva in aula e per email, non su questo sito. Se i gruppi sono più di otto, qualche dataset va a due gruppi, che lavorano ognuno per conto suo.

Ogni dataset ha una scheda con il contesto, la domanda dell'azienda e la descrizione di tutte le variabili.

| Settore | Dataset | Cosa si prevede |
|---|---|---|
| Sanità | [Riammissioni ospedaliere entro 30 giorni]({{ site.baseurl }}/progetti/2/sanita_riammissioni/) | il paziente torna in ospedale entro un mese |
| Sanità | [Visite prenotate e non disdette]({{ site.baseurl }}/progetti/2/sanita_prenotazioni/) | il paziente non si presenta alla visita |
| Banca e finanza | [Insolvenze sul credito al consumo]({{ site.baseurl }}/progetti/2/banca_prestiti/) | il prestito non viene restituito |
| Banca e finanza | [Chiusura del conto corrente]({{ site.baseurl }}/progetti/2/banca_conti/) | il cliente chiude il conto |
| Marketing ed e-commerce | [Riacquisto entro 90 giorni]({{ site.baseurl }}/progetti/2/ecommerce_riacquisto/) | il cliente compra di nuovo |
| Assicurazioni | [Sinistri RC auto entro dodici mesi]({{ site.baseurl }}/progetti/2/assicurazioni_sinistri/) | l'assicurato fa un incidente |
| Logistica | [Consegne in ritardo]({{ site.baseurl }}/progetti/2/logistica_consegne/) | l'ordine arriva in ritardo |
| Risorse umane | [Dimissioni volontarie entro dodici mesi]({{ site.baseurl }}/progetti/2/risorse_umane_dimissioni/) | il dipendente se ne va |

I dati sono costruiti per il corso partendo da studi e statistiche reali di ogni settore: gli effetti che troverete sono quelli documentati, anche quando sorprendono. In tutti e otto i casi positivi sono circa il 30 %, più che nella realtà, altrimenti l'albero non avrebbe abbastanza esempi da cui imparare.

## Cosa fare

1. **Leggete la scheda** del vostro dataset: chi è l'azienda, cosa deve decidere, quanti casi può gestire. È la domanda a cui risponderete alla fine.
2. **Analisi descrittiva.** Almeno tre grafici e due tabelle di sintesi, ognuno con una frase che dice cosa si vede. Le domande utili sono quelle della lezione 10: in quali gruppi il target è più frequente? Ci sono soglie, valori strani, valori mancanti? I valori mancanti (`NA`) decidete voi come trattarli, e scrivete perché.
3. **Training e test.** Dividete i dati, 70 % training e 30 % test, con `train_test_split` e un `random_state` fissato.
4. **Il primo albero.** Un albero **senza limiti**: accuracy sul training e sul test, una accanto all'altra. Cosa vi dicono i due numeri?
5. **Scegliete la profondità.** Provate almeno tre valori di `max_depth` e mettete in una tabella l'accuracy sul training e sul test di ognuno. Se volete, provate tutte le profondità da 1 a 10 e disegnate le due linee in un grafico, come nella lezione 12. Scegliete la profondità guardando il test, e scrivete perché.
6. **La verifica.** Con la profondità scelta: la tabella di confusione sul test e il confronto con chi risponde sempre «no», che nella scheda trovate già calcolato.
7. **La risposta.** Disegnate l'albero scelto con `plot_tree` e dite quali sono le prime domande che fa. Poi, in poche righe, rispondete alla domanda della scheda: chi conviene segnalare, e quale dei due errori costa di più all'azienda, i falsi allarmi o i casi che sfuggono.
8. **Compilate il registro AI** e inviate i due file.
{: .steps }

<div class="via" markdown="1">
<div class="via__k">Python o R</div>
Il progetto si fa in **Python in Colab**, come nelle lezioni 11 e 12: un notebook solo, con pandas per l'analisi descrittiva e scikit-learn per l'albero. Chi preferisce può usare **R**, tutto o in parte: i grafici, per esempio, si possono fare con ggplot2. Se usate tutti e due, consegnate entrambi i file.
</div>

<div class="via" markdown="1">
<div class="via__k">Le colonne di testo</div>
L'albero di scikit-learn lavora solo con i numeri, e ogni dataset ha qualche colonna di testo (`area`, `sesso`, `contratto`...). Prima di dividere in training e test, trasformatele con `pd.get_dummies`, che crea una colonna di 0 e 1 per ogni categoria: `area` diventa `area_centro`, `area_sud` e così via. Per esempio, con il dataset dei prestiti:

```python
y = dati["insolvente"]
X = pd.get_dummies(dati.drop(columns="insolvente"), dtype=int)
```

Il nome della colonna da prevedere è nella scheda del vostro dataset.
</div>

<div class="via" markdown="1">
<div class="via__k">Prima di consegnare</div>
In Colab: *Runtime → Riavvia sessione ed esegui tutto*. Il notebook deve arrivare in fondo senza errori, e lo consegnate con gli output, così si vedono i grafici e i numeri. I dati si leggono direttamente dal sito, con l'indirizzo che trovate nella scheda: niente file da caricare.
</div>

<div class="via" markdown="1">
<div class="via__k">Facoltativo · fino a 1 punto in più</div>
Allenate sugli stessi dati una **random forest** (`RandomForestClassifier` di scikit-learn) e confrontatela con l'albero scelto, sullo **stesso test**: accuracy e tabella di confusione. Poi dite se, per la vostra azienda, il guadagno vale la perdita di leggibilità: l'albero si può disegnare e spiegare a un responsabile, la foresta no.

La random forest **non l'abbiamo vista a lezione**: è l'occasione per impararla da soli. Qualche punto di partenza:

- il libro **ISLR2**, *An Introduction to Statistical Learning*, capitolo 8 sui metodi basati sugli alberi, gratuito su [statlearning.com](https://www.statlearning.com/);
- la [documentazione di scikit-learn](https://scikit-learn.org/stable/modules/ensemble.html#random-forests), con esempi di codice;
- video e materiale online: ce n'è moltissimo, anche in italiano.

L'**AI** può aiutarvi sia a scrivere il codice sia a **capire**: chiedetele di spiegarvi l'idea con un esempio, di dirvi cosa fa ogni riga, di trovare i punti deboli del vostro confronto. Scrivete nel registro come l'avete usata. E per qualunque dubbio, **chiedete a me**, a lezione o per email.
</div>

## Il registro AI

Come nel progetto 1, l'AI è ammessa. Il registro, uno per gruppo, dice quali strumenti avete usato e, per ogni uso importante, cosa avete chiesto, cosa vi ha dato l'AI e cosa avete deciso voi. Se non l'avete usata, scrivetelo.

## Come viene valutato

Il progetto riceve un **giudizio unico da 0 a 3**, lo stesso per tutto il gruppo. Contano:

- la **risposta alla domanda** della scheda, sostenuta dai numeri;
- l'uso corretto di **training e test**, e una profondità scelta guardando il test;
- la **lettura degli errori** nel contesto dell'azienda;
- grafici e tabelle leggibili, ognuno con la sua frase;
- il **registro AI**.

Il confronto facoltativo con la random forest vale fino a 1 punto in più. Il progetto non consegnato entro la scadenza vale 0 punti.
