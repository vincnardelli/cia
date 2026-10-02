# ==============================================================
# Coding e Fondamenti di Intelligenza Artificiale - A.A. 2026/27
# Lezione 4 - Ripetere: vettori e cicli
#
# Come si usa: apri questo file in RStudio, metti il cursore su una
# riga e premi Ctrl + Invio (su Mac: Cmd + Invio).
# ==============================================================


# ---- 1. Ripasso: un vettore, tanti valori ---------------------

vettore <- c(23, 57, 14, 8)
vettore[1]
vettore[c(1, 2)]
1:2
vettore[1:2]
vettore[c(TRUE, TRUE, FALSE, FALSE)]

length(vettore)        # quanti elementi ci sono


# ---- 2. Un confronto su tutto il vettore ----------------------

vettore < 50           # un TRUE o un FALSE per ogni elemento
vettore[vettore < 50]  # tiene solo quelli veri

nomi <- c("Raffaele", "Giovanni", "Carmela", "Gioele")
eta  <- c(89, 6, 45, 102)

eta[eta > 67]
nomi[eta > 67]         # due vettori allineati: stessa posizione, stessa persona


# ---- 3. Una regola per una persona sola -----------------------

if(eta[2] > 67){
  print("In pensione")
}else{
  print("Non in pensione")
}

# Funziona, ma riguarda solo eta[2]. Per tutti gli altri?


# ---- 4. Il ciclo for: la stessa regola su tanti casi ----------

for(i in 1:4){
  print(i)
}

# i è un contaposizioni: prende 1, poi 2, poi 3, poi 4.
# Dentro il ciclo usiamo i per leggere l'elemento giusto.

for(i in 1:length(nomi)){
  if(eta[i] > 67){
    print(paste0(nomi[i], " è in pensione"))
  }else{
    print(paste0(nomi[i], " non è in pensione"))
  }
}

# paste0() incolla pezzi di testo e numeri in una frase sola.


# ---- 5. L'accumulatore: un numero che cresce nel ciclo --------

# Quante persone sono in pensione?
quanti <- 0                    # si parte da zero, FUORI dal ciclo

for(i in 1:length(eta)){
  if(eta[i] > 67){
    quanti <- quanti + 1       # il valore nuovo è quello vecchio + 1
  }
}
quanti

# Lo stesso schema serve per sommare: il totale di una spesa,
# il costo di una corsa in taxi, il fatturato di un anno.
spese <- c(12.5, 4, 31.2, 7.3)
totale <- 0
for(i in 1:length(spese)){
  totale <- totale + spese[i]
}
totale

sum(spese)                     # R ha già la scorciatoia, ma il ciclo si vede


# ---- 6. Attenzione: fuori o dentro il ciclo? ------------------

# Se l'accumulatore si azzera DENTRO il ciclo, resta sempre l'ultimo valore.
totale <- 0
for(i in 1:length(spese)){
  totale <- 0                  # errore: riparte ogni volta
  totale <- totale + spese[i]
}
totale                         # 7.3, non 55

# È un errore che non dà nessun messaggio: il codice gira e sbaglia.


# Adesso i due lab di oggi:
#   bmi.R    il BMI di cinque pazienti, con un ciclo
#   taxi.R   il costo di una corsa, minuto per minuto
