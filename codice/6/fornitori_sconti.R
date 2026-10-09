# ==============================================================
# LAB 3 - Due fornitori, con lo sconto        Lezione 6, A.A. 2026/27
#
# Stesso ordine del lab 2, ma ogni fornitore fa uno sconto a chi
# supera una soglia di spesa.
#
#            Carta   Penne   Cartucce   Spedizione   Sconto
#   A          20      30       40           8       -12 da 70 €
#   B          22      32       38           5        -5 da 90 €
#
# Lo sconto si calcola sui prodotti, PRIMA della spedizione, e la
# soglia è compresa: a 70 € esatti lo sconto di A spetta.
#
# Input:   le scelte, una lettera per prodotto: "A" oppure "B"
# Output:  il costo totale dell'ordine
# ==============================================================

prodotti <- c("Carta", "Penne", "Cartucce")
prezzi_a <- c(20, 30, 40)
prezzi_b <- c(22, 32, 38)

spedizione_a <- 8
spedizione_b <- 5

minimo_sconto_a <- 70
sconto_a <- 12

minimo_sconto_b <- 90
sconto_b <- 5


# ---- Prima funzione: il costo di un ordine già deciso ----------
# L'ordine dei tre passaggi conta: prima si sommano i prodotti,
# poi si toglie lo sconto, e solo alla fine si aggiunge la
# spedizione. Uno sconto applicato dopo la spedizione sarebbe
# un'altra regola, e darebbe un altro numero.

costo <- function(scelte){
  totale_a <- sum(prezzi_a[scelte == "A"])
  totale_b <- sum(prezzi_b[scelte == "B"])

  if(totale_a >= minimo_sconto_a){
    totale_a <- totale_a - sconto_a
  }
  if(totale_b >= minimo_sconto_b){
    totale_b <- totale_b - sconto_b
  }

  if(totale_a > 0){
    totale_a <- totale_a + spedizione_a
  }
  if(totale_b > 0){
    totale_b <- totale_b + spedizione_b
  }

  return(totale_a + totale_b)
}

costo(c("A", "A", "A"))   # 90 - 12 + 8 = 86
costo(c("B", "B", "B"))   # 92 - 5 + 5  = 92
costo(c("B", "A", "A"))   # A: 70 esatti -> sconto, 70-12+8 = 66; B: 22+5 = 27 -> 93


# ---- Seconda funzione: prova tutte le combinazioni -------------
# Identica al lab 2: cambia solo la regola dentro costo().

minimo <- function(scelte){
  if(length(scelte) == length(prodotti)){
    return(costo(scelte))
  }

  con_a <- minimo(c(scelte, "A"))
  con_b <- minimo(c(scelte, "B"))

  return(min(con_a, con_b))
}

minimo(c())   # 86 euro: tutto da A

# Nel lab 2, senza sconti, il minimo era 97 euro ordinando tutto
# da B. Una regola in più e la risposta cambia fornitore: è il
# motivo per cui le combinazioni si provano tutte, invece di
# ragionare "a occhio" prodotto per prodotto.


# ---- Tutte le combinazioni, per vederle ------------------------

minimo_con_stampa <- function(scelte){
  if(length(scelte) == length(prodotti)){
    c_tot <- costo(scelte)
    print(paste0(paste(scelte, collapse = " "), " -> ", c_tot, " euro"))
    return(c_tot)
  }

  con_a <- minimo_con_stampa(c(scelte, "A"))
  con_b <- minimo_con_stampa(c(scelte, "B"))

  return(min(con_a, con_b))
}

minimo_con_stampa(c())

# A A A -> 86    B A A -> 93    (le due combinazioni con lo sconto di A)
# B B B -> 92    tutte le altre sopra i 100


# ---- Il caso al confine ----------------------------------------
# "da 70 euro" vuol dire 70 compreso. L'ordine B A A lascia ad A
# esattamente 70 euro di prodotti: lo sconto spetta.

totale_a_test <- prezzi_a[2] + prezzi_a[3]
totale_a_test                      # 70

totale_a_test >= minimo_sconto_a   # TRUE con >=, FALSE con >

# Scritto con > al posto di >= il programma gira lo stesso e dà
# 105 euro invece di 93 per quella combinazione: il solito confine.


# ---- Da provare in aula ----------------------------------------
# 1. Alzate la soglia di A a 80 euro: lo sconto scatta solo con
#    l'ordine completo, e il minimo torna vicino al lab 2.
# 2. Portate lo sconto di B a 15 euro da 90: chi vince adesso?
# 3. Applicate lo sconto dopo la spedizione invece che prima:
#    cambia qualche risultato? E la combinazione migliore?
