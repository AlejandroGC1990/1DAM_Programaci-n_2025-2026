"""
Ej. 116: Confeccionar una aplicación que muestre una presentación en pantalla del programa.
Solicitar la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de
despedida del programa.

"""

def mostrarMensaje(mensaje):
        print(mensaje)
        
def programa():
        num1 = float(input("Introduce el valor del primer número: "))
        num2 = float(input("Introduce el valor del segundo número: "))
        suma = num1 + num2
        print(f"La suma es {suma}")

mostrarMensaje("Saludos")
programa()
mostrarMensaje("Adios")

"""
Ej. 117: Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos.
La carga de los valores hacerlo por teclado.
"""
def mostrarValorMayor(v1, v2, v3):
        if v1 > v2 and v1 > v3:
                print(v1)
        elif v2 > v3:
                print(v2)
        else:
                print(v3)

def cargarValores():
        num1 = int(input("Introduce el primero número: "))
        num2 = int(input("Introduce el segundo número: "))
        num3 = int(input("Introduce el tercer número: "))

        mostrarValorMayor(num1, num2, num3)

cargarValores()

"""
Ej. 118: Desarrollar un programa que permita introducir el lado de un cuadrado. Despues
preguntar si quiere calcular y mostrar su perímetro o su superficie
"""
def calcularPerimetro(lado):
        per = lado * 4
        print(f"El perímetro del cuadrado es {per}")

def calcularSuperficie(lado):
        sup = lado * lado
        print(f"La superficie del cuadrado {sup}")

def cargarDato():
        la = float(input("Introduce el valor del lado del cuadrado: "))
        respuesta = input("¿Quieres calcular el perímetro o la superficie [introducir texto: perímetro / superficie]?")

        if respuesta == "perímetro":
                calcularPerimetro(la)
        else:
                calcularSuperficie(la)


cargarDato()

"""
Ej. 119: Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a
mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la
primera función definida.
"""
def ordenarNums(v1, v2, v3):
        if v1 < v2 and v1 < v3:
                if(v2 < v3):
                        print(v1, v2, v3)
                else:
                        print(v1, v3, v2)
        else:
                if(v2 < v3):
                        if(v1 < v3):
                                print(v2, v1, v3)
                        else:
                                print(v2, v3, v1)
                else:
                        if(v1 < v2):
                                print(v3, v1, v2)
                        else:
                                print(v3, v2, v1)

def cardarDatos():
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        num3 = int(input("Introduce el tercer número entero: "))

        ordenarNums(num1, num2, num3)

cardarDatos()
