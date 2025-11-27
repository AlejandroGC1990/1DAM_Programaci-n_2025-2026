"""
Ej. 190: Confeccionar una clase que represente un empleado. Definir como atributos su nombre
y su sueldo. En el método __init__ cargar los atributos por teclado y luego en otro método
imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el
sueldo supera a 3000)
"""
class Empleado:
    def __init__(self):
        self.nombre = input("Introduce el nombre del empleado: ")
        self.sueldo = float(input("Introduce el sueldo: "))

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Sueldo: ", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuesto")


empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

"""
Ej. 191: Desarrollar una clase que represente un punto en el plano y tenga los siguientes
métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que
cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son
positivas, si x < 0 e y > 0 segundo cuadrante, etc.)
"""
class Punto:
    def __init__(self):
        self.x = float(input("Introduce el valor de x: "))
        self.y = float(input("Introduce el valor de y: "))

    def imprimir(self):
        if self.x > 0 and self.y > 0:
            print("Está en el cuadrante 1")
        elif self.x > 0 and self.y < 0:
            print("Está en el cuadrante 2")
        elif self.x < 0 and self.y < 0:
            print("Está en el cuadrante 3")
        elif self.x > 0 and self.y < 0:
            print("Está en el cuadrante 4")
        elif self.x == 0 and self.y != 0:
            print("Está sobre el eje Y")
        elif self.y == 0 and self.x != 0:
            print("Está sobre el eje X")
        else:
            print("Está en el origen (0,0)")

punto1 = Punto()
punto1.imprimir()

"""
Ej. 192: Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
inicializar el valor del lado llegando como parámetro al método __init__ (definir un
atributo llamado lado), imprimir su perímetro y su superficie.
"""
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def mostrar_perimetro(self):
        per = self.lado * 4
        print("El períemtro del cuadrado es: ", per)

    def mostrar_superficie(self):
        sup = self.lado * self.lado
        print("La superficie del cuadrado es: ", sup)

  
cuadrado1 = Cuadrado()
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
