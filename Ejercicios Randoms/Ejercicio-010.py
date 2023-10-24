"""
Definir un histograma procedimiento() que tome una lista de números
enteros e imprima un histograma en la pantalla. Ejemplo:
procedimiento([4, 9, 7]) debería imprimir lo siguiente:
"""
list = [4, 9, 7]


def procedimientos(numeros: list, caracter: str):
    for x in list:
        print(caracter*x)


procedimientos(list, "*")