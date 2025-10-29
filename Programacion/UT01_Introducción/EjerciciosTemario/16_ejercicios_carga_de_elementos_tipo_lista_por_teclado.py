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

"""
Ej. 104: Definir dos listas de 3 elementos.
En la primera lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.
"""
listaPadres = []
listaHijos = []

for x in range(3):
        sublistaPadres = []
        sublistaHijos = []

        while True:
                try:
                        nombrePadre = input(f"Introduce el nombre del padre de la familia {x + 1}: ")
                        sublistaPadres.append(nombrePadre)
                        nombreMadre = input(f"Introduce el nombre de la madrede la familia {x + 1}: ")
                        sublistaPadres.append(nombreMadre)

                        hijos = input("¿Tienen hijos?(Sí/No) ").lower()

                        if hijos in ("si", "sí", "s", "yes", "y"):
                                while True:
                                        try:
                                                numHijos = int(input("¿Cuántos hijos tienen? "))
                                                
                                                for y in range(numHijos):
                                                        nombreHijo = input(f"Introduce el nombre del hijo {y + 1} de la lista {x + 1}: ")
                                                        sublistaHijos.append(nombreHijo)

                                                break
                                        except ValueError:
                                                print("X Introduce un número válido para la cantidad de hijos.")
                        else:
                                sublistaHijos.append(0)

                        break
                
                except ValueError:
                         print("X Introduce un valor correcto")

        listaPadres.append(sublistaPadres)
        listaHijos.append(sublistaHijos)

for i in range(3):
        print(f"Padre: {listaPadres[i][0]}\nMadre:{listaPadres[i][1]}\nHijos: {listaHijos[i]}")
        print(f"{listaPadres[i][0]} tiene {len(listaHijos)} hijo/s")

"""
Ej. 105: Se desea saber la temperatura media trimestral de cuatro países. Para ello se tiene como dato las temperaturas medias
mensuales de dichos países.
Se debe introducir el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los países y las temperaturas medias mensuales.
b - Imprimir los nombres de las países y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los países y las temperaturas medias trimestrales.
b - Imprimir el nombre del país con la temperatura media trimestral mayor
"""
paises = []
temperaturaT = []
temperaturaTMes = []

for x in range(4):
        pais = input(f"Introduce el nombre del país {x + 1}: ")
        paises.append(pais)
        sumaTemperatura = 0
        sublista = []
        
        for y in range(3):
                while True:
                        try:
                                g = float(input(f"Introduce la temperatura media del país {x + 1} del mes {y + 1}: "))
                                sumaTemperatura += g
                                sublista.append(g)
                                break
                        except ValueError:
                                print("X Introduce un valor correcto")

        temperaturaT.append(sumaTemperatura / 3)
        temperaturaTMes.append(sublista)

temperaturaTMayor = temperaturaT[0]
paisTM = paises[0]
for z in range(1, 4):
        if temperaturaT[z] > temperaturaT[0]:
                temperaturaTMayor = temperaturaT[z]
                paisTM = paises[z]

print(paises)
print(temperaturaT)
for i in range(4):
        print(f"El país {paises[i]} tiene una temperatura media trimestral de {temperaturaT[i]} grados centígrados\ny unas temperaturas duramnte esos meses de {temperaturaTMes[i]}grados centígrados")
        
print(f"El país con la temperatura trimestral media superior es {paisTM} con {temperaturaTMayor}grados centígrados")

"""
Ej. 106: Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el
empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
"""
nombres = []
dias = []
cuantosDias = []

for x in range(3):
        name = input(f"Ingresa el nombre del empleado número {x + 1}: ")
        nombres.append(name)

        while True:
                try:
                        cuantos = int(input("¿Cuántos días ha faltado? "))
                        break
                except ValueError:
                        print("X Introduce un valor correcto")

        sublista = []

        for y in range(cuantos):
                while True:
                        try:                                      
                                d = int(input(f"Intruce el número del día {y + 1} que faltó {name}"))
                                sublista.append(d)
                                break
                        except:
                                print("X Introduce un valor correcto")

        dias.append(sublista)
        cuantosDias.append(cuantos)

menosFaltas = cuantosDias[0]
for z in range(1, len(cuantosDias)):
        if cuantosDias[z] < cuantosDias[0]:
                menosFaltas = cuantosDias[z]
        
for i in range(len(nombres)):
        print(f"El empleado {nombres[i]} ha faltado {cuantosDias[i]} los siguientes días: {dias[i]}")

print(f"Empleados con menos faltas:")
for j in range(len(nombres)):
        if cuantosDias[j] == menosFaltas:
                print(f"- {nombres[j]}")

"""
Ej. 107: Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es
una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
La lista debería tener esta estructura y asignarle esos valores a medida que se crean los
elementos: [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
"""
lista = []
count = 1

for x in range(50):
        lista.append([])
        valor = 1
        
        for y in range(count):
                lista[x].append(valor)
                valor += 1

        count += 1

print(lista)