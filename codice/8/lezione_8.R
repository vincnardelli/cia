# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 8 - Dati: ripasso dell'ecommerce, poi il Titanic
# ==============================================================
#
# File che servono, nella stessa cartella di questo script
# (si scaricano dalla pagina del modulo 6 sul sito):
#   ecommerce.csv   una riga per ordine
#   titanic.csv     una riga per passeggero
#
# In RStudio: Session > Set Working Directory > To Source File Location
#
# Il percorso completo, passo per passo, è in lezione_7.R.
# Qui lo stesso percorso in breve, e la parte che non avevamo fatto.


# ---- 1. Leggere e guardare la tabella --------------------------

library(dplyr)
ecommerce <- read.csv("ecommerce.csv")

str(ecommerce)       # 10.000 righe, 17 colonne, e il tipo di ognuna
summary(ecommerce)   # Age ha 1500 NA

ecommerce$Membership <- as.factor(ecommerce$Membership)
summary(ecommerce$Membership)        # Basic 5152, Gold 1600, Silver 3248


# ---- 2. NA: il valore che non c'è -----------------------------

mean(ecommerce$Age)                  # NA
mean(ecommerce$Age, na.rm = TRUE)    # 38.4, calcolata su 8500 ordini

# Con le quadre una condizione NA diventa una riga di NA:
nrow(ecommerce[ecommerce$Age < 35, ])                          # 5023 (sbagliato)
nrow(ecommerce[ecommerce$Age < 35 & !is.na(ecommerce$Age), ])  # 3523

# filter invece tiene solo i TRUE, e gli NA spariscono da soli:
nrow(filter(ecommerce, Age < 35))                              # 3523


# ---- 3. I verbi, uno per riga con la pipe ----------------------
#
#   select     sceglie le colonne
#   filter     sceglie le righe
#   arrange    ordina (desc() dal più grande)
#   mutate     aggiunge una colonna calcolata
#   summarise  riduce a una riga di statistiche; n() conta
#   group_by   divide in gruppi: il summarise dopo fa una riga per gruppo
#
# x %>% f(y) vuol dire f(x, y). In RStudio: Ctrl+Shift+M (Mac: Cmd+Shift+M)

ecommerce %>%
  select(CustomerID, Age) %>%
  filter(!is.na(Age)) %>%
  mutate(gruppo_eta = ifelse(Age < 35, "Giovane", "Adulto")) %>%
  group_by(gruppo_eta) %>%
  summarise(n = n())

#   Adulto   4977
#   Giovane  3523


# ---- 4. La parte nuova: domande vere sull'ecommerce ------------

# Età media e numero di ordini per tessera
ecommerce %>%
  filter(!is.na(Age)) %>%
  group_by(Membership) %>%
  summarise(eta_media = mean(Age), ordini = n())

# Quale categoria fattura di più?
ecommerce %>%
  group_by(ProductCategory) %>%
  summarise(ordini = n(), fatturato = sum(TotalAmount)) %>%
  arrange(desc(fatturato))

# Ordini quasi uguali per categoria (circa 2000), fatturato molto
# diverso: l'elettronica fattura 14 volte i libri.

# Quale categoria ha più resi?
ecommerce %>%
  group_by(ProductCategory) %>%
  summarise(quota_resi = mean(ReturnStatus)) %>%
  arrange(desc(quota_resi))

# ReturnStatus vale 0 o 1: la media di una colonna 0/1 è la
# PROPORZIONE di 1. Abbigliamento 46% di resi, elettronica 24%.
# Lo stesso trucco servirà sul Titanic con Survived.

# I dieci ordini più cari
ecommerce %>%
  arrange(desc(TotalAmount)) %>%
  select(OrderID, ProductCategory, ProductName, Quantity, TotalAmount) %>%
  head(10)


# ---- 5. Prova tu -----------------------------------------------
# Le tre domande di ecommerce.R (lezione 7): una pipe ciascuna.
#   1. Quanti ordini sono stati pagati con PayPal?
#   2. Quale corriere consegna più in fretta, in giorni medi?
#   3. I clienti Gold spendono di più per ordine dei clienti Basic?



# Adesso il lab: titanic.R (lezione 7), con titanic.csv.
