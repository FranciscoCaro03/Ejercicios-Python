"""
Escribir un programa que almacene las asignaturas de un curso (por
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine
de la lista las asignaturas aprobadas. Al final el programa debe mostrar
por pantalla las asignaturas que el usuario tiene que repetir.
"""

lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspensas = []
for x in lista:
    nota = int(input(f"Nota Obtenida en {x}\n"))
    if nota < 5:
        suspensas.append(x)

print(f"Tienes que repetir {suspensas}")
