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

"""
Ej. 144: Confeccionar una función que reciba una serie de edades y me retorne la cantidad que
son mayores o iguales a 18(como mínimo se envía un entero a la función)

 
"""
def mayor18(edad1, *edades):
        count = 0

        if edad1 >= 18:
                count += 1

        for x in range(len(edades)):
                if edades[x] >= 18:
                        count += 1

        return count

print("La cantidad de personas mayores de 18 son: ", mayor18(23, 6, 8, 19, 24))
