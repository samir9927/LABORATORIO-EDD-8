"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
son divisibles por un número determinado.
"""

def numeros_divisibles_por(conjunto_numeros, divisor):
    numeros_seleccionados = set()  # Creamos un conjunto vacío para almacenar los números seleccionados
    for numero in conjunto_numeros:
        # Verificamos si el número actual es divisible por el divisor especificado
        if numero % divisor == 0:
            # Si el número es divisible por el divisor, lo agregamos al conjunto de números seleccionados
            numeros_seleccionados.add(numero)
    return numeros_seleccionados

# Ejemplo de uso:
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3
numeros_seleccionados = numeros_divisibles_por(conjunto_numeros, divisor)
print("Números del conjunto que son divisibles por", divisor, ":", numeros_seleccionados)
