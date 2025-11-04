"""
Ej. 120: Confeccionar una función a la cual le enviemos como parámetro el valor del lado de
un cuadrado y nos retorne su superficie
"""
def calcularSuperficie(lado):
        sup = lado * lado
        return sup


valor = float(input("Introduce el valor del lado del cuadrado: "))
superficie = calcularSuperficie(valor)
print(f"La superficie del cuadrado cuyo lado obtenido es {superficie}")

"""
Ej. 121: Confeccionar una función a la cual le enviemos como parámetros dos enteros y nos
retorne el mayor.
"""
def returnMayor(v1, v2):
        if v1 < v2:
                mayor = v2
        else:
                mayor = v1

        return mayor

valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))
print(returnMayor(valor1, valor2))

"""
Ej. 122: Confeccionar una función a la que le enviemos como parámetro un string y nos retorne
la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres
por teclado y llamar a la función dos veces. Imprimir en el bloque principal cuál de las dos
palabras tiene más caracteres.
"""
def largo(cadena):
        return len(cadena)

nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")
la1 = largo(nombre1)
la2 = largo(nombre2)

if la1 == la2:
        print("Los nombres tienen la misma cantidad de carácteres")
else:
        if la1 > la2:
                print(f"{nombre1} es más largo")
        else:
                print(f"{nombre2} es más largo")
        
"""
Ej. 123: Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los
mismos 
"""
def retornar_promedio(v1, v2, v3):
        promedio = (v1 + v2 + v3)/3
        return promedio

n1 = int(input("Introduce el primero valor"))
n2 = int(input("Introduce el segundo valor"))
n3 = int(input("Introduce el tercer valor"))

print("El promedio de los tres valores es", retornar_promedio(n1, n2, n3))
