"""
Ej. 62: Realizar la carga del nombre de una persona y luego mostrar 
el primer carácter del nombre y la cantidad de letras que lo componen
"""
name = input("Introduce un nombre: ")

print(f"El primer carácter del nombre es {name[0].capitalize()} y tiene {len(name)} letras")

"""
Ej. 63: Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si 
comienza con vocal dicho nombre.
"""
name = input("Introduce un nombre en minúsculas: ")

if name[0] == "a" or name[0] == "e" or name[0] == "i" or name[0] == "o" or name[0] == "u":
    print("El nombre introducido empieza con vocal")
else:
    print("El nombre introducido no empieza con vocal")
