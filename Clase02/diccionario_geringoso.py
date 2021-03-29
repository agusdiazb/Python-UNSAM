# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 02:21:36 2021

@author: Samsung
"""
#Ejercicio 2.14: Diccionario geringoso.


def diccionario_geringoso(lista_frutas):
    valores = []
    for fruta in lista_frutas:
        for i in "aeiou":
            remp_vocal = i + "p" + i
            fruta = fruta.replace( i , remp_vocal)
        valores.append(fruta)
    
    return dict(zip(lista_frutas, valores))
    
diccionario = diccionario_geringoso(['banana', 'manzana', 'mandarina'])
print(diccionario)