"""Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son 
palíndromos, tienen una longitud determinada y están ordenadas de 
menor a mayor."""

def es_palindromo(palabra):

    # Convertimos la palabra a minúsculas y eliminamos los espacios en blanco
    palabra = palabra.lower().replace(" ", "")
    # Verificamos si la palabra es igual a su inversa
    return palabra == palabra[::-1]

def palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud):

    # Creamos un conjunto con las palabras palíndromas y con la longitud especificada
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud}
    # Ordenamos las palabras seleccionadas de menor a mayor y las devolvemos
    return sorted(palabras_seleccionadas)

# Ejemplo de uso:
conjunto_palabras = {"radar", "amor", "oso", "reconocer", "casa", "saca", "anita", "civic"}
longitud = 5
palabras_palindromas_longitud_ordenadas_resultado = palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud)
print(f"Palabras palíndromas de longitud {longitud} ordenadas de menor a mayor:", palabras_palindromas_longitud_ordenadas_resultado)
