"""
Ej. 95: Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada
elemento debe ser una lista de 3 enteros. Imprimir sus elementos accediendo de diferentes
modos.


"""
listaNodriza = []

for x in range(4):
    sublista = []
    
    for y in range(3):
        while True:
            try:
                valor = int(input(f"Introduce el valor entero {y + 1} para la sublista {x + 1}: "))
                sublista.append(valor)
                break
            except ValueError:
                print("X Introduce un valor correcto")

    listaNodriza.append(sublista)

print(f"Tercer número de la primera sublista {listaNodriza[0][2]}")
print(f"Segunda sublista {listaNodriza[1]}")
print(f"ListaNodriza {listaNodriza}")
                
"""
Ej. 96: Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento
debe ser una lista de 5 enteros. Calcular y mostrar la suma de cada lista contenida en la
lista principal.
"""
listaN = []

for x in range(2):
    sublista = []

    for y in range(5):
        while True:
            try:
                valor = int(input(f"Introduce el valor {y + 1} de la lista {x + 1}: "))
                sublista.append(valor)
                break
            except ValueError:
                print("X Introduce un valor correcto")

    listaN.append(sublista)

suma = [[
    listaN[0][0] +
    listaN[0][1] +
    listaN[0][2] +
    listaN[0][3] +
    listaN[0][4]
    ], [
    listaN[1][0] +
    listaN[1][1] +
    listaN[1][2] +
    listaN[1][3] +
    listaN[1][4]
    ]] 

print(suma)

"""
Ej. 97: Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento
debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos,
la tercera tres elementos y así sucesivamente. Sumar todos los valores de las listas.
"""
listaN = []

for x in range(1, 6):
    sublista = []
    print(f"Sublista {x}")

    for y in range(x):
        while True:
            try:
                valor = int(input(f"Introduce el valor {y + 1} de la lista {x}: "))
                sublista.append(valor)
                break
            except ValueError:
                print("X Introduce un valor correcto")

    listaN.append(sublista)

suma = 0

for z in range(len(listaN)):
    for a in range(len(listaN[z])):
        suma += listaN[z][a]

print(f"Lista de números: {listaN}")
print(f"La suma total de los elementos es: {suma}")

"""
Ej. 98: Se tiene la siguiente lista:
lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Después fijar con el valor cero todos los elementos mayores a 50 del
primer elemento de "lista". Volver a imprimir la lista.
"""

lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

for x in range(len(lista[0])):
    if lista[0][x] > 50:
        lista[0][x] = 0

print(lista)

"""
Ej. 99: Se tiene la siguiente lista:
lista = [[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos
en todos los elementos de la variable "lista".
Volver a imprimir la lista
"""

lista = [[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print(lista)

for x in range(len(lista)):
    for y in range(len(lista[x])):
        if lista[x][y] > 10:
            lista[x][y] = 0

print(lista)
