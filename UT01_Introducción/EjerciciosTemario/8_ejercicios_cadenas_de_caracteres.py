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

"""
Ej. 64: Introducir un mail por teclado. Verificar si el string introducido contiene 
solo un carácter "@".
"""
mail = input("Introduce tu email:")
count = 0
x = 0

while x < len(mail):
    if mail[x] == "@":
        count += 1
    x += 1

if count == 1:
    print("Mail aprobado")
else:
    print(f"El mail introducido es erróneo, tiene {count} @")

"""
Ej. 65: Inicializamos un string con la cadena "mAriA" después llamamos a sus métodos upper(), lower() 
y capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla.
"""
nombre1 = "mAriA"
nombre2 = nombre1.upper()
nombre3 = nombre1.lower()
nombre4 = nombre1.capitalize()

print(nombre1)
print(nombre2)
print(nombre3)
print(nombre4)

"""
eJ. 66: Cargar una oración por teclado. Mostrar cuantos espacios en blanco se introdujeron. Tener en cuenta que un espacio
en blanco es igual a " ", en cambio una cadena vacía es ""

"""
frase = input("Introduce una oración: ")
count = 0
x = 0

print(frase.count(" "))

"""
Ej. 67: Introducir una oración que pueda tener letras tanto en mayúsculas como minúsculas.
Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que sea más fácil
disponer la condición que verifica que es una vocal.
"""
frase = input("Introduce la oración: ")
fraseMinus = frase.lower()
vocales = 0
count = 0

while count < len(frase):
    if fraseMinus[count] in "aeiou":
        vocales += 1

    count += 1

print(f"la oración tiene {vocales} vocales")