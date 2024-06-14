"""
 Lee el fichero "22. Challenge.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 - El .txt se corresponde con las entradas de una calculadora.
 - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 - Soporta números enteros y decimales.
 - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
"""


def calculadora():
    try:
        with open("22. Challenge.txt", "r") as f:
            lines = f.readlines()
            result = 0
            for i in range(len(lines)):
                if i % 2 == 0:
                    if i == 0:
                        result = float(lines[i].strip())
                    else:
                        if lines[i - 1].strip() == "+":
                            result += float(lines[i].strip())
                        elif lines[i - 1].strip() == "-":
                            result -= float(lines[i].strip())
                        elif lines[i - 1].strip() == "*":
                            result *= float(lines[i].strip())
                        elif lines[i - 1].strip() == "/":
                            result /= float(lines[i].strip())
            print(result)
    except Exception as e:
        print("No se han podido resolver las operaciones.")


calculadora()
