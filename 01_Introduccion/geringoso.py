# Ejercicio Geringoso.py
'''basado en codigo de compañero'''
cadena = "Geringoso"
for i in "aeiou":
    remp_vocal = i + "p" + i
    cadena = cadena.replace( i , remp_vocal)

print(cadena)

