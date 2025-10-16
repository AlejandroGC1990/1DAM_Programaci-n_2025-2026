"""
Ej. 75: Definir una lista vacía y luego pedir la carga de 5 enteros por teclado y añadirlos
a la lista. Imprimir la lista generada. 
"""

nums = []

for i in range(5):
    while True:
        try:
            n = input(f"Introduce el número {i + 1}: ")
            nums.append(n)
            break
        except ValueError:
            print("X Introduce un número entero")
        
print(f"Los números son {nums}")
