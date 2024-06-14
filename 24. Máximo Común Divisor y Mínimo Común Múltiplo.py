"""
 Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de
 dos números enteros.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""


def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mcm(a, b):
    return a * b // mcd(a, b)


print(mcd(24, 36))  # 12
print(mcm(24, 36))  # 72
