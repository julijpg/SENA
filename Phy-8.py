engranaje = 112
cilindro = 75

numeroengranajes = int(input("Introduce el numero de engranajes"))
numerocilindros= int(input("Introduce el numero de cilindros vendidos: "))

total = (numeroengranajes * engranaje) + (numerocilindros*cilindro)

print(f"El peso total del paquete es: {total} gramos")
