""" Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que 
están ordenados de menor a mayor y que no están duplicados."""

def numeros_ordenados_sin_duplicados(conjunto_numeros):

    numeros_ordenados = sorted(conjunto_numeros)  # Ordenamos los números del conjunto de menor a mayor
    numeros_sin_duplicados = sorted(set(numeros_ordenados))  # Convertimos la lista ordenada a un conjunto para eliminar duplicados y luego la ordenamos nuevamente
    return numeros_sin_duplicados

# Ejemplo de uso:
conjunto_numeros = {5, 2, 7, 1, 8, 3, 5, 2, 7}  # Ejemplo con números duplicados
numeros_ordenados_sin_duplicados_resultado = numeros_ordenados_sin_duplicados(conjunto_numeros)
print("Números ordenados de menor a mayor y sin duplicados:", numeros_ordenados_sin_duplicados_resultado)
