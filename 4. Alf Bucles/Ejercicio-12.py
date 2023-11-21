"""
Escribir un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece
la letra en la frase.
"""

texto = input("Introduzca un texto:\n")
letra = input("Introduzca una letra a buscar en el texto:\n")
conta_letras = 0

for x in texto:
    if letra == x:
        conta_letras += 1

print(f"Hay {conta_letras} {letra.upper()} encontradas en el texto")
