"""
Ej. 194: Plantear una clase Operaciones que solicite en el método __init__ la carga de dos
enteros e inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada
operación en otro método de la clase Operación y llamarlos desde el mismo método __init__

"""
class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Introduce el primer valor: "))
        self.valor2 = int(input("Introduce el segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma de los 2 valores es: ", suma)

    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta de los 2 valores es: ", resta)

    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print("La multiplacicón de los 2 valores es: ", multi)

    def dividir(self):
        div = self.valor1 / self.valor2
        print("La división de los 2 valores es: ", div)


operacion1 = Operaciones()