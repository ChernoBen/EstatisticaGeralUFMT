data <- read.csv(file = 'dadosR.csv')


##Questao 2
#A) Estado Civil
colEst  <-  data["EstCivil"]
absEst <- table(colEst)
relEst <- (absEst/36)

absEst<- data.frame(t(absEst))
absEst <- subset(absEst, select = -Var1)
absEst <- data.frame(absEst) 
absEst

relEst<- data.frame(t(relEst))
relEst <- subset(relEst, select = -Var1)
relEst <- data.frame(relEst) 
relEst

dfEst <- merge(absEst, relEst, by ="colEst")#merge(absIdade,relIdade,by="colIdade","r1")
names(dfEst)[2] <- "Frequencia Absoluta"
names(dfEst)[3] <- "Frequencia Relativa"
dfEst

#B) Procedencia
data <- read.csv(file = 'dadosR.csv')
colProc  <-  data["Procedencia"]
absProc <- table(colProc)
relProc <- (absProc/36)

absProc<- data.frame(t(absProc))
absProc <- subset(absProc, select = -Var1)
absProc <- data.frame(absProc) 
absProc

relProc<- data.frame(t(relProc))
relProc <- subset(relProc, select = -Var1)
relProc <- data.frame(relProc) 
relProc

dfProc<- merge(absProc, relProc, by ="colProc")#merge(absIdade,relIdade,by="colIdade","r1")
names(dfProc)[2] <- "Frequencia Absoluta"
names(dfProc)[3] <- "Frequencia Relativa"
dfProc

#C) Filhos por casados


#D)Idade
data <- read.csv(file = 'dadosR.csv')
colIdade  <- data["idadeAnoMes"]
absIdade <- table(colIdade)
relIdade <- (absIdade/36)

absIdade<- data.frame(t(absIdade))
absIdade <- subset(absIdade, select = -Var1)
absIdade <- data.frame(absIdade) 
absIdade

relIdade<- data.frame(t(relIdade))
relIdade <- subset(relIdade, select = -Var1)
relIdade <- data.frame(relIdade) 
relIdade

dfIdade <- merge(absIdade, relIdade, by ="colIdade")#merge(absIdade,relIdade,by="colIdade","r1")
names(dfIdade)[2] <- "Frequencia Absoluta"
names(dfIdade)[3] <- "Frequencia Relativa"
dfIdade

