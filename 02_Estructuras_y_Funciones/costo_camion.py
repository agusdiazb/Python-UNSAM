# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:20:34 2021

@author: Samsung
"""

#%%Ejercicio 2.9 Funciones de la biblioteca
#costocamion.py
import csv
def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    costo_total = 0
    headers = next (rows)
    for line in rows:
        try:
            costo = float(line[1]) * float (line[2])
            costo_total += costo
        except ValueError:
            print('Faltan datos')
    
    f.close()
    return costo_total
        
costo_total = costo_camion('../Data/camion.csv')  # o missing.csv
print ('Costo total', costo_total)
