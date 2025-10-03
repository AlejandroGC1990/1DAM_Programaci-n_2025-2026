"""
1. Imprime tu nombre y edad en la misma línea utilizando la función print.
"""
print("Alejandro García Carmona, 35 años")

"""
2. Usa la función type() para imprimir el tipo de dato de una cadena de 
texto, un número entero y un número decimal.
"""
valor1 = input("Introduce texto para ver el tipo de dato: ")
valor2 = float(input("Introduce un número decimal para ver el tipo de dato: "))
valor3 = int(input("Introduce un número entero para ver el tipo de dato: "))

print(type(valor1))
print(type(valor2))
print(type(valor3))

"""
3. Escribe un comentario en varias líneas explicando qué son los tipos de
datos en Python.
"""
"""
Los tipos de datos indican la clase de valores que puede tomar una variable
y determinan qué operaciones se pueden realizar con dichos valores.

Existen varios tipos de datos básicos en Python:
- int: números enteros (ejemplo: 5, -12, 1000).
- float: números decimales o de punto flotante (ejemplo: 3.14, -2.5, 0.0).
- str: cadenas de texto, es decir, secuencias de caracteres (ejemplo: "Hola", 'Python').
- bool: valores lógicos que pueden ser True o False.
- list: colecciones ordenadas y modificables de elementos (ejemplo: [1, 2, 3]).
- tuple: colecciones ordenadas pero inmutables (ejemplo: (10, 20, 30)).
- dict: diccionarios, que almacenan pares clave-valor (ejemplo: {"nombre": "Ana", "edad": 25}).
- set: conjuntos, que almacenan elementos únicos sin orden (ejemplo: {1, 2, 3}).

Python es un lenguaje de tipado dinámico, lo que significa que no es necesario
declarar el tipo de una variable al crearla; el tipo se asigna automáticamente
según el valor que contenga.
"""

"""
4. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: 
"Hola" y "Mundo".
"""
print("Hola " + "mundo")

"""
5. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas
en la misma línea.
"""
name = "Alejandro"
age = 35

print(name, age)

"""
6. Escribe un programa que solicite al usuario su nombre y lo imprima junto con
un saludo.
"""
nombre = input("¿Cómo te llamas?")

print("Hola ", nombre)

"""
7. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo
de dato resultante.
"""
num1 = int(input("Inserta el primer número a sumar"))
num2 = int(input("Inserta el segundo número a sumar"))

suma = num1 + num2

print(f"La suma de {num1} y {num2} es {suma}")

"""
8. Declara y asigna valores a las siguientes variables:
- name: una cadena que contenga tu nombre.
- age: un número entero que represente tu edad.
- height: un número flotante que represente tu altura.
Imprime cada variable en una línea separada.
"""
"""
9. Compara dos cadenas de texto (“apple” y “banana”) usando los operadores > y <
y explica cuál tiene mayor orden alfabético.
"""
"""
10. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5.
Imprime el resultado.
"""
"""
11. Aplica el operador not para invertir el resultado de la comparación 15 > 20.
¿Cuál es el resultado?
"""
"""
12. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la
expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
"""
"""
13. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es
mayor de edad (18 años o más) o menor de edad.
"""
"""
14. Crea un programa que solicite dos números al usuario y compare cuál es mayor.
Si son iguales, muestra un mensaje indicando la igualdad.
"""
"""
15. Crea un programa que solicite una contraseña al usuario y verifique si coincide
con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
"""
"""
16. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un
color (rojo, amarillo,verde) y muestra un mensaje indicando si debe detenerse,
estar alerta o avanzar.
"""
"""
17. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
"""
"""
18. Escribe un programa que use un bucle while para imprimir los números pares
entre 1 y 20.
"""
"""
19. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en
orden inverso.
"""