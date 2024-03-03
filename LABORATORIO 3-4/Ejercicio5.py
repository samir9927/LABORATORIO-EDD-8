""" Escribe una función recursiva que 
imprima la tabla de multiplicar del n."""

def imprimir_tabla_multiplicar(n, multiplicador=1):

    # Caso base: si el multiplicador es mayor que 10, terminar la recursión
    if multiplicador > 12:
        return
    # Imprimir la multiplicación de n por el multiplicador actual
    print(f"{n} x {multiplicador} = {n * multiplicador}")
    # Llamar recursivamente a la función con el mismo número n y el siguiente multiplicador
    imprimir_tabla_multiplicar(n, multiplicador + 1)

# Pedir al usuario que ingrese el número para imprimir su tabla de multiplicar
n = int(input("Ingrese un número para imprimir su tabla de multiplicar: "))
# Llamar a la función para imprimir la tabla de multiplicar
imprimir_tabla_multiplicar(n)
