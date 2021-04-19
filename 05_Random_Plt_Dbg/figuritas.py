# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:56:35 2021

@author: Samsung
"""

import numpy as np
import random

figus_total = 670


#Ejercicio 5.9: Crear
def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album

album = crear_album(figus_total)

#Ejercicio 5.10: Incompleto
def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False

estado = album_incompleto(album)

#Ejercicio 5.11: Comprar
def comprar_figu(figus_total):
    figu = random.randint(1,figus_total)
    return figu

#Ejercicio 5.12: Cantidad de compras
def cuantas_figus(figus_total):
    cantidad_compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album) == True:
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
        cantidad_compras +=1
    return cantidad_compras
    
    
print(cuantas_figus(figus_total))    

#%%
#Ejercicio 5.13:
#ALBUM DE 6 FIGURITAS    
figus_total = 6
n_repeticiones = 1000
    
figus6 = [cuantas_figus(figus_total)for i in range(n_repeticiones)]    

print(f'En promedio hay que comprar {np.mean(figus6)} para llenar el album de 6 figuritas')    
    
    
#%%    
#Ejercicio 5.14:

figus_total = 670
n_repeticiones = 100

figus = [cuantas_figus(figus_total) for i in range (n_repeticiones)]

print(f'En promedio hay que comprar {np.mean(figus)} para llenar el album de 670 figuritas') 

#%%
#5.15

figus_paquete = 5
def comprar_paquete(figus_total, figus_paquete):
    paquete= list()
    for i in range(5):
        paquete.append(comprar_figu(figus_total))
    return paquete
    
paquete = comprar_paquete(figus_total, figus_paquete)

#%%

#Ejercicio 5.17:    
def cuantos_paquetes(figus_total, figus_paquete):
    cantidad_paquetes = 0
    album = crear_album(figus_total)
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i-1] += 1
        cantidad_paquetes +=1
    return cantidad_paquetes
    
    
    
cantidad_paquetes =cuantos_paquetes(figus_total, figus_paquete)
#%%
#Ejercicio 5.18:
n_repeticiones = 100
figus_total = 670
figus_paquete = 5

paquetes = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]


print(f'En promedio hay que comprar {np.mean(paquetes)} para llenar el album de 670 figuritas')




#%%
import matplotlib.pyplot as plt
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1  # esta linea se modifico del codigo de github dado por el ej. se le agrego el -1. ver explicacion en slack buscando "index 670 is out of bounds for axis 0 with size 670"
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show() 