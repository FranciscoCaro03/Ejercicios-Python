"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
un descuento del 60%. Escribir un programa que comience leyendo el número de barras
vendidas que no son del día. Después el programa debe mostrar el precio habitual de
una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

p_barra = 3.49
descuento = 60
p_barra_descuento = round((descuento*3.49)/100, 2)
n_barras = int(input("Introduca el numero de barras que no son del dia:\n"))
t_barras_descuento = round(n_barras*p_barra_descuento, 2)
txt = ("Una barra cuesta {0}, pero al no ser del dia tiene un\ndescuento del {1}% por lo que cuesta {2} Euros "
       "la unidad\ny {3} Euros todas.")
print(txt.format(p_barra, descuento, p_barra_descuento, t_barras_descuento))
