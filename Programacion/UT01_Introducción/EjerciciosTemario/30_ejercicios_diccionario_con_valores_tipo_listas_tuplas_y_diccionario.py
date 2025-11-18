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
