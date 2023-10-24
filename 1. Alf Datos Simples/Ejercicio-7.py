"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice
de masa corporal calculado redondeado con dos decimales.
"""

peso = float(input("Introduce tu peso:\n"))
estatura = float(input("Introduce tu estatura en metros:\n"))
imc = peso/(estatura)**2
txt = "Tu índice de masa corporal es {}"
print(txt.format(round(imc, 2)))
