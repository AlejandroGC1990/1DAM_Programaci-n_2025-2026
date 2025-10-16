"""
Ej. 80: Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el
mayor valor de la lista.
"""
lista= []

for x in range (5):
    while True:
        try:
            valor = int(input(f"Introduce el valor {x + 1}: "))
            lista.append(valor)
            break
        except ValueError:
            print("X Introduce un valor válido")

mayor = lista[0]

for y in range (1,5):
    if lista[y] > mayor:
        mayor = lista[y]

print(f"{mayor} es el mayor número de la lista {lista}")