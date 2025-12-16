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

"""
Ej. 94: Crear y cargar una lista con los nombres de 5 países y en otra lista paralela la
cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por
último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.


"""
paises = []
poblaciones = []

for u in range(5):
    while True:
        try:
            country = input(f"Introduce el país número {u + 1}: ")
            paises.append(country)
            habitantes = int(input(f"Introdue la población del país {u + 1}: "))
            poblaciones.append(habitantes)
            break
        except ValueError:
            print("X Introduce un valor correcto")

for v in range(4):
    for w in range(4 - v):
        if paises[w] > paises[w + 1]:
            aux = paises[w]
            paises[w] = paises[w + 1]
            paises[w + 1] = aux
            aux2 = poblaciones[w]
            poblaciones[w] = poblaciones[w + 1]
            poblaciones[w + 1] = aux2

print("Países ordenador alfabéticamente")
print(paises)
print(poblaciones)

for x in range(4):
    for y in range(4 - x):
        if poblaciones[y] < poblaciones[y + 1]:
            aux = poblaciones[y]
            poblaciones[y] = poblaciones[y + 1]
            poblaciones[y + 1] = aux
            aux2 = paises[y]
            paises[y] = paises[y + 1]
            paises[y + 1] = aux2

print("Países ordenador por población de mayor a menor")
print(paises)
print(poblaciones)

