# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 10 - Un'analisi completa: la campagna telefonica
# ==============================================================
#
# File che serve, nella stessa cartella di questo script
# (si scarica dalla pagina del modulo sul sito):
#   campagna_banca.csv   una riga per cliente chiamato
#
# In RStudio: Session > Set Working Directory > To Source File Location
#
# Una banca portoghese telefona a 4.521 clienti per proporre un
# deposito vincolato (dati veri, 2008-2010).
#
#   DOMANDA DI BUSINESS: chi conviene chiamare, e quando?
#
# Usiamo tutto quello che abbiamo visto nelle lezioni 7, 8 e 9:
# i verbi di dplyr e i grafici di ggplot. Le cose nuove sono due,
# e sono segnate con  # NUOVO.


# ---- 0. Pacchetti ----------------------------------------------

library(dplyr)
library(ggplot2)
library(GGally)      # ggpairs
library(corrplot)    # corrplot

colori <- c("no" = "grey70", "si" = "darkblue")   # per chi sottoscrive


# ---- 1. Leggere e guardare la tabella ---------------------------

campagna <- read.csv("campagna_banca.csv")

head(campagna)
str(campagna)
summary(campagna)
nrow(campagna)       # 4521 clienti
ncol(campagna)       # 18 colonne

#   eta, lavoro, stato_civile, istruzione   chi è il cliente
#   saldo                                   saldo medio annuo del conto (euro)
#   insolvente, mutuo, prestito             debiti ("si" / "no")
#   contatto, giorno, mese                  come e quando è stato chiamato
#   durata                                  secondi dell'ultima telefonata
#   chiamate                                telefonate in questa campagna
#   giorni_da_contatto, contatti_prima,
#   esito_prima                             la campagna precedente
#   sottoscrive                             1 = ha aperto il deposito

mean(campagna$sottoscrive)    # 0.115

# sottoscrive vale 0 o 1: la media è la PROPORZIONE di 1, come
# Survived nel Titanic. Su 100 telefonate, 11 o 12 vanno a buon fine.

campagna$lavoro <- as.factor(campagna$lavoro)
summary(campagna$lavoro)      # 38 NA: lavoro non dichiarato


# ---- 2. Prima di analizzare: i valori mancanti ------------------

sum(is.na(campagna$lavoro))       # 38
sum(is.na(campagna$istruzione))   # 187
sum(is.na(campagna$contatto))     # 1324: quasi un terzo!

# Con le quadre: le righe senza contatto
senza_contatto <- campagna[is.na(campagna$contatto), ]
nrow(senza_contatto)              # 1324

# Sono sparsi a caso, o concentrati da qualche parte?
campagna %>%
  group_by(mese) %>%
  summarise(chiamate = n(), quota_senza_contatto = mean(is.na(contatto))) %>%
  arrange(desc(quota_senza_contatto))

# giu 85%, mag 59%, poi quasi zero. Non sono i clienti a essere
# diversi: a maggio e giugno qualcuno non ha registrato il canale.
# Un NA concentrato in un periodo è un indizio su come sono stati
# raccolti i dati, non sui clienti. Il contatto lo useremo poco.


# ---- 3. Insight 1: più chiami, meno vendi -----------------------

# I mesi come testo finiscono in ordine alfabetico (ago, apr, dic...).
# factor() con levels fissa l'ordine del calendario.
campagna$mese <- factor(campagna$mese,                       # NUOVO: levels
                        levels = c("gen", "feb", "mar", "apr", "mag", "giu",
                                   "lug", "ago", "set", "ott", "nov", "dic"))

# Quante telefonate ogni mese? geom_bar conta le righe da solo.
ggplot(campagna, aes(x = mese)) +
  geom_bar(fill = "darkblue") +
  theme_minimal() +
  ylab("Telefonate")

per_mese <- campagna %>%
  group_by(mese) %>%
  summarise(chiamate = n(), conversione = mean(sottoscrive))
per_mese %>% arrange(desc(conversione))

# mag: 1398 telefonate, 6.7% di sì
# ott:   80 telefonate,  46% di sì

