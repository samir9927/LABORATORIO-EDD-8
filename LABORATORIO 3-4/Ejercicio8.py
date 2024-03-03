"""Crea una matriz de matrices"""
# Tamaño de la matriz principal
filas = 2
columnas = 2

# Tamaño de las matrices internas
tamano_interno = (2, 3)  # Por ejemplo, una matriz de 2x3

# Crear una matriz de matrices
matriz_de_matrices = []

# Rellenar la matriz con matrices internas
for _ in range(filas):
    fila = []
    for _ in range(columnas):
        # Generar una matriz interna con números secuenciales
        matriz_interna = [[i + j * tamano_interno[1] + 1 for i in range(tamano_interno[1])] for j in range(tamano_interno[0])]
        fila.append(matriz_interna)
    matriz_de_matrices.append(fila)

# Imprimir la matriz de matrices
print("Matriz de matrices:")
for fila in matriz_de_matrices:
    print(fila)

