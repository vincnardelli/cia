# ==============================================================
# LAB - Boomer finder                         Lezione 3, A.A. 2026/27
#
# È boomer chi è nato dal 1946 al 1964, ESTREMI COMPRESI.
#
# Input:   anno    anno di nascita (un numero)
# Output:  status  "Boomer" oppure "Non Boomer"
# ==============================================================

anno <- 1964   # un anno al confine: deve dare "Boomer"


# ---- Soluzione 1: due condizioni in catena ---------------------

if(anno > 1964){
  status <- "Non Boomer"
}else if(anno < 1946){
  status <- "Non Boomer"
}else{
  status <- "Boomer"
}
print(status)   # "Boomer"


# ---- Soluzione 2: con & ----------------------------------------
# >= e <= perché gli estremi sono compresi.

if(anno >= 1946 & anno <= 1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
print(status)   # "Boomer"


# ---- Soluzione 3: con %in% -------------------------------------
# 1946:1964 sono tutti gli anni da 1946 a 1964, estremi compresi.

if(anno %in% 1946:1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
print(status)   # "Boomer"


# ---- La soluzione sbagliata ------------------------------------
# < e > sono stretti: escludono proprio il 1946 e il 1964.

if(anno < 1964 & anno > 1946){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
print(status)   # "Non Boomer": sbagliato, il 1964 è compreso


# ---- Controllo sui casi limite ---------------------------------
# I confronti funzionano su un vettore intero: proviamo tutti gli
# anni insieme. TRUE vuol dire "Boomer".

anni <- c(1945, 1946, 1955, 1964, 1965, 2006)

giusta    <- anni >= 1946 & anni <= 1964
sbagliata <- anni >  1946 & anni <  1964
con_in    <- anni %in% 1946:1964

giusta
sbagliata
con_in

anni[giusta != sbagliata]   # 1946 e 1964: proprio i confini
anni[giusta != con_in]      # numeric(0): nessuna differenza