ggplot(per_mese, aes(x = mese, y = conversione)) +
  geom_col(fill = "darkblue") +
  geom_hline(yintercept = mean(campagna$sottoscrive), color = "red", linetype = 2) +
  theme_minimal() +
  ylab("Quota di sì")

# Le due cose insieme: un punto per mese.
ggplot(per_mese, aes(x = chiamate, y = conversione)) +
  geom_point(color = "darkblue", size = 3) +
  geom_text(aes(label = mese), vjust = -1) +                 # NUOVO: geom_text
  geom_hline(yintercept = mean(campagna$sottoscrive), color = "red", linetype = 2) +
  theme_minimal() +
  xlab("Telefonate nel mese") +
  ylab("Quota di sì")

cor(per_mese$chiamate, per_mese$conversione)    # -0.69

# I mesi in cui la banca chiama tantissimo sono quelli in cui
# vende peggio. Allora bisogna chiamare a ottobre?


# ---- 4. Insight 2: è il mese, o chi chiami? ---------------------

# Prima: conta chi era già stato chiamato nella campagna precedente?
campagna %>%
  group_by(esito_prima) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive)) %>%
  arrange(desc(conversione))

# Chi aveva già detto sì: 64%. Chi non era mai stato chiamato: 9%.

# Ora mesi "rari" (marzo, settembre, ottobre, dicembre) contro gli
# altri, separando i clienti per la loro storia.
campagna <- campagna %>%
  mutate(periodo = ifelse(mese %in% c("mar", "set", "ott", "dic"),
                          "mesi rari", "altri mesi"))

storia <- campagna %>%
  group_by(esito_prima, periodo) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive), .groups = "drop")
storia

ggplot(storia, aes(x = periodo, y = conversione, fill = periodo)) +
  geom_col() +
  facet_wrap(~ esito_prima, ncol = 4) +
  scale_fill_manual(values = c("altri mesi" = "grey70", "mesi rari" = "darkblue")) +
  theme_minimal() +
  ylab("Quota di sì")

# Anche tra chi non era MAI stato chiamato: 35% nei mesi rari,
# 8% negli altri. Non è solo "chi richiami": quando la banca chiama
# poco, sceglie meglio chi chiamare. Il mese da solo non spiega,
# conta come si sceglie la lista.


# ---- 5. Insight 3: l'età a forma di U ---------------------------

# Frequenze per fascia d'età (cut, come le fasce di fatturato)
campagna <- campagna %>%
  mutate(fascia_eta = cut(eta, breaks = c(18, 25, 30, 40, 50, 60, 90)))

campagna %>%
  count(fascia_eta) %>%
  mutate(freq_rel = n / sum(n))

ggplot(campagna, aes(x = eta)) +
  geom_histogram(bins = 30, fill = "darkblue") +
  geom_vline(xintercept = mean(campagna$eta), color = "red") +
  geom_vline(xintercept = median(campagna$eta), color = "red", linetype = 2) +
  theme_minimal() +
  xlab("Età")

# Quasi tutti tra 30 e 50 anni. Ma chi dice sì?
per_fascia <- campagna %>%
  group_by(fascia_eta) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive))
per_fascia

ggplot(per_fascia, aes(x = fascia_eta, y = conversione)) +
  geom_col(fill = "darkblue") +
  geom_hline(yintercept = mean(campagna$sottoscrive), color = "red", linetype = 2) +
  theme_minimal() +
  xlab("Età") +
  ylab("Quota di sì")

# Una U: 21% sotto i 25 anni, circa 10% tra 30 e 60, 38% oltre i 60.
# La banca chiama soprattutto i clienti che rispondono meno.

# Anno per anno, solo le età con almeno 20 clienti:
campagna %>%
  group_by(eta) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive)) %>%
  filter(clienti >= 20) %>%
  ggplot(aes(x = eta, y = conversione)) +
  geom_line(color = "darkblue") +
  geom_point(color = "darkblue") +
  theme_minimal() +
  xlab("Età") +
  ylab("Quota di sì")

