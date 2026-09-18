---
layout: modulo
number: 5
title: Leggere i dati
sezione: 1
language: R
idea: "Una tabella si riassume con pochi numeri e pochi grafici; saperli leggere è più difficile che calcolarli."
hours: 4
published: false
concepts_new: [media e mediana, quantili, deviazione standard, correlazione, ggplot2, case_when, ntile]
concepts_required: [data frame, dplyr, pipe, group_by, valori mancanti, if/else]
explorations: []
slides_pdf:
---

## Quattro titoli, un anno di Borsa

Il file dei rendimenti contiene, per ogni giorno di Borsa del 2023, il rendimento giornaliero di quattro titoli di Piazza Affari: Ferrari, Enel, Intesa e Unicredit. Un rendimento dello 0,01 significa che il titolo ha guadagnato l'1 % rispetto al giorno prima. È il dataset della sezione 1 su cui impariamo a **riassumere**: una colonna di 250 numeri in due o tre.

```r
library(readxl)
library(dplyr)
library(ggplot2)
rendimenti <- read_excel("finanza_returns.xlsx")

summary(rendimenti)
mean(rendimenti$Ferrari)
median(rendimenti$Ferrari)
```

La **media** è la somma diviso il numero: il rendimento «tipico» se ogni giorno fosse uguale. La **mediana** è il valore che sta a metà una volta ordinati i giorni: metà dei giorni ha fatto peggio, metà meglio. Sono uguali quando la distribuzione è simmetrica; si allontanano quando ci sono pochi giorni estremi, e la media viene trascinata da quelli (è l'aspettativa di vita del Burundi, modulo 1). I **quantili** generalizzano la mediana: il quantile 0,25 lascia sotto di sé un quarto dei giorni.

```r
quantile(rendimenti$Ferrari, c(0.25, 0.5, 0.75))
```

## Rischio è variabilità

Ferrari e Unicredit hanno chiuso l'anno con medie giornaliere simili (0,17 % e 0,26 %). Ma un investitore non vive di medie: vive dei giorni in cui il titolo perde il 5 %. La **deviazione standard** misura quanto i valori si allontanano dalla media, in media:

```r
sd(rendimenti$Ferrari)
sd(rendimenti$Enel)
sd(rendimenti$Intesa)
sd(rendimenti$Unicredit)
```

Ferrari 1,3 %, Enel 1,1 %, Intesa 1,5 %, Unicredit 2,2 %. In finanza si chiama rischio, in statistica variabilità: sono la stessa cosa. Un titolo con deviazione standard doppia ha giornate buone e cattive di ampiezza doppia. Per confrontare i quattro titoli con una tabella sola:

```r
rendimenti %>%
  summarise(media_ferrari = mean(Ferrari), sd_ferrari = sd(Ferrari),
            media_unicredit = mean(Unicredit), sd_unicredit = sd(Unicredit))
```

> **Attenzione** `sd()` e `mean()` con un `NA` restituiscono `NA`: vale il `na.rm = TRUE` del modulo scorso. Ma togliere gli `NA` non è neutro: se i giorni mancanti sono proprio quelli di crisi (dati non scaricati perché il mercato era sospeso), la deviazione standard è sottostimata. Prima di togliere, chiedersi perché mancano.

I titoli si muovono insieme? La **correlazione** va da −1 a 1 e misura quanto due colonne salgono e scendono insieme:

```r
cor(rendimenti$Intesa, rendimenti$Unicredit)
round(cor(rendimenti[, c("Ferrari", "Enel", "Intesa", "Unicredit")]), 2)
```

Intesa e Unicredit, due banche, hanno correlazione alta: nei giorni in cui sale una tende a salire l'altra. Ferrari è meno legata alle banche. Per un portafoglio è un'informazione più utile dei singoli rendimenti: due titoli correlati non diversificano. E vale il promemoria del modulo 1: correlazione non è causazione, nemmeno quando il coefficiente è 0,9.

## Tre grafici con ggplot2

Un riassunto numerico dice molto; un grafico dice il resto. Con ggplot2 un grafico si costruisce a strati: i dati, la corrispondenza tra colonne ed elementi visivi (`aes`), il tipo di segno (`geom_`).

L'**istogramma** mostra la distribuzione di una variabile numerica: quanti giorni cadono in ogni intervallo di rendimento.

```r
ggplot(rendimenti, aes(x = Ferrari)) +
  geom_histogram(bins = 30, fill = "red", alpha = 0.7) +
  geom_vline(xintercept = mean(rendimenti$Ferrari)) +
  theme_minimal() +
  labs(x = "Rendimento giornaliero", y = "Giorni")
```

Il **grafico a barre** conta o confronta categorie. Sull'ecommerce del modulo scorso, il fatturato per categoria:

```r
ecommerce <- read.csv("ecommerce.csv")

ecommerce %>%
  group_by(ProductCategory) %>%
  summarise(fatturato = sum(TotalAmount)) %>%
  ggplot(aes(x = ProductCategory, y = fatturato)) +
  geom_col() +
  theme_minimal()
```

Notate che la pipe può finire in `ggplot`: si prepara la tabella riassunta con dplyr e la si passa al grafico. `geom_col` disegna l'altezza che gli diamo; `geom_bar` conta le righe da solo.

Il **grafico di dispersione** mostra due variabili numeriche, un punto per osservazione; è la correlazione vista a occhio:

```r
ggplot(rendimenti, aes(x = Intesa, y = Unicredit)) +
  geom_point(alpha = 0.5) +
  theme_minimal()
```

Una nuvola allungata lungo la diagonale è correlazione alta; una nuvola tonda è correlazione zero.

> **In aula** abbiamo fatto questi tre grafici e basta. In piattaforma trovate colori per categoria (`aes(fill = Membership)`), pannelli (`facet_grid`), boxplot, etichette con `labs`, e come ordinare le barre per altezza con `fct_reorder`.

## Come mentire con i grafici

Gli stessi dati possono raccontare storie opposte. Le tecniche sono poche e vanno riconosciute:

- **asse tagliato**: un asse y che parte da 95 invece che da 0 trasforma una differenza del 2 % in una torre;
- **scala scelta ad arte**: allungare o comprimere l'asse del tempo fa sembrare una crescita esplosiva o piatta;
- **categorie riaggregate**: sommare o spezzare classi fino a far vincere quella che si vuole (Simpson, di nuovo);
- **torte**: l'occhio confronta male gli angoli, e con più di tre fette non si legge nulla;
- **3D**: la prospettiva ingrandisce ciò che sta davanti.

La regola pratica: asse y da zero per le barre, mai torte, mai 3D, e in ogni grafico scrivere nel titolo cosa mostra e nella didascalia da dove vengono i dati.

> **Attenzione** `xlim()` e `ylim()` in ggplot2 non solo tagliano l'asse: **scartano** i dati fuori dai limiti prima di calcolare l'istogramma. Se fissate `xlim(c(-0.05, 0.05))` i giorni con perdite oltre il 5 % spariscono dal conteggio, non solo dalla vista. Per zoomare senza perdere dati si usa `coord_cartesian()`.

## RFM: un if/else su un data frame

Il marketing classifica i clienti con tre metriche: **Recency** (giorni dall'ultimo acquisto), **Frequency** (numero di acquisti), **Monetary** (totale speso). Un cliente recente, frequente e che spende molto vale più degli altri. Dal file degli scontrini (`CustomerID`, `InvoiceDate`, `Quantity`, `UnitPrice`, `Total`) le tre metriche sono un `group_by` più un `summarise`:

```r
library(lubridate)
scontrini <- read.csv("retail_rfm.csv")
scontrini$InvoiceDate <- as_date(scontrini$InvoiceDate)
data_riferimento <- max(scontrini$InvoiceDate)

rfm <- scontrini %>%
  group_by(CustomerID) %>%
  summarise(recency = as.numeric(data_riferimento - max(InvoiceDate)),
            frequency = n(),
            monetary = sum(Total)) %>%
  mutate(r_score = ntile(desc(recency), 4),
         f_score = ntile(frequency, 4),
         m_score = ntile(monetary, 4))
```

`ntile(x, 4)` divide i clienti in quattro gruppi di uguale numerosità (quartili) e assegna 1 al peggiore e 4 al migliore: per la recency il migliore è chi ha pochi giorni, da cui `desc()`. Ora ogni cliente ha tre punteggi da 1 a 4, e vogliamo assegnargli un segmento. Con un `if/else` dovremmo scrivere un ciclo sui clienti; `case_when` fa la stessa cosa su tutta la colonna:

```r
rfm <- rfm %>%
  mutate(segmento = case_when(
    r_score == 4 & f_score == 4 & m_score == 4 ~ "Gold",
    r_score == 1 & f_score == 1 & m_score == 1 ~ "Persi",
    f_score == 4 ~ "Fedeli",
    r_score == 4 ~ "Attivi",
    m_score == 4 ~ "Alta spesa",
    TRUE ~ "Altri"
  ))

rfm %>%
  group_by(segmento) %>%
  summarise(clienti = n(), fatturato = sum(monetary)) %>%
  arrange(desc(fatturato))
```

Ogni riga di `case_when` è un `else if`: condizione a sinistra della tilde, valore a destra. Come nell'`if` del modulo 2, vince la **prima** condizione vera dall'alto: un cliente 4-4-4 è Gold e non Fedele, perché Gold viene prima. La riga `TRUE ~ "Altri"` è l'`else` finale.

> **Attenzione** Senza la riga `TRUE ~ ...`, i clienti che non soddisfano nessuna condizione ricevono `NA`, e nel `group_by` finale compare un segmento senza nome. E `ntile` con molti valori uguali (tanti clienti con un solo acquisto) spezza i pareggi per ordine di riga: due clienti identici possono finire in quartili diversi. Il test in piattaforma «quanti clienti Gold» controlla entrambe le cose.

## Per approfondire

I verbi di dplyr su cui si regge ogni riga di questo modulo sono nel [modulo 4](04-dati). Nella [modulo 6](06-software-2-0) le regole dell'autovelox, che finora abbiamo scritto noi, le farà trovare un algoritmo ai dati.
