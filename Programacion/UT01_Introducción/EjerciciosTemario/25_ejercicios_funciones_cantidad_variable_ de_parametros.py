"""
Ej. 143: Confeccionar una función que reciba entre 2 y n (siendo n = 2, 3, 4, 5, 6 etc.) valores
enteros, retornar la suma de dichos parámetros
 
"""
def suma(v1, v2, *lista):
        suma = v1 + v2
        for x in range(len(lista)):
                suma += lista[x]

        return suma


print("La suma de 1 + 2")
print(suma(1, 2))
print("La suma de 1 + 2 + 3 + 4 + 5")
print(suma(1, 2, 3, 4, 5))
