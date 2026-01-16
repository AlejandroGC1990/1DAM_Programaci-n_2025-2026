def gestionar_cesta():
    cesta = {}
    continua = "s"
    while continua == "s":
        articulo = input("Introduce el nombre del articulo: ")
        precio = float(input(f"Introduce el precio de {articulo}: "))
        cesta[articulo] = precio
        respuesta = input("Quieres añadir otro artículo? (s/n): ")
        if respuesta.lower() != "s":
            continua = "n"

    return cesta

def mostrar_ticket(cesta_compra):
    print("\n--- TICKET COMPRA ---")
    print(f"{'ARTÍCULO': <20} | {'PRECIO':>10}")
    print("-" * 33)

    coste_total = 0

    for articulo, precio in cesta_compra.items():
        print(f"{articulo:<20} | {precio:>9.2f}€")
        coste_total += precio

    print("-" * 33)
    print(f"COSTE TOTAL:      {coste_total:.2f}€")

mi_cesta = gestionar_cesta()
mostrar_ticket(mi_cesta)
""""""
"""
Crear un programa que converta un número entero (mayor que 1 y menor o igual que 1000) a
número romano
"""


def convertir_a_romano(numero):
    if not (1 <= numero <= 1000):
        return "Error: El número debe ser igual o mayor que 1 y menor o igual a 1000."

    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = ""

    for valor_entero, simbolo_romano in valores:
        while numero >= valor_entero:
            resultado += simbolo_romano
            numero -= valor_entero

    return resultado


numero = int(input("Introduce un número entero entre el 1 y el 1000: "))
romano = convertir_a_romano(numero)
print(f"El número {numero} en romano es: {romano}")

"""
escribir un programa que solicite una cantidad de dinero y calcule el mejor desglose de
moneda utilizando el mínimo número de billetes y monedas. Usar una tupla para guardar los
distintos billetes y monedas que existen. Monedas y billetes:

-billetes: 500€, 200€, 100€, 50€, 20€, 10€, 5€.
-monedas: 2€, 1€, 0.5€, 0.20€, 0.10€, 0.05€, 0.02€, 0.01€
"""
def desglosar_dinero():

    sistema_monetario = (
        500,
        200,
        100,
        50,
        20,
        10,
        5,
        2,
        1,
        0.50,
        0.20,
        0.10,
        0.05,
        0.02,
        0.01,
    )

    entrada = float(input("Introduce la cantidad de dinero (ej. 137.56): "))

    cantidad_centimos = int((entrada * 100) + 0.001)

    print(f"--- Desglose para {entrada} euros ---")

    for valor in sistema_monetario:
        valor_centimos = int((valor * 100) + 0.001)

        if cantidad_centimos >= valor_centimos:
            num_unidades = cantidad_centimos // valor_centimos

            cantidad_centimos = cantidad_centimos % valor_centimos

            if num_unidades > 0:
                if valor >= 5:
                    print(f"{num_unidades} billetes de {valor} euros")
                else:
                    print(f"{num_unidades} monedas de {valor} euros")


desglosar_dinero()

"""
Escribe un programa que pida al usuario el nombre de una ciudad, su temperatura máxima y su temperatura mínima.
-Debes guardar esos tres datos en una tupla (ciudad, max, min).
-Esa tupla debes guardarla en una lista general.
-Repetir hasta que el usuario decida parar.
-Al final, recorre la lista y muestra los datos formateados, calculando la temperatura media de cada ciudad.
"""


def gestionar_clima():
    registros_climaticos = []
    continuar = "s"

    print("---ESTACIÓN DE METEOROLOGÍA---")

    while continuar.lower() == "s":
        ciudad = input("Introduce el nombre de la ciudad: ")
        tempMax = float(input("Introduce la temperatura m'axima: "))
        tempMin = float(input("Introduce la temperatura minima: "))

        datosCiudad = (ciudad, tempMax, tempMin)

        registros_climaticos.append(datosCiudad)

        continuar = input("Quieres introducir otra ciudad m'as? ")

    return registros_climaticos


