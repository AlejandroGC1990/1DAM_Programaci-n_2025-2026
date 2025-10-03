"""
15. Crea un programa que solicite una contraseña al usuario y verifique si coincide
con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
"""
password = 12345
passwordUser = input("Introduce la contraseña: ")

if password == passwordUser:
    print("Bienvenid@")
else: 
    print("Error: La contraseña no coincide")