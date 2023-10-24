"""
Definir una función max_de_tres(), que tome tres números como
argumentos y devuelva el mayor de ellos.
"""

def maximo3( num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    else:
        print("Los tres son iguales")



maximo3(1, 1, 1)