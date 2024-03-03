"""Multiplica una matriz por un número."""
def multiplicar_matriz_por_numero(matriz, numero):
    # Inicializar una matriz para almacenar el resultado
    resultado = []

    # Iterar sobre las filas de la matriz
    for fila in matriz:
        fila_resultado = []
        # Iterar sobre los elementos de cada fila y multiplicar por el número dado
        for elemento in fila:
            resultado_elemento = elemento * numero
            fila_resultado.append(resultado_elemento)
        resultado.append(fila_resultado)

    return resultado

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numero = 2

# Multiplicar la matriz por el número
resultado_multiplicacion = multiplicar_matriz_por_numero(matriz, numero)

# Imprimir el resultado
for fila in resultado_multiplicacion:
    print(fila)
