""" Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están ordenados de mayor a menor."""

def numeros_ordenados_de_mayor_a_menor(conjunto_numeros):

    numeros_ordenados = sorted(conjunto_numeros, reverse=True)  # Ordenamos los números del conjunto de mayor a menor
    return set(numeros_ordenados)  # Convertimos la lista ordenada a un conjunto y la devolvemos

# Ejemplo de uso:
conjunto_numeros = {5, 2, 7, 1, 8, 3}
numeros_ordenados_resultado = numeros_ordenados_de_mayor_a_menor(conjunto_numeros)
print("Números ordenados de mayor a menor:", numeros_ordenados_resultado)
