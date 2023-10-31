"""
Escribir un programa que pida al usuario dos números y muestre por
pantalla su división. Si el divisor es cero el programa debe mostrar
un error.
"""

dividendo = int(input("Introduce el dividendo:\n"))
divisor = int(input("Introduce el divisor:\n"))
if divisor == 0:
    print("Error: El divisor debe de ser mayor que 0")
else:
    division = dividendo / divisor
    print(f"El resultdo de la division es: {division}")
