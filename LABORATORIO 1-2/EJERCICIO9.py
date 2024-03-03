"""Cuenta el número de vocales en una cadena de texto."""

def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para hacer la cuenta insensible a mayúsculas y minúsculas
    cadena = cadena.lower()

    contador_vocales = 0
    vocales = "aeiou"
    
    # Iterar sobre cada caracter en la cadena
    for caracter in cadena:
        # Incrementar el contador si el caracter es una vocal
        if caracter in vocales:
            contador_vocales += 1
    
    return contador_vocales

cadena = input("Ingrese una cadena de texto: ")

resultado = contar_vocales(cadena)
print(f"El número de vocales en la cadena es: {resultado}")
