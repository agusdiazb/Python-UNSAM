# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 02:15:50 2021

@author: Samsung
"""

#4.8 invertir lista

def invertir_lista(lista):
    inv_list = []
    for i in reversed(lista):
        inv_list.append(i)
    return inv_list

lista_invertida_c = invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])

lista_invertida_n = invertir_lista([1, 2, 3, 4, 5])

print(lista_invertida_c)

print(lista_invertida_n)