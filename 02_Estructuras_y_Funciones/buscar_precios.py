# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 17:40:29 2021

@author: Samsung
"""

#Ejercicio 2.7: Buscar precios
def buscar_precio (fruta):
    '''busca en archivo ../Data/precios.csv el precio de determinada fruta 
    (o verdura) y lo imprime en pantalla. Si la fruta no figura en el listado
    de precios,imprime un mensaje que lo indique.'''
    
    f = open("../Data/precios.csv", "rt")
    precio = 0
    for line in f:
        row = line.split(',')
        if row [0] == fruta:
            precio = row[1]
    if precio == 0:
        return f'{fruta} no figura en el listado de precios.'
    else:
        return f'El precio de un cajon de {fruta} es de {precio}'
precio = buscar_precio ('Naranja')
print(precio)
