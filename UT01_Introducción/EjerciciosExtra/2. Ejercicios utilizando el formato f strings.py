#Ejercicios utilizando el formato f strings

"""
1. Escribir un programa en que pida al usuario el radio de un círculo. Calcular la
longitud de la circunferencia y el diámetro del círculo y mostrar el resultado
utilizando cadenas con formato (f-strings). Mostrar solo dos decimales
"""
r = float(input("Introduce la longitud del radio del círculo: "))
pi = 3.14

dia = r * 2

c = 2 * pi * r

print(f"El diámetro de la circunferencia es {dia} y la longitud de la circunferencia es {c}")

"""
2. Escribir un programa que pida al usuario una temperatura en grados Fahrenheit. A
continuación, convertir esa temperatura a grados Celsius utilizando la
fórmula C= 5/9(F-32) y mostrar el resultado.
"""
f = float(input("Introduce la temperatura en Fahrenheit a transformar: "))

c = (5/9) * (f - 32)

print(f"{f:.2f}ºF equivalen a {c:.2f}ºC")

"""
3. Escribir un programa en que muestre una tabla formateada de la siguiente
manera: * El nombre en un campo de 10 caracteres (alineado a la izquierda). *
La edad en un campo de 5 dígitos (alineado a la derecha). * El saldo en un
campo de 12 dígitos (alineado a la derecha).
                        Nombre  Edad  Saldo
                        Juan     25  123.456
                        Ana      30  245.987
                        Carlos   22  567.123
"""