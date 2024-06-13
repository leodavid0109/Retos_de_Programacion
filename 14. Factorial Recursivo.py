"""
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120
print(factorial(0))  # 1
