"""
Ej. 101: Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos
notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe
ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.
"""
 
listaNombres = []
listaNotas = []

for x in range(3):
        nombre = input(f"Introduce el nombre del alumno nº{x + 1}: ")
        listaNombres.append(nombre)

        sublista = []
        for y in range(2):
            while True:
                try:
                    nota = float(input(f"Ingresa la nota {y + 1}: "))
                    sublista.append(nota)
                    break
                except ValueError:
                    print("X Introduce un valor válido para la nota")

        listaNotas.append(sublista)
                
for z in range(len(listaNombres)):
    print(f"{listaNombres[z]} tiene las notas: {listaNotas[z]}")
                        
"""
Ej. 102: Se tiene que cargar la siguiente información:
 Nombres de 3 empleados
 Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
 Confeccionar el programa para:
a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

"""
 
listaNombres = []
listaSueldos = []
listaSueldosSumados = []

for x in range(3):
        nombre = input(f"Introduce el nombre del empleado número {x + 1}")
        listaNombres.append(nombre)

        sublista = []
        sueldoSumado = 0

        for y in range(3):
            while True:
                try:
                    sueldo = float(input(f"Introduce el sueldo número {y + 1} del empleado número {x + 1}: "))
                    sublista.append(sueldo)
                    sueldoSumado += sueldo
                    break
                except ValueError:
                    print("X Introduce un valor válido para el sueldo")

        listaSueldos.append(sublista)
        listaSueldosSumados.append(sueldoSumado)
        
for z in range(3):
    print(f"{listaNombres[z]} cobró estos sueldos: {listaSueldos[z]} (Total: {listaSueldosSumados[z]})")

                 
mayor_ingreso = max(listaSueldosSumados)
indice_mayor = listaSueldosSumados.index(mayor_ingreso)
print(f"El empleado con mayor ingreso acumulado es {listaNombres[indice_mayor]}")                
                
"""
Ej. 103: Solicitar por teclado la introducción de dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista.
El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.
"""

elementos = int(input("Introduyce el número de sublistas: "))
subelementos = int(input("Introduyce el número de elementos para las sublistas: "))

lista = []
sumaSuma = 0

for x in range(elementos):
        sublista = []
        suma = 0

        for y in range(subelementos):
                while True:
                        try:
                                valor = float(input(f"Introduce el valor {y + 1} de la sublista {x + 1}: "))
                                sublista.append(valor)
                                suma += valor
                                break
                        except ValueError:
                                print("X Introduce un valor correcto")

        lista.append(sublista)
        sumaSuma += suma
        
print(lista)
print(sumaSuma)

