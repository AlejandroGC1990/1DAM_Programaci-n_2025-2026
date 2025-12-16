"""
1. Realizar la carga de dos nombres por teclado. Mostrar cuál de los dos es
mayor alfabéticamente o si son iguales.
"""

nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")

if nombre1 == nombre2:
    print("Introdujiste dos nombres iguales")
else:
    if nombre1 > nombre2:
        print(nombre1, "es mayor alfabéticamente")
    else:
        print(nombre2, "es mayor alfabéticamente")

"""
2. Realizar la carga de enteros por teclado. Preguntar después de introducir
el valor si debemos cargar otro valor debiendo el operador introducir la 
cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores introducidos
"""
comando = "si"
suma = 0

while comando == "si":
    valor = int(input("Introduce el valor a sumar "))
    suma += valor

    comando = input("Sumar otro número (si/no)")

print("La suma total da ", suma)

"""
3. Realizar la carga de dos nombres de personas distintos. Mostrarlos por
pantalla ordenados en forma alfabética.
"""
nombre1 = input("Introduce el primer nombre:")
nombre2 = input("Introduce el segundo nombre:")

print("Listado alfabético:")
if nombre1 < nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)
