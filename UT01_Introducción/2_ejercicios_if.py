"""
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo imprimir su
suma y diferencia, en caso contrario imprimir el producto y la división del primero respecto al segundo
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print("Suma: ")
    print(suma)
    print("Diferencia: ")
    print(diferencia)
else:
    producto = num1 * num2
    division = num1 / num2
    print("Producto: ")
    print(producto)
    print("División: ")
    print(division)

"""
Se introducen tres notas de un alumno, si el promedio es mayor o igual a cinco mostrar un mensaje "Aprobado".
"""
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 5:
    print("Aprobado")

"""
Se introduce por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número
tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""

num = int(input("Ingrese un número positivo de uno o dos dígitos (1..99): "))
if 1 <= num <= 9:
    print("El número tiene un dígito.")
else:
    if 10 <= num <= 99:
        print("El número tiene dos dígitos.")
    else:
        print("El número no es válido.")

"""
Se carga por teclado tres números distintos. Mostrar por pantalla el mayor de ellos
"""
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El mayor es: ")
    print(num1)
else:
    if num2 > num1 and num2 > num3:
        print("El mayor es: ")
        print(num2)
    else:
        print("El mayor es: ")
        print(num3)

"""
Se introduce por teclado un valor entero, mostrar una leyenda
que indique que el número es positivo, negativo o nulo (es decir, 0)
"""

num = float(input("Ingresar el número"))

if num > 0:
    print("El número es positivo")
if num < 0:
    print("El número es negativo")
else:
    print("El número es nulo")
    