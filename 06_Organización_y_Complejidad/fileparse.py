# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 01:52:32 2021

@author: Samsung
"""
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        #Con headers
        if has_headers:
            
            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
                
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                        fila = [func(val) for func, val in zip(types, fila) ]
                        
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        
        #sin headers
        else:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                     continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                        
                registros.append(fila)
    return registros
# Lee todos los datos
camion = parse_csv('../Data/camion.csv',select = None, types=[str, int, float])

 # Lee solo algunos datos
cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre','cajones'])

#Ejercicio 6.9: Trabajando sin encabezados
precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)