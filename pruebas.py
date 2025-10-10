"""
Hacer una pirámide de asteriscos con el número introducido por el usuario
"""
pisos = int(input("Introduce el númerode pisos de la pirámide: "))
asteriscos = 1
for x in range (pisos):
    print(f"{' ' * pisos}{'*' * asteriscos}")
    asteriscos += 2
    pisos -= 1

