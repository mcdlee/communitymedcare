library(shiny)
library(rCharts)

db <- read.csv("content/clinicGPS.csv")
for(i in 1:(length(db)-2)){
  db[[i]] <- as.factor(db[[i]])
}

filterList <- function (crit) {
  L1 <- subset(db, hos1Name==crit |hos2Name==crit |hos3Name==crit | hos4Name==crit, select=c(clinicName, lon, lat))
  return(L1)
}

plotMap <- function(data) {
  center <- c(mean(data$lat), mean(data$lon))
  L2 <- Leaflet$new()
  L2$setView(center, 12)
#  L2$geoJson(toGeoJSON(data), lat.lon=c("lat", "lon"))
  return(L2)
}


#tn.hos <- levels(as.factor(c(as.character(tn$hos1Name),as.character(tn$hos2Name), as.character(tn$hos3Name), as.character(tn$hos4Name))))

shinyServer(function(input, output) {
  output$text <- renderText(input$hospital, "UTF-8")
  output$table <- renderTable(filterList(input$hospital))
  output$map <- renderMap({
    plotMap(filterList(input$hospital))
  })
})