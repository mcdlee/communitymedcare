clinic.list <- read.csv("../content/clinic_list.csv", fileEncoding="UTF-8")

attach(clinic.list)
clinic.list$clinicRef <- as.factor(clinicRef)
clinic.list$groupRef <- as.factor(groupRef)
clinic.list$hos1Ref <- as.factor(hos1Ref)
clinic.list$hos2Ref <- as.factor(hos2Ref)
clinic.list$hos3Ref <- as.factor(hos3Ref)
clinic.list$hos4Ref <- as.factor(hos4Ref)

library(ggmap)
library(leafletR)
library(scales)

# geocode 很脆弱
sub.1 <- head(clinic.list, 900)
sub.2 <- tail(head(clinic.list, 1800), 900)
sub.3 <- tail(head(clinic.list, 2700), 900)
sub.4 <- tail(clinic.list, 301)

gps.1 <- geocode(iconv(as.character(sub.1$clinicAddr), to="utf8"), source="google")
sub.1 <- cbind(sub.1, gps.1)

gps.2 <- geocode(iconv(as.character(sub.2$clinicAddr), to="utf8"), source="google")
sub.2 <- cbind(sub.2, gps.2)

gps.3 <- geocode(iconv(as.character(sub.3$clinicAddr), to="utf8"), source="google")
sub.3 <- cbind(sub.3, gps.3)

gps.4 <- geocode(iconv(as.character(sub.4$clinicAddr), to="utf8"), source="google")
sub.4 <- cbind(sub.4, gps.4)

clinic.list.gps<-rbind(sub.1, sub.2, sub.3, sub.4)

write.csv(clinic.list.gps, "../content/clinicGPS.csv")
# backup
