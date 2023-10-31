"""
Escribir un programa que pregunte por consola por los productos de una
cesta de la compra, separados por comas, y muestre por pantalla cada
uno de los productos en una línea distinta.
"""

cadena = input("Introduzca su lista de productos separadas por ,:\n")
lista = cadena.split(",")
for x in lista:
    print(x)
