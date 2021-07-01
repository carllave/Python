from random import random, seed
# generamos numeros aleatorios entre 0 y 1
for i in range(5):
    print(random())
# generamos numeros aleatorios estableciendo semilla, esto hace que siempre tengamos los mismos resultados
print ('establecinedo semilla')
seed(0)

for i in range(5):
    print(random())