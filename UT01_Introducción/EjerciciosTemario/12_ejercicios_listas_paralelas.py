"""
Ej. 84: Desarrollar un programa que permita cargar 5 nombres de personas y sus edades
respectivas. Una vez realizada la carga por teclado de todos los datos imprimir los nombres
de las personas mayores de edad (mayores o iguales a 18 años)

"""
listaName = []
listaAge = []

for x in range(5):
    while True:
        try:
            name = input(f"Introduce el nombre {x + 1}: ")
            listaName.append(name)
            age = int(input(f"Introduce también la edad: "))
            listaAge.append(age)
            break
        except ValueError:
            print("X Introduce un valor correcto")

mayores = []

for y in range(5):
    if listaAge[y] >= 18:
        mayores.append(listaName[y])

print(f"Los mayores de edad son: {mayores}")

"""
Ej. 85: Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos
precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio
mayor al primer producto introducido.
"""
listaName = []
listaPrice = []

for x in range(5):
    while True:
        try:
            name = input(f"Introduce el nombre {x + 1}: ")
            listaName.append(name)
            price = float(input(f"Introduce también el precio: "))
            listaPrice.append(price)
            break
        except ValueError:
            print("X Introduce un valor correcto")

mayores = []

for y in range(5):
    if listaPrice[y] > listaPrice[0]:
        mayores.append(listaName[y])

print(f"Los productos más caros que el primero son: {mayores}")

"""
Ej. 86: En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar
de acuerdo a lo siguiente:
a) Introducir nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la
condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está
entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
 
"""

listaName = []
listaNotes = []
listaCondiciones = []
listaMuyBueno = []

for x in range(4):
    while True:
        try:
            name = input(f"Introduce el nombre {x + 1}: ")
            listaName.append(name)
            note = float(input(f"Introduce también la nota: "))
            listaNotes.append(note)
            break
        except ValueError:
            print("X Introduce un valor correcto")

for y in range(4):
    if listaNotes[y] >= 8:
        listaCondiciones.append("Muy bueno")
        listaMuyBueno.append(listaName[y])
    elif listaNotes[y] < 4:
        listaCondiciones.append("Insuficiente")
    else:
        listaCondiciones.append("Bueno")

print(f"Nombres : {listaName}")
print(f"Notas: {listaNotes}")
print(f"Condición: {listaCondiciones}")
print(f"Alumnos muy buenos: {listaMuyBueno}")

"""
Ej. 87: Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos
cada una. Generar una tercera lista que surja de la suma de los elementos de la misma posición
de cada lista. Mostrar esta tercera lista. 
"""

lista1 = []
lista2 = []
listaSuma = []

for x in range(4):
    while True:
        try:
            num1 = int(input(f"Introduce el número {x +1} de la primera lista: "))
            lista1.append(num1)
            num2 = int(input(f"Introduce el número {x +1} de la segunda lista: "))
            lista2.append(num2)
            listaSuma.append(num1 + num2)
            break
        except ValueError:
            print("X Introduce un valor válido")


print(listaSuma)
