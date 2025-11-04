"""
Ej. 127: Definir por asignación una lista de enteros en el bloque principal del programa.
Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos,
la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el
menor.

"""
def sumarLista(lista):
        suma = 0
        for x in range(len(lista)):
                suma += lista[x]

        return suma

def mayorLista(lista):
        mayor = lista[0]

        for y in range(1, len(lista)):
                if lista[y] > mayor:
                        mayor = lista[y]

        return mayor

def menorLista(lista):
        menor = lista[0]

        for z in range(1, len(lista)):
                if lista[z] < menor:
                        menor = lista[z]

        return menor

cantNums = int(input("Introduce cuantos números tiene la lista: "))
lista = []

for z in range(cantNums):
        num = float(input(f"Introduce el valor {z + 1} de la lista"))
        lista.append(num)
        
print("La suma de los valores de la lista es ", sumarLista(lista))
print("El valor mayor de la lista es ", mayorLista(lista))
print("El valor menor de la lista es ", menorLista(lista))

