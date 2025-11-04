"""
Ej. 132: Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10.
Desde el bloque principal del programa llamar a ambas funciones
"""
def cargaLista():
        li = []
        
        for x in range(5):
                valor = int(input(f"Introduce el valor {x + 1} de la lista"))
                li.append(valor)

        return li
        
def imprimir_mayor10(li):
        print("Elementos de la lista mayores a 10")

        for y in range(len(li)):
                if li[y] > 10:
                        print(li[y])

lista = cargaLista()
imprimir_mayor10(lista)

"""
Ej. 133: Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.
"""
def cargaLista():
        li = []
        
        for x in range(5):
                valor = int(input(f"Introduce el valor {x + 1} de la lista"))
                li.append(valor)

        return li
        
def imprimir_menorMayor(li):
        menor = li[0]
        mayor = li[0]
        
        for y in range(1, len(li)):
                if li[y] < menor:
                        menor = li[y]

                if li[y] > mayor:
                        mayor = li[y]

        print(f"El menor de la lista es {menor}")
        print(f"El mayor de la lista es {mayor}")


lista = cargaLista()
imprimir_menorMayor(lista)
