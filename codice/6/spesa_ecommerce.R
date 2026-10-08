# Lezione 6 - LAB: Tre prodotti, due e-commerce
#
# Compriamo una unita di ciascun prodotto, da A oppure da B.
# Ogni negozio usato aggiunge 8 euro di spedizione, senza soglie.
# Le due funzioni leggono il catalogo definito qui sotto.
# I prezzi sono positivi e nello stesso ordine in entrambi i negozi.
# Tariffe inventate per il laboratorio. Il risultato e il costo minimo.

prodotti <- c("Carta", "Penne", "Cartucce")
prezzi_a <- c(20, 30, 40)
prezzi_b <- c(22, 32, 38)


# 1. Il costo di una scelta completa.
# Per esempio, c("A", "A", "B") significa:
# carta e penne da A, cartucce da B.

costo <- function(scelte){
  totale_a <- sum(prezzi_a[scelte == "A"])
  totale_b <- sum(prezzi_b[scelte == "B"])

  if(totale_a > 0){
    totale_a <- totale_a + 8
  }
  if(totale_b > 0){
    totale_b <- totale_b + 8
  }

  return(totale_a + totale_b)
}


# 2. Il costo minimo, partendo dalle scelte gia fatte.
# Questa funzione restituisce un numero: il costo minimo.

minimo <- function(scelte){
  # Caso base: tutti i prodotti hanno un negozio assegnato.
  if(length(scelte) == length(prodotti)){
    return(costo(scelte))
  }

  # Aggiungiamo la scelta per il prossimo prodotto.
  con_a <- minimo(c(scelte, "A"))
  con_b <- minimo(c(scelte, "B"))

  return(min(con_a, con_b))
}


# Confrontiamo due ordini e poi cerchiamo il minimo tra tutti e otto.
print(costo(c("A", "A", "B")))  # 104: due spedizioni
print(costo(c("A", "A", "A")))  # 98: una spedizione
print(minimo(c()))                 # 98: partiamo senza scelte

# Prova anche minimo(c("B")): fissiamo il primo prodotto da B
# e lasciamo alla funzione la scelta degli altri due. Risultato: 100.
#
# Le chiamate aggiungono una lettera alla volta:
# c() -> c("A") -> c("A", "B") -> c("A", "B", "A")
# Con tre lettere ci si ferma e si calcola il costo dell'ordine.
