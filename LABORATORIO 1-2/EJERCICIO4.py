"""Crea una función que calcule la factorial de un número."""

def factorial(numero): #Funcion Factorial que recibe un parametro

    if numero == 0: #Si el parametro es igaul a 0, retorna 1
        return 1

    else:
        return numero * factorial(numero - 1) #Caso contrario, se aplica la recursividad, hasta que el parametro sea 0


numero_ingresado = int(input("Ingrese un número para calcular su factorial: ")) #Ingrese un valor como parametro

if numero_ingresado >= 0: #Si el valor es mayor igual que 0 pasa a la funcion 

    resultado = factorial(numero_ingresado)
    print(f"El factorial de {numero_ingresado} es: {resultado}") #Al terminar la funcion con la recursivida, se arroja la respuesta.

else:
    print("El factorial solo está definido para números no negativos.")