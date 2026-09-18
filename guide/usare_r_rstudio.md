---
layout: page
title: Usare R e Rstudio
permalink: /guide/usare_r_rstudio
parent: Guide
nav_order: 2
---


# Usare R e RStudio
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Usare R
R non è un programma che puoi aprire e iniziare a utilizzare, come Microsoft Word o un browser. Invece, R è un linguaggio informatico, come C, C++ o Python. Usi R scrivendo comandi nel linguaggio R e chiedendo al tuo computer di interpretarli. In passato, le persone eseguivano il codice R nella finestra di un terminale UNIX, come se fossero hacker in un film degli anni '80. Ora quasi tutti usano R con un'applicazione chiamata RStudio e ti consiglio di farlo anche tu.

### R e UNIX

Puoi comunque eseguire R in una finestra UNIX o BASH (prompt o Powershell) digitando il comando `R`, che apre un interprete R. Puoi quindi fare il tuo lavoro e chiudere l'interprete eseguendo `q()` quando hai finito.

## Utilizzo di RStudio
R di per sé è solo il 'cuore' della programmazione R, ma non ha un'interfaccia utente particolare. Se preferisci (come me) un'interfaccia più gradevole con funzionalità aggiuntive, ti suggerisco di utilizzare RStudio. RStudio è un ambiente di sviluppo integrato (IDE) e sarà il nostro strumento principale per interagire con R. Per installarlo segui la guida [Installazione di R e RStudio]({{ site.baseurl }}/guide/installazione_r_rstudio), che ha i link diretti per scaricare R da CRAN e RStudio Desktop da Posit.

Congratulazioni, sei pronto per imparare R. D'ora in poi devi solo avviare RStudio e non R. Naturalmente, se sei un tipo curioso, nulla ti impedirà di provare R senza RStudio.

### I riquadri di RStudio
Quando apri RStudio la finestra è divisa in quattro riquadri:

- **Script** (in alto a sinistra, compare quando apri o crei un file con *File > New File > R Script*): è dove scrivi il codice e lo salvi in un file `.R`. Per eseguire la riga su cui si trova il cursore premi `Ctrl + Invio` (su Mac `⌘ + Invio`).
- **Console** (in basso a sinistra): è dove R esegue i comandi e mostra i risultati. Puoi scrivere anche direttamente qui, ma ciò che scrivi in console non viene salvato.
- **Environment** (in alto a destra): l'elenco delle variabili e delle tabelle che hai creato nella sessione.
- **Files / Plots / Packages / Help** (in basso a destra): i file della cartella di lavoro, i grafici, i pacchetti installati e la documentazione delle funzioni (prova a scrivere `?mean` in console).

### Personalizzazione di RStudio (un consiglio)
Prima di iniziare a programmare, devi voler apportare subito alcune modifiche alle tue impostazioni per avere un'esperienza migliore (secondo la mia opinione). Per aprire le impostazioni di RStudio devi cliccare su **Tools > Global Options** (su Mac puoi anche premere `⌘ + ,`).

Ti consiglio di apportare almeno le seguenti modifiche per prepararti al successo fin dall'inizio:

Già nella prima scheda, ovvero *General > Basic*, dovremmo apportare una delle modifiche più significative. Disattiva tutte le opzioni che iniziano con Restore. Ciò garantirà che ogni volta che avvii RStudio, inizi con una tabula rasa. A prima vista potrebbe sembrare controintuitivo non ricominciare tutto da dove eri rimasto, ma è fondamentale rendere tutti i tuoi progetti facilmente riproducibili. Inoltre, se si lavora insieme ad altri, non ripristinare le impostazioni personali garantisce anche che la programmazione funzioni su computer diversi. Pertanto, ti consiglio di deselezionare quanto segue:

- *Restore most recently opened project at startup*
- *Restore previously open source documents at startup*
- *Restore .RData into workspace at startup*


Nella stessa scheda in Workspace, selezionare *Never* per l'impostazione *Save workspace to .RData on exit*. Si potrebbe pensare che sia saggio mantenere i risultati intermedi archiviati da una sessione R all'altra. Tuttavia, mi sono spesso ritrovato a risolvere problemi dovuti a questa impostazione. Con l'esperienza, scoprirai che questo evita molti mal di testa.

Naturalmente, se desideri personalizzare ulteriormente il tuo spazio di lavoro, puoi farlo. Il modo visivamente più efficace per modificare l'aspetto predefinito di RStudio è selezionare *Appearance* e scegliere un tema colore completamente diverso. Sentiti libero di navigare tra le varie opzioni e vedere cosa preferisci. Non c'è giusto o sbagliato qui. Fallo tuo.

## Installare i pacchetti del corso
Un **pacchetto** è una raccolta di funzioni scritte da altri che si aggiunge a R. Nel corso usiamo `dplyr` (per lavorare con le tabelle, dal modulo 4), `ggplot2` (per i grafici), `readxl` (per leggere i file Excel) e `lubridate` (per le date). Si installano **una volta sola**, scrivendo in console:

```r
install.packages(c("dplyr", "ggplot2", "readxl", "lubridate"))
```

Se R ti chiede di scegliere un mirror CRAN, va bene il primo della lista (*0-Cloud*). L'installazione si fa una volta; invece **ogni volta** che apri una nuova sessione devi caricare i pacchetti che ti servono con `library()`, senza virgolette:

```r
library(dplyr)
```

Se `library(dplyr)` risponde `there is no package called 'dplyr'`, il pacchetto non è installato: ripeti `install.packages("dplyr")`.

## Aggiornare R e RStudio
Sebbene non sia strettamente qualcosa che ti aiuta a diventare un programmatore migliore, questo consiglio potrebbe tornare utile per evitare di trasformarti in un programmatore frustrato. Quando si aggiorna il software, è necessario aggiornare R e RStudio separatamente l'uno dall'altro. Sebbene sia R che RStudio lavorino a stretto contatto tra loro, costituiscono comunque parti separate di software. Pertanto, è essenziale tenere presente che l'aggiornamento di RStudio non aggiornerà automaticamente R.