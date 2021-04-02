# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:22:11 2021

@author: Benjamim
"""

from ferramentas.ferramentas import Ferramentas
from scipy.stats import norm

#arr = [1.55,1.70,1.80]
tools = Ferramentas()
#tools.Dp()
#tools.Score()
#test = tools.status['zcore']
#for chave,valor in tools.status.items():
#  print(chave+" : "+'{}'.format(valor))
  
#tools.Colunas()
table = tools.table
#x,u,dp
'''obtendo zscore e calculando probabilidades'''
z = tools.getZscore(1,1.5,0.25)
y = tools.getArea(z)
ex0 = tools.getZscore(24,45,12)
ex2 = tools.getZscore(54,45,12)
ex1 = tools.getArea(ex0)
ex4 = tools.getArea(ex2)

#area,media,prob
'''descobrindo os valores de x usando zscore, media distribuição:'''
quest = tools.getInvertZ(0.01,181.37,37.6)
q3 = norm.ppf(.01,181,37.6)

#obter desvio padrão
''' se na tiver uma media pré definidar passar 0 como parametro'''
desvio = tools.Dp([550,600,650,700,750,800],0)
#obtendo media
media = tools.ma
#zscore
z = tools.Score()
arr = []
somatoria = 0
for item in z:
    arr.append(tools.getArea(item))
    
for item in arr:
    print(f'Area acumulada: {item * 100}%')

test = tools.getArea(-1.50)
test2 = tools.getArea(1.25)
test3 = test2 - test
 