# ==============================================================
# LAB - Classificazione BMI                   Lezione 4, A.A. 2026/27
#
# BMI = peso / altezza^2
#
# Sottopeso .............. BMI < 18.5
# Normopeso .............. 18.5 <= BMI < 25
# Sovrappeso ............. 25   <= BMI < 30
# Obesità grado I ........ 30   <= BMI < 35
# Obesità grado II ....... 35   <= BMI < 40
# Obesità grado III ...... BMI >= 40
#
# Input:   altezza (m), peso (kg)
# Output:  classificazione, una delle sei categorie scritte così:
#          "Sottopeso", "Normopeso", "Sovrappeso",
#          "Obesità grado I", "Obesità grado II", "Obesità grado III"
#
# Fonte delle fasce: Ministero della Salute.
# ==============================================================


# ---- Un paziente solo ------------------------------------------

altezza <- 1.73
peso <- 86

bmi <- peso / altezza^2
print(round(bmi, 2))        # 28.73

if(bmi < 18.5){
  classificazione <- "Sottopeso"
}else if(bmi < 25){
  classificazione <- "Normopeso"
}else if(bmi < 30){
  classificazione <- "Sovrappeso"
}else if(bmi < 35){
  classificazione <- "Obesità grado I"
}else if(bmi < 40){
  classificazione <- "Obesità grado II"
}else{
  classificazione <- "Obesità grado III"
}
print(classificazione)      # "Sovrappeso"

# Le soglie sono chiuse a sinistra: un BMI di esattamente 25 è
# "Sovrappeso", non "Normopeso". Per questo i confronti sono
# tutti con < e mai con <=.


# ---- Cinque pazienti, con un ciclo for -------------------------

altezza <- c(1.58, 1.73, 1.81, 1.47, 1.74)
peso    <- c(62,   86,   85,   95,   75)

# Un'operazione su un vettore si applica a tutti gli elementi:
# qui otteniamo i cinque BMI in una riga sola.
bmi <- peso / altezza^2
print(round(bmi, 2))        # 24.84 28.73 25.95 43.96 24.77

sovrappeso_o_oltre <- 0     # il contatore parte da zero, fuori dal ciclo

for(i in 1:length(altezza)){

  if(bmi[i] < 18.5){
    classificazione <- "Sottopeso"
  }else if(bmi[i] < 25){
    classificazione <- "Normopeso"
  }else if(bmi[i] < 30){
    classificazione <- "Sovrappeso"
  }else if(bmi[i] < 35){
    classificazione <- "Obesità grado I"
  }else if(bmi[i] < 40){
    classificazione <- "Obesità grado II"
  }else{
    classificazione <- "Obesità grado III"
  }

  print(paste0("Paziente ", i, ": BMI ", round(bmi[i], 2),
               " - ", classificazione))

  if(bmi[i] >= 25){
    sovrappeso_o_oltre <- sovrappeso_o_oltre + 1
  }
}

print(paste0("Pazienti in sovrappeso o oltre: ", sovrappeso_o_oltre))   # 3


# ---- Controllo sui casi limite ---------------------------------
# Le soglie esatte: 18.5, 25, 30, 35 e 40.

altezza_test <- c(2.00, 2.00, 2.00, 1.81, 2.00)
peso_test    <- c(74,   100,  120,  60,   160)
atteso       <- c("Normopeso", "Sovrappeso", "Obesità grado I",
                  "Sottopeso", "Obesità grado III")

bmi_test <- peso_test / altezza_test^2
print(round(bmi_test, 2))   # 18.50 25.00 30.00 18.31 40.00

for(i in 1:length(bmi_test)){
  if(bmi_test[i] < 18.5){
    calcolato <- "Sottopeso"
  }else if(bmi_test[i] < 25){
    calcolato <- "Normopeso"
  }else if(bmi_test[i] < 30){
    calcolato <- "Sovrappeso"
  }else if(bmi_test[i] < 35){
    calcolato <- "Obesità grado I"
  }else if(bmi_test[i] < 40){
    calcolato <- "Obesità grado II"
  }else{
    calcolato <- "Obesità grado III"
  }
  print(paste0(round(bmi_test[i], 2), ": ", calcolato,
               " (atteso ", atteso[i], ")"))
}

# Con <= al posto di < il codice gira lo stesso e sbaglia
# esattamente su 18.5, 25, 30, 35 e 40.
