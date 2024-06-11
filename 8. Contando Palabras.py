"""
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 - Los signos de puntuación no forman parte de la palabra.
 - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

import re


def conteo_palabras(frase):
    # Patrones para eliminar puntuación
    frase = frase.lower()
    frase = re.sub(r'[^\w\s]', '', frase)
    frase = frase.split()

    palabras = {}
    for i in frase:
        if i not in palabras.keys():
            palabras[i] = 1
        else:
            palabras[i] = palabras[i] + 1

    return len(palabras)


print(conteo_palabras("Hola!!, Como estás?, hola"))
