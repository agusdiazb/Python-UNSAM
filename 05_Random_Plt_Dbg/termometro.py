# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:59:02 2021

@author: Samsung
"""

#Termometro.py
#Ejercicio 5.5: Gaussiana
import numpy as np
import random

def temperatura(n):
    dist = []
    for i in range(n):
    
        dist.append(random.normalvariate(0,0.2) + 37.5)
    return dist



media = 0
desvio = 0.2
N = 99

temp = temperatura(999)
print(f'Temperatura Maxima:{max(temp)}')
print(f'Temperatura Minima:{min(temp)}')
print(f'PROMEDIO: {np.mean(temp)}')
print(f'MEDIANA: {np.median(temp)}')

np.save('Temperaturas.npy', temp)

#Ejercicio 5.7: Guardar temperaturas
# GUARDO UN NDARRAY CON LAS TEMPERATURAS EN LA CARPETA DATA
b = np.load('Temperaturas.npy')

#Ejercicio 5.8: Empezando a plotear

