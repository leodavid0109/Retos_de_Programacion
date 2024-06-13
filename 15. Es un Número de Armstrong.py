"""
 Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
 Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
"""

"""
Número de Armstrong Un número de Armstrong es un número que es igual a la suma de sus propios dígitos cada uno 
elevado a la potencia de la cantidad de dígitos en el número.
"""


def es_armstrong(numero):
    digitos = len(str(numero))
    suma = sum([int(digito) ** digitos for digito in str(numero)])
    return suma == numero


print(es_armstrong(153))  # True
print(es_armstrong(9474))  # True
print(es_armstrong(9475))  # False
print(es_armstrong(120))  # False
