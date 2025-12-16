"""
Ej. 69: Definir una lista que almacene 5 enteros. Sumar todos sus elementos
y mostrar dicha suma.
"""
lista = [1, 2, 3, 4, 5]
count = 0
suma = 0

while count < len(lista):
    suma += lista[count]
    count += 1

print(f"Los elementos de la lista son {lista} y su suma total es {suma}")

"""
Ej. 70:  Definir una lista por asignación que almacene los nombres de los primeros
cuatro meses de año. Mostrar el primer y último elemento de la lista solamente.
"""
listaMeses = ["enero", "febrero", "marzo", "abril"]

print(listaMeses[0])
print(listaMeses[-1])

"""
Ej. 71:  Definir una lista por asignación que almacene en el primer componente
el nombre de un alumno y en los dos siguientes sus notas. Imprimir luego el
nombre y el promedio de las dos notas.
"""
alumno = []
name = input("Introduce el nombre del alumno: ")
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
promedio = (nota1 + nota2)/2
alumno.extend([name, nota1, nota2])

print(f"La nota promedio del alumno {alumno[0].capitalize()} y su nota promedia es de {promedio}")

"""
Ej. 72: Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor
superior a 100.
"""
elementos = input("Introduce ocho elementos separados por comas: ") 
lista = [float(num) for num in elementos.split(",")]
count = 0
x = 0

while x < len(lista):
    if lista[x] > 100:
        count += 1

    x += 1

print(f"Hay {count} números superiores a 100")

"""
Ej. 73: Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguale o superiore a
7.
"""

num = []
numMsiete = []

for i in range(5):
    while True:
        try:
            n = int(input(f"Introduce el número entero {i + 1}: "))
            num.append(n)
            break
        except ValueError:
            print("X Introduce un numero válido")
    
for x in num:
    if x >= 7:
        numMsiete.append(x)
        
print(f"Los números mayores a 7 son: {numMsiete}")

"""
Ej. 74: Definir una lista que almacene por asignación los nombres de 5 personas. Contar
cuántos de esos nombres tienen 5 o más caracteres
"""

names = []
namesMcharacters = []

for i in range(5):
    while True:
        try:
            n = input(f"Introduce el nombre {i + 1}: ")
            names.append(n)
            break
        except ValueError:
            print("X Introduce un nombre válido")
    
for x in names:
    if len(x) >= 5:
        namesMcharacters.append(x)
        
print(f"Los nombres con más de 5 caracteres son {len(namesMcharacters)}: {namesMcharacters}")
