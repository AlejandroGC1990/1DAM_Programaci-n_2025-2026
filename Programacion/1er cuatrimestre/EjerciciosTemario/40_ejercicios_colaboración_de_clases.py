"""
Ej. 197: Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el
banco requiere que al final del día calcule la cantidad de dinero que hay depositado.
Lo primero que hacemos es identificar las clases:
Podemos identificar la clase Cliente y la clase Banco.
Por lo tanto debemos definir los atributos y los métodos de cada clase:
Cliente
 atributos
 nombre
 monto
 métodos
 __init__
 depositar
 extraer
 retornar_monto
Banco
 atributos
 3 Cliente (3 objetos de la clase Cliente)
 métodos
 __init__
 operar
 depositos_totales

"""
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "tiene depositada la suma de ", self.monto)

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print("El total de dinero del banco es: ", total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

banco1 = Banco()
banco1.operar()
banco1.depositos_totales()

"""
Ej. 198: Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje en el siga "gano",
sino "perdió".
Lo primero que hacemos es identificar las clases:
Podemos identificar la clase Dado y la clase JuegoDeDados.
Luego los atributos y los métodos de cada clase:
Dado
 atributos
 valor
 métodos
 tirar
 imprimir
 retornar_valor
goDeDados
 atributos
 3 Dado (3 objetos de la clase Dado)
 métodos
 __init__
 Jugar
"""
import random

class Dado:
    def tirar(self):
        self.valor = random.randint(1,6)

    def imprimir(self):
        print("Valor del dado: ", self.valor)

    def retornar_valor(self):
        return self.valor

class JuegoDeDados:
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor() == self.dado2.retornar_valor() and self.dado1.retornar_valor() == self.dado1.retornar_valor():
            print("Gano")
        else:
            print("Perdió")

juego_dados = JuegoDeDados()
juego_dados.jugar()

"""
Ej. 199: Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en
años). En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su
antigüedad. La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.
"""
class Socio:
    def __init__(self):
        self.nombre = input("Introduce el nombre del socio: ")
        self.antiguedad = int(input("Introduce la antigüedad: "))

    def imprimir(self):
        print(self.nombre, " tiene una antigüedad de ", self.antiguedad)

    def retornar_antiguedad(self):
        return self.antiguedad

class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def mayor_antiguedad(self):
        print("Socio con mayor antigüedad")
        if (self.socio1.retornar_antiguedad() > self.socio2.retornar_antiguedad() and
            self.socio1.retornar_antiguedad() > self.socio3.retornar_antiguedad()):
            self.socio1.imprimir()
        else:
            if self.socio2.retornar_antiguedad() > self.socio3.retornar_antiguedad():
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()

club = Club()
club.mayor_antiguedad()
