from math import e, exp, log
# funcion de potencia
print (pow(3,3))
# funcion exponente  e elevado a x
print (exp(10))
# funcion logaritmo natural
log (5)
# funcion logaritmo de x con base b
print(log(2,10))

#ejmplos
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))