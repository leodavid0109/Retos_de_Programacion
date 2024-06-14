"""
 Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 ¿De cuántas maneras eres capaz de hacerlo?
 Crea el código para cada una de ellas.
"""

# 1. Usando un bucle for
print("1. Usando un bucle for")
for i in range(1, 101):
    print(i)

# 2. Usando un bucle while
print("2. Usando un bucle while")
i = 1
while i <= 100:
    print(i)
    i += 1

# 3. Usando una función recursiva
print("3. Usando una función recursiva")


def contar(n):
    if n <= 100:
        print(n)
        contar(n + 1)


contar(1)

# 4. Usando una lista y un bucle for
print("4. Usando una lista y un bucle for")
numeros = list(range(1, 101))
for n in numeros:
    print(n)

# 5. Usando una lista y un bucle while
print("5. Usando una lista y un bucle while")
numeros = list(range(1, 101))
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1

# 6. Usando una lista y un bucle for con enumerate
print("6. Usando una lista y un bucle for con enumerate")
numeros = list(range(1, 101))
for i, n in enumerate(numeros):
    print(n)
