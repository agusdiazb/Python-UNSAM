# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:02:08 2021

@author: Samsung
"""
#informe_funciones.py

#Ejercicio 6.11: Usemos tu módulo 

#LEER CAMION Y LEER PRECIOS CON PARSE_CSV

from fileparse import parse_csv

def leer_camion (nombre_archivo):
    camion = parse_csv(nombre_archivo ,select = None, types=[str, int, float])
    return camion

def leer_precios(nombre_archivo):
    vent = parse_csv(nombre_archivo ,types=[str,float], has_headers=False)
    return dict(vent)




#Ejercicio 3.13: Recolectar datos

def hacer_informe(lista_camion, dic_precios):
    lista_informe = []
    for dic in lista_camion:
        nombre = dic['nombre']
        num_cajones = dic['cajones']
        precio_c = dic['precio']
        precio_venta = dic_precios[nombre]
        diferencia_de_precio = precio_venta - precio_c
    
        tupla = (nombre, num_cajones, precio_c, diferencia_de_precio)
        lista_informe.append(tupla)
    
    return lista_informe


  


def imprimir(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:^10s} {headers[1]:^10s} {headers[2]:^10s} {headers[3]:^10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
    

  
#Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
     camion = leer_camion(nombre_archivo_camion) #Llamo a las funciones
     precios = leer_precios (nombre_archivo_precios)
     informe = hacer_informe(camion, precios)   
     imprimir(informe)
     
informe_camion('../Data/camion.csv','../data/precios.csv')


