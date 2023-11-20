"""
Escribir un programa que muestre por pantalla la tabla de multiplicar
del 1 al 10.
"""

for x in range(1, 11):
    print("\n")
    print(f"Tabla del {x}\n")
    for y in range(1, 11):
        print(x * y ,end=", ")