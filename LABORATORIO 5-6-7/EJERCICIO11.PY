"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están ordenados de menor a mayor"""

def numeros_ordenados(conjunto_numeros):

    numeros_ordenados = sorted(conjunto_numeros)  # Ordenamos los números del conjunto
    return set(numeros_ordenados)  # Convertimos la lista ordenada a un conjunto y la devolvemos

# Ejemplo de uso:
conjunto_numeros = {5, 2, 7, 1, 8, 3}
numeros_ordenados_resultado = numeros_ordenados(conjunto_numeros)
print("Números ordenados de menor a mayor:", numeros_ordenados_resultado)
