"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
palíndromos."""

def es_palindromo(palabra):

    # Convertimos la palabra a minúsculas y eliminamos los espacios en blanco
    palabra = palabra.lower().replace(" ", "")
    # Verificamos si la palabra es igual a su inversa
    return palabra == palabra[::-1]

def palindromos_en_conjunto(conjunto_palabras):

    palindromos = set()  # Creamos un conjunto vacío para almacenar los palíndromos encontrados
    # Iteramos sobre cada palabra en el conjunto
    for palabra in conjunto_palabras:
        # Si la palabra es un palíndromo, la agregamos al conjunto de palíndromos
        if es_palindromo(palabra):
            palindromos.add(palabra)
    return palindromos

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "amor", "perro", "reconocer", "casa", "saca"}
palindromos = palindromos_en_conjunto(conjunto_palabras)
print("Palabras que son palíndromos:", palindromos)
