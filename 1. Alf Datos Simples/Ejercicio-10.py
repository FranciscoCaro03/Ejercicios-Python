"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete
a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
del paquete que será enviado.
"""

p_payaso = 0.112
p_muneca = 0.075
n_munecas = int(input("Numero de munecas vendidas en el ultimo pedido?\n"))
n_payasos = int(input("Numero de payasos vendidos en el ultimo pedido?\n"))
peso = n_payasos*p_payaso+n_munecas*p_muneca
txt = "En el ultimo pedido se vendieron:\n{0} munecas\n{1} payasos\ncon un peso de {2} kilos"
print(txt.format(n_munecas, n_payasos, round(peso, 2)))

