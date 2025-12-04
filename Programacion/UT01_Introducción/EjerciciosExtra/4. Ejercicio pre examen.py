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