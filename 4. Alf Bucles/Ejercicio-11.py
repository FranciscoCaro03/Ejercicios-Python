"""
Escribir un programa que pida al usuario una palabra y luego muestre
por pantalla una a una las letras de la palabra introducida empezando
por la última.
"""

p = input("Introduce una pablabra\n")[::-1]
for x in p:
    print(x)
