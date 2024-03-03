"""Toma una cadena de texto y muestra su inversión"""

def invertir_cadena(cadena):
    # Invertir la cadena usando slicing
    cadena_invertida = cadena[::-1]
    return cadena_invertida

# Solicitar al usuario que ingrese una cadena de texto
cadena_original = input("Ingrese una cadena de texto: ")

# Llamar a la función para invertir la cadena
cadena_invertida = invertir_cadena(cadena_original)

# Mostrar la cadena original y la invertida
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")