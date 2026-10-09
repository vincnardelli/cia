# ==============================================================
# LAB 1 - Biglietti e carnet                  Lezione 6, A.A. 2026/27
#
# Tariffe inventate per l'esercizio:
#   un biglietto singolo .... 3 €
#   un carnet da cinque ..... 10 €   (i viaggi possono avanzare)
#
# Input:   viaggi   quanti viaggi devi fare
# Output:  la spesa minima, in euro
#
# L'idea: per ogni viaggio da fare ci sono due strade, comprare un
# singolo o comprare un carnet. La funzione prova tutte e due e
# tiene la più economica. Per sapere quanto costa "il resto del
# viaggio" chiama sé stessa: è la RICORSIONE.
# ==============================================================


# ---- La soluzione ---------------------------------------------

costo_minimo <- function(viaggi){
  if(viaggi <= 0){
    return(0)                      # caso base: niente da fare, niente da pagare
  }

  con_singolo <- 3 + costo_minimo(viaggi - 1)    # pago 3 e resta un viaggio in meno
  con_carnet <- 10 + costo_minimo(viaggi - 5)    # pago 10 e restano cinque viaggi in meno

  return(min(con_singolo, con_carnet))           # tengo la strada più economica
}

costo_minimo(4)   # 10 euro
costo_minimo(6)   # 13 euro


# ---- Perché funziona ------------------------------------------
# Due pezzi, sempre gli stessi in ogni funzione ricorsiva:
#   1. il CASO BASE, che non richiama niente: viaggi <= 0 -> 0
#   2. il PASSO, che richiama la funzione su un problema più piccolo
#
# Senza il caso base la funzione non si ferma più: provate a
# togliere le prime tre righe e R si blocca con
# "evaluation nested too deeply".
#
# Attenzione a <= 0 e non == 0: con il carnet si scende sotto zero
# (6 - 5 = 1, ma 4 - 5 = -1). Con == 0 la funzione non si fermerebbe.


# ---- Tutti i casi da 0 a 12 ------------------------------------

for(v in 0:12){
  print(paste0(v, " viaggi: ", costo_minimo(v), " euro"))
}

# 0:0  1:3  2:6  3:9  4:10  5:10  6:13  7:16  8:19  9:20  10:20 ...
#
# Da guardare insieme:
#   a 4 viaggi conviene già il carnet (10 invece di 12): si butta via un viaggio
#   a 5 costa come a 4
#   a 9 conviene un carnet più quattro singoli? No: due carnet, 20 euro
#   il prezzo non cresce di 3 ogni volta: è questo che rende il problema interessante


# ---- Varianti da provare in aula -------------------------------
# Cambiate i prezzi dentro la funzione e guardate come cambia la
# scelta: con il carnet a 16 euro non conviene quasi mai, con il
# carnet a 9 conviene quasi sempre.

costo_minimo_parametrico <- function(viaggi, prezzo_singolo, prezzo_carnet){
  if(viaggi <= 0){
    return(0)
  }

  con_singolo <- prezzo_singolo + costo_minimo_parametrico(viaggi - 1, prezzo_singolo, prezzo_carnet)
  con_carnet <- prezzo_carnet + costo_minimo_parametrico(viaggi - 5, prezzo_singolo, prezzo_carnet)

  return(min(con_singolo, con_carnet))
}

costo_minimo_parametrico(6, 3, 10)   # 13, come prima
costo_minimo_parametrico(6, 3, 16)   # 18: il carnet non conviene più
costo_minimo_parametrico(6, 3, 9)    # 12: conviene sempre il carnet
