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
