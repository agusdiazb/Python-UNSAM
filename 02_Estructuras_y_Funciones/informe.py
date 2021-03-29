# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:14:14 2021

@author: Samsung
"""

#Ejercicio 2.18
#BALANCE

camion = leer_camion('../data/camion.csv') #Llamo a las funciones
precios = leer_precios ('../data/precios.csv')

pago_prod = 0.0
valor_mercado = 0.0
res = ''
for s in camion:
    pago_prod += s['cajones'] * s ['precio']
    valor_mercado += precios[s['nombre']] * s['cajones']

if pago_prod > valor_mercado:
    res = 'perdida'
   
else:
    res = 'ganancia'

print (f'Se pagaron {pago_prod} y se vendió por {valor_mercado}. Por lo que hubo {res}')