"""
Ej. 73: Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguale o superiore a
7.
"""

num = []
numMsiete = []

for i in range(5):
    while True:
        try:
            n = int(input(f"Introduce el número entero {i + 1}: "))
            num.append(n)
            break
        except ValueError:
            print("X Introduce un numero válido")
    
for x in num:
    if x >= 7:
        numMsiete.append(x)
        
print(f"Los números mayores a 7 son: {numMsiete}")
