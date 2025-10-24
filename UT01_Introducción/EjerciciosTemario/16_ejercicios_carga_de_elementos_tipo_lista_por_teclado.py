"""
Ej. 101: Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos
notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe
ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.
"""
 
listaNombres = []
listaNotas = []

for x in range(3):
        nombre = input(f"Introduce el nombre del alumno nº{x + 1}: ")
        listaNombres.append(nombre)

        sublista = []
        for y in range(2):
            while True:
                try:
                    nota = float(input(f"Ingresa la nota {y + 1}: "))
                    sublista.append(nota)
                    break
                except ValueError:
                    print("X Introduce un valor válido para la nota")

        listaNotas.append(sublista)
                
for z in range(len(listaNombres)):
    print(f"{listaNombres[z]} tiene las notas: {listaNotas[z]}")
                        