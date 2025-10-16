"""
Ej. 81: Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que
identifique el menor valor de la lista y la posición donde se encuentra
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

menor = lista[0]

for y in range (1,5):
    if lista[y] < menor:
        menor = lista[y]

print(f"{menor} es el menor número de la lista {lista}")
    
