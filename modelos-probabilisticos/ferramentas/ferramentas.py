import math
import numpy as np
import pandas as pd
from scipy.stats import norm
#recebe um array p/ calcular desvio padrão
class Ferramentas:
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
        
        self.eiy.append('0.0'+str(item)[3])

    self.status['eixoY'] = self.eiy
    
    #x,u,dp
  def getZscore(self,valor,media,distruicao):
    return (valor-media)/distruicao
    
  def getArea(self,zscore):
      
    zscore = float(zscore)  
    position = 2  
    coluna = '0.00'
    
    if '-' in str(zscore): 
        
      zscore *= -1
      zcolum = str(zscore)
      
      if len(str(zscore))>3:
          
          zcolum = ''
          position = 3
          coluna = '0.0'+str(zscore)[position]
          
          for i in range(3):
              
              zcolum += str(zscore)[i]
              
   
                
      y = self.table.loc[(self.table['Z']== float(zcolum)) & (self.table[f'{coluna}'])]
      return 1 - y[f'{coluna}'].values[0]
  
    else:
      print(f'z-score: {zscore}')  
      zcolum = str(zscore)
      position = 2 
      
      if len(str(zscore))>3:
          
          zcolum = ''
          position = 3  
          coluna = '0.0'+str(zscore)[position]
          
          for i in range(3):
              
              zcolum += str(zscore)[i]
              
      print(f'coluna Z: {zcolum}')        
      print(f'coluna Y: {coluna}')
      
      y = self.table.loc[(self.table['Z']==float(zcolum)) & (self.table[f'{coluna}'])]
      return y[f'{coluna}'].values[0]
      #return y[coluna].values[0]  
  
  #zscore,media,prob  
  def getInvertZ(self,zscore,media,probZ):
      
      return norm.ppf(zscore,media,probZ)
     

    
    

      






