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
