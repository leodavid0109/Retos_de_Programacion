"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


def isPrimo(num):
    if num < 2:
        return False

    for i in range(2, num + 1 // 2):
        if num % i == 0:
            return False

    return True


for i in range(1, 101):
    if isPrimo(i):
        print(i)
