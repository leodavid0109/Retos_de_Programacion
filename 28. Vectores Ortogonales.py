"""
Crea un programa que determine si dos vectores son ortogonales.
 - Los dos array deben tener la misma longitud.
 - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def ortogonal(v1, v2):
    if len(v1) != len(v2):
        return False
    return sum([v1[i] * v2[i] for i in range(len(v1))]) == 0

print(ortogonal([1, -2], [2, 1])) # True
print(ortogonal([1, 0], [0, 1])) # True
print(ortogonal([1, 1], [-1, 1])) # True
print(ortogonal([1, 2], [2, 1])) # False