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
#for chave,valor in tools.status.items():
#  print(chave+" : "+'{}'.format(valor))
  
tools.Colunas()
table = tools.table
#x,u,dp
'''obtendo zscore e calculando probabilidades'''
z = tools.getZscore(1,1.5,0.25)
y = tools.getProbZ(z)
ex0 = tools.getZscore(24,45,12)
ex2 = tools.getZscore(54,45,12)
ex1 = tools.getProbZ(ex0)
ex4 = tools.getProbZ(ex2)

#mais que 39
#ex5 = tools.getZscore(39,45,12)
#ex6 = tools.getY(ex5)
#ex7 = tools.getZscore(90-39,45,12)
#ex8 = tools.getY(ex7)

#zscore,media,prob
'''descobrindo os valores de y usando zscore, media distribuição'''
valorX = tools.getInvertZ(1.96,9,2)
valorx2 = tools.getInvertZ(-0.44,9,2)
