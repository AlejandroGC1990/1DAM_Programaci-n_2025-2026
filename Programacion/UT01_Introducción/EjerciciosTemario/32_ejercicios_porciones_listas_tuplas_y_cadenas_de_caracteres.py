"""
Ej. 171: Confeccionar una función a la que le enviemos un número de un mes como parámetro y
nos retorne una tupla con todos los nombres de meses que faltan hasta fin de año.

"""
def meses_faltantes(numeromes):
        meses = ('enero','febrero','marzo','abril','mayo','junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

        return meses[numeromes:]


print("Imprimir los nombres de meses que faltan hasta fin de año")
numeromes = int("Introduce el número del mes: ")
mesesfalta = meses_faltantes(numeromes)
print(mesesfalta)

"""
Ej. 172: Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres
primeros.
En el bloque principal del programa definir una tupla con los nombres de meses. Mostrar por
pantalla los primeros tres caracteres de cada mes
"""
def primeros_tres(cadena):
        return cadena[:3]

meses=('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
for x in meses:
    print(primeros_tres(x))

"""
Ej. 173: Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una
lista con una cantidad par de elementos)
3) Imprimir una lista.
"""
def cargar():
        lista = []
        for x in range(10):
                valor = int(input("Cargar valor: "))
                lista.append(valor)
        return lista

def retornar_mitad(lista):
        mitad = len(lista)/2
        return lista[:mitad]

def imprimir(lista):
        print("Contenido de la lista")
        print(lista)

lista = cargar()
lista2 = retornar_mitad(lista)
imprimir(lista)
imprimir(lista2)