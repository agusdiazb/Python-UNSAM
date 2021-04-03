# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:01:09 2021

@author: Samsung
"""

#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1.
#El error era semantico
# lo corregi cambiando la funcion utilizando "if 'a' is in expression"
def tiene_a(expresion):
    if 'a' in expresion:
        return True
    elif 'A' in expresion:
        return True
    else:
        return False
        

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.2.
#El error era de sintaxis
#le agregue ':' , el doble ==
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%Ejercicio 3.3: Tipos


def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


#%%
#Ejercicio 3.4: Alcances
#El error era que la funcion no devolvia ningun valor
#la solucion fue agregar 'return c'

def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5: Pisando memoria

#error: al modificar un valor modificamos todos los valores anteriores por eso
#todas las lineas quedan igual a los valores de la ultima iteracion

#Lo corrijo creando el diccionario registro = {} dentro del bucle FOR
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro= {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)