"""
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número
separados por comas.
"""

numero = int(input("Introduce un numero:\n"))
for x in range(1, numero):
    if x % 2 == 1:
        print(x)