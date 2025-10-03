"""
14. Crea un programa que solicite dos números al usuario y compare cuál es mayor.
Si son iguales, muestra un mensaje indicando la igualdad.
"""
num1 = float(input("Introduce un número "))
num2 = float(input("Introduce un número "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} es igual que {num2}")
