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

"""
Desarrollar un programa que permita la carga de 10 valores por teclado y 
nos muestre posteriormente la suma de los valores introducidos y su 
promedio.
"""
num1 = float(input("Insertar número1"))
num2 = float(input("Insertar número2"))
num3 = float(input("Insertar número3"))
num4 = float(input("Insertar número4"))
num5 = float(input("Insertar número5"))
num6 = float(input("Insertar número6"))
num7 = float(input("Insertar número7"))
num8 = float(input("Insertar número8"))
num9 = float(input("Insertar número9"))
num10 = float(input("Insertar número10"))

suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 
print(suma)
print(suma/10)

"""
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida introducir por teclado la cantidad de piezas a procesar y luego
introduzca la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el 
rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
"""

numPiezas = int(input("Número de piezas"))
numPiezasAptas = 0
counter = 0

while counter <= numPiezas:
    longPiezas = float(input("Longitud de los perfiles"))

    if longPiezas >= 1.20 and longPiezas <= 1.30:
        print(counter)

    counter += 1
