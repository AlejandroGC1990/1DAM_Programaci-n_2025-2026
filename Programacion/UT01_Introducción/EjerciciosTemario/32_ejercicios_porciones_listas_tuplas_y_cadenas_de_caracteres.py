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