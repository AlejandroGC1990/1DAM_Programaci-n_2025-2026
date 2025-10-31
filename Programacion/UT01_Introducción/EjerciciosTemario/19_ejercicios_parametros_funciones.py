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

