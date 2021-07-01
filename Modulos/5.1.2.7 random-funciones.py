# Si deseas valores aleatorios enteros, una de las siguientes funciones encajaría mejor:

# randrange(fin)x
# randrange(inico, fin)
# randrange(inicio, fin, incremento)
# randint(izquierda, derecha)
# Las primeras tres invocaciones generarán un número entero tomado (pseudoaleatoriamente) del rango:

# range(fin)
# range(inicio, fin)
# range(inicio, fin, incremento)

from random import randrange, randint

# genera numeros aleatorios de 0 a 10
print(randrange(10), end=' ')
# genera numeros aleatorios entre 5 y 11
print(randrange(5, 11), end=' ')
# generar numeros aleatorios pares entre 0 y 12
print(randrange(0, 12, 2), end=' ')
# genera numeros aleatorios entre 0 y 10
print(randint(0, 10))