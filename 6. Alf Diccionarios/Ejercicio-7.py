"""
Escribir un programa que cree un diccionario simulando una cesta de
la compra. El programa debe preguntar el artículo y su precio y
añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste
total, con el siguiente formato
"""

lista = {}
precio_final = 0
while True:
    producto = input("Introduzca el articulo que desee añadir:\n")
    if producto != "Salir":
       precio = round(float(input("Introduzca el precio del articulo a añadir:\n")), 2)
       lista[producto] = precio
    else:
        print("Esta es la lista <Producto : Precio>")
        print(lista, end= " \n")
        for x in lista:
            precio_final += lista[x]
        print(f"El precio final de la compra es {precio_final} Euros")
        break
