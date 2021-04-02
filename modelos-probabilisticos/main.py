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
#x,u,dp
z = tools.getZscore(1,1.5,0.25)
y = tools.getY(z)
ex0 = tools.getZscore(24,45,12)
ex1 = tools.getZscore(54,45,12)
ex2 = tools.getY(ex0)
ex3 = tools.getY(ex1)

#mais que 39
