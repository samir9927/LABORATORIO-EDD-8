"""Escribe una función recursiva que imprima la suma 
de los números del 1 al n."""

def suma_n(n):
    # Caso base: si n es 1, imprimirlo y devolverlo como resultado
    if n == 1:
        print(n)
        return n
    # Llamar recursivamente a la función con n-1 y sumarlo a n
    else:
        suma = n + suma_n(n - 1)
        print(n)  # Imprimir el número actual
        return suma

# Llamar a la función para imprimir la suma de los números del 1 al n
n = int(input("Ingrese un número entero positivo: "))
resultado = suma_n(n)
print("La suma de los números del 1 al {} es: {}".format(n, resultado))
