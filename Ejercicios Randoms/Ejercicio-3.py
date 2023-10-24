"""
Definir una función que calcule la longitud de una lista o una cadena
dada. (Es cierto que python tiene la función len() incorporada, pero
escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

lista = ["uno", "dos", "tres"]
texto = "holaquetal"
def longString(textoIn):
    a = 0
    for x in textoIn:
        a = a + 1

    print(a)

longString(texto)
longString(lista)