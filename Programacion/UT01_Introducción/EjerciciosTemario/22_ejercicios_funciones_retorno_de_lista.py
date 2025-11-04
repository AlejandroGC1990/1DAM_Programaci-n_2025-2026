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

"""
Ej. 134: Desarrollar un programa que permita cargar 5 nombres de personas y sus edades
respectivas. Despues de realizar la carga por teclado de todos los datos, imprimir los
nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.
"""
def cargaLista():
        liNames = []
        liAges = []
        
        for x in range(5):
                name = input(f"Introduce el nombre {x + 1} de la lista: ")
                age = int(input(f"Introduce la edad {x + 1} de la lista: "))
                liNames.append(name)
                liAges.append(age)

        return liNames, liAges
        
def imprimirMayoresEdad(liNames, liAges):
        print(f"Los mayores de edad son: ")
        
        for y in range(len(liAges)):
                if liAges[y] >= 18:
                        print(f"{liNames[y]}, con {liAges[y]} años")

names, ages = cargaLista()
imprimirMayoresEdad(names, ages)

"""
Ej. 135: En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Imprimir todos los sueldos.
3) Cuántos tienen un sueldo superior a 4000 Euros.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.

"""
def cargaLista():
        liSueldos = []
        
        for x in range(10):
                sueldo = int(input(f"Introduce el sueldo {x + 1} de la lista: "))
                liSueldos.append(sueldo)

        return liSueldos
        
def imprimirSueldos(liSueldos):
    print("\nLista de sueldos:")
    for i in range(len(liSueldos)):
        print(f"{i + 1}. {liSueldos[i]}")


def contarMayoresA4000(liSueldos):
    count = 0
    for s in liSueldos:
        if s > 4000:
            count += 1
    print(f"\nHay {count} sueldos mayores a 4000€")


def calcularPromedio(liSueldos):
    total = 0
    for s in liSueldos:
        total += s
    promedio = total / len(liSueldos)
    print(f"\nEl promedio de los sueldos es {promedio:.2f}€")
    return promedio


def mostrarMenoresPromedio(liSueldos, promedio):
    menores = []
    for s in liSueldos:
        if s < promedio:
            menores.append(s)
    print(f"\nSueldos menores al promedio ({promedio:.2f}€): {menores}")


lista = cargaLista()
imprimirSueldos(lista)
contarMayoresA4000(lista)
promedio = calcularPromedio(lista)
mostrarMenoresPromedio(lista, promedio)
