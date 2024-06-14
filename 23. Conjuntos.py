"""
Crea una función que reciba dos array, un booleano y retorne un array.
 - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""


def conjuntos(array1, array2, booleano):
    if booleano:
        return [i for i in array1 if i in array2]
    else:
        return [i for i in array1 if i not in array2] + [i for i in array2 if i not in array1]


print(conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], True))
print(conjuntos([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], False))
