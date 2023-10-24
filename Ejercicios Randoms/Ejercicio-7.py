"""
Definir una función es_palindromo() que reconoce palíndromos
(es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo():
    palabra1 = "oso"
    palabra2 = palabra1[::-1]
    if palabra1 == palabra2:
        print("Es palindrmo")
    else:
        print("No es palindromo")

es_palindromo()