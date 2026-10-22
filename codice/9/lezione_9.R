library(dplyr)
library(ggplot2)
library(corrplot)
library(GGally)

vendite <- read.csv("business_intelligence.csv")
vendite$prodotto <- 1:nrow(vendite)

str(vendite)
summary(vendite)

vendite %>%
  group_by(categoria) %>%
  summarise(prodotti = n(),
            fatturato_totale = sum(fatturato),
            prezzo_medio = mean(prezzo),
            valutazione_media = mean(valutazione_clienti))


# Frequenza

vendite <- vendite %>%
  mutate(fascia = cut(fatturato, breaks = c(0, 50000, 100000, 150000, 200000, Inf)))

vendite %>%
  count(fascia) %>%
  mutate(freq_rel = n / sum(n))

ggplot(vendite, aes(x = fatturato, fill = fascia)) +
  geom_histogram(breaks = c(0, 50000, 100000, 150000, 200000, 325000)) +
  theme_minimal() +
  xlab("Fatturato")

ggplot(vendite, aes(x = fatturato, fill = fascia)) +
  geom_histogram(binwidth = 25000, boundary = 0) +
  theme_minimal() +
  xlab("Fatturato")


# Distribuzione

ggplot(vendite, aes(x = prodotto, y = fatturato)) +
  geom_point(color = "darkblue") +
  theme_minimal() +
  ylab("Fatturato")

ggplot(vendite, aes(y = fatturato)) +
  geom_histogram(binwidth = 25000, boundary = 0, fill = "darkblue") +
  theme_minimal() +
  ylab("Fatturato")

summary(vendite$fatturato)

ggplot(vendite, aes(x = fatturato)) +
  geom_histogram(binwidth = 25000, boundary = 0, fill = "darkblue") +
  geom_vline(xintercept = min(vendite$fatturato)) +
  geom_vline(xintercept = quantile(vendite$fatturato, 0.25)) +
  geom_vline(xintercept = median(vendite$fatturato)) +
  geom_vline(xintercept = mean(vendite$fatturato)) +
  geom_vline(xintercept = quantile(vendite$fatturato, 0.75)) +
  geom_vline(xintercept = max(vendite$fatturato)) +
  theme_minimal() +
  xlab("Fatturato")

ggplot(vendite, aes(x = fatturato)) +
  geom_boxplot(fill = "darkblue", alpha = 0.4) +
  theme_minimal() +
  xlab("Fatturato")

Q1 <- quantile(vendite$fatturato, 0.25)
Q3 <- quantile(vendite$fatturato, 0.75)
IQR_value <- IQR(vendite$fatturato)

lower_whisker_limit <- Q1 - 1.5 * IQR_value
upper_whisker_limit <- Q3 + 1.5 * IQR_value

ggplot(vendite, aes(x = fatturato)) +
  geom_histogram(binwidth = 25000, boundary = 0, fill = "darkblue") +
  geom_vline(xintercept = Q1) +
  geom_vline(xintercept = median(vendite$fatturato), color = "red") +
  geom_vline(xintercept = Q3) +
  geom_vline(xintercept = lower_whisker_limit, linetype = 2) +
  geom_vline(xintercept = upper_whisker_limit, linetype = 2) +
  theme_minimal() +
  xlab("Fatturato")


# Variabilità

sd(vendite$fatturato)
var(vendite$fatturato)

media <- mean(vendite$fatturato)
dev_std <- sd(vendite$fatturato)

ggplot(vendite, aes(x = prodotto, y = fatturato)) +
  geom_point(color = "darkblue") +
  geom_hline(yintercept = media, color = "red") +
  geom_hline(yintercept = media - dev_std, color = "red", linetype = 2) +
  geom_hline(yintercept = media + dev_std, color = "red", linetype = 2) +
  theme_minimal() +
  ylab("Fatturato")

due <- vendite %>%
  filter(categoria %in% c("Elettronica", "Sport")) %>%
  group_by(categoria) %>%
  mutate(prodotto = row_number())

ggplot(due, aes(x = prodotto, y = fatturato, color = categoria)) +
  geom_point() +
  scale_color_manual(values = c("Elettronica" = "steelblue", "Sport" = "firebrick")) +
  theme_minimal() +
  ylab("Fatturato")

due %>%
  group_by(categoria) %>%
  summarise(media = mean(fatturato), dev_std = sd(fatturato))

ggplot(due, aes(x = fatturato, fill = categoria)) +
  geom_histogram(binwidth = 25000, boundary = 0) +
  facet_wrap(~ categoria) +
  scale_fill_manual(values = c("Elettronica" = "steelblue", "Sport" = "firebrick")) +
  theme_minimal() +
  xlab("Fatturato")


# Confronto

vendite %>%
  group_by(categoria) %>%
  summarise(fatturato_medio = mean(fatturato)) %>%
  ggplot(aes(x = categoria, y = fatturato_medio, fill = categoria)) +
  geom_col() +
  theme_minimal() +
  ylab("Fatturato medio")

ggplot(vendite, aes(x = categoria, y = fatturato, fill = categoria)) +
  geom_boxplot() +
  theme_minimal() +
  ylab("Fatturato")

ggplot(vendite, aes(x = fatturato, fill = categoria)) +
  geom_histogram(binwidth = 25000, boundary = 0) +
  facet_grid(categoria ~ .) +
  theme_minimal() +
  xlab("Fatturato")

ggplot(vendite, aes(x = fatturato, y = categoria, fill = categoria)) +
  geom_boxplot() +
  theme_minimal() +
  xlab("Fatturato")


# Forma

skewness <- function(x) {
  n <- length(x)
  n / ((n - 1) * (n - 2)) * sum(((x - mean(x)) / sd(x))^3)
}

