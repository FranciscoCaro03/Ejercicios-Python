"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
cantidad = int(input("Introduzca la cantidad a invertir:\n"))
interes = float(input("Introduzca el interes anual:\n"))
anios = int(input("Introduzca los anios:\n"))
ganancia = (cantidad * interes * anios)/100
txt = "-- invirtiendo {0}$ con un interes anual\ndel {1}% durante {2} anios ganaras {3}$ --"
print(txt.format(cantidad, interes, anios, ganancia))
