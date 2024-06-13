"""
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""


def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = texto.replace(".", "")
    texto = texto.replace(",", "")
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    return texto == texto[::-1]  # texto[::-1] es para invertir el texto


print(es_palindromo("Ana lleva al oso la avellana."))  # True
print(es_palindromo("Hola"))  # False
