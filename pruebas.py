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
