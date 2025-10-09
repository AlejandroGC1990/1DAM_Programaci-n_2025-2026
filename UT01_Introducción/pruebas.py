"""
3. Escribir un programa en que muestre una tabla formateada de la siguiente
manera: * El nombre en un campo de 10 caracteres (alineado a la izquierda). *
La edad en un campo de 5 dígitos (alineado a la derecha). * El saldo en un
campo de 12 dígitos (alineado a la derecha).
                        Nombre  Edad    Saldo
                        Juan      25  123.456
                        Ana       30  245.987
                        Carlos    22  567.123
"""
print(f"{'Nombre':<10}{'Edad':>5}{'Saldo':>12}")
print(f"{'Juan':<10}{25:>5}{123.456:>12}")
print(f"{'Ana':<10}{30:>5}{245.987:>12}")
print(f"{'Carlos':<10}{22:>5}{567.123:>12}")