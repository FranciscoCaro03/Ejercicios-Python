"""
Escribir un programa que pida al usuario una palabra y muestre por
pantalla si es un palíndromo.
"""

word = input("Introduce una palabra\n")
l1 = []
l2 = []
for x in word:
    l1.append(x)
    l2.append(x)

l2.reverse()
print(l1)
print(l2)

if l1 == l2:
    print("Es palindromo")
else:
    print("No es palindromo")





