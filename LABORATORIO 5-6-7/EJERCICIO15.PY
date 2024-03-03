"""Escriba una función que reciba un conjunto 
de números y devuelva un conjunto con los números que 
son primos y están ordenados de menor a mayor"""

def es_primo(numero):

    # Verificamos si el número es menor o igual a 1
    if numero <= 1:
        return False
    # Verificamos si el número es 2 o 3
    elif numero <= 3:
        return True
    # Verificamos si el número es divisible por 2 o 3
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    # Realizamos la comprobación con los múltiplos de 6
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_ordenados(conjunto_numeros):
    # Creamos un conjunto con los números primos presentes en el conjunto dado
    numeros_primos = {numero for numero in conjunto_numeros if es_primo(numero)}
    # Ordenamos los números primos y los devolvemos
    return sorted(numeros_primos)

# Ejemplo de uso:
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_primos_ordenados_resultado = numeros_primos_ordenados(conjunto_numeros)
print("Números primos ordenados de menor a mayor:", numeros_primos_ordenados_resultado)
