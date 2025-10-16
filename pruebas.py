"""
Ej. 77: Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la
lista y el promedio de sueldos.
"""

sueldos = []
sumaSueldos = 0

for x in range (5):
    while True:
        try:
            sueldo = float(input(f"Introduce el sueldo del operario {x + 1}: "))
            sueldos.append(sueldo)
            sumaSueldos += sueldo
            break
        except ValueError:
            print("X Introduce un valor válido")

promedioSueldos = sumaSueldos / len(sueldos)

print(f"Los sueldos de los operarios son {sueldos} y el promedio de sueldos es {promedioSueldos}")

