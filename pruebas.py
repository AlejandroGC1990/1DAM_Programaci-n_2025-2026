"""
Ej. 76: Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
Finalizar la carga de enteros al introducir el cero. Mostrar finalmente el tamaño de la
lista.
 
"""

nums = []

while True:
    try:
        n = int(input(f"Introduce números enteros (escribe '0' para finalizar la carga):"))
        nums.append(n)

        if n == 0:
            break
    except ValueError:
        print("X Introduce un número entero")
        
print(f"Los números son {nums}")
