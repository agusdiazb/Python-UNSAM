# rebotes.py

altura = 100
cantidad_rebotes = 1
while cantidad_rebotes<=10:
    altura = altura * 3/5
    cantidad_rebotes = cantidad_rebotes + 1
    print(cantidad_rebotes, round(altura,4))