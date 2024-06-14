"""
Simula el funcionamiento de una máquina expendedora creando una operación que reciba dinero (array de monedas) y un
número que indique la selección del producto.
 - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
 - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje y retornar todas las
   monedas.
 - Si no hay dinero de vuelta, el array se retornará vacío.
 - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

monedas_maquina = {5 : 10, 10 : 10, 50 : 10, 100 : 10, 200 : 10, "total" : 3650}

def maquina_expendedora(monedas, producto):
    productos = {
        1: {"nombre": "Coca Cola", "precio": 100},
        2: {"nombre": "Agua", "precio": 50},
        3: {"nombre": "Pepsi", "precio": 150},
        4: {"nombre": "Fanta", "precio": 200},
        5: {"nombre": "Aquarius", "precio": 100},
        6: {"nombre": "Monster", "precio": 250},
        7: {"nombre": "Red Bull", "precio": 200},
        8: {"nombre": "Nestea", "precio": 100},
        9: {"nombre": "Lipton", "precio": 150},
        10: {"nombre": "Powerade", "precio": 200},
    }

    if producto not in productos:
        return "Producto no disponible", monedas
    if productos[producto]["precio"] > sum(monedas):
        return "Dinero insuficiente", monedas

    cambio = sum(monedas) - productos[producto]["precio"]
    monedas_cambio = []

    if monedas_maquina["total"] < cambio:
        return "No hay cambio disponible", monedas_cambio
    else:
        monedas_maquina["total"] -= cambio
        monedas_cambio = devolver_cambio(cambio)

    return productos[producto]["nombre"], monedas_cambio

def devolver_cambio(cambio):
    monedas_cambio = []
    monedas = [200, 100, 50, 10, 5]

    for moneda in monedas:
        while cambio >= moneda and monedas_maquina[moneda] > 0:
            cambio -= moneda
            monedas_cambio.append(moneda)
            monedas_maquina[moneda] -= 1

    return monedas_cambio

# Test
print(maquina_expendedora([200, 200, 100], 1))  # ('Coca Cola', [100])
print(maquina_expendedora([200, 200, 100], 2))  # ('Agua', [])
print(maquina_expendedora([200, 200, 100], 3))  # ('Pepsi', [50])
print(maquina_expendedora([200, 200, 100], 4))  # ('Fanta', [50, 50])
print(maquina_expendedora([200, 200, 100], 5))  # ('Aquarius', [100])
print(maquina_expendedora([200, 200, 100], 6))  # ('Monster', [])
print(maquina_expendedora([200, 200, 100], 7))  # ('Red Bull', [50])
print(maquina_expendedora([200, 200, 100], 8))  # ('Nestea', [])
print(maquina_expendedora([200, 200, 100], 9))  # ('Lipton', [50])
