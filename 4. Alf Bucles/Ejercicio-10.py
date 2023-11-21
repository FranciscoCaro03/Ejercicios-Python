"""
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es un número primo o no.
"""

num = int(input("Introduce un numero mayor que 2:\n"))
for i in range(2, num):
    if num % i == 0:
        break
if (i + 1)  == num:
    print(str(num) + " es primo")
else:
    print(str(num) + " no es primo")