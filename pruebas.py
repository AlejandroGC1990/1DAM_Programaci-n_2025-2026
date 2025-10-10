"""
Ej. 72: Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor
superior a 100.
"""
elementos = input("Introduce ocho elementos separados por comas: ") 
lista = [float(num) for num in elementos.split(",")]
count = 0
x = 0

while x < len(lista):
    if lista[x] > 100:
        count += 1

    x += 1

print(f"Hay {count} números superiores a 100")
