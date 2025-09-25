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
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

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

"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y
muestre un medidor indicando si tiene 1, 2 o 3 cifras. Mostrar un mensaje de error si el 
número de cifras es mayor 
"""
num = int(input("Introduce un valor de hasta tres dígitos positivo:"))
if num < 10:
    print("Tiene un dígito")
else:
    if num < 100:
        print("Tiene dos dígitos")
    else:
        if num < 1000:
            print("Tiene tres dígitos")
        else:
            print("Error en la entrada de datos.")

"""
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de
preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un
programa que introduzca los dos datos por teclado e imprima por pantalla el nivel del mismo según el porcentaje de
respuestas correctas que ha obtenido, y sabiendo que:

Nivel máximo: Porcentaje >= 90%.
Nivel medio: Porcentaje >= 75% y < 90%.
Nivel regular: Porcentaje >= 50% y < 75%.
Fuera de nivel: Porcentaje < 50%.
"""
numPreOk = int(input("Número de preguntas acertadas"))
numPreResp = int(input("Número de preguntas respondidas"))
porcent = numPreOk * 100 / numPreResp

if porcent >= 90:
    print("Nivel máximo")
else:
    if porcent >= 75:
        print("Nivel medio")
    else:
        if porcent >= 50:
            print("Nivel regular")
        else: 
            print("Fuera de nivel")
