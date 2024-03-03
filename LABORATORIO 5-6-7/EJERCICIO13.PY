""" Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están duplicados"""

def numeros_duplicados(conjunto_numeros):

    numeros_vistos = set()  # Conjunto para registrar los números que ya hemos visto
    numeros_duplicados = set()  # Conjunto para almacenar los números duplicados
    
    for numero in conjunto_numeros:
        if numero in numeros_vistos:
            numeros_duplicados.add(numero)
        else:
            numeros_vistos.add(numero)
    
    return numeros_duplicados

# Ejemplo de uso:
conjunto_numeros = {1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1}
numeros_duplicados_resultado = numeros_duplicados(conjunto_numeros)
print("Números duplicados en el conjunto:", numeros_duplicados_resultado)
