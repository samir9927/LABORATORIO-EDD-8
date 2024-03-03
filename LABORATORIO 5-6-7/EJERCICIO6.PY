"""Escriba una función que reciba dos conjuntos de números 
y devuelva un conjunto con los números que 
están en el segundo conjunto pero no en el primero."""

def diferencia_entre_conjuntos(conjunto1, conjunto2):

    diferencia = conjunto2.difference(conjunto1)
    return diferencia

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
diferencia = diferencia_entre_conjuntos(conjunto1, conjunto2)
print("Números en el segundo conjunto pero no en el primero:", diferencia)
