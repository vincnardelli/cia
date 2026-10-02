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


# ==============================================================
# VARIANTE - Autovelox con i punti della patente
#
# Stessi scaglioni, ma ogni fascia porta con sé anche i punti:
#   non oltre 10 km/h ..... 36 euro,   0 punti
#   oltre 10, non oltre 40  148 euro,  3 punti
#   oltre 40, non oltre 60  370 euro,  6 punti
#   oltre 60 km/h ......... 500 euro, 10 punti (+ sospensione)
#
# Input:   velocita, limite, saldo_punti del guidatore
# Output:  multa, punti_decurtati, punti_finali
# ==============================================================

velocita <- 120
limite <- 50
saldo_punti <- 20

differenza <- velocita - limite

# Una catena sola decide due cose insieme: importo e punti.
if(differenza <= 0){
  multa <- 0
  punti_decurtati <- 0
}else if(differenza <= 10){
  multa <- 36
  punti_decurtati <- 0
}else if(differenza <= 40){
  multa <- 148
  punti_decurtati <- 3
}else if(differenza <= 60){
  multa <- 370
  punti_decurtati <- 6
}else{
  multa <- 500
  punti_decurtati <- 10
}

punti_finali <- saldo_punti - punti_decurtati

print(multa)             # 500
print(punti_decurtati)   # 10
print(punti_finali)      # 10

# Oltre i 60 km/h c'è anche la sospensione della patente, da 6 a
# 12 mesi: è un'informazione in più, non un calcolo.
if(differenza > 60){
  print("Patente sospesa da 6 a 12 mesi")
}

# Il saldo punti non può scendere sotto zero: chi ha 4 punti e ne
# perde 10 resta a zero, non a -6.
punti_finali <- saldo_punti - punti_decurtati
if(punti_finali < 0){
  punti_finali <- 0
}
print(punti_finali)

# Lo stesso in una riga: max() sceglie il più grande tra i due.
punti_finali <- max(0, saldo_punti - punti_decurtati)
print(punti_finali)
