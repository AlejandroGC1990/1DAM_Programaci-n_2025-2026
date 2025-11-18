"""
Ej. 157: Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5
caracteres.
"""
def carga():
        lista = []
        cuantas = int(input("¿Cuántas palabras quieres añadir a la lista?"))
                      
        for x in range(cuantas):
                word = input(f"Introduce la palabra número {x + 1} de la lista")
                lista.append(word)

        return lista

def mas5(lista):
        mas = []

        for y in range(len(lista)):
                if len(lista[y]) > 5:
                        mas.append(lista[y])

        return mas

palabras = carga()
print("Lista", palabras)
print("Palabras con más de 5 carácteres:", mas5(palabras))

"""
Ej. 158: Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""
def carga():
        lista = []
        count = int(input("¿Cuántos productoss quieres añadir a la lista?"))
                      
        for x in range(count):
                producto = input(f"Introduce el nombre del producto número {x + 1} de la lista")
                precio = float(input(f"Introduce el precio del producto número {x + 1} de la lista"))
                productoPrecio = (producto, precio)
                lista.append(productoPrecio)

        return lista

def imprimirLista(lista):
        produc1015 = []

        print("Lista de productos y su precio")
        for y in range(len(lista)):
                print("Producto: ", lista[y][0]," --- ", lista[y][1], "€")

                if 10 < lista[y][1] < 15:
                        produc1015.append(lista[y])

        return produc1015

def entre10y15(produc1015):
        print("Lista de productos y su precio entre 10 y 15")
        for z in range(len(produc1015)):
                print("Producto: ", lista[z][0]," --- ", lista[z][1], "€")

compra = carga()
productosFiltrados = imprimirLista(compra)
entre10y15(productosFiltrados)
