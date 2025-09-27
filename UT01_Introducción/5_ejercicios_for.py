"""
1. Realizar un programa que imprima en pantalla los números del 0 al 100. Este problema 
lo podemos resolver perfectamente con el ciclo while pero en esta situación lo 
resolveremos empleando el for.
"""
for x in range(101):
    print(x)

"""
2. Realizar un programa que imprima en pantalla los números del 20 al 30.
"""
for x in range (20, 31):
    print(x)

"""
3. Imprimir todos los números impares que hay entre 1 y 100.
"""
for x in range(1,100,2):
    print(x)

"""
4. Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre
posteriormente la suma de los valores introducidos y su promedio. Este problema ya lo 
desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los
diez valores por teclado.
"""
suma = 0

for x in range(10):
    n = int(input("Introduce un número: "))
    suma += n

promedio = suma / 10

print("La suma es ", suma)
print("El promedio es ", promedio)

"""
5. Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe 
cuántos tienen notas mayores o iguales a 5 y cuántos menores.
"""
aprobados = 0
suspensos = 0

for n in range(10):
    nota = float(input("Introducir nota del alumno "))

    if nota < 5:
        suspensos += 1
    else:
        aprobados += 1

print("La cantidad de aprobados es ", aprobados, " y la de suspensos es ", suspensos)

"""
6. Escribir un programa que lea 10 números enteros y luego muestre cuántos valores 
introducidos fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay 
números que son múltiplos de 3 y de 5 a la vez.
"""
mul3 = 0
mul5 = 0

for n in range(10):
    valor = int(input("Introduce el número: "))

    if valor % 3 == 0:
        mul3 += 1
    elif valor % 5 == 0:
        mul5 += 1

print("Los múltiplos de 3 son ", mul3, " y los múltiplos de 5 son ", mul5)

"""
7. Codificar un programa que lea n números enteros y calcule la cantidad de valores 
mayores o iguales a 1000 (n se carga por teclado)
"""
igualMayor = 0
n = int(input("Cuantos valores quieres introducir: "))

for x in range(n):
    valor = int(input("Introduce un valor: "))
    if valor >= 1000:
        igualMayor += 1

print("La cantidad de valores introducidos mayores o iguales a 1000 son: ", igualMayor)

"""
8. Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a 
la medida de la base y la altura de un triángulo. El programa deberá mostrar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.
"""
n = int(input("Número de triángulos: "))
mayores12 = 0

for x in range(n):
    base = float(input("Introducir en cm la medida de la base: "))
    altura = float(input("Introducir en cm la medida de la altura: "))

    superficie = (base * altura) / 2

    if superficie > 12:
        mayores12 += 1
    
    print("Base: ", base)
    print("Altura: ", altura)
    print("Superficie: ", superficie)

print("La cantidad de triángulos con superficie mayor a 12 es: ", mayores12)

"""
9. Desarrollar un programa que solicite la carga de 10 números e imprima la suma de 
los últimos 5 valores introducidos.
"""
counter = 0
suma = 0

for n in range(10):
    valor = float(input("Introduce un valor: "))

    if counter > 4:
        suma += valor
    
    counter += 1

print("La suma de los últimos 5 números es: ", suma)

"""
10. Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)
"""
for x in range(5,51,5):
    print(x)
"""
11. Confeccionar un programa que permita introducir un valor del 1 al 10 y nos muestre 
la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si introducimos 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.
"""
n = int(input("Introduce un número del 1 al 10: "))

for i in range(n,n*13,n):
    print(x)

"""
12. Realizar un programa que lea los lados de n triángulos y muestre:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""
n = int(input("Introduce el número de triángulos: "))
equ = 0
iso = 0
esc = 0

for i in range(n):
    lado1 = float(input("Introduce la medida del lado 1: "))
    lado2 = float(input("Introduce la medida del lado 2: "))
    lado3 = float(input("Introduce la medida del lado 3: "))

    if lado1 == lado2 and lado1 == lado3:
        equ += 1
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        iso += 1
        tipo = "Isósceles"
    else:
        esc += 1
        tipo = "Escaleno"

    print("Este triángulo es: ", tipo)

print("El número de triángulos equiláteros es ", equ,", de isósceles hay", iso, " y escaleno ", esc)

"""
13. Escribir un programa que pida introducir coordenadas (x,y) que representan puntos en 
el plano. Mostrar cuántos puntos se han introducido en el primer, segundo, tercer y 
cuarto cuadrante. Al comenzar el programa se pide que se introduzca la cantidad de 
puntos a procesar.
"""
z = int(input("Introduce la cantidad de coordenadas a calcular: "))
cuadrante1 = 0
cuadrante2 = 0
cuadrante3 = 0
cuadrante4 = 0

for cor in range(z):
    x = float(input("Introduce coordenadas X :"))
    y = float(input("Introduce coordenadas Y :"))

    if x > 0 and y > 0:
        cuadrante1 += 1
    elif x < 0 and y > 0:
        cuadrante2 += 1
    elif x < 0 and y < 0:
        cuadrante3 += 1
    else:
        cuadrante4 += 1

print("El número de coordenadas en el primer cuadrante es ", cuadrante1)
print("El número de coordenadas en el segundo cuadrante es ", cuadrante2)
print("El número de coordenadas en el tercer cuadrante es ", cuadrante3)
print("El número de coordenadas en el cuarto cuadrante es ", cuadrante4)

"""
14. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores introducidos negativos.
b) La cantidad de valores introducidos positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números introducidos que son pares.
"""
"""
15. Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben introducirse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio de edades mayor.
"""