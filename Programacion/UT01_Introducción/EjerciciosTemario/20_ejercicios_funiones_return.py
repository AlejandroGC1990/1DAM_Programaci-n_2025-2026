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
