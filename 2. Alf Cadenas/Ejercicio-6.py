"""
Escribir un programa que pida al usuario que introduzca una frase en la consola
y una vocal, y después muestre por pantalla la misma frase pero con la vocal
introducida en mayúscula.
"""

cadena = input("Introduce una cadena de texto:\n")
vocal = input("Introduce una vocal\n")
final = ""

for x in cadena:
    if x == vocal:
        x = x.upper()
    final += x

print(final)
