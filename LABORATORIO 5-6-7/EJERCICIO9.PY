"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
tienen una longitud determinada"""

def palabras_con_longitud(conjunto_palabras, longitud):

    palabras_seleccionadas = set()  # Creamos un conjunto vacío para almacenar las palabras seleccionadas
    # Iteramos sobre cada palabra en el conjunto
    for palabra in conjunto_palabras:
        # Verificamos si la longitud de la palabra es igual a la longitud especificada
        if len(palabra) == longitud:
            # Si la longitud coincide, agregamos la palabra al conjunto de palabras seleccionadas
            palabras_seleccionadas.add(palabra)
    return palabras_seleccionadas

# Ejemplo de uso:
conjunto_palabras = {"gato", "perro", "elefante", "girafa", "león", "tigre", "mono"}
longitud = 5
palabras_seleccionadas = palabras_con_longitud(conjunto_palabras, longitud)
print("Palabras del conjunto con longitud", longitud, ":", palabras_seleccionadas)

