# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:22:11 2021

@author: Benjamim
"""

from ferramentas.ferramentas import Ferramentas
from scipy.stats import norm

arr = [1.55,1.70,1.80]
tools = Ferramentas(arr)
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

#zscore,media,prob
'''descobrindo os valores de x usando zscore, media distribuição:'''

quest = tools.getInvertZ(0.01,181.37,37.6)
q3 = norm.ppf(.01,181,37.6)
