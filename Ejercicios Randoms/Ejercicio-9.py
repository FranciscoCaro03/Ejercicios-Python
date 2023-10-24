"""
Definir una función generar_n_caracteres() que tome un entero n y
devuelva el caracter multiplicado por n. Por ejemplo:
generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(numero: int, letra: str):
    print(numero*letra)


generar_n_caracteres(6, "a")