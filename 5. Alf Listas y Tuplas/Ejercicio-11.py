"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
"""

list1 = [1, 2, 3]
list2 = [-1, 0, 2]
num = 0
pos = 0
for x in range(len(list1)):
    num += list1[pos] * list2[pos]
    pos += 1

print(num)


