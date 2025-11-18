"""
Ej. 159: En el bloque principal del programa definir un diccionario que
almacene los nombres de países como clave y como valor la cantidad de
habitantes. Implementar una función para mostrar cada clave y valor. 
"""
def imprimir(paises):
        for clave in paises:
                print(clave, paises[clave])

paises = {"argentina":40000000, "españa":460000000, "brasil":190000000, "uruguay":340000}
imprimir(paises)
