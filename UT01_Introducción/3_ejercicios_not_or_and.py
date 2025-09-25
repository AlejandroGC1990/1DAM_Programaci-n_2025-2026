"""
 Realizar un programa que pida cargar una fecha cualquiera, después verificar si dicha fecha corresponde a Navidad.
"""
day = int(input("Ingresar el día"))
month = int(input("Ingresar el mes"))
year = int(input("Ingresar el año"))

if day == 25 and month == 12 and year == 2025:
    print("¡Es Navidad!")
else:
    print(day + "/" + month + "/" + year)