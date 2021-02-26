

# 1)
#  a) Quantitativa continua

#  b) Qualitativa nominal
  
#  c) Quantitativa continua
  
#  d) Qualitativa ordinal
  
#  e) Quantitativa discreta
  
#  f) Quantitativa contınua
  
#  g) Quantitativa contınua

#  h) Quantitativa contınua

# 2)

library(readr)
dadosR <- read_csv("C:/Users/Benjamim/Desktop/estatistica/ex1/dadosR.csv")

# a)
#frequencia absoluta
estadoCivil <- dadosR['Estado Civil']
etCivil <- table(estadoCivil)
print(etCivil)

# b)
regioes <- dadosR['Regiao de procedencia']
frequenciaRegiao <- table(regioes)
print(frequenciaRegiao)

# c)

#3
#a
hist(etCivil,ylabel='Frequencia',xlabel='Estado Civil',labels = TRUE)
#b
grau <- table(grau <- dadosR['Grau de Instrucao'])
barplot(grau, ylab= "Frequência", xlab="graus")


#4

#frequencia absoluta(quantidade de itens menores que cada classe)
#relativa porcentagem de cada classe
#fr acululada primeiro item + segundo = acumulada do segundo e assim vai

#a
estados <- c(3.7,1.82,3.73,1.28,8.14,2.43,
                 3.96,6.54,5.84,2.93,2.82,8.45,
                 7.77,4.65,1.88,2.78,5.54,0.90,
                 4.10,4.30,4.17,5.36,7.35,3.63,
                 5.28,5.41,2.12,4.26,5.09,4.07)
estados <- sort(estados)
#encontrando amplitude de classes
#maior valor - menor valor / numero de classes = amplitude
amplitude <- max(estados) - min(estados)
intervalo <- amplitude/length(estados)

#limites
limite <- c()
contador <- 0
total <- (max(estados)-min(estados))/5

for (item in estados){
  
  if(contador == 0 ){
    
    limite <- append(limite,item)
    contador <- 1
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

library(ggplot2)
ggplot(df, aes(x=xl,y=limite)) + geom_point()

#5
#a)
impressao <- c(8,11,8,12,14,13,11,14,14,15,6,10,14,19,6,12,7,5,8,8
               ,10,16,10,12,12,8,11,6,7,12,7,10,14,5,12,7,9,12,11,9
               ,14,8,14,8,12,10,12,22,7,15)
dias <- c(1:50)

barplot(dias,impressao,xlabel='dias',ylabel='erros')

#b
#histograma
hist(impressao,xlabel='dias',ylabel='erros')

#grafico de folhas
stem(impressao)

#6

# a)

# func: quantitativa discreta
# Seção: qualitativa nominal
# admnistr,direito, redação, estatist, politica, economia : quantitativa continua
# ingles:qualitativa ordinal
# metodologia: qualitativa nominal

# b)

direito <- c(9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9)
estatistica <- c(9,9,8,8,9,10,8,8,9,8,10,7,7,9,9,7,8,7,4,7,7,8,10,9,9)
politica <- c(9,6.5,9,6,6.5,6.5,9,6,10,9,10,6.5,6,10,10,9,10,6,6,6,6.5,6,9,6.5,9)

stem(direito)
stem(estatistica)
stem(politica)

# Em direito Toda a turma obteve nota 9, em estatistica a maior parte dos alunos atingiu 8, politica a nota mais atingida foi 6.
# As materias estatistica e politica possuem maior distruição de notas atingidas que a matéria direito, e as notas mais atingidas
# em estatistica e direito são inferiores as notas predominantes em politica. 

# c)

redacao <- c(8.6,7,8.6,8,8.5,8.2,7.5,9.4,7.9,8.6,7.6,8.3,7,8.6,8.6,9.5,6.3,7.6,6.8,7.5,
             7.7,8.7,7.3,8.5,7)
hist(redacao)

# d)
metodologia <- c('a','c','b','c','a','a','c','c','b','c','b','b','c','b','b','a','c','c','c','b','b','a','c','a','a')
#encontrando amplitude de classes
metClasses <- c()
a <- c()
b <- c()
c <- c()

for (item in metodologia){
  
  if(item == 'c'){
    
    c <- append(c,qtdC)
    
  }else if(item == 'b'){
    
    b <- append(b,qtdB)
    
  }else if(item == 'a'){
    
    a <- append(a,qtdA)
    
  }
}
freqMet <- c(length(a),length(b),length(c))
hist(freqMet)
















