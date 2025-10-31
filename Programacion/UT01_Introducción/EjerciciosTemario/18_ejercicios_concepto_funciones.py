"""
Ej. 112: Confeccionar una aplicación que muestre una presentación en pantalla del programa.
Solicitaremos la carga de dos valores y nos mostrara la suma. Mostrar finalmente un mensaje
de despedida del programa. Implementar estas actividades en tres funciones.
"""

def presentacion():
        print("Función presentación")

def sumar_numeros():
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es {suma}")

def despedida():
        print("Adios")

presentacion()
sumar_numeros()
despedida()
