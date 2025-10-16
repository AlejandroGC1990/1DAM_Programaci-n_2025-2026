"""
Ej. 75: Definir una lista vacía y luego pedir la carga de 5 enteros por teclado y añadirlos
a la lista. Imprimir la lista generada. 
"""

nums = []

for i in range(5):
    while True:
        try:
            n = input(f"Introduce el número {i + 1}: ")
            nums.append(n)
            break
        except ValueError:
            print("X Introduce un número entero")
        
print(f"Los números son {nums}")

"""
Ej. 76: Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
Finalizar la carga de enteros al introducir el cero. Mostrar finalmente el tamaño de la
lista.
 
"""

nums = []

while True:
    try:
        n = int(input(f"Introduce números enteros (escribe '0' para finalizar la carga):"))
        nums.append(n)

        if n == 0:
            break
        
    except ValueError:
        print("X Introduce un número entero")
        
print(f"Los números son {nums}")

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

