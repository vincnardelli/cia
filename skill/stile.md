# Stile del codice del corso

Il codice delle lezioni ha un aspetto riconoscibile. Quando scrivi o correggi codice per lo studente, imitalo. Gli esempi qui sotto sono presi dai file delle lezioni 3–6 (https://www.vincnardelli.com/cia/codice/).

## Convenzioni

- Assegnazione con `<-`, mai `=`.
- Nomi in italiano, minuscoli, con underscore: `prezzo_netto`, `quota_fissa`, `sovrappeso_o_oltre`. Niente `x`, `tmp`, `result`.
- Commenti in italiano, brevi, sopra il blocco o a fine riga.
- Una istruzione per riga.
- `if(condizione){` senza spazio dopo `if`; `}else if(...){` e `}else{` sulla stessa riga della graffa.
- Condizioni composte con `&`, `|` e `!` (non `&&`, `||`); insiemi con `%in%`.
- Cicli con `for(i in 1:length(x)){`; l'accumulatore parte da zero **fuori** dal ciclo.
- Funzioni con `nome <- function(argomenti){ ... return(valore) }`: `return()` sempre esplicito. Una funzione restituisce, `print()` serve solo per guardare.
- Quello che serve a una funzione glielo si passa come argomento: niente variabili prese da fuori.
- Per stampare una frase: `print(paste0("Testo: ", valore))`. Per arrotondare: `round(x, 2)`.
- Le soglie si scrivono come nel testo: "non oltre 10" → `<= 10`; "oltre 10" → `> 10`; "dal 1946 al 1964, estremi compresi" → `>= 1946 & <= 1964`.
- Ogni file inizia con un blocco di commenti che dice regola, input e output; le parti sono separate da `# ---- titolo ----`; accanto alle chiamate di prova, nel commento, il risultato atteso.

## 1. Una regola a fasce (lezione 3, Autovelox)

```r
# ==============================================================
# LAB - Autovelox                             Lezione 3, A.A. 2026/27
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
```

## 2. La stessa regola in tre modi (lezione 3, Boomer)

```r
anno <- 1964   # un anno al confine: deve dare "Boomer"

# ---- Soluzione 1: due condizioni in catena ---------------------
if(anno > 1964){
  status <- "Non Boomer"
}else if(anno < 1946){
  status <- "Non Boomer"
}else{
  status <- "Boomer"
}

# ---- Soluzione 2: con & ----------------------------------------
# >= e <= perché gli estremi sono compresi.
if(anno >= 1946 & anno <= 1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}

# ---- Soluzione 3: con %in% -------------------------------------
if(anno %in% 1946:1964){
  status <- "Boomer"
}else{
  status <- "Non Boomer"
}
```

## 3. Vettori e selezione (lezioni 3 e 4)

```r
nomi <- c("Raffaele", "Giovanni", "Carmela", "Gioele")
eta  <- c(89, 6, 45, 102)

eta[2]
nomi[c(1, 3)]
eta > 67               # un TRUE o un FALSE per ogni elemento
nomi[eta > 67]         # due vettori allineati: stessa posizione, stessa persona
length(nomi)
```

## 4. Il ciclo con l'accumulatore (lezione 4)

```r
# Quante persone sono in pensione?
quanti <- 0                    # si parte da zero, FUORI dal ciclo
for(i in 1:length(eta)){
  if(eta[i] > 67){
    quanti <- quanti + 1       # il valore nuovo è quello vecchio + 1
  }
}
quanti

for(i in 1:length(nomi)){
  if(eta[i] > 67){
    print(paste0(nomi[i], " è in pensione"))
  }else{
    print(paste0(nomi[i], " non è in pensione"))
  }
}
```

## 5. Un ciclo con una regola dentro (lezione 5, Taxi)

```r
tariffa_min <- 32.58/60
tariffa_km <- 1.33
distanza <- c(1, 0.3, 0.5, 0.8, 0.2)   # km percorsi in ogni minuto

costo <- 0                      # l'accumulatore parte da zero
velocita <- distanza * 60       # i km/h di ogni minuto, tutti insieme

for(i in 1:length(distanza)){
  if(velocita[i] < 20){
    costo <- costo + tariffa_min            # fermo nel traffico: si paga il tempo
  }else{
    costo <- costo + tariffa_km * distanza[i]   # in corsa: si pagano i km
  }
}
costo <- round(costo, 2)
print(costo)                    # 4.15
```

If annidati, come nella quota fissa del taxi:

```r
if(ora >= 6 & ora <= 22){
  if(giorno == "D"){
    costo <- 5
  }else{
    costo <- 3.5
  }
}else{
  costo <- 7.5
}
```

## 6. Funzioni che restituiscono e si compongono (lezione 6)

```r
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

referto <- function(peso, altezza){
  valore <- bmi(peso, altezza)
  classe <- classificazione(valore)
  return(paste0("BMI ", round(valore, 1), ": ", classe))
}

referto(86, 1.73)

# Provare una funzione è una riga, a partire dalle soglie esatte
classificazione(24.9) == "Normopeso"
classificazione(25) == "Sovrappeso"
```

## 7. Una funzione dentro un ciclo (lezione 6)

```r
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
```

## 8. Ricorsione con caso base (lezione 6, Due fornitori)

```r
prodotti <- c("Carta", "Penne", "Cartucce")

# costo(scelte) restituisce il costo di un ordine già deciso,
# per esempio costo(c("A", "B", "B"))

minimo <- function(scelte){
  if(length(scelte) == length(prodotti)){
    return(costo(scelte))             # caso base: ordine completo, lo valuto
  }

  con_a <- minimo(c(scelte, "A"))     # il prossimo prodotto lo prendo da A
  con_b <- minimo(c(scelte, "B"))     # ... oppure da B

  return(min(con_a, con_b))
}

minimo(c())   # 97 euro: tutto da B
```

## 9. La stessa funzione dentro un'app Shiny (lezione 6, app.R)

```r
library(shiny)


# ---- 1. Le funzioni: identiche a quelle della lezione ---------

bmi <- function(peso, altezza){
  return(peso / altezza^2)
}

# classificazione() come nell'esempio 6


# ---- 2. ui: che cosa si vede ----------------------------------

ui <- fluidPage(

  titlePanel("Calcolatore BMI"),

  sidebarLayout(

    sidebarPanel(
      sliderInput("peso", "Peso (kg)", min = 30, max = 150, value = 86),
      sliderInput("altezza", "Altezza (m)", min = 1.40, max = 2.10,
                  value = 1.73, step = 0.01)
    ),

    mainPanel(
      h3(textOutput("valore")),
      h2(textOutput("classe"))
    )
  )
)


# ---- 3. server: che cosa succede ------------------------------
# input$peso e input$altezza sono i valori dei cursori.

server <- function(input, output){

  output$valore <- renderText({
    valore <- bmi(input$peso, input$altezza)
    paste0("BMI: ", round(valore, 1))
  })

  output$classe <- renderText({
    valore <- bmi(input$peso, input$altezza)
    classificazione(valore)
  })
}


# ---- 4. Avvia l'applicazione ----------------------------------

shinyApp(ui = ui, server = server)
```

L'interfaccia cambia, la funzione no: se sbaglia a BMI 25 esatto, sbaglia anche con i cursori.

## Errori che il corso fa vedere apposta

```r
# L'accumulatore azzerato DENTRO il ciclo: resta solo l'ultimo valore
totale <- 0
for(i in 1:length(spese)){
  totale <- 0                  # errore: riparte ogni volta
  totale <- totale + spese[i]
}

# Una funzione che stampa invece di restituire: il numero si vede,
# ma la funzione restituisce l'ultima riga, cioè la frase
bmi_stampa <- function(peso, altezza){
  print(peso / altezza^2)
  print("calcolo fatto")
}
x <- bmi_stampa(86, 1.73)   # x vale "calcolo fatto", non il BMI

# Una funzione che usa una variabile presa da fuori
soglia <- 25
sovrappeso_sbagliata <- function(valore){
  return(valore >= soglia)        # soglia non è un argomento!
}
```
