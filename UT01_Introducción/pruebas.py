"""
Ej. 63: Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si 
comienza con vocal dicho nombre.
"""
name = input("Introduce un nombre en minúsculas: ")

if name[0] == "a" or name[0] == "e" or name[0] == "i" or name[0] == "o" or name[0] == "u":
    print("El nombre introducido empieza con vocal")
else:
    print("El nombre introducido no empieza con vocal")