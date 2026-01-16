"""
Ej. 163: Confeccionar un programa que permita cargar un código de producto
como clave en un diccionario. Guardar para dicha clave el nombre del
producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y
stock.
4) Listado de todos los productos que tengan un stock con valor cero.
"""
def cargar():
        productos = {}
        continua = "s"
        while continua == "s":
                codigo = int(input("Introduce el código del producto: "))
                descripcion = input("Introduce la descripción: ")
                precio = float(input("Introduce el precio; "))
                stock = int(input("Introduce el stock actual: "))
                productos[codigo] = (descripcion, precio,stock)
                continua = input("Desea cargar otro producto: [s/n]?")
        return productos

def imprimir(productos):
        print("Listado completo de productos: ")
        for codigo in productos:
                print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def consulta(productos):
        codigo = int(input("Introduce el codigo de articulo a consultar: "))

def listado_stock_cero(productos):
        print("Listado de artículos con stock en cero. ")
        for codigo in productos:
                if productos[codigo][2] == 0:
                        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

productos = cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)

"""
Ej. 164: Confeccionar una agenda. Utilizar un diccionario cuya clave
sea la fecha. Permitir almacenar distintas actividades para la misma
fecha (se introduce la hora y la actividad)
Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha.

"""
def cargar():
        agenda = {}
        continua1 = "s"
        while continua1 == "s":
                fecha = input("Introduce la fecha con formato dd/mm/aa. ")
                continua2 = "s"
                lista = []
                while continua2 == "s":
                        hora = input("Introduce la hora de la actividad con formato hh:mm ")
                        actividad = input("Introduce la desccripcion de la actividad: ")
                        lista.append((hora,actividad))
                        continua2 = input("Introduce otra actividad para la misma fecha: [s/n]")

                agenda[fecha] = lista
                continua1 = input("Introduce otra fecha: [s/n]")

        return agenda

def imprimir(agenda):
    print("Listado completa de la agenda")
    for fecha in agenda:
        print("Para la fecha: ", fecha)
    
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)

def consulta_fecha(agenda):
        fecha = input("Introduce la fecha que desea consultar: ")
        if fecha in agenda:
                for hora,actividad in agenda[fecha]:
                        print(hora, actividad)
        else:
                print("No hay actividades agendadas para dicha fecha")

agenda = cargar()
imprimir(agenda)
consulta_fecha(agenda)

"""
Ej. 165: Se desea almacenar los datos de 3 alumnos. Definir un diccionario
cuya clave sea el número de documento del alumno. Como valor almacenar
una lista con componentes de tipo tupla donde se almacenen el nombre de
materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres
de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y
sus notas
"""
def cargar():
        alumnos = {}
        for x in range(3):
                dni = int(input("Introduce el DNI del alumno: "))
                listaMaterias = []
                continua = "s"
                while continua == "s":
                        materia = input("Introduce el nombre de la materia que cursa: ")
                        nota = float(input("Introduce la nota: "))
                        listaMaterias.append((meteria, nota))
                        continua = input("Desea cargar otra materia para dicho alumno?[s/n]")

                alumnos[dni] = listamaterias

        return alumnos

def lista(alumnos):
        for dni in alumnos:
                print("DNI del alumno", dni)
                print("Materias que cursa y notas")
                for nota, materia in alumnos[dni]:
                        print(materia, nota)

def consulta_notas(alumnos):
        dni = int(input("Introduce el DNI a consultar"))
        if dni in alumnos:
                for nota, materia in alumnos[dni]:
                        print(materia, nota)

alumnos = cargar()
lista(alumnos)
consulta_notas(alumnos)