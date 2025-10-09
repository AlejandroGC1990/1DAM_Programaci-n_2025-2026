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