def mostrar_informacion(lista_tuplas):
    print("\n--- INFORME DEL TIEMPO ---")
    print(f"{'ciudad':<15} | {'max':<6} | {'min':<6} | {'media':<6}")
    print("-" * 45)

    for ciudad, maxima, minima in lista_tuplas:
        media = (maxima + minima) / 2

        print(f"{ciudad:<15} | {maxima:<6} | {minima:<6} | {media:<6}")


datos = gestionar_clima()
mostrar_informacion(datos)

"""
Escribe un programa que utilice un diccionario para almacenar el inventario de una tienda.
1.La Clave del diccionario será el Código del Producto (un número entero).
2.El Valor asociado a esa clave será una Lista con tres datos: [Nombre, Precio, Cantidad].
    -Ejemplo visual de la estructura: { 101: ["Ratón", 15.50, 10], 102: ["Teclado", 20.00, 5] }.

El programa debe tener un menú (controlado por un bucle) con estas funciones:
-Añadir Producto: Pide los datos. Si el código ya existe, avisa del error.
-Actualizar Stock: Pide el código y la nueva cantidad. Modifica solo la cantidad en la lista del producto.
-Listar Inventario: Muestra una tabla bonita con todos los productos.
-Valor del Almacén: Calcula cuánto dinero hay invertido en total (suma de Precio * Cantidad de todos los productos).
"""
def añadirProducto(inventario):
    try:
        codigo = int(input("Introduce el c'odigo del producto nuevo (n'umero): "))

        if codigo in inventario:
            print("Error!! Ese c'odigo ya existe en el inventario")
        else:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto en el almac'en: "))

            inventario[codigo] = [nombre, precio, cantidad]
            print("Producto a;adido correctamente")

    except ValueError:
        print("Error: El c'odigo, precio y cantidad deben ser num'ericos")


def actualizar_stock(inventario):
    try:
        codigo = int(input("Introduce el c'odigo del producto a actualizar: "))

        if codigo in inventario:
            stock_actual = inventario[codigo][2]
            print(f"El stock actual de {inventario[codigo][0]} es: {stock_actual}")

            nuevo_stock = int(input("Introduce la nueva cantidad total: "))

            inventario[codigo][2] = nuevo_stock
        else:
            print("El producto no existe.")
    except ValueError:
        print("Error: Introduce un código numérico.")


def listar_inventario(inventario):
    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'CODIGO':<15} | {'NOMBRE':<6} | {'PRECIO':<6} | {'STOCK':<6}")
    print("_" * 45)

    for codigo in inventario:
        datos = inventario[codigo]
        nombre = datos[0]
        precio = datos[1]
        stock = datos[2]

        print(f"{codigo:<15} | {nombre:<6} | {precio:<6} | {stock:<6}")


def calcular_valor_almacen(inventario):
    valor_total = 0.0

    for codigo in inventario:
        precio = inventario[codigo][1]
        cantidad = inventario[codigo][2]

        valor_total = valor_total + (precio * cantidad)

    print(f"\n Valor total del stock en el almac'en: {valor_total}")


def menu():
    almacen = {}

    opcion = 0

    while opcion != 5:
        print("\n --- GESTIO'ON DEL ALMAC'EN ---")
        print("1. Añadir producto. ")
        print("2. Actualizar stock. ")
        print("3. Listar inventario. ")
        print("4. Valor total del almacén. ")
        print("5. Salir. ")

        try:
            opcion = int(input("Introduce una opci'on: "))

            if opcion == 1:
                añadirProducto(almacen)
            elif opcion == 2:
                actualizar_stock(almacen)
            elif opcion == 3:
                listar_inventario(almacen)
            elif opcion == 4:
                calcular_valor_almacen(almacen)
            elif opcion == 5:
                print("Saliendo...")
            else:
                print("Opci'on incorrecta.")
        except ValueError:
            print("Error: Debes introducir un número.")


menu()
