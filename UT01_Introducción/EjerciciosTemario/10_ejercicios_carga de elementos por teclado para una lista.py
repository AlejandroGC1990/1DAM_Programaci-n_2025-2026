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

"""
Ej. 78: Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y
cuántas más bajas.
"""

alturas = []
sumaAlturas = 0
alturasMpromedio = 0
alturas_m_promedio = 0
for x in range (5):
    while True:
        try:
            altura = float(input(f"Introduce la altura {x + 1}: "))
            alturas.append(altura)
            sumaAlturas += altura
            break
        except ValueError:
            print("X Introduce un valor válido")

promedioAlturas = sumaAlturas / len(alturas)

for altura in alturas:
    if altura > promedioAlturas:
        alturasMpromedio += 1
    elif altura < promedioAlturas:
        alturas_m_promedio += 1

print(f"El promedio de alturas es {promedioAlturas} y hay {alturasMpromedio} más altas que el promedio y {alturas_m_promedio} más bajas")

"""
Ej. 79: Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por
la mañana y 4 por la tarde). Confeccionar un programa que permita almacenar los sueldos de
los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.
"""

sueldosM = []
sueldosT = []

for x in range (4):
    while True:
        try:
            sueldoM = float(input(f"Introduce el sueldo del operario {x + 1} de mañana: "))
            sueldosM.append(sueldoM)
            break
        except ValueError:
            print("X Introduce un valor válido en los sueldos")

    while True:
        try:
            sueldoT = float(input(f"Introduce el sueldo del operario {x + 1} de tarde: "))
            sueldosT.append(sueldoT)
            break
        except ValueError:
            print("X Introduce un valor válido en los sueldos")


print(f"El sueldo del turno de mañana es {sueldosM} y el de tarde es {sueldosT}.")
