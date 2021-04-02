# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:22:11 2021

@author: Benjamim
"""

from ferramentas.ferramentas import Desvio

arr = [1.55,1.70,1.80]
tools = Desvio(arr)
tools.Dp()
tools.Score()
test = tools.status['zcore']
for chave,valor in tools.status.items():
  print(chave+" : "+'{}'.format(valor))
  
tools.Colunas()
table = tools.table
#y = table.loc[(table['Z']==2) & (table['0.00'])]

#print(y['0.00'].values[0])  
# filtering data on basis of both filters
#y = table.where(filtro,inplace = True)
#table[table['0.00'] and table['Z'] == 2]
z = tools.getZscore(1,1.5,0.25)
y = tools.getY(2.0)