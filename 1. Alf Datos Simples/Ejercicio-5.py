"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y
el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
horas = int(input("Cuantas horas has trabajado hoy?\n"))
precio = int(input("Cunto vale una hora de tu trabajo?\n"))
txt = "Te corresponden {}$ por el trabajo de hoy"
print(txt.format(horas*precio))
