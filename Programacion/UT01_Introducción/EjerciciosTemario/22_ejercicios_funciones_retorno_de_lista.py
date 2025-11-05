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

"""
Ej. 136: Desarrollar una aplicación que permita introducir por teclado los nombres de 5
artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Introducir por teclado un importe y luego mostrar todos los artículos con un precio menor
o igual al valor introducido
"""
def cargaLista():
    liNames = []
    liPrecios = []
    
    for x in range(5):
        name = input(f"Introduce el nombre del producto {x + 1}: ") 
        precio = float(input(f"Introduce el precio del producto {x + 1}: "))
        liNames.append(name)
        liPrecios.append(precio)

    return liNames, liPrecios


def imprimirNombreYPrecio(liNames, liPrecios):
    print("\nLista de productos y precios:")
    for i in range(len(liNames)):
        print(f"{liNames[i]} - {liPrecios[i]}€")


def imprimirNombreMasCaro(liNames, liPrecios):
    mayor = liPrecios[0]
    indice_mayor = 0

    for s in range(1, len(liPrecios)):
        if liPrecios[s] > mayor:
            mayor = liPrecios[s]
            indice_mayor = s

    print(f"\nEl artículo más caro es '{liNames[indice_mayor]}' con un precio de {liPrecios[indice_mayor]}€")


def filtroPorPrecio(liNames, liPrecios):
    valor = float(input("\nIntroduce un valor para recomendarte artículos más baratos o iguales: "))
    print(f"\nArtículos con precio menor o igual a {valor}€:")

    encontrado = False
    for j in range(len(liPrecios)):
        if liPrecios[j] <= valor:
            print(f"{liNames[j]} - {liPrecios[j]}€")
            encontrado = True

    if not encontrado:
        print("No hay artículos con un precio igual o inferior a ese valor.")


liNames, liPrecios = cargaLista()
imprimirNombreYPrecio(liNames, liPrecios)
imprimirNombreMasCaro(liNames, liPrecios)
filtroPorPrecio(liNames, liPrecios)

"""
Ej. 137: Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos
y en otra los negativos.
3) Imprimir las dos listas generadas.
"""
def cargaLista():
    liNums = []
    
    for x in range(10):
        num = int(input(f"Introduce el número positivo o negativo {x + 1} de la lista: ")) 
        liNums.append(num)

    return liNums

def asignarLista(liNums):
    liPos = []
    liNeg = []
    
    for i in range(len(liNums)):
        if liNums[i] < 0:
                liNeg.append(liNums[i])
        else:
                liPos.append(liNums[i])

    return liPos, liNeg

liNums = cargaLista()
liPos, liNeg = asignarLista(liNums)

print("Lista de negativos: \n", liNeg)
print("Lista de positivos: \n", liPos)
