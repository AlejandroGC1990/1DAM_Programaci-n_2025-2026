"""
Ej. 149: Confeccionar un programa con las siguientes funciones:
1) Cargar una lista de 5 enteros.
2) Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""
def cargar():
        lista = []
        for x in range(5):
                num = int(input("Introduce un valor entero: "))
                lista.append(num)

        return lista

def retornar_mayormenor(lista):
        mayor = lista[0]
        menor = lista[0]
        for y in range(1, len(lista)):
                if lista[y] > mayor:
                        mayor = lista[y]
                else:
                        if lista[y] < menor:
                                menor = lista[y]

        return (mayor, menor)

lista = cargar()
mayor,menor = retornar_mayormenor(lista)
print("Mayor valor de la lista: ", mayor)
print("Menor valor de la lista: ", menor)
