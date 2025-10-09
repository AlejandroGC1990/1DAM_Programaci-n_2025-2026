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



