"""
Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios.
 - No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""


def equilibrio(frase):
    frase = frase.split(" ")
    pila = []
    for i in frase:
        if i == "[" or i == "{" or i == "(":
            pila.append(i)
        elif i == "]" or i == "}" or i == ")":
            if len(pila) == 0:
                return False
            if i == "]" and pila[-1] == "[":
                pila.pop()
            elif i == "}" and pila[-1] == "{":
                pila.pop()
            elif i == ")" and pila[-1] == "(":
                pila.pop()
            else:
                return False
        else:
            continue
    return len(pila) == 0


print(equilibrio("{ [ a * ( c + d ) ] - 5 }")) # True
print(equilibrio("{ a * ( c + d ) ] - 5 }")) # False