# È l'età o il lavoro? Pensionati e studenti stanno agli estremi.
ggplot(campagna %>% filter(!is.na(lavoro)), aes(x = eta, y = lavoro)) +
  geom_boxplot(fill = "darkblue", alpha = 0.4) +
  theme_minimal() +
  xlab("Età")

campagna %>%
  filter(lavoro %in% c("pensionato", "studente", "dirigente", "operaio")) %>%
  group_by(lavoro, fascia_eta) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive), .groups = "drop") %>%
  filter(clienti >= 15) %>%
  ggplot(aes(x = fascia_eta, y = conversione, fill = lavoro)) +
  geom_col() +
  facet_wrap(~ lavoro, ncol = 4) +
  theme_minimal() +
  xlab("Età") +
  ylab("Quota di sì")

# Pensionati tra 50 e 60 anni: 15%. Pensionati oltre i 60: 39%.
# Dentro lo stesso lavoro l'età conta ancora: sono tutte e due.


# ---- 6. Insight 4: insistere non paga ---------------------------

campagna %>% count(chiamate)       # da 1 a 50 telefonate allo stesso cliente

# Raggruppiamo "8 o più" in una sola colonna
per_chiamate <- campagna %>%
  mutate(chiamate_max8 = ifelse(chiamate >= 8, 8, chiamate)) %>%
  group_by(chiamate_max8) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive))
per_chiamate

ggplot(per_chiamate, aes(x = chiamate_max8, y = conversione)) +
  geom_col(fill = "darkblue") +
  geom_hline(yintercept = mean(campagna$sottoscrive), color = "red", linetype = 2) +
  theme_minimal() +
  xlab("Telefonate allo stesso cliente (8 = 8 o più)") +
  ylab("Quota di sì")

# Alla prima telefonata 14%; dalla quinta in poi quasi sempre sotto
# la media; dall'ottava in poi 5%.

ggplot(campagna, aes(x = chiamate, y = factor(sottoscrive), fill = factor(sottoscrive))) +
  geom_boxplot() +
  scale_fill_manual(values = c("0" = "grey70", "1" = "darkblue")) +
  theme_minimal() +
  xlab("Telefonate") +
  ylab("Sottoscrive")

# E in che giorni del mese si chiama?
campagna %>%
  group_by(giorno) %>%
  summarise(chiamate = n()) %>%
  ggplot(aes(x = giorno, y = chiamate)) +
  geom_line(color = "darkblue") +
  geom_point(color = "darkblue") +
  theme_minimal() +
  xlab("Giorno del mese") +
  ylab("Telefonate")

# Le telefonate si concentrano tra il 18 e il 21 del mese.


# ---- 7. Insight 5: soldi e debiti -------------------------------

summary(campagna$saldo)
mean(campagna$saldo)              # 1423
median(campagna$saldo)            # 444
sd(campagna$saldo)
var(campagna$saldo)
IQR(campagna$saldo)
quantile(campagna$saldo, 0.95)
sum(campagna$saldo < 0)           # 366 clienti in rosso

# Media quasi tre volte la mediana: pochi clienti molto ricchi tirano
# su la media. Il cliente "medio" da 1423 euro quasi non esiste.

# Fino a 10.000 euro, per vedere la forma (oltre ci sono 2 clienti su 100)
campagna %>%
  filter(saldo < 10000) %>%
  ggplot(aes(x = saldo)) +
  geom_histogram(binwidth = 250, boundary = 0, fill = "darkblue") +
  geom_vline(xintercept = mean(campagna$saldo), color = "red") +
  geom_vline(xintercept = median(campagna$saldo), color = "red", linetype = 2) +
  geom_vline(xintercept = 0) +
  theme_minimal() +
  xlab("Saldo (euro)")

# Il saldo serve a vendere?
campagna %>%
  mutate(fascia_saldo = cut(saldo, breaks = c(-Inf, 0, 500, 2000, 5000, Inf))) %>%
  group_by(fascia_saldo) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive))

