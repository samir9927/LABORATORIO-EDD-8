""" Crea un programa que genere la tabla de multiplicar 
de un número ingresado por el usuario."""

numero = int(input("Ingrese un número para generar la tabla de multiplicar: ")) #Ingresamos nuemro que queremos tener su tabal de multiplciar

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 13): #Variable "i" con valores del 1 al 12
    resultado = numero * i #Resultado sera desde 1 hasta el 12 multiplicado por el numero
    print(f"{numero} x {i} = {resultado}") #Se imprimen los resultados
