# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:39:38 2021

@author: Samsung
"""

import pandas as pd
import os
import numpy as np


#Creo los DF con ambos dataset
directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)

df_parques = pd.read_csv(fname)

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
filename = os.path.join(directorio,archivo)

df_veredas = pd.read_csv(filename)

#

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][['altura_tot','diametro']].copy()

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'] [['altura_arbol','diametro_altura_pecho' ]].copy()

#Cambio los nombres de la columna para que ambos DFs coincidan
df_tipas_veredas = df_tipas_veredas.rename(columns = {'altura_arbol': 'altura_tot', 'diametro_altura_pecho':'diametro'})

#Agrego una columna 'AMBIENTE' en cada DF con 'parques' o 'vereda' segun corresponda

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#Junto los DF
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#boxplot de diametro

df_tipas.boxplot('diametro',by = 'ambiente')

#boxplot de alturas

df_tipas.boxplot('altura_tot',by = 'ambiente')




