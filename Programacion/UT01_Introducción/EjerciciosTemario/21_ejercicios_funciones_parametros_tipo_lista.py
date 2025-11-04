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

"""
Ej. 128: Crear y cargar por teclado en el bloque principal del programa una lista de 5
enteros. Implementar una función que imprima el mayor y el menor valor de la lista
"""
def mayorMenor(lista):
        result = []
        mayor = lista[0]
        menor = lista[0]

        for x in range(1, len(lista)):
                if lista[x] > mayor:
                        mayor = lista[x]

        result.append(mayor)

        for y in range(1, len(lista)):
                if lista[y]  < menor:
                        menor = lista[y]

        result.append(menor)

        return result
      

lista = []

for z in range(5):
        num = int(input(f"Introduce el valor {z + 1} de la lista"))
        lista.append(num)

resultado = mayorMenor(lista)
        
print("El valor mayor de la lista es ", resultado[0])
print("El valor menor de la lista es ", resultado[1])

"""
Ej. 129: Crear una lista de enteros por asignación. Definir una función que reciba una lista
de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento
de la lista multiplicado por el valor entero enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
"""
def multiplicarLista(lista, num):
        newLista = []

        for x in range(len(lista)):
                mult = lista[x] * num
                newLista.append(mult)

        return newLista
                
numMult = int(input("Introduce un número entero como multiplicador: "))
cantidadLista = int(input("¿Cuántos números tiene la lista? "))
lista = []

for z in range(5):
        num = int(input(f"Introduce el valor {z + 1} de la lista"))
        lista.append(num)
        
print(f"La lista introducida es {lista} y ha sido multiplicada por {numMult}, dando como resultado {multiplicarLista(lista, numMult)}")
