"""
Escribir un programa que lea un entero positivo, n , introducido por el usuario y
después muestre en pantalla la suma de todos los enteros desde 1 hasta n . La suma
de los primeros enteros positivos puede ser calculada de la siguiente forma:
"""

numero = int(input("Introduce un numero positvo:\n"))
txt = "El resultado es {}"
print(txt.format(numero*(numero+1)/2))