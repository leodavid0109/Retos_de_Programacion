"""
 Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 - La función recibe un listado que contiene pares, representando cada jugada.
 - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""


def piedra_papel_tijera(lista):
    p1 = 0
    p2 = 0
    for i in lista:
        if i[0] == i[1]:
            continue
        elif i[0] == "R" and i[1] == "S":
            p1 += 1
        elif i[0] == "S" and i[1] == "P":
            p1 += 1
        elif i[0] == "P" and i[1] == "R":
            p1 += 1
        else:
            p2 += 1
    if p1 == p2:
        return "Tie"
    elif p1 > p2:
        return "Player 1"
    else:
        return "Player 2"


# Test
print(piedra_papel_tijera([("R", "S"), ("S", "R"), ("P", "S")]))  # Player 2
print(piedra_papel_tijera([("R", "S"), ("S", "R"), ("P", "R")]))  # Player 1
print(piedra_papel_tijera([("R", "S"), ("S", "R"), ("P", "P")]))  # Tie
print(piedra_papel_tijera([("R", "S"), ("S", "S"), ("P", "P")]))  # Player 1
