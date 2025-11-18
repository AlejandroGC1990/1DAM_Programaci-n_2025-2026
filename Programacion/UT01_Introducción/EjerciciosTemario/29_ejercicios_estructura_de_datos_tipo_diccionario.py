"""
Ej. 159: En el bloque principal del programa definir un diccionario que
almacene los nombres de países como clave y como valor la cantidad de
habitantes. Implementar una función para mostrar cada clave y valor. 
"""
def imprimir(paises):
        for clave in paises:
                print(clave, paises[clave])

paises = {"argentina":40000000, "españa":460000000, "brasil":190000000, "uruguay":340000}
imprimir(paises)

"""
Ej. 160: Crear un diccionario que permita almacenar 5 artículos, utilizar
como clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100. 
"""
def cargar():
        productos = {}
        for x in range(5):
                nombre = input("Introduce el nombre del producto: ")
                precio = int(input("Introduce el precio: "))
                productos[nombre] = precio

        return productos

def imprimirProductos(productos):
        print("Listado de todos los productos")
        for nombre in productos:
                print(nombre, productos[nombre])

def imprimirMayor100(productos):
        print("Listado de artículos con precio mayores a 100")
        for nombre in productos:
                if productos[nombre] > 100:
                        print(nombre)

productos = cargar()
imprimir(productos)
imprimirMayor100(productos)