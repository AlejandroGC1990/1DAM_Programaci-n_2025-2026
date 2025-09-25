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

"""
De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de
entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %,
 mostrar el sueldo a pagar.
b) Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
"""
sueldo = float(input("Introducir sueldo del operario"))
time = int(input("Introducir los años de antigüedad"))

if sueldo < 500 and time >= 10:
    newSueldo = sueldo * 0,20
    print("El sueldo acaba siendo " + newSueldo)
else:
    if sueldo < 500 and time < 10:
        newSueldo = sueldo * 0,50
        print("El sueldo acaba siendo " + newSueldo)
    else:
        if sueldo >= 500:
            print("El sueldo se queda como está: " + sueldo)

"""
Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e imprima su rango de
variación (debe mostrar el mayor y el menor de ellos)
"""