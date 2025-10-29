"""
Ej. 108: Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el
último de la lista.
"""
lista = []

for x in range(5):
        while True:
                try:
                        num = int(input(f"Escribe el número {x + 1} de la lista: "))
                        lista.append(num)
                        break
                except ValueError:
                        print("X Introduce un valor correcto")


print(f"Previa eliminación: {lista}")

lista.pop(0)
lista.pop(1)
lista.pop(2)

print(f"Tras la eliminación: {lista}")
        
"""
Ej. 109: Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los
elementos que sean iguales al número entero 5. 
"""
lista = []
listaSin5 = []

for x in range(10):
        while True:
                try:
                        num = int(input(f"Escribe el número {x + 1} de la lista: "))
                        lista.append(num)
                        break
                except ValueError:
                        print("X Introduce un valor correcto")


print(f"Previa eliminación: {lista}")

for y in range(len(lista)):
        if lista[y] != 5:
                listaSin5.append(lista[y])

print(f"Tras la eliminación: {lista}")
        
"""
Ej. 110: Crear dos listas paralelas. En la primera introducir los nombres de empleados y en
la segunda los sueldos de cada empleado.
Introducir por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su
nombre)
 
"""
listaNombres = []
listaSueldos = []

numEmpleados = int(input("¿Cuántos empleados tiene  la empresa? "))

for x in range(numEmpleados):
        while True:
                try:
                        name = input(f"Escribe el nombre del empleado {x + 1} de la lista: ")
                        listaNombres.append(name)
                        sueldo = float(input(f"Escribe el sueldo de {name}: "))
                        listaSueldos.append(sueldo)
                        break
                except ValueError:
                        print("X Introduce un valor correcto")


print(f"Previa eliminación: {listaNombres}")
print(f"Previa eliminación: {listaSueldos}")

cont = 0
while cont < len(listaSueldos):
        if listaSueldos[cont] > 1000:
                listaSueldos.pop(cont)
                listaNombres.pop(cont)
        else:
                cont += 1
for y in range(len(listaSueldos)):
        print(listaNombres[y], listaSueldos[y])
        
