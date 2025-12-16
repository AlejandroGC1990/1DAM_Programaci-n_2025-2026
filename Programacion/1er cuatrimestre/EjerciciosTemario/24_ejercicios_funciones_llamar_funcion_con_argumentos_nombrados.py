"""
Ej. 140: Confeccionar una función que reciba el nombre de un operario, el pago por hora y la
cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada de la función
mediante argumentos nombrados. 
"""
def calcular_sueldo(nombre, costeHoras, horas):
        sueldo = costeHoras * horas
        print(nombre, "trabajó ", horas, "horas y cobra un sueldo de ", sueldo, "€")

calcular_sueldo("juan", 10, 120)
calcular_sueldo(costeHoras = 12, horas = 40, nombre = "ana")
calcular_sueldo(nombre = "juan", costeHoras = 22, horas = 140 )

"""
Ej. 141: Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados
por una coma. 
"""
def cargar():
        lista = []
        for x in range(10):
                num = int(input("Introduce un valor numérico entero: "))
                lista.append(num)

        return lista

def imprimirLista(lista):
        for y in range(len(lista)):
                print(lista[y], end = ", ")

lista = cargar()
imprimirLista(lista)

"""
Ej. 142: Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos
como parámetro.
Definir un segundo parámetro llamado termino que por defecto almacene el valor 10.
Se deben mostrar tantos términos de la tabla de multiplicar como indicque el segundo
parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
 
"""
def tablaMultiplicar(num, terminos = 10):
        resultados = []
        for x in range(terminos):
                resultados.append((x + 1) * num)

        return resultados



print("Tabla del 3")
print(tablaMultiplicar(3))
print(tablaMultiplicar(3, 5))
