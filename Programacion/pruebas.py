"""
Ej. 102: Se tiene que cargar la siguiente información:
 Nombres de 3 empleados
 Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
 Confeccionar el programa para:
a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado
"""
 
listaNombres = []
listaSueldos = []
listaSueldosSumados = []

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
                        
