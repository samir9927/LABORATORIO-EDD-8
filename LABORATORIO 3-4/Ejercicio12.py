"""Calcula la media de los elementos de una matriz."""
def media_matriz(matriz):
    # Inicializar la suma de todos los elementos y el contador de elementos
    suma_total = 0
    contador_elementos = 0

    # Iterar sobre las filas de la matriz
    for fila in matriz:
        # Iterar sobre los elementos de cada fila
        for elemento in fila:
            suma_total += elemento  # Sumar cada elemento a la suma total
            contador_elementos += 1  # Incrementar el contador de elementos

    # Calcular la media dividiendo la suma total por el número total de elementos
    media = suma_total / contador_elementos

    return media

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular la media de la matriz
media = media_matriz(matriz)

# Imprimir el resultado
print("La media de los elementos de la matriz es:", media)
