"""
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
"""

aux0 = 0
aux1 = 1
print(aux0)
print(aux1)

for i in range(3, 51):
    aux = aux0 + aux1
    aux0 = aux1
    aux1 = aux
    print(aux)
