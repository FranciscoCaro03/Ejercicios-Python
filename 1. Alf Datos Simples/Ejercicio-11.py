"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales
de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad
a dos decimales.
"""

cantidad = int(input("Introduzca la cantidad a invertir:\n"))
interes = 4.00
ganancia1 = cantidad + ((cantidad * interes * 1)/100)
ganancia2 = cantidad + ((cantidad * interes * 2)/100)
ganancia3 = cantidad + ((cantidad * interes * 3)/100)
txt = ("Invirtiendo {0}$ con un interes anual del 4% obtendra la siguiente suma segun estos anos:\n"
       "1 anio: {1}\n"
       "2 anios: {2}\n"
       "3 anios: {3}\n")
print(txt.format(cantidad, ganancia1, ganancia2, ganancia3))
