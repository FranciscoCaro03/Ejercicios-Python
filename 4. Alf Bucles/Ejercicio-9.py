"""
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que
introduzca la contraseña correcta.
"""

clave = input("Introduce tu contraseña\n")
contrasenia = "1234abcd"
while clave == contrasenia:
    print("Correct passwd")
    break
else:
    print("Error passwd")



