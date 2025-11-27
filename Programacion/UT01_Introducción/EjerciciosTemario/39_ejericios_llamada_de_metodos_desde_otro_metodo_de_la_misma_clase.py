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

"""
Ej. 195: Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas.
Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.

"""
class Alumnos:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def menu(self):
        option = 0
        while option != 4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            option = int(input("Introduce una opción:"))
            if option == 1:
                self.cargar()
            elif option == 2:
                self.listar()
            elif option == 3:
                self.notas_altas()
            elif option == 4:
                print("Programa finalizado.")
            else:
                print("Opción no válida.")

    def cargar(self):
        for x in range(5):
            nom = input(f"Introduce nombre del alumno {x + 1}: ")
            while True:
                try:
                    no = float(input(f"Nota del alumno {nom}"))
                    if 0 <= no <=10:
                        break
                    else:
                        print("La nota debe estar entre 0 y 10")
                except ValueError:
                    print("Introduce un número válido")
            self.nombres.append(nom)
            self.notas.append(no)

    def listar(self):
        print("Listado completo de alumnos: ")
        for x in range(5):
            print(self.nombres[x], self.notas[x])
        print("_____________________________")

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(len(self.nombres)):
            if self.notas[x] >= 7:
                print(self.nombres[x], self.notas[x])
        print("_____________________________")


alumno = Alumnos()
alumno.menu()
