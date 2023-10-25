"""
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de céntimos
del precio introducido.
"""

precio = input("Introduce el precio:\n")
final = precio.split(",")
print(f"El producto vale {final[0]} euros con {final[1]} centimos")

