"""Crea una matriz de números complejos."""

import numpy as np

# Tamaño de la matriz
filas = 3
columnas = 3

# Crear una matriz de números complejos 
matriz_compleja = np.random.rand(filas, columnas) + np.random.rand(filas, columnas) * 1j

# Imprimir la matriz de números complejos
print("Matriz de números complejos aleatorios:")
print(matriz_compleja)
