# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 3 - Le prime regole in R
# Venerdì 25 settembre 2026
#
# Come si usa: apri questo file in RStudio, metti il cursore su una
# riga e premi Ctrl + Invio (su Mac: Cmd + Invio). Il risultato
# compare in basso, nella Console.
# ==============================================================


# ---- 1. R è una calcolatrice ---------------------------------

1 + 2
10 - 4
2 * 3
7 / 2
2^10

# Le parentesi funzionano come in matematica
(1 + 2) * 3


# ---- 2. Una variabile è un nome dato a un valore -------------

risultato <- 2 * 2   # "<-" si legge "prende il valore"
risultato
risultato + 3        # usa il valore, ma non lo cambia
risultato

risultato <- risultato + 3   # così invece lo cambia
risultato


# ---- 3. Tre tipi di dato --------------------------------------

prezzo  <- 19.90       # numeric: un numero
cliente <- "Giorgio"   # character: un testo, sempre tra virgolette
pagato  <- TRUE        # logical: vero o falso

class(prezzo)
class(cliente)
class(pagato)

# Le virgolette cambiano tutto: "21" è un testo, non un numero
21 + 1
# "21" + 1   # togli il # e prova: R risponde con un errore


# ---- 4. Dare i nomi -------------------------------------------

nome_cliente <- "Giorgio"
NomeCliente  <- "Antonio"
nomecliente  <- "Luca"
nomecliente1 <- "Roberto"

# Sono tre variabili diverse: R distingue maiuscole e minuscole
nome_cliente
NomeCliente
nomecliente

# Nomi NON validi (togli il # e guarda l'errore):
# 1cliente <- "Marco"       # non può iniziare con un numero
# nome cliente <- "Marco"   # niente spazi


# ---- 5. Un vettore: tanti valori, un solo nome -----------------

clienti <- c("Antonio", "Luca", "Giorgio")
eta <- c(23, 19, 93)
clienti
eta

# Non è la stessa cosa di un testo con le virgole
clienti_stringa <- "Antonio, Luca, Giorgio"
length(clienti)           # 3 elementi
length(clienti_stringa)   # 1 elemento solo


# ---- 6. Le parentesi quadre: si conta da 1 ---------------------

clienti[3]
eta[3]
1:3             # i numeri da 1 a 3
clienti[2:3]
clienti[c(1, 3)]


# ---- 7. Un confronto risponde TRUE o FALSE ---------------------

1 == 1          # uguale: DUE simboli di uguale
1 == 2
18 > 12
12 <= 90
"Luca" != "Giorgio"   # diverso


# ---- 8. Il confronto su un vettore -----------------------------

eta < 35
eta == 19

clienti[c(TRUE, FALSE, TRUE)]   # tiene solo i TRUE
clienti[eta < 35]               # i clienti con meno di 35 anni


# ---- 9. if / else: il computer sceglie una strada ---------------

voto <- 12
voto >= 18

if(voto >= 18){
  status <- "Promosso"
}else{
  status <- "Bocciato"
}
status

# Prova con voto <- 17, 18 e 19: il 18 è il confine


# ---- 10. else if: più di due strade ----------------------------

voto <- 28

if(voto < 18){
  giudizio <- "Bocciato"
}else if(voto < 27){
  giudizio <- "Promosso"
}else{
  giudizio <- "Ottimo"
}
giudizio

# R prova le condizioni dall'alto e si ferma alla prima vera


# ---- 11. E, o, non: & | ! ---------------------------------------

eta_cliente <- 24
giorno <- "sabato"

eta_cliente >= 18 & eta_cliente <= 25        # e: vere tutte e due
giorno == "sabato" | giorno == "domenica"    # o: ne basta una
!(eta_cliente >= 18)                         # non: rovescia


# ---- 12. %in%: è uno di questi? ---------------------------------

giorno %in% c("sabato", "domenica")
5 %in% 1:10
11 %in% 1:10


# Adesso i tre lab di oggi, uno per file:
#   boomer.R       chi è nato dal 1946 al 1964
#   autovelox.R    la multa secondo l'art. 142
#   prezzi_voli.R  il prezzo del biglietto (con l'AI ammessa)
#
# Per ognuno: scrivi la regola, poi provala sui confini.
