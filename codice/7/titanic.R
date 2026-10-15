# ==============================================================
# LAB - Titanic                                Lezione 7, A.A. 2026/27
#
# Dati:  titanic.csv, una riga per passeggero (891 righe)
#
#   PassengerId  identificativo
#   Survived     1 = sopravvissuto, 0 = no
#   Pclass       classe del biglietto: 1, 2, 3
#   Name, Sex, Age
#   SibSp        fratelli, sorelle e coniugi a bordo
#   Parch        genitori e figli a bordo
#   Ticket       codice del biglietto
#   Fare         prezzo pagato
#   Cabin        cabina
#   Embarked     porto d'imbarco: C = Cherbourg, Q = Queenstown,
#                S = Southampton
#
# Una pipe per domanda. Prima di eseguire scrivete il risultato
# che vi aspettate; dopo, controllate che il denominatore sia
# quello che volevate.
# ==============================================================

library(dplyr)
titanic <- read.csv("titanic.csv")

str(titanic)
summary(titanic)


# ---- Parte A: in aula -----------------------------------------

# 1. Quante persone oltre i 50 anni erano sul Titanic?



# 2. Qual era la percentuale di uomini e di donne tra gli over 50?



# 3. In valore assoluto ci sono più uomini tra gli over 50 o tra
#    gli under 50? Quante donne sono under 50?



# 4. In percentuale sono sopravvissuti più passeggeri in prima o
#    in terza classe?



# ---- Parte B: lezione 8 e a casa ------------------------------

# 5. Qual è stato il costo del biglietto minimo, medio e massimo,
#    per ogni classe e per ogni sesso?



# 6. I sopravvissuti hanno pagato di più il viaggio?



# 7. Le famiglie più numerose hanno avuto una percentuale più alta
#    di sopravvivenza?



# 8. C'è differenza nella percentuale di sopravvivenza rispetto al
#    porto d'imbarco?



# ---- Extra ----------------------------------------------------

# 9. Chi ha pagato i 10 biglietti più costosi?



# 10. Quali sono i biglietti associati a più passeggeri?


