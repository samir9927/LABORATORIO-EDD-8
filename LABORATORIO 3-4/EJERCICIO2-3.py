"""Escribe una función que encuentre el elemento máximo de una matriz."""
import numpy as np

def encontrar_maximo(matriz):
    # Utilizar la función np.max() para encontrar el elemento máximo de la matriz
    maximo = np.max(matriz)
    return maximo

# Ejemplo de uso
matriz = np.random.randint(1, 100, size=(5, 5))  # Ejemplo de una matriz de tamaño 5x5 con números aleatorios entre 1 y 100
print(matriz)
# Encontrar el elemento máximo de la matriz
elemento_maximo = encontrar_maximo(matriz)

# Imprimir el resultado
print("El elemento máximo de la matriz es:", elemento_maximo)
