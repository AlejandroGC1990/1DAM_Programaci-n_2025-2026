pisos = int(input("Introduce el número de pisos de la pirámide: "))
for x in range(1, pisos + 1):
    print(' ' * (pisos - x) + '*' * (2 * x -1))
