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

"""
Ej. 113: Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre
su suma. Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez cargados los dos valores y su suma.
"""

def sumaNumeros():
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        suma = num1 + num2
        print(f"El valor de la suma es {suma}")

def lineaSeparadora():
        print("********************")

for x in range(5):
        sumaNumeros()
        lineaSeparadora()

"""
Ej. 114: Desarrollar un programa con dos funciones. La primera solicita introducir un entero
y muestra el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y
muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas
funciones.
"""
def cuadrado():
        num1 = int(input("Introduce un número entero: "))
        cuadrado = num1 * num1
        print(f"El cuadrado de {num1} es {cuadrado}")

def multiplicacion():
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        multiplicacion = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es {multiplicacion}")
        
cuadrado()
multiplicacion()
