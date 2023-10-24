"""
Definir una función superposicion() que tome dos listas y devuelva
True si tienen al menos 1 miembro en común o devuelva False de lo
contrario. Escribir la función usando el bucle for anidado.
"""

lista1 = ["Azul", "Rojo", "Morado"]
lista2 = ["Amarillo", "Verde", "Rojo"]


def superposicion(list1: list, list2: list):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False


print(superposicion(lista1, lista2))
