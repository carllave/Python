from random import randint, sample,choice

# genera 10 elementos enternos entre 1 y 10, pueden ser repetidos
for i in range(10):
    print(randint(1, 10), end=',')

# establecemos una lista
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# seleccionamos el orden aleatorio los elementos de la lista, no hay repeticion
print(choice(lst))
# crea una lista con  solo 5 elementos de la lista, no hay repeticion
print(sample(lst, 5))
# crea una lista de 10 elementos de la lista sin repeticion
print(sample(lst, 10))