skewness(vendite$valutazione_clienti)
skewness(vendite$tasso_reso)
skewness(vendite$prezzo)

ggplot(vendite, aes(x = valutazione_clienti)) +
  geom_histogram(bins = 15, fill = "darkblue") +
  geom_vline(xintercept = mean(vendite$valutazione_clienti), color = "red") +
  geom_vline(xintercept = median(vendite$valutazione_clienti), color = "red", linetype = 2) +
  theme_minimal()

ggplot(vendite, aes(x = prezzo)) +
  geom_histogram(bins = 15, fill = "darkblue") +
  geom_vline(xintercept = mean(vendite$prezzo), color = "red") +
  geom_vline(xintercept = median(vendite$prezzo), color = "red", linetype = 2) +
  theme_minimal()

vendite %>%
  group_by(categoria) %>%
  summarise(media = mean(fatturato),
            dev_std = sd(fatturato),
            skewness = skewness(fatturato))

vendite %>%
  filter(categoria %in% c("Abbigliamento", "Alimentari")) %>%
  ggplot(aes(x = fatturato, fill = categoria)) +
  geom_histogram(binwidth = 25000, boundary = 0, alpha = 0.6, position = "identity") +
  theme_minimal() +
  xlab("Fatturato")


# Curtosi

curtosi <- function(x) {
  m <- mean(x)
  mean((x - m)^4) / mean((x - m)^2)^2 - 3
}

vendite %>%
  summarise(media = mean(costo_magazzino), mediana = median(costo_magazzino),
            skewness = skewness(costo_magazzino), curtosi = curtosi(costo_magazzino))

vendite %>%
  summarise(media = mean(giorni_giacenza), mediana = median(giorni_giacenza),
            skewness = skewness(giorni_giacenza), curtosi = curtosi(giorni_giacenza))

ggplot(vendite, aes(x = costo_magazzino)) +
  geom_histogram(bins = 20, fill = "darkblue") +
  theme_minimal()

ggplot(vendite, aes(x = giorni_giacenza)) +
  geom_histogram(bins = 20, fill = "darkblue") +
  theme_minimal()

pareto <- vendite %>%
  arrange(desc(costo_magazzino)) %>%
  mutate(posizione = row_number(),
         quota_cumulata = cumsum(costo_magazzino) / sum(costo_magazzino))

pareto %>% select(codice_prodotto, costo_magazzino, quota_cumulata) %>% head(10)

ggplot(pareto, aes(x = posizione, y = quota_cumulata)) +
  geom_col(fill = "darkblue") +
  geom_hline(yintercept = 0.8, color = "red", linetype = 2) +
  theme_minimal()


domanda <- read.csv("domanda_giornaliera.csv")

domanda %>%
  group_by(prodotto) %>%
  summarise(media = mean(unita), dev_std = sd(unita),
            skewness = skewness(unita), curtosi = curtosi(unita),
            giorni_oltre_140 = sum(unita > 140), massimo = max(unita))

ggplot(domanda, aes(x = giorno, y = unita, color = prodotto)) +
  geom_line() +
  geom_hline(yintercept = 140, linetype = 2) +
  facet_wrap(~ prodotto, ncol = 1) +
  theme_minimal()

ggplot(domanda, aes(x = unita, fill = prodotto)) +
  geom_histogram(binwidth = 5) +
  facet_wrap(~ prodotto) +
  theme_minimal()

ggplot(domanda, aes(x = unita, y = prodotto, fill = prodotto)) +
  geom_boxplot() +
  theme_minimal()


mean(vendite$ritardo_fornitore_giorni)
median(vendite$ritardo_fornitore_giorni)
quantile(vendite$ritardo_fornitore_giorni, 0.95)
skewness(vendite$ritardo_fornitore_giorni)
curtosi(vendite$ritardo_fornitore_giorni)

ggplot(vendite, aes(x = ritardo_fornitore_giorni)) +
  geom_histogram(binwidth = 1, fill = "darkblue") +
  geom_vline(xintercept = mean(vendite$ritardo_fornitore_giorni), color = "red") +
  geom_vline(xintercept = quantile(vendite$ritardo_fornitore_giorni, 0.95), color = "red", linetype = 3) +
  theme_minimal()


recensioni <- read.csv("recensioni.csv")

recensioni %>%
  group_by(prodotto) %>%
  summarise(media = mean(stelle), dev_std = sd(stelle),
            curtosi = curtosi(stelle), una_stella = mean(stelle == 1))

ggplot(recensioni, aes(x = factor(stelle), fill = prodotto)) +
  geom_bar() +
  facet_wrap(~ prodotto) +
  theme_minimal()


# Bivariata

ggplot(vendite, aes(x = valutazione_clienti, y = fatturato)) +
  geom_point(color = "darkblue") +
  theme_minimal()

ggplot(vendite, aes(x = numero_recensioni, y = unita_vendute)) +
  geom_point(color = "darkblue") +
  theme_minimal()

ggplot(vendite, aes(x = valutazione_clienti, y = tasso_reso)) +
  geom_point(color = "darkblue") +
  theme_minimal()

numeriche <- vendite %>%
  select(prezzo, unita_vendute, numero_recensioni, fatturato,
         valutazione_clienti, tasso_reso)

ggpairs(numeriche, upper = list(continuous = "blank"))


# Correlazione

cov(vendite$valutazione_clienti, vendite$tasso_reso)
cor(vendite$valutazione_clienti, vendite$tasso_reso)
cor(vendite$numero_recensioni, vendite$unita_vendute)
cor(vendite$valutazione_clienti, vendite$fatturato)

ggpairs(numeriche)

round(cor(numeriche), 2)
corrplot(cor(numeriche))
