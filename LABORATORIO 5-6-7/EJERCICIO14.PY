"""Escriba una función que reciba un conjunto de números 
y devuelva un conjunto con los números que no 
están duplicados.
"""

def numeros_no_duplicados(conjunto_numeros):

    frecuencia_numeros = {}  # Diccionario para contar la frecuencia de cada número
    
    # Contamos la frecuencia de cada número en el conjunto
    for numero in conjunto_numeros:
        frecuencia_numeros[numero] = frecuencia_numeros.get(numero, 0) + 1
    
    numeros_no_duplicados = {numero for numero, frecuencia in frecuencia_numeros.items() if frecuencia == 1}
    
    return numeros_no_duplicados

# Ejemplo de uso:
conjunto_numeros = {1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1}
numeros_no_duplicados_resultado = numeros_no_duplicados(conjunto_numeros)
print("Números que no están duplicados en el conjunto:", numeros_no_duplicados_resultado)
