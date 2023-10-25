"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola
y muestre por pantalla otro correo electrónico con el mismo nombre (la parte
delante de la arroba @) pero con dominio ceu.es.
"""

email = input("Introduce tu correo electronico:\n")
print(email.replace("gmail.com", "ceu.es."))