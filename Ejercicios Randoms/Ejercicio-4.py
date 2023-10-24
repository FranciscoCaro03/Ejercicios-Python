"""
Escribir una función que tome un carácter y devuelva True si es
una vocal, de lo contrario devuelve False.
"""

vocales = ["a", "e", "i", "o", "u"]

def ifvocal(caracter):

    if caracter in vocales:
        result = True
    else:
        result = False

    print(result)

ifvocal("w")