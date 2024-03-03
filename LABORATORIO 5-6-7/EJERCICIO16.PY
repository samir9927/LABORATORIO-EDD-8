""" Escriba una función que reciba un conjunto de palabras 
y devuelva un conjunto con las palabras que son 
palíndromos y están ordenadas de menor a mayor."""

def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas y eliminamos los espacios en blanco
    palabra = palabra.lower().replace(" ", "")
    # Verificamos si la palabra es igual a su inversa
    return palabra == palabra[::-1]

def palabras_palindromas_ordenadas(conjunto_palabras):

    # Creamos un conjunto con las palabras palíndromas presentes en el conjunto dado
    palabras_palindromas = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    # Ordenamos las palabras palíndromas y las devolvemos
    return sorted(palabras_palindromas)

# Ejemplo de uso:
conjunto_palabras = {"radar", "amor", "oso", "perro", "reconocer", "casa", "saca"}
palabras_palindromas_ordenadas_resultado = palabras_palindromas_ordenadas(conjunto_palabras)
print("Palabras palíndromas ordenadas de menor a mayor:", palabras_palindromas_ordenadas_resultado)
