"""
2. Escribir un programa que pida al usuario una temperatura en grados Fahrenheit. A
continuación, convertir esa temperatura a grados Celsius utilizando la
fórmula C= 5/9(F-32) y mostrar el resultado.
"""
f = float(input("Introduce la temperatura en Fahrenheit a transformar: "))

c = (5/9) * (f - 32)

print(f"{f:.2f}ºF equivalen a {c:.2f}ºC")