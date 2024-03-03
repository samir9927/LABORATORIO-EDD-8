""" Escriba una función que reciba un conjunto de números 
y devuelva un conjunto con los números primos."""

def es_primo(numero):

    # Un número menor o igual a 1 no es primo
    if numero <= 1:
        return False
    
    # Iteramos desde 2 hasta la raíz cuadrada del número, más 1
    for i in range(2, int(numero ** 0.5) + 1):
        # Si el número es divisible por algún número en este rango, no es primo
        if numero % i == 0:
            return False
    
    # Si el número no es divisible por ningún número en el rango, es primo
    return True

def numeros_primos(conjunto):

    primos = set()  # Creamos un conjunto vacío para almacenar los números primos
    for num in conjunto:
        # Verificamos si el número actual es primo usando la función es_primo
        if es_primo(num):
            # Si el número es primo, lo agregamos al conjunto de primos
            primos.add(num)
    return primos

# Ejemplo de uso:
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
primos = numeros_primos(conjunto)
print("Números primos en el conjunto:", primos)
