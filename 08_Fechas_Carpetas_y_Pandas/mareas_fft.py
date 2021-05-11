# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:31:37 2021

@author: Samsung
"""

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col = ['Time'], parse_dates = True)
df.head()

#Ejercicio 8.10

dh = df['12-25-2014':].copy()


delta_t = 2 # tiempo que tarda la marea entre ambos puertos
delta_h = 3 # diferencia de los ceros de escala entre ambos puertos

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()