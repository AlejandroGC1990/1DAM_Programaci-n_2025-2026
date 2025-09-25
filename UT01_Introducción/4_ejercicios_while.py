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

"""
Problemas propuestos
Escribir un programa que solicite introducir 10 notas de alumnos y nos imprima por pantalla cuántos
tienen notas mayores o iguales a 7 y cuántos menores
"""
not1 = float(input("Introducir nota de alumno1 "))
not2= float(input("Introducir nota de alumno2 "))
not3= float(input("Introducir nota de alumno3"))
not4= float(input("Introducir nota de alumno4"))
not5= float(input("Introducir nota de alumno5"))
not6= float(input("Introducir nota de alumno6"))
not7= float(input("Introducir nota de alumno7"))
not8= float(input("Introducir nota de alumno8"))
not9= float(input("Introducir nota de alumno9"))
not10= float(input("Introducir nota de alumno10"))

"""
Se introducen un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
"""
n = int(input("¿Cuántas personas?"))
counter = 0
suma = 0 

while counter < n:
    altura = float(input("Inserta la altura de la persona"))
    suma += altura
    counter += 1

promedio = suma / n
print("La altura media es ", promedio)

"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los
sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de
$300. Además el programa deberá mostrar el importe que gasta la empresa en sueldos al personal.
"""

"""
Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se introducen valores por
teclado)
"""
"""
Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
"""
""" 
Realizar un programa que permita cargar dos listas de 15 valores cada una. Mostrar con un mensaje cuál de las dos
listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""
"""
Desarrollar un programa que permita cargar n números enteros y luego nos indique cuántos valores fueron pares y
cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de
dos valores, por ejemplo 11 % 2 retorna un 1):
 if valor % 2 == 0: 
"""