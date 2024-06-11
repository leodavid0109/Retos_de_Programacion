"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def inversion(palabra):
    nueva = ""
    for i in palabra:
        nueva = i + nueva

    return nueva


print(inversion("Hola mundo"))