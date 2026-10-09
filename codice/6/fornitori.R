# ==============================================================
# LAB 2 - Due fornitori                       Lezione 6, A.A. 2026/27
#
# L'ufficio acquisti deve comprare tre prodotti. Ogni prodotto si
# può prendere dal fornitore A o dal fornitore B, a prezzi diversi.
# Ogni fornitore da cui si ordina aggiunge la sua spedizione, e le
# due spedizioni costano diverso.
#
#            Carta   Penne   Cartucce   Spedizione
#   A          20      30       40          8
#   B          22      32       38          5
#
# Input:   le scelte, una lettera per prodotto: "A" oppure "B"
# Output:  il costo totale dell'ordine, spedizioni comprese
#
# La domanda: qual è la combinazione che costa meno? Le possibilità
# sono 2 x 2 x 2 = 8. Invece di scriverle a mano, le costruiamo
# una alla volta con una funzione che chiama sé stessa.
# ==============================================================

prodotti <- c("Carta", "Penne", "Cartucce")
prezzi_a <- c(20, 30, 40)
prezzi_b <- c(22, 32, 38)
spedizione_a <- 8
spedizione_b <- 5


# ---- Prima funzione: quanto costa un ordine già deciso ---------

costo <- function(scelte){
  totale_a <- sum(prezzi_a[scelte == "A"])
  totale_b <- sum(prezzi_b[scelte == "B"])

  if(totale_a > 0){
    totale_a <- totale_a + spedizione_a     # si paga la spedizione di A
  }
  if(totale_b > 0){
    totale_b <- totale_b + spedizione_b     # e quella di B
  }

  return(totale_a + totale_b)
}

costo(c("A", "A", "A"))   # 90 + 8 = 98
costo(c("B", "B", "B"))   # 92 + 5 = 97
costo(c("A", "A", "B"))   # 50+8 + 38+5 = 101

# Il terzo è il risultato sorprendente: prendere ogni prodotto dove
# costa meno (carta e penne da A, cartucce da B) porta a 101 euro,
# mentre ordinare tutto da B, che su carta e penne costa di più,
# ne costa 97. Il problema non si risolve prodotto per prodotto,
# ma guardando l'ordine intero, spedizioni comprese.


# ---- Seconda funzione: prova tutte le combinazioni -------------

minimo <- function(scelte){
  if(length(scelte) == length(prodotti)){
    return(costo(scelte))             # caso base: ordine completo, lo valuto
  }

  con_a <- minimo(c(scelte, "A"))     # il prossimo prodotto lo prendo da A
  con_b <- minimo(c(scelte, "B"))     # ... oppure da B

  return(min(con_a, con_b))
}

minimo(c())   # 97 euro: tutto da B

# Il caso base qui non è "zero", è "ho deciso tutto": length(scelte)
# è arrivato al numero dei prodotti. A ogni chiamata l'elenco delle
# scelte si allunga di uno, quindi il problema si avvicina al caso
# base esattamente come i viaggi del lab precedente.


# ---- Vedere l'albero delle possibilità -------------------------
# Stessa funzione, con una stampa in più: così si vedono tutte e
# otto le combinazioni che vengono provate.

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

# Otto righe stampate, una sola restituita: print mostra, return
# restituisce. Qui si vede la differenza in un colpo solo.


# ---- Da provare in aula ----------------------------------------
# 1. Mettete le due spedizioni uguali a 8 euro: la combinazione
#    migliore torna a essere "tutto da A", 98 euro.
# 2. Abbassate il prezzo B delle cartucce a 25: a quel punto
#    conviene dividere l'ordine fra i due fornitori?
# 3. Aggiungete un quarto prodotto a prezzi_a e prezzi_b: la
#    funzione non va toccata, le combinazioni diventano sedici.
