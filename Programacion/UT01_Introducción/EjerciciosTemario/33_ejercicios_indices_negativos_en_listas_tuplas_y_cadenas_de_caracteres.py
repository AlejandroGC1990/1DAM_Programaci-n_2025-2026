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