# ==============================================================
# Lezione 6 - La stessa funzione, dentro una pagina web
#
# Shiny trasforma una funzione R in un'applicazione con cui si
# interagisce dal browser. Il codice del calcolo è lo stesso di
# lezione_6.R: cambia solo chi gli passa i numeri.
#
# Come si avvia: apri questo file in RStudio e premi "Run App"
# in alto a destra (oppure esegui  shiny::runApp("app.R")  ).
# La prima volta serve installare il pacchetto:
#   install.packages("shiny")
# ==============================================================

library(shiny)


# ---- 1. Le funzioni: identiche a quelle della lezione ---------

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


# ---- 2. ui: che cosa si vede ----------------------------------
# Due cursori per i dati in entrata, due spazi per le risposte.

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
# output$valore e output$classe sono i due spazi della pagina.

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


# Da provare in aula: muovete i cursori fino a far comparire
# "Sovrappeso" esattamente a BMI 25. È lo stesso confine dei test,
# visto da fuori: l'app non protegge dagli errori della funzione.
