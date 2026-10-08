# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 6 - Funzioni e ricorsione
#
# Esegui un blocco alla volta in RStudio.
# Le tariffe di questa lezione sono inventate per gli esercizi.
# ==============================================================


# ---- 1. Una funzione riceve un dato e restituisce un risultato --

spedizione <- function(importo){
  if(importo == 0){
    return(0)
  }else{
    return(8)
  }
}

spedizione(30)  # 8
spedizione(0)   # 0

# importo e l'argomento: il valore che entra nella funzione.
# return() indica il valore che la funzione restituisce.
# Negli esempi importo e sempre un numero maggiore o uguale a zero.


# ---- 2. Il risultato si puo conservare e riutilizzare -----------

consegna <- spedizione(30)
print(consegna)
print(30 + consegna)

# print() mostra un risultato; return() lo restituisce a chi chiama.


# ---- 3. Una funzione puo chiamarne un'altra ---------------------

totale_ordine <- function(importo){
  consegna <- spedizione(importo)
  totale <- importo + consegna
  return(totale)
}

print(totale_ordine(30))  # 38
print(totale_ordine(0))   # 0

# consegna e totale, create nel corpo di totale_ordine(), sono locali.
# Per provare le regole basta confrontare il risultato con l'atteso.
totale_ordine(30) == 38
totale_ordine(0) == 0


# ---- 4. La stessa funzione dentro un ciclo ---------------------

importi <- c(30, 0, 90)

for(i in seq_along(importi)){
  print(totale_ordine(importi[i]))
}

# seq_along(importi) fornisce le posizioni del vettore: 1, 2, 3.
# Se importi e vuoto, il ciclo non parte.


# ---- 5. Una funzione puo richiamare se stessa -------------------
#
# La ricorsione richiede:
# - un caso base, in cui si restituisce subito il risultato;
# - una chiamata sul problema ridotto, che si avvicina al caso base.
#
# Prosegui con gli altri due file della lezione 6:
# biglietti_ricorsione.R - singoli o carnet, un numero in ingresso
# spesa_ecommerce.R     - tre prodotti, due negozi, scelte in un vettore
