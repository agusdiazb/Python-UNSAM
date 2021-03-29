# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:15:45 2021

@author: Samsung
"""

# Camióncommandline Ejercicio 2.8

import csv
import sys
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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
costo_total = costo_camion(nombre_archivo)
print ('Costo total', costo_total)
