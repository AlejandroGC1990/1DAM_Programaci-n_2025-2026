"""
Ej. 138: Confeccionar una función que reciba un string como parámetro y en forma opcional un
segundo string con un caracter. La función debe mostrar el string subrayado con el caracter que
indica el segundo parámetro

"""
def titulo_subrayado(titulo, caracter = "*"):
        print(titulo)
        print(caracter * len(titulo))

titulo_subrayado("Sistema de Administración")
titulo_subrayado("Ventas", "*")

"""
Ej. 139: Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la
suma de dichos valores. Debe tener tres parámetros por defecto. 
"""
def suma(v1, v2, v3 = 0, v4 = 0, v5 = 0):
        s = v1 + v2 + v3 + v4 + v5
        return s

print("La suma de 5 + 6")
print(suma(5,6))

print("La suma de 1 + 2 + 3")
print(suma(1,2, 3))

