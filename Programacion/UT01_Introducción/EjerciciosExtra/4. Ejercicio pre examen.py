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