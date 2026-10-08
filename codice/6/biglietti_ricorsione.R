# ==============================================================
# Lezione 6 - LAB: Biglietti singoli o carnet?
#
# Regole inventate per il laboratorio:
# - Un biglietto singolo copre 1 viaggio e costa 3 euro.
# - Un carnet copre 5 viaggi e costa 10 euro.
# - Si possono comprare piu carnet; i biglietti possono avanzare.
#
# Input: quanti viaggi fare (un numero intero, almeno zero).
# Output: la spesa minima per coprirli tutti.
# Per seguire la ricorsione, partiamo da pochi viaggi: da 0 a 10.
# ==============================================================

costo_minimo <- function(viaggi){
  # Caso base: abbiamo gia coperto tutti i viaggi.
  if(viaggi <= 0){
    return(0)
  }

  # Compriamo un singolo: resta da coprire un viaggio in meno.
  con_singolo <- 3 + costo_minimo(viaggi - 1)

  # Oppure un carnet: restano da coprire cinque viaggi in meno.
  con_carnet <- 10 + costo_minimo(viaggi - 5)

  # min() restituisce il minore dei due costi completi.
  return(min(con_singolo, con_carnet))
}


# ---- Proviamo ------------------------------------------------

print(costo_minimo(0))   # 0: nessun viaggio, nessuna spesa
print(costo_minimo(3))   # 9: tre singoli
print(costo_minimo(4))   # 10: un carnet, con un biglietto avanzato
print(costo_minimo(6))   # 13: un carnet e un singolo
print(costo_minimo(10))  # 20: due carnet


# ---- Seguiamo una chiamata ------------------------------------
#
# costo_minimo(4) confronta:
#   3 + costo_minimo(3)   -> 3 + 9 = 12
#  10 + costo_minimo(-1)  -> 10 + 0 = 10
# Restituisce 10.
#
# Il valore -1 significa che il carnet copre un viaggio in piu.
# Per questo il caso base controlla <= 0, non soltanto == 0.
#
# Domande per la classe:
# - Perche entrambe le chiamate si avvicinano al caso base?
# - Quanto spendiamo per 5 viaggi esatti? E per 9?
# - Se il carnet costasse 14 euro, converrebbe ancora per 4 viaggi?
#
# Questa versione ricalcola alcuni sottoproblemi: serve a capire
# la ricorsione su pochi viaggi, non a gestire quantita grandi.
