"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.
"""

fecha = input("Introduza una fecha con el formato \"dd/mm/aaaa\":\n")
fecha_final = fecha.split("/")
print(f"Dia {fecha_final[0]}\nMes {fecha_final[1]}\nDia {fecha_final[2]}")