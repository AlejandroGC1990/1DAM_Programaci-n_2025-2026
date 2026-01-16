"""
Ej. 183: Confeccionar un programa que solicite la carga de un valor entero por teclado y luego
nos muestre la raíz cuadrada del número y el valor elevado al cubo.
Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math
de la biblioteca estándar de Python. Podemos consultar el módulo math aquí
"""
from math import sqrt, pow

valor = int(input("Introduce un valor entero: "))
r1 = sqrt(valor)
r2 = pow(valor, 3)
print("La raíz cuadrada es", r1)
print("El cubo es", r2)

"""
Ej. 185: Calcular el factorial de un número introducido por teclado.
El factorial de un número es la cantidad que resulta de la multiplicación de determinado
número natural por todos los números naturales que le anteceden excluyendo el cero. Por
ejemplo el factorial de 4 es 24, que resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial sino hay que importar dicha
funcionalidad del módulo math.
El módulo math tiene una función llamada factorial que recibe como parámetro un entero del
que necesitamos que nos retorne el factorial.
Solo importar la funcionalidad factorial del módulo math de la biblioteca estándar de Python
"""
from math import factorial

valor = int(input("Introduce un valor: "))
resu = factorial(valor)
print("El factorial de ", valor, " es ", resu)