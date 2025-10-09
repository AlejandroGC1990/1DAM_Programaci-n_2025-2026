"""
Introducir una oración que pueda tener letras tanto en mayúsculas como minúsculas.
Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que sea más fácil
disponer la condición que verifica que es una vocal.
"""
oracion = input("Introduce la oración: ")
oracionMinus = oracion.lower()
vocales = 0
count = 0

while count < len(oracion):
    if oracionMinus[count] in "aeiou":
        vocales += 1

    count += 1

print(f"la oración tiene {vocales} vocales")
        


