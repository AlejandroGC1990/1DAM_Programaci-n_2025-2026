"""
Ej. 69: Definir una lista que almacene 5 enteros. Sumar todos sus elementos
y mostrar dicha suma.
"""
lista = [1, 2, 3, 4, 5]
count = 0
suma = 0

while count < len(lista):
    suma += lista[count]
    count += 1

print(f"Los elementos de la lista son {lista} y su suma total es {suma}")

"""
Ej. 70:  Definir una lista por asignación que almacene los nombres de los primeros
cuatro meses de año. Mostrar el primer y último elemento de la lista solamente.
"""
listaMeses = ["enero", "febrero", "marzo", "abril"]

print(listaMeses[0])
print(listaMeses[-1])

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
