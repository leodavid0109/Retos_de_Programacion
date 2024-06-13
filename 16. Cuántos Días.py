"""
 Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 - La función recibirá dos String y retornará un Int.
 - La diferencia en días será absoluta (no importa el orden de las fechas).
 - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

def cuantos_dias(fecha1: str, fecha2: str) -> int:
    try:
        from datetime import datetime
        fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
        return abs((fecha1 - fecha2).days)
    except ValueError:
        return "Una de las fechas no es válida."

# Test
print(cuantos_dias("01/01/2021", "01/01/2022"))  # 365
print(cuantos_dias("01/01/2022", "01/01/2021"))  # 365
print(cuantos_dias("01/01/2021", "13/01/2021"))  # 12
print(cuantos_dias("13/01/2021", "01/13/2021"))  # 12
print(cuantos_dias("13/01/2021", "01/01/2021"))  # 12