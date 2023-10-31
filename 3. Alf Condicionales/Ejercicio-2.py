"""
Escribir un programa que almacene la cadena de caracteres contraseña en
una variable, pregunte al usuario por la contraseña e imprima por
pantalla si la contraseña introducida por el usuario coincide con la
guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
clave = "1234ABcd"
clave_in = input("Introduza una clave\n")
if clave_in.lower() == clave.lower():
    print("Las claves coinciden")
else:
    print("Las claves no coinciden")
