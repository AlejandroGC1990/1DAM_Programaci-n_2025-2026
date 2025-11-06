"""
Ej. 149: Confeccionar un programa con las siguientes funciones:
1) Cargar una lista de 5 enteros.
2) Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""
def cargar():
        lista = []
        for x in range(5):
                num = int(input("Introduce un valor entero: "))
                lista.append(num)

        return lista

def retornar_mayormenor(lista):
        mayor = lista[0]
        menor = lista[0]
        for y in range(1, len(lista)):
                if lista[y] > mayor:
                        mayor = lista[y]
                else:
                        if lista[y] < menor:
                                menor = lista[y]

        return (mayor, menor)

lista = cargar()
mayor,menor = retornar_mayormenor(lista)
print("Mayor valor de la lista: ", mayor)
print("Menor valor de la lista: ", menor)

"""
Ej. 150: Confeccionar un programa con las siguientes funciones:
1) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2) Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y
muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar
a la función que muestra el nombre de empleado con sueldo mayor.

# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""
def cargarEmpleado():
        nombre = input("Introduce el nombre del empleado: ")
        sueldo = float(input("Introduce un valor entero: "))

        return (nombre,sueldo)

def retornar_mayorSueldo(empleado1, empleado2):
        if empleado1[1] > empleado2[1]:
                print(empleado1[0], " tiene el sueldo mayor")
        else:
                print(empleado2[0], " tiene el sueldo mayor")
                
empleado1=cargarEmpleado()
empleado2=cargarEmpleado()
retornar_mayorSueldo(empleado1,empleado2)
