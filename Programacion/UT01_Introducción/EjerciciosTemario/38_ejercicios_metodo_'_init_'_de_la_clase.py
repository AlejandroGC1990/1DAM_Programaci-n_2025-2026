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
