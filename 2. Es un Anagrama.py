"""
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
 """


def anagrama(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    elif len(palabra1) != len(palabra2):
        return False
    else:
        for i in palabra1:
            if i not in palabra2:
                return False
            else:
                posicion = palabra2.index(i)
                palabra2 = palabra2[:posicion] + palabra2[posicion + 1:]

        return True


print(anagrama("roma", "amor"))
print(anagrama("roma", "roma"))
print(anagrama("amor", "calzado"))
print(anagrama("amor", "romantico"))
