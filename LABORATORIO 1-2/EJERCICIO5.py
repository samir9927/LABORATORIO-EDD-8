"""Verifica si un número ingresado por el usuario es primo o no."""

def es_primo(numero):
    # Verificar si el número es menor o igual a 1 (no es primo)
    if numero <= 1:
        return False
    # Verificar si el número es divisible por algún otro número hasta la raíz cuadrada de este
    for i in range(2, numero):
        if numero % i == 0:
            return False
    # Si no es divisible por ningún otro número, es primo
    return True

# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

# Verificar si el número es primo usando la función
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")