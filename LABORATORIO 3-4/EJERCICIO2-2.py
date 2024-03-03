"""Calcula la media, la mediana y la desviación 
estándar de los elementos de una matriz."""

import numpy as np

def estadisticas_matriz(matriz):
    # Calcular la media de los elementos de la matriz
    media = np.mean(matriz)

    # Calcular la mediana de los elementos de la matriz
    mediana = np.median(matriz)

    # Calcular la desviación estándar de los elementos de la matriz
    desviacion_estandar = np.std(matriz)

    return media, mediana, desviacion_estandar

# Ejemplo de uso
matriz = np.random.randint(1, 10, size=(4, 5))  # Ejemplo de una matriz de tamaño 4x5 con números aleatorios entre 1 y 10
print(matriz)
# Calcular las estadísticas de la matriz
media, mediana, desviacion_estandar = estadisticas_matriz(matriz)

# Imprimir los resultados
print("Media de los elementos de la matriz:", media)
print("Mediana de los elementos de la matriz:", mediana)
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)
