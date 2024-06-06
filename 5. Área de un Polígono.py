"""
 Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
 """

def area(poligono):
    lados = len(poligono)

    suma = 0
    for i in range(lados):
        suma += lados[i]

    if lados == 3:
        print(suma / 2)
    elif lados == 4:
        print(suma)