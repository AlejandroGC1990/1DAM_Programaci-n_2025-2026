"""
Ej. 154: Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5
caracteres.
"""
def carga():
        lista = []
        cuantas = int(input("¿Cuántas palabras quieres añadir a la lista?"))
                      
        for x in range(cuantas):
                word = input(f"Introduce la palabra número {x + 1} de la lista")
                lista.append(word)

        return lista

def mas5(lista):
        mas = []

        for y in range(len(lista)):
                if len(lista[y]) > 5:
                        mas.append(lista[y])

        return mas

palabras = carga()
print("Lista", palabras)
print("Palabras con más de 5 carácteres:", mas5(palabras))
