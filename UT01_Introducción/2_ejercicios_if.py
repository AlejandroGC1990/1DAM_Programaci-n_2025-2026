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