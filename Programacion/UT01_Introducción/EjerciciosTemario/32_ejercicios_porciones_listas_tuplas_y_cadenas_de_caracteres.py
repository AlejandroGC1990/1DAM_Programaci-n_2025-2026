"""
Ej. 171: Confeccionar una función a la que le enviemos un número de un mes como parámetro y
nos retorne una tupla con todos los nombres de meses que faltan hasta fin de año.

"""
def meses_faltantes(numeromes):
        meses = ('enero','febrero','marzo','abril','mayo','junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

        return meses[numeromes:]


print("Imprimir los nombres de meses que faltan hasta fin de año")
numeromes = int("Introduce el número del mes: ")
mesesfalta = meses_faltantes(numeromes)
print(mesesfalta)

"""
Ej. 172: Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres
primeros.
En el bloque principal del programa definir una tupla con los nombres de meses. Mostrar por
pantalla los primeros tres caracteres de cada mes
"""
def primeros_tres(cadena):
        return cadena[:3]

meses=('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
for x in meses:
 print(primeros_tres(x))