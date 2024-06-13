"""
 Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
 - La función recibirá dos parámetros:
 - Un array que sólo puede contener String con las palabras "run" o "jump"
 - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 - La función imprimirá cómo ha finalizado la carrera:
 - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
 - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 - Si hace "run" en "|" (valla), se variará la pista por "/".
 - La función retornará un Boolean que indique si ha superado la carrera.
 Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""


def carrera_obstaculos(atleta, pista):
    resultado = True
    if len(atleta) != len(pista):
        return "Error: La longitud de los arrays no coincide."
    for i in range(len(atleta)):
        if atleta[i] == "run" and pista[i] == "_":
            continue
        elif atleta[i] == "jump" and pista[i] == "|":
            continue
        elif atleta[i] == "run" and pista[i] == "|":
            pista[i] = "/"
            resultado = False
        elif atleta[i] == "jump" and pista[i] == "_":
            pista[i] = "x"
            resultado = False
    print(pista)
    return resultado


print(carrera_obstaculos(["run", "jump", "run", "jump", "run", "jump", "run", "jump", "run", "jump"],
                         ["_", "|", "_", "|", "_", "|", "_", "|", "_", "|"]))  # True
print(carrera_obstaculos(["run", "jump", "run", "jump", "run", "jump", "run", "jump", "run", "jump"],
                         ["_", "|", "_", "|", "_", "|", "_", "|", "_", "_"]))  # False
