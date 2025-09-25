"""
Realizar un programa que pida cargar una fecha cualquiera, después verificar si dicha fecha corresponde a Navidad.
"""

day = int(input("Ingresar el día"))
month = int(input("Ingresar el mes"))
year = int(input("Ingresar el año"))

if day == 25 and month == 12 and year == 2025:
    print("¡Es Navidad!")
else:
    print(day + "/" + month + "/" + year)

""" 
Se introducen por teclado tres números, si todos los valores introducidos son menores a 10, imprimir en pantalla la
leyenda "Todos los números son menores a diez".
"""
num1 = int(input("Ingresar primer número"))
num2 = int(input("Ingresar segundo número"))
num3 = int(input("Ingresar tercer número"))

if num1 <= 10 and num2 <= 10 and num3 <= 10:
    print("Todos los números son menores a diez")
else:
    print("Los números son " + num1 + "/" + num2 + "/" + num3)


"""
Se introducen por teclado tres números, si al menos uno de los valores introducidos es menor a 10, imprimir en
pantalla la leyenda "Alguno de los números es menor a diez".
"""
num1 = int(input("Ingresar primer número"))
num2 = int(input("Ingresar segundo número"))
num3 = int(input("Ingresar tercer número"))

if num1 <=10 or num2 <=10 or num3 <=10:
    print("Alguno de los números es menor a diez")
else:
    print("Los números son " + num1 + "/" + num2 + "/" + num3)

"""
Se introducen tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este
resultado se le multiplica por el tercero.
"""
num1 = int(input("Ingresar primer número"))
num2 = int(input("Ingresar segundo número"))
num3 = int(input("Ingresar tercer número"))

result = (num1 + num2) * num3

if num1 == num2 and num1 == num3:
    print("La suma de los 2 primeros números, multiplicando la suma por el num3, el resultado es " + result)
else:
    print("Los números son " + num1 + "/" + num2 + "/" + num3)

"""
Escribir un programa que pida introducir la coordenada de un punto en el plano, es decir dos valores enteros x e y
(distintos a cero). Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y
y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""
x = float(int("Ingresar primer número"))
y = float(int("Ingresar segundo número"))

if x > 0 and y > 0:
    print("Se ubica en el cuadrante 1")

else:
    if x < 0 and y > 0:
        print("Se ubica en el 2º cuadrante")
    else: 
        print("No se pueden introducir valores menores a 0")

