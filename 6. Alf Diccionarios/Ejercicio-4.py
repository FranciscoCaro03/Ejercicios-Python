"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa
donde <mes> es el nombre del mes.
"""

user = input("Introduce una fecha con este formato dd/mm/aaaa\n")
fecha = user.split("/")

meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril",
         5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto",
         9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}


print(f"{fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}")
