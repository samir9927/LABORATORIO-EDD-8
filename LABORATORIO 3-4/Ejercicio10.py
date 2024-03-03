""" Suma dos matrices de diferentes tamaños."""

def suma_matrices(matriz1, matriz2):
    # Verificar que las matrices tengan las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "Las matrices deben tener las mismas dimensiones para poder sumarlas."

    # Inicializar una matriz para almacenar el resultado
    resultado = []

    # Iterar sobre las filas de las matrices
    for i in range(len(matriz1)):
        fila_resultado = []
        # Iterar sobre los elementos de cada fila
        for j in range(len(matriz1[0])):
            # Sumar los elementos correspondientes de las dos matrices
            suma_elementos = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma_elementos)
        resultado.append(fila_resultado)

    return resultado

# Ejemplo de uso
matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8, 9],
    [10, 11, 12]
]

# Sumar las dos matrices
resultado_suma = suma_matrices(matriz1, matriz2)

# Imprimir el resultado
for fila in resultado_suma:
    print(fila)
