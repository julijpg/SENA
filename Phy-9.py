precio1 = 3.49
descuento = 60

barrasviejas = int(input("introduce el numero de barras de pan viejas: "))
descuentototal = (precio1 * descuento)/ 100
preciodescuento= precio1 - descuentototal
total = preciodescuento * barrasviejas

print(f"Precio habitual de una barra de pan:${precio1:.2f}")
print(f"Descuento por no ser fesca: ${descuentotal:.2f}")