"""Escribe una función recursiva que imprima 
los números pares del 1 al 100."""

def imprimir_pares(numero):
    # Verificar si el número actual es menor o igual a 100
    if numero <= 100:
        # Verificar si el número actual es par
        if numero % 2 == 0:
            # Si es par, imprimirlo
            print(numero)
        # Llamar recursivamente a la función con el siguiente número par
        imprimir_pares(numero + 2)

# Llamar a la función inicialmente con el primer número par
imprimir_pares(2)
