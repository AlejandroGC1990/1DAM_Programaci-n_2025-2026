"""
Hacer una pirámide de asteriscos con el número introducido por el usuario. Ej: 6.
        *
       ***
      *****
     *******
    *********
   ***********
"""
pisos = int(input("Introduce el número de pisos de la pirámide: "))
asteriscos = 1
for x in range (pisos):
    print(f"{' ' * pisos}{'*' * asteriscos}")
    asteriscos += 2
    pisos -= 1

"""
for x in range(1, pisos + 1):
    print(' ' * (pisos - x) + '*' * (2 * x -1))
"""