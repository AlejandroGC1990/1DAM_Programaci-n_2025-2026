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