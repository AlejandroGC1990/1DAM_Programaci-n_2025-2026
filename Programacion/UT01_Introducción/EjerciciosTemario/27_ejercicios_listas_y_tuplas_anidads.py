"""
Ej. 152: Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un país y la
cantidad de habitantes. Definir tres funciones, en la primera cargar la lista, en la segunda
imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes
"""
def carga():
        paises = []

        for x in range(5):
                pais = input(f"Introduce el nombre del país {x + 1}: ")
                cant = int(input(f"Introduce la cantidad de habitantes del país {x + 1}"))
                paises.append((pais,cant))

        return paises

def imprimirLista(paises):
        for y in range(len(paises)):
                print(f"En {paises[y][0]} hay {paises[y][1]} habitantes")

def mayorPoblacion(paises):
        pos = 0
        for z in range(1, len(paises)):
                if paises[z][1] > paises[pos][1]:
                        pos = z

        print("Pais con mayor cantidad de habitantes: ", paises[z][0])


paises = carga()
imprimirLista(paises)
mayorPoblacion(paises)
