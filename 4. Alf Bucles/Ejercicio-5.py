"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión.
"""
dinero = float(input("¿Cantidad a invertir? "))
intereses = float(input("¿Interés anual? "))
anios = int(input("¿Años?"))
for x in range(anios):
    dinero *= 1 + intereses / 100
    print(round(dinero, 2))