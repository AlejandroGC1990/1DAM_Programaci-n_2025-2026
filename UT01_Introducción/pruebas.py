"""
17. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
"""
n = 1

while n < 50:
    print(n)

    if n % 7 == 0:
        print(f"El primer número divisible por 7 es {n}")
        n = 50
    
    n += 1