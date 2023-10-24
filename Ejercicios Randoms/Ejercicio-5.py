"""
Escribir una función sum() y una función multip() que sumen y
multipliquen respectivamente todos los números de una lista.
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.
"""

lista = [1, 2, 3, 4]

def suma(lista):
    result = 0
    for x in lista:
        result += x

    print(result)

def multip(lista):
    result = lista[0]
    for x in lista:
        result *= x
    print(result)

suma(lista)
multip(lista)
