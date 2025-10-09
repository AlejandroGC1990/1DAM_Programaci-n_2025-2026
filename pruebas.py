"""
Ej. 68: Solicitar la introducción de una clave por teclado y almacenarla en una
cadena de caracteres. Controlar que el string introducido tenga entre 10 y 20
caracteres para que sea válido, en caso contrario mostrar un mensaje de error.
"""
clave = input("Introduce la clave: ")

if len(clave) >= 10 or len(clave) <= 20:
    print("Clave válida")
else:
    print("Clave inválida")


