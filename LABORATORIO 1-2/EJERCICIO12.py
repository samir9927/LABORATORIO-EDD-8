"""Verifica si una palabra ingresada por el usuario es un palíndromo."""

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    # Eliminar espacios en blanco y signos de puntuación
    palabra = ''.join(caracter for caracter in palabra if caracter.isalnum())
    # Verificar si la palabra es igual a su reverso
    return palabra == palabra[::-1]

# Pedir al usuario que ingrese una palabra
palabra_usuario = input("Ingrese una palabra: ")

# Verificar si la palabra es un palíndromo
if es_palindromo(palabra_usuario):
    print("¡La palabra ingresada es un palíndromo!")
else:
    print("La palabra ingresada NO es un palíndromo.")
