# ==============================================================
# LAB - Pricing dei voli                      Lezione 3, A.A. 2026/27
#
# Tariffa base:  Economy 100, Premium 180, Business 350 euro
# Anticipo (days_before):
#   oltre 60 giorni -20% | da 31 a 60 -10% | da 15 a 30 0%
#   da 7 a 14 +20%       | da 3 a 6 +40%   | da 0 a 2 +70%
# Riempimento (load_factor):
#   sotto 0.50 -10% | da 0.50 a 0.70 0%
#   oltre 0.70 fino a 0.85 +15% | oltre 0.85 +35%
# Fee fissa: 25 euro, aggiunti ALLA FINE.
# Stress di mercato: days_before <= 2 E load_factor > 0.85 -> +10%.
#
# In cascata: base * anticipo * riempimento * stress, poi + 25.
# Output: prezzo_finale, arrotondato a 2 decimali.
# ==============================================================

seat_type   <- "Economy"   # "Economy", "Premium", "Business"
days_before <- 5           # giorni prima della partenza
load_factor <- 0.82        # tra 0 e 1


# ---- Soluzione 1: una catena di if per ogni regola -------------

# 1. la tariffa base
if(seat_type == "Economy"){
  prezzo <- 100
}else if(seat_type == "Premium"){
  prezzo <- 180
}else if(seat_type == "Business"){
  prezzo <- 350
}

# 2. l'anticipo
moltip_anticipo <- 1
if(days_before > 60){
  moltip_anticipo <- 0.80        # -20%
}else if(days_before >= 31){
  moltip_anticipo <- 0.90        # -10%
}else if(days_before >= 15){
  moltip_anticipo <- 1.00        #   0%
}else if(days_before >= 7){
  moltip_anticipo <- 1.20        # +20%
}else if(days_before >= 3){
  moltip_anticipo <- 1.40        # +40%
}else{                           # da 0 a 2 giorni
  moltip_anticipo <- 1.70        # +70%
}

# 3. il riempimento
moltip_riempimento <- 1
if(load_factor < 0.50){
  moltip_riempimento <- 0.90     # -10%
}else if(load_factor <= 0.70){
  moltip_riempimento <- 1.00     #   0%
}else if(load_factor <= 0.85){
  moltip_riempimento <- 1.15     # +15%
}else{                           # oltre 0.85
  moltip_riempimento <- 1.35     # +35%
}

# 4. lo stress di mercato: l'unica regola con due condizioni insieme
extra_stress <- 1
if(days_before <= 2 & load_factor > 0.85){
  extra_stress <- 1.10           # +10%
}

# 5. il prezzo finale
fee_fissa <- 25

prezzo_dinamico <- prezzo * moltip_anticipo * moltip_riempimento
prezzo_lordo <- prezzo_dinamico * extra_stress
prezzo_finale <- round(prezzo_lordo + fee_fissa, 2)
print(prezzo_finale)   # 186


# ---- Soluzione 2: la stessa regola, scritta più corta ----------
# %in% per le fasce di giorni interi, e un unico calcolo finale.

prezzo <- 100
if(seat_type == "Premium"){ prezzo <- 180 }
if(seat_type == "Business"){ prezzo <- 350 }

if(days_before %in% 0:2){
  moltip_anticipo <- 1.70
}else if(days_before %in% 3:6){
  moltip_anticipo <- 1.40
}else if(days_before %in% 7:14){
  moltip_anticipo <- 1.20
}else if(days_before %in% 15:30){
  moltip_anticipo <- 1.00
}else if(days_before %in% 31:60){
  moltip_anticipo <- 0.90
}else{
  moltip_anticipo <- 0.80
}

moltip_riempimento <- 1.35
if(load_factor <= 0.85){ moltip_riempimento <- 1.15 }
if(load_factor <= 0.70){ moltip_riempimento <- 1.00 }
if(load_factor < 0.50){ moltip_riempimento <- 0.90 }

extra_stress <- 1
if(days_before <= 2 & load_factor > 0.85){ extra_stress <- 1.10 }

prezzo_finale <- round(prezzo * moltip_anticipo * moltip_riempimento *
                       extra_stress + 25, 2)
print(prezzo_finale)   # 186

# Nella soluzione 2 l'ordine degli if sul riempimento è rovesciato:
# si parte dal caso più alto e si scende. Ogni if che è vero
# sovrascrive il precedente, quindi l'ultimo vero è quello che vale.


# ---- I casi al confine da provare ------------------------------
# Cambia i tre input in cima al file e riesegui: il prezzo atteso
# è quello della colonna a destra.
#
#   Economy    5 giorni   0.82   ->  186.00   caso base
#   Business  90 giorni   0.30   ->  277.00
#   Economy   60 giorni   0.60   ->  115.00   60 giorni è ANCORA -10%
#   Economy   61 giorni   0.60   ->  105.00   61 è "oltre 60": -20%
#   Economy   15 giorni   0.60   ->  125.00   15 è ancora fascia 0%
#   Economy    7 giorni   0.60   ->  145.00
#   Economy    3 giorni   0.60   ->  165.00
#   Premium   20 giorni   0.50   ->  205.00   0.50 esatto: nessuna correzione
#   Premium   20 giorni   0.70   ->  205.00
#   Premium   20 giorni   0.85   ->  232.00   0.85 esatto: +15%, non +35%
#   Economy    2 giorni   0.85   ->  220.50   a 0.85 lo stress NON scatta
#   Economy    2 giorni   0.86   ->  277.45   due giorni e aereo pieno
