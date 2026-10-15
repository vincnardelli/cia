# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 7 - Dati: data frame e dplyr
# ==============================================================
#
# File che servono, nella stessa cartella di questo script
# (scaricabili dalla pagina Dati del sito):
#   ecommerce.csv   una riga per ordine
#   titanic.csv     una riga per passeggero (lo usiamo nel lab)
#
# In RStudio: Session > Set Working Directory > To Source File Location


# ---- 1. Dai vettori alla tabella ------------------------------

# Nel modulo 3 i dati stavano in vettori separati: solo noi
# sapevamo che il secondo cliente ha il secondo valore di eta.
clienti <- c("Anna", "Bruno", "Carla", "Dario")
eta     <- c(34,     51,      NA,      28)
spesa   <- c(120,    80,      45,      300)

# Il data frame li mette uno accanto all'altro, come colonne.
tabella <- data.frame(clienti, eta, spesa)
tabella

nrow(tabella)        # quante righe (osservazioni)
ncol(tabella)        # quante colonne (variabili)
tabella$spesa        # una colonna è un vettore normale
tabella$spesa[2]     # ... e si indicizza come un vettore


# ---- 2. Leggere un file CSV -----------------------------------

ecommerce <- read.csv("ecommerce.csv")

head(ecommerce)      # le prime sei righe
str(ecommerce)       # struttura: righe, colonne, tipo di ogni colonna
summary(ecommerce)   # minimo, quartili, media, massimo, NA

# 10.000 ordini, 17 colonne. int e num sono numeri, chr è testo.


# ---- 3. Il valore mancante: NA --------------------------------

mean(ecommerce$Age)                  # NA: basta un mancante
mean(ecommerce$Age, na.rm = TRUE)    # 38.4: media di chi ha l'età

sum(is.na(ecommerce$Age))            # 1500 età mancanti

# NA non è zero e non è "falso": è "non lo so".
NA > 50          # NA: non so se è maggiore di 50
NA == NA         # NA: due cose che non conosco non so se sono uguali
is.na(NA)        # TRUE: questa è l'unica domanda giusta


# ---- 4. Le categorie: i fattori -------------------------------

summary(ecommerce$Membership)        # per il testo summary non conta

ecommerce$Membership <- as.factor(ecommerce$Membership)
ecommerce$ProductCategory <- as.factor(ecommerce$ProductCategory)
ecommerce$Gender <- as.factor(ecommerce$Gender)

summary(ecommerce$Membership)        # Basic 5152, Gold 1600, Silver 3248


# ---- 5. Righe e colonne con le parentesi quadre ---------------

# Su un data frame: tabella[righe, colonne]
ecommerce[1:3, ]                                # prime tre righe, tutte le colonne
head(ecommerce[, c("CustomerID", "Age")])       # due colonne (head: solo le prime righe)

giovani <- ecommerce[ecommerce$Age < 35, ]
nrow(giovani)                                   # 5023 ... troppi?
sum(is.na(giovani$CustomerID))                  # 1500 righe tutte NA!

# Con le quadre, una condizione NA produce una riga di NA.
# Bisogna escluderli a mano:
giovani <- ecommerce[ecommerce$Age < 35 & !is.na(ecommerce$Age), ]
nrow(giovani)                                   # 3523

# Funziona, ma è già illeggibile. Per questo esiste dplyr.


# ---- 6. I verbi di dplyr --------------------------------------

# install.packages("dplyr")    # solo la prima volta
library(dplyr)

# head() solo per non riempire la console con 10.000 righe.
head(select(ecommerce, CustomerID, Age))            # colonne
head(filter(ecommerce, Age < 35))                   # righe (gli NA spariscono)
head(arrange(ecommerce, desc(TotalAmount)))         # ordina
head(mutate(ecommerce, gruppo_eta = ifelse(Age < 35, "Giovane", "Adulto")))
summarise(ecommerce, eta_media = mean(Age, na.rm = TRUE), ordini = n())

# ifelse(condizione, se_vero, se_falso) è l'if del modulo 2
# applicato a tutta la colonna in un colpo.
# n() conta le righe.

nrow(filter(ecommerce, Age < 35))                   # 3523, come sopra


# ---- 7. group_by: una riga per gruppo -------------------------

ecommerce_per_tessera <- group_by(ecommerce, Membership)
summarise(ecommerce_per_tessera, eta_media = mean(Age, na.rm = TRUE), ordini = n())

# group_by da solo non cambia niente: divide la tabella in gruppi,
# e il summarise successivo produce una riga per gruppo.


# ---- 8. La pipe: un verbo per riga ----------------------------

# Annidati si leggono dall'interno all'esterno:
summarise(group_by(filter(ecommerce, !is.na(Age)), Membership), eta_media = mean(Age))

# Con la pipe %>% si leggono dall'alto in basso, come una ricetta.
# (In RStudio: Ctrl+Shift+M, su Mac Cmd+Shift+M)
ecommerce %>%
  filter(!is.na(Age)) %>%
  group_by(Membership) %>%
  summarise(eta_media = mean(Age))

ecommerce %>%
  select(CustomerID, Age) %>%
  filter(!is.na(Age)) %>%
  mutate(gruppo_eta = ifelse(Age < 35, "Giovane", "Adulto")) %>%
  group_by(gruppo_eta) %>%
  summarise(n = n())


# ---- 9. Due domande sull'ecommerce ----------------------------

# Quale categoria fattura di più?
ecommerce %>%
  group_by(ProductCategory) %>%
  summarise(ordini = n(), fatturato = sum(TotalAmount)) %>%
  arrange(desc(fatturato))

# Ordini quasi uguali per categoria, fatturato molto diverso:
# l'elettronica fattura 14 volte i libri.

# Quale categoria ha più resi?
ecommerce %>%
  group_by(ProductCategory) %>%
  summarise(quota_resi = mean(ReturnStatus)) %>%
  arrange(desc(quota_resi))

# ReturnStatus vale 0 o 1: la media di una colonna 0/1 è la
# PROPORZIONE di 1. Abbigliamento: 46% di resi; elettronica: 24%.


# Adesso: ecommerce.R (tre domande da fare voi), poi il lab titanic.R
