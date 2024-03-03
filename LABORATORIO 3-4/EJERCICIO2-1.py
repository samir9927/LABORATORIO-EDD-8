"""Crea una matriz de números aleatorios de tamaño 100x100."""

import numpy as np

# Definir el tamaño de la matriz
filas = 100
columnas = 100

# Definir el rango de los números aleatorios
rango_inferior = 1
rango_superior = 100  # Cambia este valor según sea necesario

# Crear la matriz de números aleatorios usando numpy
matriz_aleatoria = np.random.randint(rango_inferior, rango_superior + 1, size=(filas, columnas))

# Imprimir la matriz aleatoria
print(matriz_aleatoria)
