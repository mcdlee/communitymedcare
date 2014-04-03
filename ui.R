library(shiny)

db <- read.csv("content/clinicGPS.csv")
for(i in 1:(length(db)-2)){
  db[[i]] <- as.factor(db[[i]])
}

hos <- levels(as.factor(c(as.character(db$hos1Name),as.character(db$hos2Name), as.character(db$hos3Name), as.character(db$hos4Name))))

shinyUI(
  pageWithSidebar(
    headerPanel(title="Orz"),
    
    sidebarPanel(
      selectInput("hospital", "Choose a hospital:", 
          choices= as.factor(hos),
          tableOutput("table")
    ),
    mainPanel(
      h3(textOutput("text")),
      mapOutput("map")
    )
))