# Chi ha già debiti con la banca?
debiti <- campagna %>%
  group_by(mutuo, prestito) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive), .groups = "drop")
debiti

ggplot(debiti, aes(x = mutuo, y = conversione, fill = prestito)) +
  geom_col() +
  facet_grid(. ~ prestito) +
  scale_fill_manual(values = colori) +
  theme_minimal() +
  xlab("Ha un mutuo") +
  ylab("Quota di sì")

# Senza mutuo né prestito: 17%. Con il solo mutuo 9%, con un prestito 6%.
# Chi deve già soldi alla banca non ne mette da parte altri.


# ---- 8. Insight 6: la variabile che sa troppo -------------------

campagna %>%
  group_by(sottoscrive) %>%
  summarise(durata_media = mean(durata), durata_mediana = median(durata))

# Chi dice sì resta al telefono più del doppio: 7 minuti contro 3 (mediane).

ggplot(campagna, aes(x = durata, fill = factor(sottoscrive))) +
  geom_histogram(binwidth = 60, boundary = 0, alpha = 0.6, position = "identity") +
  scale_fill_manual(values = c("0" = "grey70", "1" = "darkblue")) +
  theme_minimal() +
  xlab("Durata della telefonata (secondi)")

campagna %>%
  filter(durata <= 1200) %>%
  ggplot(aes(x = durata, fill = factor(sottoscrive))) +
  geom_histogram(breaks = c(0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600,
                            720, 840, 960, 1080, 1200)) +
  facet_grid(factor(sottoscrive) ~ .) +
  scale_fill_manual(values = c("0" = "grey70", "1" = "darkblue")) +
  theme_minimal() +
  xlab("Durata della telefonata (secondi)")

campagna %>%
  mutate(minuti = cut(durata, breaks = c(-Inf, 60, 120, 240, 480, Inf))) %>%
  group_by(minuti) %>%
  summarise(clienti = n(), conversione = mean(sottoscrive))

# Sotto il minuto: 0,2% di sì. Oltre gli 8 minuti: 38%.

ggplot(campagna, aes(x = durata, y = chiamate, color = factor(sottoscrive))) +
  geom_point(alpha = 0.5) +
  scale_color_manual(values = c("0" = "grey70", "1" = "darkblue")) +
  theme_minimal() +
  xlab("Durata (secondi)") +
  ylab("Telefonate")


# ---- 9. Tutte le variabili numeriche insieme --------------------

numeriche <- campagna %>%
  select(eta, saldo, durata, chiamate, contatti_prima, sottoscrive)

cov(campagna$durata, campagna$sottoscrive)
cor(campagna$durata, campagna$sottoscrive)      # 0.40
cor(campagna$chiamate, campagna$sottoscrive)    # -0.06
round(cor(numeriche), 2)

ggpairs(numeriche)
corrplot(cor(numeriche))

# La durata è di gran lunga la variabile più legata al sì.
# Venerdì una macchina imparerà da sola chi dice sì: sceglierebbe
# la durata per prima. Ma la durata si conosce solo DOPO aver
# telefonato: per decidere chi chiamare non serve a niente.
# Una variabile che sa il risultato prima di noi si chiama leakage.


# ---- 10. Le risposte alla domanda di business ------------------
#
#   1. Più telefonate non vogliono dire più vendite: a maggio 1398
#      chiamate e 7% di sì, a ottobre 80 chiamate e 46%.
#   2. Il segreto è la lista: chi aveva già detto sì converte al 64%,
#      e nei mesi in cui si chiama poco si sceglie meglio.
#   3. L'età fa una U: giovani e over 60 rispondono meglio, ma la
#      banca chiama soprattutto i 30-50enni.
#   4. Oltre la quarta telefonata allo stesso cliente si spreca tempo.
#   5. Chi ha mutuo e prestito non apre depositi.
#   6. La durata predice tutto ma arriva troppo tardi: attenzione
#      alle variabili che conoscono già la risposta.


# ---- 11. Adesso il laboratorio --------------------------------
# lab_campagna.R: dieci domande sugli stessi dati, poi le correggiamo
# insieme.
