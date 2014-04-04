library(shiny)
library(rCharts)

shinyServer(function(input, output) {
  output$text <- renderText(paste(input$hospital,"所屬社區醫療群"))
  output$table <- renderTable(filterData(input$hospital, select=c("clinicName", "clinicAddr", "groupName")))
  output$map <- renderMap({
    plotMap(filterData(input$hospital, select=c("X", "clinicName", "clinicAddr", "lon", "lat", "groupName", "groupRef")))
  })
})