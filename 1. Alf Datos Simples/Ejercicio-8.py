"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
entera respectivamente.
"""
numero1 = int(input("Introduzca un numero\n"))
numero2 = int(input("Introduzca otro numero\n"))
cociente = numero1 / numero2
resto = numero1 % numero2
txt = "{0} entre {1} da un cociente {2} y un resto {3}"
print(txt.format(numero1 ,numero2 ,cociente ,resto))