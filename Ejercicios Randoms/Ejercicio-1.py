"""
Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""

def maximo( num1, num2):
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("Son iguales")


maximo(1, 1)