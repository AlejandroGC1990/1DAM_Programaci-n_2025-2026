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
