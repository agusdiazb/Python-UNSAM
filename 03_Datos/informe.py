# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:14:14 2021

@author: Samsung
"""
#ABAJO DE TODO ESTA INFORME.PY CON EL BALANCE
#2021
#modficado segun Ejercicio 3.9 FUNCION ZIP()


#Ejercicio leer_camion 2.16
import csv
def leer_camion(nombre_archivo):
    contenido = []
    f = open (nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next (rows)
    for n_linea, linea in enumerate (rows, start = 1):
        try:
            record = dict(zip(headers, linea))
            contenido.append({'nombre' : record['nombre'], 'cajones' : int(record['cajones']), 'precio' : float(record['precio'])})
        except:
            print(f'fila {n_linea}: no entiendo {linea}')
    return contenido
                                     
camion = leer_camion('../data/camion.csv')

print(camion)


# Ejercicio 2.17 leer_precios

import csv

def leer_precios (nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for n_line, line in enumerate (rows, start = 1):
            try:
             
                precios[line[0]] = float(line [1])
    
            except IndexError:
                print( f'Fila{n_line} no entiendo:{line} en file {rows}')
    
    return precios


precios = leer_precios ('../data/precios.csv')
from pprint import pprint
pprint(precios)       

#%%
#Ejercicio 2.18
#BALANCE

camion = leer_camion('../Data/fecha_camion.csv') #Llamo a las funciones
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



          