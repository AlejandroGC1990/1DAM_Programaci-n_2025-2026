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