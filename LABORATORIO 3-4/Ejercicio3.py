""" Escribe una función recursiva que 
imprima la pirámide de números del 1 al n."""

def imprimir_piramide(n, i=1):
    
    # Caso base: si el índice es mayor que n, terminar la recursión
    if i > n:
        return
    # Imprimir los números de 1 a i en la fila actual
    print(*range(1, i+1))
    # Llamar recursivamente a la función con n e incrementar el índice en 1
    imprimir_piramide(n, i+1)

# Pedir al usuario que ingrese el número para la pirámide
n = int(input("Ingrese un número entero positivo para la pirámide: "))
# Llamar a la función para imprimir la pirámide
imprimir_piramide(n)
