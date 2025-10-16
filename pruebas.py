"""
Ej. 78: Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y
cuántas más bajas.
"""

alturas = []
sumaAlturas = 0
alturasMpromedio = 0
alturas_m_promedio = 0
for x in range (5):
    while True:
        try:
            altura = float(input(f"Introduce la altura {x + 1}"))
            alturas.append(altura)
            sumaAlturas += altura
            break
        except ValueError:
            print("X Introduce un valor válido")

promedioAlturas = sumaAlturas / len(alturas)

for y in range (len(alturas)):
    if y > promedioAlturas:
        alturasMpromedio += 1
    elif y < promedioAlturas:
        alturas_m_promedio += 1

print(f"El promedio de alturas es {promedioAlturas} y hay {alturasMpromedio} más altas que el promedio y {alturas_m_promedio} más bajas")
