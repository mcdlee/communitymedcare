library(plyr)
library(rCharts)
library(scales)


# get database
db <- read.csv("content/clinicGPS.csv")

for(i in 1:(length(db)-2)){
  db[[i]] <- as.factor(db[[i]])
}
groupP <- levels(droplevels(db$groupRef)) #for color
groupPool <- sample(groupP, length(groupP), replace=FALSE) #dirty code

# filterData
filterData <- function (crit, select=c("clinicName", "clinicAddr", "lon", "lat", "groupName")) {
  L1 <- subset(db, hos1Name==crit |hos2Name==crit |hos3Name==crit | hos4Name==crit,
               drop=TRUE,
               select=select)
  return(L1)
}

#from data.frame to list
getList <- function (df) {
  L2 <- dlply(df, .(X), .drop=TRUE,
        summarize,
        Name = clinicName,
        Addr = clinicAddr,
        group = groupName,
        groupRef = groupRef,
        longitude=lon, latitude=lat,
        fillColor = hue_pal()(length(groupPool))[match(groupRef, groupPool)],
        popup = sprintf("%s <br/> %s", clinicName, groupName)
        )
  
  for(i in 1:length(L2)) {
    L2[[i]] <- as.list(L2[[i]])
  }
  
  return(L2)
}

#get center
getCenter <- function(data) {
  center <- c(mean(data$lat), mean(data$lon))
  return(center)
}

#from data to list then map
plotMap <- function(data) {
  center <- getCenter(data)
  list <- getList(data)
  L2 <- Leaflet$new()
  L2$setView(center, 11)
  L2$geoJson(toGeoJSON(list),
             onEachFeature = '#! function(feature, layer){
              layer.bindPopup(feature.properties.popup)
              } !#',
             pointToLayer = "#! function(feature, latlng){
              return L.circleMarker(latlng, {
              radius: 8,
              fillColor: feature.properties.fillColor || 'red',
              color: '#000',
              weight: 1,
              fillOpacity: 0.7
              })
              } !#")
  L2$fullScreen(TRUE)
  return(L2)
}
