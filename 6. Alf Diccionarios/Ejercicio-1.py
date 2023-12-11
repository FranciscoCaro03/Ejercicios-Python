"""
Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por
una divisa y muestre su símbolo o un mensaje de aviso si la
divisa no está en el diccionario.
"""

dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduzca una divisa:\n")
if divisa in dic:
    print(f"Ha elegido {divisa} {dic[divisa]}")
else:
    print(f"La divisa {divisa} no se encuentra en la lista")
