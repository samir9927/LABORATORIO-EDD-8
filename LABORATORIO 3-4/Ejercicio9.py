"""Accede al elemento central de una matriz."""

def elemento_central(matriz):
    # Determinar el número de filas y columnas de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])  # Suponemos que todas las filas tienen la misma longitud

    # Calcular el índice de la fila central
    fila_central = filas // 2

    # Calcular el índice de la columna central
    columna_central = columnas // 2

    # Acceder al elemento central utilizando los índices calculados
    elemento_central = matriz[fila_central][columna_central]

    return elemento_central

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Llamar a la función para obtener el elemento central
elemento_central = elemento_central(matriz_ejemplo)

# Imprimir el elemento central
print("El elemento central de la matriz es:", elemento_central)
