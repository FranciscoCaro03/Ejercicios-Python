"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado
con información sobre una persona (por ejemplo nombre, edad, sexo,
teléfono, correo electrónico, etc.) que se le pida al usuario. Cada
vez que se añada un nuevo dato debe imprimirse el contenido del
diccionario.
"""
dic = {}
datos = ["nombre", "edad", "sexo", "telefono", "correo electrónico"]
for x in datos:
    dato = input(f"Introduzca su {x}\n")
    dic[x] = dato
    print(dic)
