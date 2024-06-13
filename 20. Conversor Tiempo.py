"""
 Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
"""


def convertir_a_milisegundos(dias, horas, minutos, segundos):
    milisegundos = 0
    milisegundos += dias * 86400000
    milisegundos += horas * 3600000
    milisegundos += minutos * 60000
    milisegundos += segundos * 1000
    return milisegundos


print(convertir_a_milisegundos(1, 1, 1, 1))  # 90061000
print(convertir_a_milisegundos(0, 0, 0, 1))  # 1000
print(convertir_a_milisegundos(0, 0, 1, 0))  # 60000
