# ==============================================================
# LAB - Autovelox                             Lezione 3, A.A. 2026/27
#
# Art. 142 del Codice della Strada (importi minimi):
#   entro il limite ................................  0 euro
#   oltre il limite di NON OLTRE 10 km/h ........... 36 euro
#   di OLTRE 10 e NON OLTRE 40 km/h ................148 euro
#   di OLTRE 40 e NON OLTRE 60 km/h ................370 euro
#   di OLTRE 60 km/h ...............................500 euro
#
# Input:   velocita   velocità rilevata, km/h
#          limite     limite del tratto, km/h
# Output:  multa      importo in euro
#
# "Non oltre 10" vuol dire fino a 10 COMPRESO: chi va esattamente
# 10 km/h sopra il limite paga 36 euro, non 148.
# ==============================================================

velocita <- 60
limite <- 50


# ---- Soluzione 1: prima la differenza, poi gli scaglioni -------

differenza <- velocita - limite

if(differenza <= 0){
  multa <- 0
}else if(differenza <= 10){
  multa <- 36
}else if(differenza <= 40){
  multa <- 148
}else if(differenza <= 60){
  multa <- 370
}else{
  multa <- 500
}
print(multa)   # 36


# ---- Soluzione 2: senza la differenza --------------------------
# Stessi scaglioni, scritti sul limite. Si legge peggio, ma vale
# la pena vedere che è la stessa regola.

if(velocita <= limite){
  multa <- 0
}else if(velocita <= limite + 10){
  multa <- 36
}else if(velocita <= limite + 40){
  multa <- 148
}else if(velocita <= limite + 60){
  multa <- 370
}else{
  multa <- 500
}
print(multa)   # 36


# ---- Controllo sui casi limite --------------------------------
# I tre confini sono +10, +40 e +60 km/h: lì si decide se il
# confronto va scritto con <= oppure con <.

velocita_test <- c(45, 50, 60, 75, 90, 110, 111, 200)
limite_test   <- c(50, 50, 50, 50, 50,  50,  50, 130)
atteso        <- c( 0,  0, 36, 148, 148, 370, 500, 500)

# ifelse() sceglie un valore per ogni elemento del vettore:
# è la stessa catena di prima, scritta su tutti i casi insieme.
d <- velocita_test - limite_test
calcolato <- ifelse(d <= 0, 0,
             ifelse(d <= 10, 36,
             ifelse(d <= 40, 148,
             ifelse(d <= 60, 370, 500))))

calcolato
calcolato == atteso                      # tutti TRUE
velocita_test[calcolato != atteso]       # numeric(0): nessun errore

# Con < al posto di <= sulle soglie di 10, 40 e 60 il codice gira
# lo stesso e sbaglia su 60, 90 e 110 km/h.
