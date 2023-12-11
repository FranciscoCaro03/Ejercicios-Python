"""
Escribir un programa que guarde en un diccionario los precios de las
frutas de la tabla, pregunte al usuario por una fruta, un número de
kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje
informando de ello.

Fruta	Precio
Platano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""
dic = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
fruta = input("Que fruta desea comprar?\n")
if fruta in dic:
    kilos = float(input("Cuantos kilos desea comprar?\n"))
    precio = round(kilos * dic[fruta], 3)
    print(f"La cantidad de {fruta} que pesa {kilos} kilos vale {precio} euros")
else:
    print(f"La fruta {fruta} no esta en la lista")


