""" Escribe una función recursiva que imprima 
la pirámide de números invertidos del 1 al n."""

def imprimir_piramide_invertida(n):

    # Caso base: si n es igual a 0, no hay nada que imprimir
    if n == 0:
        return
    # Imprimir la fila actual de números invertidos del 1 a n
    print(*range(n, 0, -1))
    # Llamar recursivamente a la función con n-1
    imprimir_piramide_invertida(n-1)

# Pedir al usuario que ingrese el número para la pirámide invertida
n = int(input("Ingrese un número entero positivo para la pirámide invertida: "))
# Llamar a la función para imprimir la pirámide invertida
imprimir_piramide_invertida(n)
