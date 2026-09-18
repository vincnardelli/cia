---
layout: page
title: Installazione di R e Rstudio
permalink: /guide/installazione_r_rstudio
parent: Guide
nav_order: 1
---


# Installazione di R e RStudio
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

Per iniziare ad usare R, devi installarlo sul tuo computer. Questa nota ti mostrerà come scaricare R e RStudio, un'applicazione software che semplifica l'utilizzo di R. Passerai dal download di R all'apertura della tua prima sessione R.


## Come scaricare e installare R
R è gestito da un team internazionale di sviluppatori che rendono disponibile il linguaggio attraverso la pagina web di The Comprehensive R Archive Network, ovvero [CRAN](https://cran.r-project.org/). Nella parte superiore della pagina Web sono disponibili tre collegamenti per il download di R. Segui il collegamento che si riferisce al tuo sistema operativo: Windows, Mac o Linux. Per il corso serve **R 4.6.1 o una versione successiva**: scarica sempre quella più recente.

### R in Windows
Per installare R su Windows vai direttamente alla pagina [**Download R for Windows → base**](https://cran.r-project.org/bin/windows/base/) di CRAN. Fai clic sul primo collegamento nella parte superiore della pagina: dovrebbe dire qualcosa come "Download R-4.6.1 for Windows", dove al posto di 4.6.1 trovi la versione più recente di R. Il collegamento scarica un programma di installazione (un file `.exe`), che installa la versione più aggiornata di R per Windows. Esegui questo programma e segui la procedura guidata di installazione che appare. La procedura guidata installerà R nelle cartelle dei file di programma e inserirà un collegamento nel menu Start. Tieni presente che dovrai disporre di tutti i privilegi di amministrazione appropriati per installare nuovo software sul tuo computer.

### R su Mac
Vai alla pagina [**Download R for macOS**](https://cran.r-project.org/bin/macosx/) di CRAN. Nella sezione *Latest release* ci sono due installer (file `.pkg`), e devi scegliere quello giusto per il processore del tuo Mac. Per scoprirlo apri il menu Apple (la mela in alto a sinistra) → **Informazioni su questo Mac**:

- se alla voce *Chip* leggi **Apple M1, M2, M3, M4…** (Apple silicon), scarica il file che finisce con **`-arm64.pkg`**;
- se alla voce *Processore* leggi **Intel**, scarica il file che finisce con **`-x86_64.pkg`**.

Apri il file scaricato e segui le istruzioni di installazione. Consiglio di lasciare le impostazioni suggerite così come sono.


### R in Linux
R viene preinstallato su molti sistemi Linux, ma se la tua non è aggiornata, ti consiglio la versione più recente di R. Il sito Web CRAN fornisce istruzioni e pacchetti per Debian, Fedora/Redhat, SUSE e Ubuntu sotto il collegamento [**Download R for Linux**](https://cran.r-project.org/bin/linux/). Fare clic sul collegamento e quindi seguire il percorso della directory alla versione di Linux su cui si desidera installare. L'esatta procedura di installazione varia a seconda del sistema Linux in uso. CRAN guida il processo con documentazione o file README che spiegano come installare sul sistema.

## Come scaricare e installare RStudio
R da solo si usa scrivendo comandi in una finestra spoglia. **RStudio** è l'applicazione con cui lavoreremo per tutta la parte del corso in R: un editor per gli script, la console, l'elenco delle variabili e i grafici nella stessa finestra. RStudio è gratuito ed è distribuito da Posit (l'azienda che prima si chiamava RStudio). **Installa prima R** (sezione precedente) e poi RStudio.

1. Vai alla pagina di download di [**RStudio Desktop**](https://posit.co/download/rstudio-desktop/) sul sito di Posit: si apre la sezione dei download gratuiti (*Open Source*).
2. Nella tabella *RStudio IDE* scegli l'installer per il tuo sistema operativo: il file `.exe` per Windows, il file `.dmg` per macOS. Più in basso nella stessa pagina ci sono le versioni *Pro* e *Server*: non servono.
3. **Windows**: apri il file `.exe` e segui la procedura guidata lasciando le impostazioni predefinite. **Mac**: apri il file `.dmg` e trascina l'icona di RStudio nella cartella *Applicazioni*.

RStudio non va confuso con R: sono due programmi separati, e RStudio funziona solo se R è già installato.

## La tua prima sessione R
Apri **RStudio** (non R): d'ora in poi è l'unico programma che devi avviare. Nel riquadro in basso a sinistra, la **Console**, scrivi

```r
1 + 1
R.version.string
```

premendo Invio dopo ogni riga. Se vedi `[1] 2` e poi la versione di R che hai appena installato (per esempio `"R version 4.6.1 ..."`), è tutto a posto. Per capire come è fatta la finestra di RStudio e installare i pacchetti del corso, prosegui con la guida [Usare R e RStudio]({{ site.baseurl }}/guide/usare_r_rstudio).
