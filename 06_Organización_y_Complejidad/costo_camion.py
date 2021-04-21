# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:26:36 2021

@author: Samsung
"""
#Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.
#Con costo_camion y leer_camion del modulo informe_funciones

from informe_funciones import leer_camion


import csv
def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    costo_total = 0
    
    for i in camion:
        costo = i['cajones']* i['precio']
        costo_total += costo
    
    return costo_total
        
costo_total = costo_camion('../Data/camion.csv')  # o missing.csv
print ('Costo total', costo_total)

