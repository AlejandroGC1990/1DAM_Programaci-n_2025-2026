"""
Ej. 95: Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada
elemento debe ser una lista de 3 enteros. Imprimir sus elementos accediendo de diferentes
modos.


"""
listaNodriza = []

for x in range(4):
    sublista = []
    
    for y in range(3):
        while True:
            try:
                valor = int(input(f"Introduce el valor entero {y + 1} para la sublista {x + 1}: "))
                sublista.append(valor)
                break
            except ValueError:
                print("X Introduce un valor correcto")

    listaNodriza.append(sublista)

print(f"Tercer número de la primera sublista {listaNodriza[0][2]}")
print(f"Segunda sublista {listaNodriza[1]}")
print(f"ListaNodriza {listaNodriza}")
                
