# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 01:01:00 2021

@author: Samsung
"""

#arboles.py
#Ejercicio 3.18: Lectura de los árboles de un parque


import csv
def leer_parque (nombre_archivo, parque):
    lista_arboles = []
    f = open(nombre_archivo,'rt', encoding="utf-8")
    rows = csv.reader(f)
    headers = next(rows)
    
    for arbol in rows:
        dic_arboles = dict(zip(headers, arbol))
        
        if dic_arboles ['espacio_ve'] == parque:
            lista_arboles.append(dic_arboles)
            
    return lista_arboles

lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
print(lista_arboles)

#%%
#Ejercicio 3.19: Determinar las especies en un parque

def especies (lista_arboles):
    especie = []
    for arbol in lista_arboles:
        especie.append(arbol ['nombre_gen']) #primero creo una lista con todos los nombres de especieas de cada arbol. aparecen repetidos
        
            
    return set(especie) #antes de pedir q me devuelva la lista le digo q me elimine los duplicados


especie = especies(lista_arboles)
print(especie)


#%%
#Ejercicio 3.20: Contar ejemplares por especie
def contar_ejemplares (lista_arboles):
    from collections import Counter
    ejemplares = Counter()
    for arbol in lista_arboles:
        ejemplares[arbol['nombre_gen']] += 1
    
    return ejemplares

ejemplares = contar_ejemplares(lista_arboles)
print (ejemplares)
        

#%%
# GENERAL PAZ

lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

ejemplares = contar_ejemplares(lista_arboles)


ranking_GP = ejemplares.most_common(5)

print('RANKING CANTIDAD: ', ranking_GP) 




# LOS ANDES
lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')

ejemplares = contar_ejemplares(lista_arboles)



ranking = ejemplares.most_common(5)

print('RANKING CANTIDAD: ', ranking) 



# CENTENARIO

lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

ejemplares = contar_ejemplares(lista_arboles)


ranking = ejemplares.most_common(5)
print('RANKING CANTIDAD : ', ranking)


#%%

#Ejercicio 3.21: Alturas de una especie en una lista
# GENERAL PAZ



def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol ['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas

#GENERAL PAZ
lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
alturasJ = obtener_alturas(lista_arboles, 'Jacarandá')

print(f' GENERAL PAZ ---> MAXIMO: {max(alturasJ)}  PROMEDIO: {sum(alturasJ) /len(alturasJ)} ')

# LOS ANDES
lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
alturasJ = obtener_alturas(lista_arboles, 'Jacarandá')
print(f' LOS ANDES ---> MAXIMO: {max(alturasJ)}  PROMEDIO: {sum(alturasJ) /len(alturasJ)} ')


# CENTENARIO

lista_arboles = leer_parque('../data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
alturasJ = obtener_alturas(lista_arboles, 'Jacarandá')
print(f' CENTENARIO ---> MAXIMO: {max(alturasJ)}  PROMEDIO: {sum(alturasJ) /len(alturasJ)} ')



#%%

#Ejercicio 3.22: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol ['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    return inclinaciones

lista_arboles = leer_parque('data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
inclinacionesJ = obtener_inclinaciones(lista_arboles, 'Jacarandá')
print(inclinacionesJ)


