"""Solicita un número al usuario y determina si es par o impar."""

#Ingresar un numero
numero = int(input("Ingrese un número: "))

if numero % 2 == 0: #El numero al ser dividido por 2 y dejar residuo 0.
    print(f"{numero} es un número par.") #Es par
else:
    print(f"{numero} es un número impar.") #Es impar