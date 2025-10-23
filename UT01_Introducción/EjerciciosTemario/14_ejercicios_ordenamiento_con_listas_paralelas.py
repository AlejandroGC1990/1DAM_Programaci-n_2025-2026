"""
Ej. 93: Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas
respectivas.
a) Luego ordenar las notas de mayor a menor.
b) Imprimir las notas y los nombres de los alumnos.
Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor
debemos intercambiar los nombres para que las listas continúen paralelas (es decir que en los
mismos subíndices de cada lista continúe la información relacionada)


"""
alumnos = []
notas = []

for x in range(5):
    while True:
        try:
            alumno = input(f"Introduce el nombre del alumno número {x + 1}: ")
            alumnos.append(alumno)
            valor = float(input(f"Introduce la nota del alumno número {x + 1}: "))
            notas.append(valor)
            break
        except ValueError:
            print("Introduce un valor correcto")

for y in range(4):
    for z in range(4 - y):
        if notas[z] > notas[z + 1]:
            auxNotas = notas[z]
            notas[z] = notas[z + 1]
            notas[z + 1] = auxNotas
            auxAlum = alumnos[z]
            alumnos[z] = alumnos[z + 1]
            alumnos[z + 1] = auxAlum

print(alumnos)
print(notas)
