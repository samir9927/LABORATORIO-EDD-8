"""Calcula la suma de los números pares en un rango especificado por el usuario."""

def sumaPares(inicio, fin):
    suma = 0 #Establecemos que la variable "suma" tenga valor incial de 0
    for numero in range(inicio, fin + 1): #Variable numero tomara valores desde el param. incio hsata un valor anterior al parametro "fin + 1"
        if numero % 2 == 0:
            suma += numero #Calculo de suma a suma que se hace con los valores de "numero"
    return suma #Resultado final

inicio_rango = int(input("Ingrese el inicio del rango: ")) #Ingresamos el rango inicial
fin_rango = int(input("Ingrese el final del rango: "))  #Ingresamos el rango final

resultado = sumaPares(inicio_rango, fin_rango) #Entramos a la funcion con los dos parametros 


print(f"La suma de los números pares en el rango [{inicio_rango}, {fin_rango}] es: {resultado}")
