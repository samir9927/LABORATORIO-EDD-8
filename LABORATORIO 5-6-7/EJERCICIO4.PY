""" Escriba una función que reciba dos conjuntos de 
números y devuelva un conjunto con los números que 
están en ambos conjuntos."""

def numeros_comunes(conjunto1, conjunto2):

    # Utilizamos el método intersection() para encontrar la intersección de los conjuntos
    numeros_comunes = conjunto1.intersection(conjunto2)
    return numeros_comunes

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
# Llamamos a la función y almacenamos el resultado en una variable
numeros_en_comun = numeros_comunes(conjunto1, conjunto2)
# Imprimimos el resultado
print("Números que están presentes en ambos conjuntos:", numeros_en_comun)
