"""Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del
lenguaje que lo hagan directamente."""


def decimal_binario(numero):
    binario = ""
    while numero != 1:
        binario = str(numero % 2) + binario
        numero = numero // 2

    binario = "1" + binario

    return binario


print(decimal_binario(78))
