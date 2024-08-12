peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc= peso/ (estatura**2)
imc_redondeado = round(imc, 2)

print(f¨Tu imc es {imc_redondeado})