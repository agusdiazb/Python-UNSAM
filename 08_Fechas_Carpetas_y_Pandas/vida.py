# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:21:43 2021

@author: Samsung
"""


#Ejercicio 8.1: Segundos vividos
from datetime import datetime

def vida (fecha_nacimiento):
    '''
    recibe una cadena con fecha de nacimiento y devuelve total de segundos vividos
    '''
    nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    fecha_actual = datetime.now()
    tiempo_vida = fecha_actual-nacimiento
    
    return ('total de segundos vividos = ', tiempo_vida.total_seconds())
    

def cuantofalta_primavera(fecha):
    '''recibe fecha y devuelve cuantos dias faltan para la primavera'''
    primavera = datetime(2021, 9, 22)
    fecha_x = datetime.strptime(fecha, '%Y/%m/%d')
    dias_faltan = primavera - fecha_x
    return(f'¡¡Faltan {dias_faltan} para la PRIMAVERA!!')

#Ejercicio 8.4: Días hábiles

feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
def dias_habiles(inicio, fin, feriados):
    