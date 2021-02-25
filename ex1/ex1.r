

# 1)
#  a) Quantitativa continua

#  b) Qualitativa nominal
  
#  c) Quantitativa continua
  
#  d) Qualitativa ordinal
  
#  e) Quantitativa discreta
  
#  f) Quantitativa continua
  
#  g) Quantitativa continua

#  h) Quantitativa continua

# 2)

libra?y(readr)
dadosR <- read_csv("C:/Users/Benjamim/Desktop/estatistica/ex1/dadosR.csv")

# a)
#frequencia absoluta
estadoCivil <- dadosR['Estado Civil']
etCivil <- table(estadoCivil)
print(etCivil)

# b)
regioes <- dadosR['Regiao de procedencia']
frequenciaReg?ao <- table(regioes)
print(frequenciaRegiao)

# c)

#3
#a
hist(etCivil,ylabel='Frequencia',xlabel='Estado Civil',labels = TRUE)
#b
grau <- table(grau <- dadosR['Grau de Instrucao'])
barplot(grau, ylab= "Frequência", xlab="graus")


#4

#frequencia absoluta?quantidade de itens menores que cada classe)
#relativa porcentagem de cada classe
#fr acululada primeiro item + segundo = acumulada do segundo e assim vai

#a
estados <- c(3.7,1.82,3.73,1.28,8.14,2.43,
                 3.96,6.54,5.84,2.93,2.82,8.45,
      ?          7.77,4.65,1.88,2.78,5.54,0.90,
                 4.10,4.30,4.17,5.36,7.35,3.63,
                 5.28,5.41,2.12,4.26,5.09,4.07)
estados <- sort(estados)
#encontrando amplitude de classes
#maior valor - menor valor / numero de classes = amplitude
a?plitude <- max(estados) - min(estados)
intervalo <- amplitude/length(estados)

#limites
limite <- c()
contador <- 0
total <- (max(estados)-min(estados))/5

for (item in estados){
  
  if(contador == 0 ){
    
    limite <- append(limite,item)
    contador ?- 1
  }
  contador <- contador + 1   
  limite <- append(limite,(contador*item)+intervalo)
  
}
hist(limite,labels = TRUE)


#barplot(estados,ylabel='frequencia',xlabel='estados')
#b
count <- 0
xl <- c(1:length(limite))
df <- data.frame(x=xl,y=limite)

lib?ary(ggplot2)
library(MASS)
ggplot(df, aes(x=xl,y=limite)) + geom_point()




















