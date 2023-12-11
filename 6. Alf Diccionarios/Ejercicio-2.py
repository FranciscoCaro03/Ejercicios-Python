"""
Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario. Después debe
mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en
<dirección> y su número de teléfono es <teléfono>.
"""

nombre = input("Introduzca su nombre:\n")
edad = input("Introduzca su edad:\n")
direccion = input("Introduzca su direccion:\n")
telefono = input("Introduzca su telefono:\n")
dic = {'Nombre': nombre, 'Edad': edad, 'Direccion': direccion,
       'Telefono': telefono}

print(f"{dic['Nombre']} tiene {dic['Edad']} años, vive en "
      f"{dic['Direccion']} y su número de teléfono "
      f"es {dic['Telefono']}")




