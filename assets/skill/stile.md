# Stile del codice del corso

Il codice del corso ha un aspetto riconoscibile. Quando scrivi o correggi codice per lo studente, imitalo.

## Convenzioni

- Assegnazione con `<-` (mai `=` per assegnare).
- Nomi in italiano, minuscoli, con underscore: `prezzo_netto`, `giorni_ritardo`, `punti_finali`. Niente `x`, `tmp`, `result`.
- Commenti in italiano, brevi, sopra il blocco che spiegano.
- Una istruzione per riga. Niente `;`.
- `if(condizione){` senza spazio tra `if` e la parentesi; `}else if(...){` e `}else{` attaccati sulla stessa riga.
- Le condizioni composte con `&` e `|` (non `&&`/`||`), gli insiemi con `%in%`.
- Fino al modulo 3 nessuna funzione definita dallo studente; dal modulo 3 `nome <- function(argomenti){ ... return(valore) }`.
- Per stampare: `print(paste0("Testo: ", valore))`.
- Prima R base (vettori, `[ ]`, `for`), poi dplyr con `%>%`, un verbo per riga.
- Le soglie delle regole scritte come sono nel testo: "non oltre 10" → `<= 10`; "oltre 10" → `> 10`; "da 31 a 60" → `>= 31 & <= 60`.

## Esempio 1 — decisione a fasce (modulo 2, Autovelox)

```r
velocita <- 70
limite <- 50

differenza <- velocita - limite

if(differenza <= 0){
  multa <- 0
}else if(differenza <= 10){
  multa <- 36
}else if(differenza <= 40){
  multa <- 148
}else if(differenza <= 60){
  multa <- 370
}else{
  multa <- 500
}
multa
```

## Esempio 2 — tre modi equivalenti (modulo 2, Boomer)

```r
anno <- 2006

# Opzione 1: due if
if(anno > 1964){
  status <- "Non Boomer"
}else if(anno < 1946){
  status <- "Non Boomer"
}else{
  status <- "Boomer"
}

# Opzione 2: una condizione composta (attenzione ai confini: >= e <=, non > e <)
if(anno >= 1946 & anno <= 1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}

# Opzione 3: appartenenza a un insieme
if(anno %in% 1946:1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
```

## Esempio 3 — ciclo su un vettore con accumulatore (modulo 3, Taxi)

```r
tariffa_min <- 28/60
tariffa_km <- 1.14
distanza <- c(1, 0.3, 0.5, 0.8, 0.2)
costo <- 0

for(i in 1:length(distanza)){
  velocita <- distanza[i] * 60
  if(velocita < 20){
    costo <- costo + tariffa_min
  }else{
    costo <- costo + tariffa_km * distanza[i]
  }
}
print(paste0("Costo della corsa: ", round(costo, 2), " euro"))
```

## Esempio 4 — ciclo con classificazione (modulo 3, BMI)

```r
altezza <- c(1.58, 1.73, 1.81, 1.47, 1.74)
peso <- c(62, 86, 85, 95, 75)

bmi <- peso / altezza^2

for(i in 1:5){
  if(bmi[i] < 18.5){
    classificazione <- "Sottopeso"
  }else if(bmi[i] < 25){
    classificazione <- "Normopeso"
  }else if(bmi[i] < 30){
    classificazione <- "Sovrappeso"
  }else{
    classificazione <- "Obesità"
  }
  print(paste0("Paziente ", i, ": ", classificazione))
}
```

## Esempio 5 — funzione (modulo 3)

```r
multa <- function(velocita, limite){
  differenza <- velocita - limite
  if(differenza <= 0){
    importo <- 0
  }else if(differenza <= 10){
    importo <- 36
  }else if(differenza <= 40){
    importo <- 148
  }else if(differenza <= 60){
    importo <- 370
  }else{
    importo <- 500
  }
  return(importo)
}

multa(75, 50)
```

## Esempio 6 — dplyr (modulo 4, Titanic)

```r
library(dplyr)
titanic <- read.csv("titanic.csv")
titanic$Sex    <- as.factor(titanic$Sex)
titanic$Pclass <- as.factor(titanic$Pclass)

summary(titanic)

# Quale era la percentuale di uomini e donne tra gli over 50?
titanic %>%
  filter(!is.na(Age), Age > 50) %>%
  group_by(Sex) %>%
  summarise(n = n()) %>%
  mutate(perc = n / sum(n))

# In percentuale sono sopravvissuti più passeggeri in prima o terza classe?
titanic %>%
  group_by(Pclass) %>%
  summarise(perc_sopravvissuti = mean(Survived))
```

## Esempio 7 — segmentazione a regole su un data frame (modulo 5, RFM)

```r
rfm <- retail %>%
  group_by(CustomerID) %>%
  summarise(f = n(),
            m = sum(Total)) %>%
  mutate(f_score = ntile(f, 4),
         m_score = ntile(m, 4)) %>%
  mutate(cluster = case_when(f_score == 4 & m_score == 4 ~ "Gold",
                             f_score == 1 & m_score == 1 ~ "Lost",
                             f_score == 4 ~ "Loyal",
                             m_score == 4 ~ "High spending",
                             TRUE ~ "Altri"))
```

## Esempio 8 — lo stesso Autovelox in Python (dal modulo 7)

```python
velocita = 70
limite = 50

differenza = velocita - limite

if differenza <= 0:
    multa = 0
elif differenza <= 10:
    multa = 36
elif differenza <= 40:
    multa = 148
elif differenza <= 60:
    multa = 370
else:
    multa = 500
print(multa)
```
