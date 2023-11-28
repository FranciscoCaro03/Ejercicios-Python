"""
Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista y los muestre por
pantalla ordenados de menor a mayor.
"""

lista = []
numero1 = int(input("Primer numero ganador:\n"))
lista.append(numero1)
numero2 = int(input("Segundo numero ganador:\n"))
lista.append(numero2)
lista.sort()
print(lista)
