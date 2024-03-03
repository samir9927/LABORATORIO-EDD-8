"""Pide la base y la altura de un triángulo al usuario y calcula su área."""

base = float(input("Ingrese la longitud de la base del triángulo: ")) #Ingresar el valor de la base
altura = float(input("Ingrese la altura del triángulo: ")) #Ingrese el valor de la alura (flotante)

area = 0.5 * base * altura #El área se calcula con esta formula

print(f"El área del triángulo con base {base} y altura {altura} es: {area}") #Arroja el valor