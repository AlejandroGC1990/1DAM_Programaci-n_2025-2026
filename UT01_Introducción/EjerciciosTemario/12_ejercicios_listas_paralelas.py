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
