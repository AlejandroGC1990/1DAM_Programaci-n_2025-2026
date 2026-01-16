"""
Ej. 166: Confeccionar un programa que contenga las siguientes funciones:
1) Cargar una lista y retornar al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor
menor a 10.
3) Imprimir la lista

"""
def cargar():
        lista = []
        continua = "s"
        while continua == "s":
                valor = int(input("Introduce un valor: "))
                lista.append(valor)
                continua = input("Agregar otro elemento a la lista [s/n]: ")
        return lista

def fijar_cero(li):
        for x in range(len(li)):
                if li[x] < 10:
                        li[x] = 0

def imprimir(lista):
        for elemento in lista:
                print(elemento, "-", sep = "", end = "")
        print("")

lista = cargar()
print("Lista antes de modificar")
imprimir(lista)
fijar_cero(lista)
print("Lista después de modificar")
imprimir(lista)

"""
Ej. 167: Confeccionar un programa que contenga las siguientes funciones:
1) Cargar una lista de 5 nombres.
2) Ordenar alfabéticamente la lista.
3) Imprimir la lista de nombres

"""
def cargar():
        nombres = []
        for x in range(5):
                nom = input("Introduce un nombre: ")
                nombres.append(nom)

        return nombres

def ordenar(nombres):
        for y in range(4):
                for z in range(4):
                        if nombres[z] > nombres[z + 1]:
                                aux = nombres[z]
                                nombres[z] = nombres[z + 1]
                                nombres[z + 1] = aux

def imprimir(nombres):
        for a in range(len(nombres)):
                print(nombres[a], " ", end = "")

nombres = cargar()
ordenar(nombres)
imprimir(nombres)

"""
Ej. 168: Confeccionar un programa que almacene en un diccionario como
clave el nombre de un contacto y como valor su número telefónico:
1) Cargar los contactos y su número de teléfono.
2) Pemitir modificar el número de teléfono. Se introduce el nombre del
contacto para su búsqueda.
3) Imprimir la lista completa de contactos con sus números de teléfono.

"""
def cargar():
        contactos = {}
        continua = "s"
        while continua == "s":
                nombre = input("Introduce el nombre del contacto: ")
                telefono = input("Introduce el número de teléfono: ")
                contactos[nombre] = telefono
                continua = input("Introduce otro contacto? [s/n]")

        return contactos

def modificar_telefonos(contactos):
        nombre = input("Introduce el nombre del contacto a modificar el teléfono: ")
        if nombre in contactos:
                telefono = input("Introduce el nuevo número de teléfono: ")
                contactos[nombre] = telefono
        else:
                print("No existe un contacto con el nombre ingresado")

def imprimir(contactos):
        print("Listado de contactos")
        for nombre in contactos:
                print(nombre, contactos[nombre])

contactos = cargar()
modificar_telefonos(contactos)
imprimir(contactos)

"""
Ej. 169: Crear un diccionario en Python para almacenar los datos de
empleados de una empresa. La clave será su número de identificación y
en su valor almacenaremos una lista con el nombre, profesión y sueldo.
"""

def cargar():
    empleados = {}
    continua = "s"
    while continua == "s":
        ident = int(input("Introduce el número de identificación: "))
        nombre = input("Introduce el nombre del empleado: ")
        profesion = input("Introduce la profesión: ")
        sueldo = float(input("Introduce el sueldo: "))
        empleados[ident] = [nombre, profesion, sueldo]
        continua = input("¿Introducir más empleados? (s/n): ")
    return empleados

def imprimir(empleados):
    print("Listado completo de empleados")
    for ident in empleados:
        print(ident, empleados[ident][0], empleados[ident][1], empleados[ident][2])

def modificar_sueldo(empleados):
    ident = int(input("Introduce el número de identificación del empleado: "))
    if ident in empleados:
        sueldo = float(input("Introduce el nuevo sueldo: "))
        empleados[ident][2] = sueldo
    else:
        print("No existe un empleado con ese número de identificación")

def imprimir_analistas(empleados):
    print("Listado de empleados con profesión 'analista de sistemas'")
    for ident in empleados:
        if empleados[ident][1].lower() == "analista de sistemas":
            print(ident, empleados[ident][0], empleados[ident][2])

# Programa principal
empleados = cargar()
imprimir(empleados)
modificar_sueldo(empleados)
imprimir(empleados)
imprimir_analistas(empleados)