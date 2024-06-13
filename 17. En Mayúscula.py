"""
 Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""


def mayuscula(string):
    string = string.split()
    for i in range(len(string)):
        string[i] = string[i].capitalize()
    return ' '.join(string)


print(mayuscula('hola mundo'))  # Hola Mundo
print(mayuscula('hola mundo como estas'))  # Hola Mundo Como Estas
