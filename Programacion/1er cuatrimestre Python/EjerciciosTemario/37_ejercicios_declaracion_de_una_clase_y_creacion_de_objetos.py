"""
Ej. 186: Implementaremos una clase llamada Persona que tendrá como atributo (variable) su
nombre y dos métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el
siguiente método mostrará en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona. 
"""
class Persona:
    def inicializar(self, nom):
        self.nombre = nom

    def imprimir(self):
        print("Nombre", self.nombre)

persona1 = Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Carla")
persona2.imprimir()

"""
Ej. 187: Implementar una clase llamada Alumno que tenga como atributos el nombre del alumno
y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un
mensaje si está regular (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.
"""
class Alumno:
    def inicializar(self, nom, nota):
        self.nombre = nom
        self.nota = nota
        
    def imprimir(self):
        if self.nota >= 4:
            print("Regular... Nombre", self.nombre, " -> " , self.nota)
        else:
            print("Nombre ", self.nombre, " -> ", self.nota)

alumno1 = Alumno()
alumno1.inicializar("Pedro", 4)
alumno1.imprimir()

alumno2 = Alumno()
alumno2.inicializar("Carla", 1)
alumno2.imprimir()

"""
Ej. 188: Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar
los datos cargados. Imprimir un mensaje si es mayor de edad (edad >= 18)

"""
class Persona:
    def inicializar(self, nom, edad):
        self.nombre = nom
        self.edad = edad
        
    def imprimir(self):
        if self.edad >= 18:
            print("Mayor de edad -> Nombre", self.nombre, " -> " , self.edad)
        else:
            print("Nombre ", self.nombre, " -> ", self.edad)

persona1 = Persona()
persona1.inicializar("Pedro", 4)
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Carla", 18)
persona2.imprimir()

"""
Ej. 189: Desarrollar un programa que cargue los lados de un triángulo e implemente los
siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método
que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.

"""
class Triangulo:
    def inicializar(self):
        self.lado1 = int(input("Introduce el lado1 del triángulo: "))
        self.lado2 = int(input("Introduce el lado2 del triángulo: "))
        self.lado3 = int(input("Introduce el lado3 del triángulo: "))
        
    def imprimir(self):
        print("Valores de los lados del triangulo: ")
        print("Lado 1", self.lado1)
        print("Lado 2", self.lado2)
        print("Lado 3", self.lado3)
      
    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
         if self.lado1 == self.lado2 and self.lado1 == self.lado3:
             print("El triangulo es equilatero")
         else:
             print("El triangulo no es equilatero")

triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
