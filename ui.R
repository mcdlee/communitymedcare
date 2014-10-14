library(shiny)

hos <- levels(as.factor(c(as.character(db$hos1Name),as.character(db$hos2Name), as.character(db$hos3Name), as.character(db$hos4Name))))

shinyUI(
  pageWithSidebar(
    headerPanel(title="社區醫療群"),
    
    sidebarPanel(
      selectInput("hospital", "Choose a hospital:", 
          choices= hos),
      tableOutput("table")
    ),
    mainPanel(
      h3(textOutput("text")),
      chartOutput("map", 'leaflet')
    )
  )
)

