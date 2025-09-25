"""
1 - Imprimir los números del 1 al 500.
"""
counter = 1

while counter <= 500:
    print(counter)
    counter += 1

"""
2 - Imprimir los números del 50 al 100.
"""

counter = 50

while counter >= 50 and counter <= 100:
    print(counter)
    counter += 1

"""
3 - Imprimir los números del -50 al 0.
"""

counter = -50

while counter >= -50 and counter <= 0:
    print(counter)
    counter += 1

"""
4 - Imprimir los números del 2 al 100 pero de 2 en 2 (2,4,6,8 ....100).
"""

counter = 2

while counter >= 2 and counter <= 100:
    print(counter)
    counter += 2

"""
Codificar un programa que solicite la carga de un valor positivo y nos 
muestre desde 1 hasta el valor introducido de uno en uno.
"""

num = int(input("Insertar número positivo"))
counter = 1

while counter != num:
    print(counter)
    counter += 1
