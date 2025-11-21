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
