"""Escribe una función que encuentre la submatriz de mayor suma de una matriz"""
def max_submatrix_sum(matrix):
    # Obtener el número de filas y columnas de la matriz
    rows = len(matrix)
    cols = len(matrix[0])

    # Variables para almacenar la submatriz de mayor suma y su valor
    max_sum = float('-inf')
    top, bottom, left, right = 0, 0, 0, 0

    # Iterar sobre todas las columnas posibles para la submatriz
    for l in range(cols):
        # Inicializar un arreglo temporal para almacenar la suma acumulada de cada fila
        temp = [0] * rows
        # Iterar sobre todas las columnas a la derecha de 'l'
        for r in range(l, cols):
            # Calcular la suma acumulada de cada fila entre las columnas 'l' y 'r'
            for i in range(rows):
                temp[i] += matrix[i][r]

            # Algoritmo de Kadane para encontrar la submatriz de mayor suma en una dimensión
            current_sum = max_temp = temp[0]  # Inicializar las variables de suma
            start_temp = 0

            # Iterar sobre las filas para actualizar la submatriz de mayor suma en una dimensión
            for i in range(1, rows):
                # Verificar si es beneficioso comenzar una nueva submatriz
                if temp[i] > temp[i] + max_temp:
                    start_temp = i
                    max_temp = temp[i]
                else:
                    max_temp += temp[i]

                # Actualizar la submatriz de mayor suma
                if max_temp > current_sum:
                    top, bottom = start_temp, i
                    left, right = l, r
                    current_sum = max_temp

            # Actualizar la submatriz de mayor suma global
            if current_sum > max_sum:
                max_sum = current_sum
                top_final, bottom_final = top, bottom
                left_final, right_final = left, right

    return max_sum, (left_final, top_final), (right_final, bottom_final)

# Ejemplo de uso
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

# Encontrar la submatriz de mayor suma
max_sum, start, end = max_submatrix_sum(matrix)

# Imprimir la submatriz de mayor suma y su valor
print("La submatriz de mayor suma es:", matrix[start[1]:end[1]+1][start[0]:end[0]+1])
print("La suma de esa submatriz es:", max_sum)
