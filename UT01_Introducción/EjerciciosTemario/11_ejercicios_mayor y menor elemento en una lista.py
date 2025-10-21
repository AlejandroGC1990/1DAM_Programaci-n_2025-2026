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

"""
Ej. 82: Introducir por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar
el nombre de la persona menor en orden alfabético.

"""
lista= []

for x in range(5):
    while True:
        name = input(f"Introduce el nombre {x + 1}: ")
        lista.append(name)
        break

menor = lista[0]

for y in range(1, 5):
    if lista[y] < menor:
        menor = lista[y]

print(f"{menor} es el nombre más pequeño alfabéticamente de la lista: {lista}")

"""
Ej. 83: Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite
dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista) 
"""
lista= []

for x in range(5):
    while True:
        try:
            num = int(input(f"Introduce el número {x + 1}: "))
            lista.append(num)
            break
        except ValueError:
            print("X Introduce un valor correcto")

mayor = lista[0]
counter = 0

for y in range(1, 5):
    if lista[y] == mayor:
        counter += 1
    if lista[y] > mayor:
        mayor = lista[y]

print(f"{mayor} es el número más alto y se repite en la lista {counter} veces")
