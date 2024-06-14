"""
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def dibujar(figura, lado):
    if figura == "cuadrado":
        for i in range(lado):
            print("*" * lado)
    elif figura == "triangulo":
        for i in range(lado):
            print("*" * (i + 1))
    elif figura == "diamond":
        for i in range(lado):
            print(" " * (lado - i) + "*" * (i * 2 + 1))
        for i in range(lado - 2, -1, -1):
            print(" " * (lado - i) + "*" * (i * 2 + 1))
    else:
        print("Figura no válida")


figura = input("¿Qué figura quieres dibujar? (cuadrado/triangulo/diamond): ")
lado = int(input("¿Cuánto mide el lado de la figura?: "))

dibujar(figura, lado)
