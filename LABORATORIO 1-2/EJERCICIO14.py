""" Pide el radio de un círculo al usuario y calcula su área."""

import math #Importamos libreria math para usar el valor de "pi"

radio = float(input("Ingrese el radio del círculo: ")) #Ingresamos valor floante del radio

area = math.pi * radio**2 #Se calcula el area con la siguiente formula

print(f"El área del círculo con radio {radio} es: {area}") #Impresion del area del circulo