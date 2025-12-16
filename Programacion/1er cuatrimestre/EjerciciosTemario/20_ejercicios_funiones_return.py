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

"""
Ej. 124: Elaborar una función que nos retorne el perímetro de un cuadrado pasando como
parámetros el valor de un lado.
"""
def retornar_perimetro(n):
        perimetro = n * 4
        return perimetro

lado = float(input("Introduce el valor del lado del cuadrado: "))

print("El perímetro del cuadrado es", retornar_perimetro(lado))

"""
Ej. 125: Confeccionar una función que calcule la superficie de un rectángulo y la retorne,
la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1, lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar
cual de los dos tiene una superficie mayor.
"""
def retornarSuperficie(lado1, lado2):
        superficie = lado1 * lado2
        return superficie

v1r1 = float(input("Introduce el valor 1 del rectángulo 1: "))
v2r1 = float(input("Introduce el valor 2 del rectángulo 1: "))
v1r2 = float(input("Introduce el valor 1 del rectángulo 2: "))
v2r2 = float(input("Introduce el valor 2 del rectángulo 2: "))
mayorSuperficie = 0

if retornarSuperficie(v1r1, v2r1) > retornarSuperficie(v1r2, v2r2):
        print("El primer rectángulo tiene una superficie mayor, con", retornarSuperficie(v1r1, v2r1))
        
else:
        print("El segundo rectángulo tiene una superficie mayor, con", retornarSuperficie(v1r2, v2r2))

"""
Ej. 126: Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la
cantidad de letras 'a' o 'A'.

"""
def contarAes(palabra):
        count = 0
        for x in range(len(palabra)):
                if palabra[x] == "a" or palabra[x] == "A":
                        count += 1

        return count

palabra = input("Introduce una palabra: ")

print(f"La palabra {palabra} tiene {contarAes(palabra)} 'a's")
