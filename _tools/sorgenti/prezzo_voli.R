# ===== INPUT =====
seat_type   <- "Economy"   # "Economy", "Premium", "Business"
days_before <- 5           # giorni prima della partenza
load_factor <- 0.82        # tra 0 e 1

# ===== BASE FARE PER TIPO POSTO =====
if (seat_type == "Economy") {
  prezzo <- 100
} else if (seat_type == "Premium") {
  prezzo <- 180
} else if (seat_type == "Business") {
  prezzo <- 350
}

# ===== MOLTIPLICATORE PER ANTICIPO =====
moltip_anticipo <- 1
if (days_before > 60) {
  moltip_anticipo <- 0.80   # -20%
} else if (days_before >= 31) {
  moltip_anticipo <- 0.90   # -10%
} else if (days_before >= 15) {
  moltip_anticipo <- 1.00   #  0%
} else if (days_before >= 7) {
  moltip_anticipo <- 1.20   # +20%
} else if (days_before >= 3) {
  moltip_anticipo <- 1.40   # +40%
} else { # 0-2 giorni
  moltip_anticipo <- 1.70   # +70%
}

# ===== MOLTIPLICATORE PER RIEMPIMENTO =====
moltip_riempimento <- 1
if (load_factor < 0.50) {
  moltip_riempimento <- 0.90   # -10%
} else if (load_factor <= 0.70) {
  moltip_riempimento <- 1.00   #  0%
} else if (load_factor <= 0.85) {
  moltip_riempimento <- 1.15   # +15%
} else { # > 0.85
  moltip_riempimento <- 1.35   # +35%
}

# ===== CALCOLO PREZZO =====
fee_fissa <- 25

prezzo_dinamico <- prezzo * moltip_anticipo * moltip_riempimento

# Extra: se last-minute e aereo quasi pieno → +10%
extra_stress <- 1
if (days_before <= 2 & load_factor > 0.85) {
  extra_stress <- 1.10
}

prezzo_finale <- (prezzo_dinamico * extra_stress) + fee_fissa
prezzo_finale