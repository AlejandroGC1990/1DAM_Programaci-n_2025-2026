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
