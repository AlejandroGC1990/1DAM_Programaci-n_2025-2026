"""
Ej. 179: Confeccionar un programa que simule tirar dos dados y luego muestre los valores que
salieron. Imprimir un mensaje con ganó si la suma de los mismos es igual a 7, en caso contrario
mostrar un mensaje con perdio.
Para resolver este problema requerimos un algoritmo para que se genere un valor aleatorio
entre 1 y 6. Como la generación de valores aleatorios es un tema muy frecuente, la biblioteca
estándar de Python incluye un módulo que nos resuelve la generación de valores aleatorios.
"""
import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Primer dado: ", dado1)
print("Segundo dado: ", dado2)

suma = dado1 + dado2
if suma == 7:
        print("Ganó")
else:
        print("Perdió")

"""
Ej. 180: Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo



"""
import random

def cargar():
        lista = []
        for x in range(10):
                lista.append(random.randint(0, 1000))

        return lista

def imprimir(lista):
        print(lista)

def mezclar(lista):
        random.shuffle(lista)

lista = cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)