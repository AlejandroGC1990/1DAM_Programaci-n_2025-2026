"""
Ej. 176: Confeccionar una función que reciba una palabra y verifique si es capicúa (es decir
que se lee igual de izquierda a derecha que de derecha a izquierda)

"""
def capicua(cadena):
        indice = -1
        iguales = 0

        for x in range(0, len(cadena)//2):
                if cadena[x] == cadena[indice]:
                        iguales += 1
                indice -= 1

        print(cadena)

        if iguales == (len(cadena)//2):
                print("Es capicúa")
        else:
                print("No es capicúa")

capicua("reconocer")
capicua("casa")
capicua("kayak")

"""
Ej. 177: Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al
principio utilizando subíndices negativos.


"""
palabra = input("Introduce una palabra: ")
indice = -1
for x in range(len(palabra)):
        print(palabra[indice], end = "")
        indice = indice -1

"""
Ej. 178: Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primera palabra con la última.
3) Imprimir la lista


"""
def cargar():
        palabras = []
        for x in range(0,5):
                pal = input("Introduce una palabra: ")
                palabras.append(pal)

        return palabras

def intercambiar(palabras):
        aux = palabras[0]
        palabras[0] = palabras[-1]
        palabras[-1] = aux

def imprimir(palabras):
        print(palabras)

palabras = cargar()
imprimir(palabras)
intercambiar(palabras)
imprimir(palabras)
        