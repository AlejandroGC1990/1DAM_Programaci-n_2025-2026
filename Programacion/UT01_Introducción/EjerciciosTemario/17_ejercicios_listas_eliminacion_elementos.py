"""
Ej. 108: Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el
último de la lista.
"""
lista = []

for x in range(5):
        while True:
                try:
                        num = int(input(f"Escribe el número {x + 1} de la lista: "))
                        lista.append(num)
                        break
                except ValueError:
                        print("X Introduce un valor correcto")


print(f"Previa eliminación: {lista}")

lista.pop(0)
lista.pop(1)
lista.pop(2)

print(f"Tras la eliminación: {lista}")
        
