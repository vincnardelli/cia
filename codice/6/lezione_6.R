# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 6 - Funzioni: restituire, comporre, ripetere
# ==============================================================


# ---- 1. print mostra, return restituisce ----------------------

# Questa funzione stampa e basta.
bmi_stampa <- function(peso, altezza){
  print(peso / altezza^2)
}

bmi_stampa(86, 1.73)          # sullo schermo compare il numero

x <- bmi_stampa(86, 1.73)     # ... ma x non contiene niente
x                             # NULL
# x + 1                       # togli il # : errore

# Questa invece restituisce.
bmi <- function(peso, altezza){
  return(peso / altezza^2)
}

y <- bmi(86, 1.73)
y                             # 28.73...
y + 1                         # si può usare: è un numero

# Regola: una funzione serve a dare indietro un valore.
# print() è solo per guardare, mentre si lavora.


# ---- 2. Due funzioni, una per lavoro --------------------------

bmi <- function(peso, altezza){
  return(peso / altezza^2)
}

classificazione <- function(valore){
  if(valore < 18.5){
    return("Sottopeso")
  }else if(valore < 25){
    return("Normopeso")
  }else if(valore < 30){
    return("Sovrappeso")
  }else if(valore < 35){
    return("Obesità grado I")
  }else if(valore < 40){
    return("Obesità grado II")
  }else{
    return("Obesità grado III")
  }
}

# bmi() fa un conto, classificazione() prende una decisione.
# Separate si provano separatamente.

bmi(86, 1.73)
classificazione(28.73)


# ---- 3. Una funzione dentro l'altra ---------------------------

# Il risultato della prima entra nella seconda.
classificazione(bmi(86, 1.73))     # "Sovrappeso"

# Se una delle due stampasse invece di restituire, questa riga
# non funzionerebbe: è il motivo del punto 1.

# Un passaggio in più: il referto, che le chiama tutte e due.
referto <- function(peso, altezza){
  valore <- bmi(peso, altezza)
  classe <- classificazione(valore)
  return(paste0("BMI ", round(valore, 1), ": ", classe))
}

referto(86, 1.73)
referto(62, 1.58)


# ---- 4. Le funzioni dentro un ciclo ---------------------------

altezza <- c(1.58, 1.73, 1.81, 1.47, 1.74)
peso    <- c(62,   86,   85,   95,   75)

sovrappeso_o_oltre <- 0

for(i in 1:length(altezza)){
  print(referto(peso[i], altezza[i]))

  if(bmi(peso[i], altezza[i]) >= 25){
    sovrappeso_o_oltre <- sovrappeso_o_oltre + 1
  }
}

print(paste0("Pazienti in sovrappeso o oltre: ", sovrappeso_o_oltre))

# Il ciclo della lezione 4 adesso è lungo tre righe: il conto e la
# decisione stanno nelle funzioni, qui resta solo il "per ognuno".


# ---- 5. Provare una funzione è una riga -----------------------

classificazione(24.9) == "Normopeso"
classificazione(25) == "Sovrappeso"     # la soglia esatta
classificazione(40) == "Obesità grado III"

# Le variabili nate dentro una funzione (valore, classe) fuori non
# esistono: provare a scrivere "classe" qui dà errore.


# ---- 6. Attenzione: la variabile presa da fuori ---------------

soglia <- 25

sovrappeso_sbagliata <- function(valore){
  return(valore >= soglia)        # soglia non è un argomento!
}

sovrappeso_sbagliata(26)          # TRUE
soglia <- 30                      # qualcuno cambia la variabile...
sovrappeso_sbagliata(26)          # FALSE: stessa chiamata, altra risposta

# Quello che serve a una funzione, la funzione se lo deve far dare.
sovrappeso <- function(valore, soglia){
  return(valore >= soglia)
}
sovrappeso(26, 25)


# Adesso: app.R (la stessa funzione dentro una pagina web),
# poi i due lab, biglietti.R e fornitori.R.
