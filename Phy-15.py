numero = int (input("Introduce un numero entero positivo: "))

if numero<= 0:
    print ("El numero debe ser un entero positivo: ")
else:

    impares = []

    for i in range (1, numero+1):
        if i %2 !=0:
            impares.appendi(str(i))
    resultado = ", ". join(impares)
    print(f"numero impares {resultado}")
