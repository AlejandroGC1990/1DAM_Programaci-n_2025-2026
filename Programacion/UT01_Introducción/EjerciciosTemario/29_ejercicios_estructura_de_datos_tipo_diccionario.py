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

"""
Ej. 161: Desarrollar una aplicación que nos permita crear un diccionario
inglés/castellano. La clave es la palabra en inglés y el valor es la
palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Introducir por teclado una palabra en inglés y si existe en el
diccionario mostrar su traducción.
"""
def cargar():
        diccionario = {}
        continua = "s"
        while continua == "s":
                caste = input("Introduce una palabra en castellano")
                ing = input("Introduce la palabra en inglés: ")
                diccionario[ing] = caste
                continua = input("Quiere cargar otra palabra?:[s/n]")
        return diccionario

def imprimir(diccionario):
        print("Listado completo del diccionario")
        for ingles in diccionario:
                print(ingles, diccionario[ingles])

def consulta_palabra(diccionario):
        pal = input("Introduce la palabra en inglés a consultar: ")
        if pal in diccionario:
                print("En castellano significa: ", diccionario[pal])

diccionario = cargar()
imprimir(diccionario)
consulta_palabra(diccionario)

"""
Ej. 162: Crear un diccionario en Python que defina como clave el número
de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona introduciendo su número de
documento.
"""
def cargar():
        personas = {}
        for x in range(4):
                numero = int(input("Introduce el número de documento: "))
                nombre = input("Introduce el nombre: ")
                persona[numero] = nombre

        return personas

def imprimir(personas):
        print("Listado del diccionario completo")
        for numero in personas:
                print(numero, personas[numero])

def consulta_por_numero(personas):
        nro = int(input("Introduce el número de documento a consultar: "))
        if nro in personas:
                print("Nombre de la persona: ", personas[nro])
        else:
                print("No existe una persona con dicho número de documento")

personas = cargar()
imprimir(personas)
consulta_por_numero(personas)