import math
import pandas as pd
#recebe um array p/ calcular desvio padrão
class Desvio:
  table = pd.read_csv('ferramentas/ztable/ztable.csv')  
  status = {}
  ma = 0
  somatoria = 0
  dp = 0
  total = 0
  z = []
  eiy = []

  def __init__(self, arr):
    self.arr = arr
    

  def Dp(self):
    #obter a somatoria
    for item in self.arr:
      self.somatoria += item

    #obter a media aritimética
    self.ma = self.somatoria / len(self.arr)
    self.status['media'] = self.ma
    self.status['somatoria'] = self.somatoria

    #subtrair itens - media Arit elevado ao quadrado
    for item in self.arr:
      self.total += math.pow((item - self.ma), 2)

    #dividir resultado p/ quantidade de itens
    self.total = self.total / len(self.arr)
    self.status['total'] = self.total
    #obter a raiz para obter desvio padrão
    self.dp = math.sqrt(self.total)
    self.status['desvio'] = self.dp

    #distribuição normal padrão
  def Score(self):
    for item in self.arr:
      self.z.append((item - self.ma)/self.dp)
      
    self.status['zcore'] = self.z  
    #falta obter dados da tabela pnorm
    #z = (x-u)/o

  def Colunas(self):
    for item in self.z:
      if '-' in str(item):
        self.eiy.append('0.0'+str(item)[4])
      else:
        print(item) 
        self.eiy.append('0.0'+str(item)[3])

    self.status['eixoY'] = self.eiy

  def getZscore(self,valor,media,distruicao):
    return (valor-media)/distruicao
    
  def getY(self,zscore):

    if '-' in str(zscore):
      coluna = '0.0'+str(zscore)[4]
      y = self.table.loc[(self.table['Z']==zscore) & (self.table[coluna])]
      return 1 - y[coluna].values[0]   
    else:
      coluna = '0.0'+str(zscore)[3]
      y = self.table.loc[(self.table['Z']==zscore) & (self.table[coluna])]
      return y[coluna].values[0]  
  

    
    

      






