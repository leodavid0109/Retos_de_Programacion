"""
 Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 - "X" si han ganado las "X"
 - "O" si han ganado los "O"
 - "Empate" si ha habido un empate
 - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 Nota: La matriz puede no estar totalmente cubierta.
 Se podría representar con un vacío "", por ejemplo.
"""

def tres_en_raya(tablero):
    ganador = []
    # Comprobamos si hay un ganador
    for i in range(3):
        # Comprobamos si hay un ganador en las filas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != "":
            if tablero[i][0] not in ganador:
                ganador.append(tablero[i][0])
        # Comprobamos si hay un ganador en las columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != "":
            if tablero[0][i] not in ganador:
                ganador.append(tablero[0][i])
    # Comprobamos si hay un ganador en las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "":
        if tablero[0][0] not in ganador:
            ganador.append(tablero[0][0])
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "":
        if tablero[0][2] not in ganador:
            ganador.append(tablero[0][2])
    # Comprobamos si han ganado los 2
    if len(ganador) == 2:
        return "Nulo"
    # Comprobamos si hay un ganador
    if len(ganador) == 1:
        return ganador[0]
    # Comprobamos si hay un empate
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "":
                return "Nulo"
    return "Empate"

# Test
print(tres_en_raya([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "X", "O"]]))  # Empate
print(tres_en_raya([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "X", ""]]))  # Nulo
print(tres_en_raya([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "", "O"]]))  # Nulo
print(tres_en_raya([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "X", "O"]]))  # Empate
print(tres_en_raya([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "O", "O"]]))  # O
print(tres_en_raya([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "X", "X"]]))  # X