"""
Escribir un programa que almacene el abecedario en una lista, elimine
de la lista las letras que ocupen posiciones múltiplos de 3, y muestre
por pantalla la lista resultante.
"""

abcd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z"]
delete = []
for x in abcd:
    if abcd.index(x) % 3 == 0:
        delete.append(x)

for y in abcd:
    if y in delete:
        abcd.remove(y)

print(abcd)
