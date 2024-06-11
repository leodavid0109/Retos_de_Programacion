"""
 Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
 """

# Se recibirá el nombre del poligono y los datos en un arreglo
def area(tipo_poligono, datos):
    if tipo_poligono == "Triángulo":
        print("Área: ", datos[0] * datos[1] / 2)
    elif tipo_poligono == "Rectángulo":
        print("Área: ", datos[0] * datos[1])
    elif tipo_poligono == "Cuadrado":
        print("Área: ", datos[0] ** 2)
    else:
        print("El polígono ingresado no es soportado")

area("Triángulo", [2, 2])
area("Cuadrado", [1])
area("Rectángulo", [5, 4])
area("Hexágono", [5, 4, 5, 56])