"""
Ej. 88: Se debe crear y cargar una lista donde almacenar 5 sueldos.
a) Desplazar el valor mayor de la lista a la última posición. La primera aproximación para
llegar en el próximo problema al ordenamiento completo de una lista tiene por objetivo analizar
los intercambios de elementos dentro de la lista y dejar el mayor en la última posición.
b) El algoritmo consiste en comparar si la primera componente es mayor a la segunda, en caso que la condición sea
verdadera, intercambiamos los contenidos de las componentes.
"""

sueldos = []
sueldosOrdenados = []

for x in range(5):
    while True:
        try:
            valor = float(input(f"Introduce el sueldo {x + 1}: "))
            sueldos.append(valor)
            break
        except ValueError:
            print("X Introduce un valor correcto")

for y in range(4):
    if sueldos[y] > sueldos[y + 1]:
        aux = sueldos[y]
        sueldos[y] = sueldos[y + 1]
        sueldos[y + 1] = aux

print(sueldos)

"""
Ej. 89: Siguiendo con el anterior ejercicio. Ordena el resto de elementos para que vayan de
menor a mayor
"""

sueldos = []

for x in range(5):
    while True:
        try:
            valor = float(input(f"Introduce el sueldo {x + 1}: "))
            sueldos.append(valor)
            break
        except ValueError:
            print("X Introduce un valor correcto")

for y in range(4):
    for z in range(4):
        if sueldos[z] > sueldos[z + 1]:
            aux = sueldos[z]
            sueldos[z] = sueldos[z + 1]
            sueldos[z + 1] = aux

print(sueldos)

