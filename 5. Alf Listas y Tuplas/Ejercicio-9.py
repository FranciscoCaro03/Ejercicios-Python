"""
Escribir un programa que pida al usuario una palabra y muestre por
pantalla el número de veces que contiene cada vocal.
"""
n_a = 0
n_e = 0
n_i = 0
n_o = 0
n_u = 0

word = input("Introduce una palabra:\n")

for x in word:
    if x == "a":
        n_a += 1
    elif x == "e":
        n_e += 1
    elif x == "i":
        n_i += 1
    elif x == "o":
        n_o += 1
    elif x == "u":
        n_u += 1

print(f"La palabra tiene {n_a} A, {n_e} E, {n_i} I, {n_o} O y {n_u} U")