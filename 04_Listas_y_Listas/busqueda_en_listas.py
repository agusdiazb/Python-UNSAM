# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 01:53:13 2021

@author: Samsung
"""
#Ejercicio 4.6

#A ) BUSCAR_U_ELEMENTO
def buscar_u_elemento(lista, u):
    ''' si u esta en la lista devolver la posicion
    de su ulitma aparicion
    '''
    pos = -1 #comenzamos suponiendo que u no esta
    
    for i, z in enumerate(lista):
        if z == u:
            pos = i
            break
    return pos

posicion = buscar_u_elemento([1,2,3,2,3,4], 1)
print(posicion)


# B) BUSCAR_N_ELEMENTO
def buscar_n_elemento(lista, N):
    cant = 0
    for i in lista: 
        if i == N:  
            cant += 1  
    return cant
    
cantidad = buscar_n_elemento([1,2,3,2,3,4],1)
print(cantidad)
#%%

# Ejercicio 3.7
 def maximo(lista):
    '''Devuelve el máximo de una lista, 
  la lista debe ser no vacía y de números positivos.
    '''
    maximo_actual = 0
    for i in lista:
        if i > maximo_actual or i < maximo_actual:
            maximo_actual = i
    return maximo_actual
    

maximo = maximo([-5,-4])
print(maximo)
