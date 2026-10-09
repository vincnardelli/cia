# ==============================================================
# LAB - Taxi o Uber?                          Lezione 5, A.A. 2026/27
#
# Il tassametro di Roma cambia tariffa minuto per minuto:
#   velocità = km del minuto * 60   (km/h)
#   sotto 20 km/h ....... tariffa oraria: 32,58 €/h, cioè 32.58/60 al minuto
#   20 km/h o più ....... tariffa a km:   1,33 € per km di quel minuto
#
# Quota fissa:  feriali lun-ven 6-22   3,50 €
#               sabato e festivi 6-22 5,00 €
#               notturna 22-6         7,50 €
#
# Tariffario Taxi di Roma Capitale, giugno 2026 (delibera 157/2026).
# La tariffa a km in realtà è progressiva (T1 1,33 - T2 1,45 - T3 1,73):
# qui usiamo solo la T1.
#
# Il lab cresce in cinque parti:
#   1  solo la quota variabile
#   2  più la quota fissa, che dipende da giorno e ora
#   3  la decisione: taxi o Uber (9 €)?
#   4  tutto dentro una funzione
#   5  la funzione su tre corse, e si conta chi vince
# ==============================================================

tariffa_min <- 32.58/60
tariffa_km <- 1.33
distanza <- c(1, 0.3, 0.5, 0.8, 0.2)


# ==============================================================
# PARTE 1 - la quota variabile, minuto per minuto
# ==============================================================

costo <- 0                      # l'accumulatore parte da zero
velocita <- distanza * 60       # i km/h di ogni minuto, tutti insieme

for(i in 1:length(distanza)){
  if(velocita[i] < 20){
    costo <- costo + tariffa_min            # fermo nel traffico: si paga il tempo
  }else{
    costo <- costo + tariffa_km * distanza[i]   # in corsa: si pagano i km
  }
  print(costo)                  # il costo che cresce, minuto per minuto
}

costo <- round(costo, 2)
print(costo)                    # 4.15

# I minuti 1, 3 e 4 vanno a 60, 30 e 48 km/h: tariffa a km.
# I minuti 2 e 5 stanno sotto i 20 km/h (18 e 12): tariffa a tempo.
# Da provare: 0.35 km in un minuto sono 21 km/h (si paga a km),
# 0.3 km sono 18 km/h (si paga a tempo). Taxi fermo: 0 km, ma il
# tassametro corre lo stesso.


# ==============================================================
# PARTE 2 - più la quota fissa: dipende da giorno e ora
# ==============================================================

giorno <- "D"      # iniziale maiuscola: L M M G V S D
ora <- 12          # da 0 a 23

# Due domande dentro l'altra: prima se siamo di giorno, poi che
# giorno è. È un if dentro un if, come nel modulo 2.
if(ora >= 6 & ora <= 22){
  if(giorno == "D"){
    costo <- 5
  }else{
    costo <- 3.5
  }
}else{
  costo <- 7.5
}

# Da qui in poi è la parte 1: il costo parte dalla quota fissa
# invece che da zero.
for(i in 1:length(distanza)){
  velocita <- distanza[i] * 60
  if(velocita < 20){
    costo <- costo + tariffa_min
  }else{
    costo <- costo + tariffa_km * distanza[i]
  }
}

costo <- round(costo, 2)
print(costo)       # domenica alle 12: 5 + 4.145 = 9.14


# ---- Alternativa: una catena di if, senza annidarli -------------
# Prima la notte, che vale per tutti i giorni; poi sabato e
# domenica insieme con %in%; il resto sono i feriali.

if(ora >= 22 | ora < 6){
  quota_fissa <- 7.5
}else if(giorno %in% c("S", "D")){
  quota_fissa <- 5
}else{
  quota_fissa <- 3.5
}
print(quota_fissa)   # 5

# Stesso risultato, due modi di scrivere la stessa regola.


# ==============================================================
# PARTE 3 - taxi o Uber? Uber costa 9 €
# ==============================================================

costo_uber <- 9

if(costo_uber < costo){
  print("Uber")
}else{
  print("Taxi")
}


# ==============================================================
# PARTE 4 - la funzione: lo stesso calcolo, su qualsiasi corsa
#
# Per cambiare corsa finora bisognava modificare le righe in cima
# e rieseguire tutto. Dentro una funzione il calcolo si riusa.
# ==============================================================

costo_corsa <- function(distanza, giorno, ora){

  tariffa_min <- 32.58/60
  tariffa_km <- 1.33

  # la quota fissa
  if(ora >= 6 & ora <= 22){
    if(giorno == "D"){
      costo <- 5
    }else{
      costo <- 3.5
    }
  }else{
    costo <- 7.5
  }

  # la quota variabile, minuto per minuto
  for(i in 1:length(distanza)){
    velocita <- distanza[i] * 60
    if(velocita < 20){
      costo <- costo + tariffa_min
    }else{
      costo <- costo + tariffa_km * distanza[i]
    }
  }

  return(round(costo, 2))
}

# Adesso una corsa è una riga sola.
costo_corsa(distanza, "D", 12)   # 9.14, domenica a pranzo
costo_corsa(distanza, "M", 9)    # 7.65, mercoledì mattina
costo_corsa(distanza, "S", 23)   # 11.64, sabato notte

# Le variabili create dentro la funzione (costo, velocita, i)
# vivono solo lì dentro: fuori non esistono.


# ==============================================================
# PARTE 5 - la funzione dentro un ciclo
#
# La stessa corsa in tre momenti diversi: in quante conviene il
# taxi rispetto a Uber?
# ==============================================================


giorni <- c("D", "M", "S")
ore <- c(12, 9, 23)

costo_uber <- 9
quante_taxi <- 0

for(i in 1:length(giorni)){
  costo <- costo_corsa(distanza, giorni[i], ore[i])

  if(costo < costo_uber){
    quante_taxi <- quante_taxi + 1
    print(paste0(giorni[i], " alle ", ore[i], ": taxi ", costo, " euro - conviene il taxi"))
  }else{
    print(paste0(giorni[i], " alle ", ore[i], ": taxi ", costo, " euro - conviene Uber"))
  }
}

print(paste0("Conviene il taxi in ", quante_taxi, " casi su ", length(giorni)))
