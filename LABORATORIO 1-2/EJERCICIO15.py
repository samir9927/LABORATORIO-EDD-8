""" Toma un número entero y calcula la suma de sus dígitos."""

def suma_digitos(numero):
    suma = 0
    # Iterar sobre cada dígito del número
    while numero > 0:
        # Obtener el dígito menos significativo
        digito = numero % 10
        # Sumar el dígito a la suma total
        suma += digito
        # Eliminar el dígito menos significativo del número
        numero //= 10
    return suma

# Pedir al usuario que ingrese un número entero
numero_entero = int(input("Ingrese un número entero: "))

# Calcular la suma de sus dígitos
resultado = suma_digitos(numero_entero)
print("La suma de los dígitos del número", numero_entero, "es:", resultado)