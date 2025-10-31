"""
Ej. 120: Confeccionar una función a la cual le enviemos como parámetro el valor del lado de
un cuadrado y nos retorne su superficie
"""
def calcularSuperficie(lado):
        sup = lado * lado
        return sup


valor = float(input("Introduce el valor del lado del cuadrado: "))
superficie = calcularSuperficie(valor)
print(f"La superficie del cuadrado cuyo lado obtenido es {superficie}")

"""
Ej. 121: Confeccionar una función a la cual le enviemos como parámetros dos enteros y nos
retorne el mayor.
"""
def returnMayor(v1, v2):
        if v1 < v2:
                mayor = v2
        else:
                mayor = v1

        return mayor

valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))
print(returnMayor(valor1, valor2))