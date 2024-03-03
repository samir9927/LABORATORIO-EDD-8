"""Escribe una función que encuentre la matriz de covarianza de dos matrices."""
import numpy as np

def matriz_covarianza(X, Y):
    # Calcular la media de las matrices X e Y
    media_X = np.mean(X, axis=0)
    media_Y = np.mean(Y, axis=0)

    # Calcular las matrices de desviación
    desviacion_X = X - media_X
    desviacion_Y = Y - media_Y

    # Calcular la matriz de covarianza
    covarianza = np.dot(desviacion_X.T, desviacion_Y) / (X.shape[0] - 1)

    return covarianza

# Ejemplo de uso
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

Y = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

matriz_cov = matriz_covarianza(X, Y)
print("Matriz de covarianza entre X e Y:")
print(matriz_cov)

