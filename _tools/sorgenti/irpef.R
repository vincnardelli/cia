reddito <- 45000

# IRPEF 2025
if (reddito <= 15000) {
  imposta_2025 <- reddito * 0.23
} else if (reddito <= 28000) {
  imposta_2025 <- 15000 * 0.23 + (reddito - 15000) * 0.23
} else if (reddito <= 50000) {
  imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (reddito - 28000) * 0.35
} else if (reddito <= 75000) {
  imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.35 + (reddito - 50000) * 0.43
} else if (reddito <= 120000) {
  imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.35 +
    (75000 - 50000) * 0.43 + (reddito - 75000) * 0.43
} else {
  imposta_2025 <- 15000 * 0.23 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.35 +
    (75000 - 50000) * 0.43 + (120000 - 75000) * 0.43 + (reddito - 120000) * 0.46
}

aliquota_totale_2025 <- (imposta_2025 / reddito) * 100



# IRPEF 2026 (PROPOSTA)
if (reddito <= 15000) {
  imposta_2026 <- reddito * 0.20
} else if (reddito <= 28000) {
  imposta_2026 <- 15000 * 0.20 + (reddito - 15000) * 0.23
} else if (reddito <= 50000) {
  imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (reddito - 28000) * 0.36
} else if (reddito <= 75000) {
  imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.36 + (reddito - 50000) * 0.40
} else if (reddito <= 120000) {
  imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.36 +
    (75000 - 50000) * 0.40 + (reddito - 75000) * 0.43
} else {
  imposta_2026 <- 15000 * 0.20 + (28000 - 15000) * 0.23 + (50000 - 28000) * 0.36 +
    (75000 - 50000) * 0.40 + (120000 - 75000) * 0.43 + (reddito - 120000) * 0.46
}

aliquota_totale_2026 <- (imposta_2026 / reddito) * 100


# -------------------------
# Confronto finale
# -------------------------
differenza_imposta <- imposta_2026 - imposta_2025
differenza_punti   <- aliquota_totale_2026 - aliquota_totale_2025

print(paste("Reddito:", reddito))
print(paste("IRPEF 2025:", round(imposta_2025, 2), "| Aliquota media 2025:", round(aliquota_totale_2025, 2), "%"))
print(paste("IRPEF 2026 (proposta):", round(imposta_2026, 2), "| Aliquota media 2026:", round(aliquota_totale_2026, 2), "%"))
print(paste("Differenza imposta (2026 - 2025):", round(differenza_imposta, 2)))
print(paste("Differenza aliquota media (punti %):", round(differenza_punti, 2)))