"""
Ej. 152: Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un país y la
cantidad de habitantes. Definir tres funciones, en la primera cargar la lista, en la segunda
imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes
"""
def carga():
        paises = []

        for x in range(5):
                pais = input(f"Introduce el nombre del país {x + 1}: ")
                cant = int(input(f"Introduce la cantidad de habitantes del país {x + 1}"))
                paises.append((pais,cant))

        return paises

def imprimirLista(paises):
        for y in range(len(paises)):
                print(f"En {paises[y][0]} hay {paises[y][1]} habitantes")

def mayorPoblacion(paises):
        pos = 0
        for z in range(1, len(paises)):
                if paises[z][1] > paises[pos][1]:
                        pos = z

        print("Pais con mayor cantidad de habitantes: ", paises[z][0])


paises = carga()
imprimirLista(paises)
mayorPoblacion(paises)

"""
Ej. 153: Almacenar en una lista 5 empleados, cada elemento de la lista es una sub-lista con
el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1) Carga de los nombres de empleados y sus últimos tres sueldos.
2) Imprimir el monto total cobrado por cada empleado.
3) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los
últimos tres meses. Tener en cuenta que la estructura de datos si se carga por asignación
debería ser similar a: empleados = [["juan",(2000, 3000, 4233)] , ["ana",(3444, 1000, 5333)] , etc. ]
"""
def carga():
        empleados = []
        
        for x in range(5):
                nombre = input(f"Introduce el nombre del empleado {x + 1}: ")

                sueldos = []
                for s in range(3):
                        cant = float(input(f"Introduce el sueldo {s + 1}: "))
                        sueldos.append(cant)
                        
                empleados.append([nombre,tuple(sueldos)])

        return empleados

def imprimirSueldo(empleados):
        for y in range(len(empleados)):
                sueldo = empleados[y][1][0] + empleados[y][1][1] + empleados[y][1][2] 
                print(f"El empleado {empleados[y][0]} tiene un sueldo de {sueldo} €")

def mayorSueldo(empleados):
        print("Los sueldos superiores a 10000 son de: ")
        mayores = []
        for z in range(len(empleados)):
                sueldo = empleados[z][1][0] + empleados[z][1][1] + empleados[z][1][2]
                if sueldo > 10000:
                        print(empleados[z][0], "con", sueldo, "€")

empleados = carga()
imprimirSueldo(empleados)
mayorSueldo(empleados)

"""
Ej. 154: Se tiene que cargar los votos obtenidos por tres candidatos en unas elecciones.
En una lista cargar en el primer componente el nombre del candidato y en el segundo componente
cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de
votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura
similar a esta:
candidatos = [
        ("juan",[("cordoba",100),("buenos aires",200)]) ,
        ("ana", [("cordoba",55)]) ,
        ("luis", [("buenos aires",20)])
]
1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos
obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las
provincias.
 , etc.]
"""
def carga():
        candidatos = []
        
        for x in range(3):
                nombre = input(f"Introduce el nombre del candidato {x + 1}: ")
                cantidadProv = int(input(f"¿En cuantas provincias ha tenido vostos {nombre}?"))

                provincias = []
                for s in range(cantidadProv):
                        provincia = input(f"Introduce el nombre de la provincia {s + 1}")
                        votos = int(input(f"Introduce la cantidad de votos obtenidos en {provincia}"))
                        provincias.append((provincia,votos))

                candidatos.append((nombre, provincias))
                
        return candidatos

def imprimirCandidatos(candidatos):
        for y in range(len(candidatos)):
                votos = 0
                for z in range(len(candidatos[y][1])):
                        votos = votos + candidatos[y][1][z][1] 

                print(f"El candidato {candidatos[y][0]} tiene {votos} votos")

candidatos = carga()
imprimirCandidatos(candidatos)
