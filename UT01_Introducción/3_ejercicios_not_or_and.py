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
