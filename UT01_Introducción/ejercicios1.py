"""Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo 
(el perímetro de un cuadrado se calcula sumando el valor de los cuatro lados)"""

lado = input("Ingrese el valor del lado del cuadrado: ")

lado = float(lado)
perimetro = lado * 4

print("El perimetro del cuadrado es: ")
print(perimetro)


"""Escribir un programa en el cual se introduzcan cuatro números, calcular e imprimir la suma de los dos primeros
y el producto del tercero y el cuarto"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

suma = num1 + num2
producto = num3 * num4

print("La suma de los dos primeros números es: ")
print(suma)

print("El producto del tercer y cuarto número es: ")
print(producto)

"""Realizar un programa que lea cuatro valores numéricos e imprima su suma y su promedio"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

suma = num1 + num2 + num3 + num4
promedio = suma /4

print("La suma de los cuatro números es: ")
print(suma)
print("El promedio de los cuatro números es: ")
print(promedio)