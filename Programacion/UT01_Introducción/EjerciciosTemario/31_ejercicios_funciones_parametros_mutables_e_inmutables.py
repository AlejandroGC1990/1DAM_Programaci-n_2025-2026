"""
Ej. 166: Confeccionar un programa que contenga las siguientes funciones:
1) Cargar una lista y retornar al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor
menor a 10.
3) Imprimir la lista

"""
def cargar():
        lista = []
        continua = "s"
        while continua == "s":
                valor = int(input("Introduce un valor: "))
                lista.append(valor)
                continua = input("Agregar otro elemento a la lista [s/n]: ")
        return lista

def fijar_cero(li):
        for x in range(len(li)):
                if li[x] < 10:
                        li[x] = 0

def imprimir(lista):
        for elemento in lista:
                print(elemento, "-", sep = "", end = "")
        print("")

lista = cargar()
print("Lista antes de modificar")
imprimir(lista)
fijar_cero(lista)
print("Lista después de modificar")
imprimir(lista)