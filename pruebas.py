"""
Ej. 71:  Definir una lista por asignación que almacene en el primer componente
el nombre de un alumno y en los dos siguientes sus notas. Imprimir luego el
nombre y el promedio de las dos notas.
"""
alumno = []
name = input("Introduce el nombre del alumno: ")
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
promedio = (nota1 + nota2)/2
alumno.extend([name, nota1, nota2])

print(f"La nota promedio del alumno {alumno[0].capitalize()} y su nota promedia es de {promedio}")
