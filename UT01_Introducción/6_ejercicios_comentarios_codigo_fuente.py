"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al introducir el
valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.
"""
suma = 0
valor = int(input("Introduce el valor (con -1 termina): "))

while valor != -1:
    suma += valor
    valor = int(input("Introduce el valor (con -1 termina): "))

print("La suma de los valores ingresados es ", suma)
    
"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. Definir
varias líneas de comentarios indicando el nombre del programa, el programador y la fecha de la última modificación.
Utilizar el carácter # para los comentarios.
"""