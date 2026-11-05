# ==============================================================
# LAB - La campagna telefonica                 Lezione 10, A.A. 2026/27
#
# Dati:  campagna_banca.csv, una riga per cliente chiamato (4521)
#
#   cliente                 identificativo
#   eta, lavoro, stato_civile, istruzione
#   insolvente              "si" se non ha pagato un debito
#   saldo                   saldo medio annuo del conto, in euro
#                           (sotto zero = in rosso)
#   mutuo, prestito         "si" / "no"
#   contatto                cellulare o fisso (NA se non registrato)
#   giorno, mese            quando è stato chiamato
#   durata                  secondi dell'ultima telefonata
#   chiamate                telefonate in questa campagna
#   giorni_da_contatto, contatti_prima, esito_prima
#                           la campagna precedente
#   sottoscrive             1 = ha aperto il deposito, 0 = no
#
# Una pipe per domanda (e un grafico dove è chiesto). Prima di
# eseguire scrivete in un commento il risultato che vi aspettate;
# dopo, controllate gli NA e il denominatore.
# ==============================================================

library(dplyr)
library(ggplot2)
campagna <- read.csv("campagna_banca.csv")

str(campagna)
summary(campagna)


# ---- Parte A ---------------------------------------------------

# 1. Quanti clienti hanno più di 60 anni? Quanti di loro hanno
#    sottoscritto il deposito?



# 2. Quanti clienti hanno il conto in rosso (saldo sotto zero)?
#    Sottoscrivono più o meno degli altri?



# 3. Quota di sì per stato civile, dalla più alta alla più bassa.
#    Poi un grafico a colonne.



# 4. Quota di sì per istruzione. Quanti clienti non hanno
#    l'istruzione? Toglieteli e fate il grafico.



# 5. Chiamati al fisso o al cellulare: chi dice più sì?



# 6. Quale lavoro ha il saldo mediano più alto? E il più basso?
#    Poi un boxplot del saldo per lavoro (fino a 10.000 euro).



# 7. I 10 clienti con il saldo più alto: che lavoro fanno, quanti
#    anni hanno, hanno sottoscritto?



# 8. Un istogramma dell'età per chi sottoscrive e uno per chi no.



# ---- Extra -----------------------------------------------------

# 9. Quanti clienti sono insolventi? Sottoscrivono meno?



# 10. I clienti chiamati più di 10 volte: quanti sono, quanti hanno
#     detto sì, e quanto è durata in media l'ultima telefonata?


