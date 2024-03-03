"""Escriba una función que reciba un conjunto de 
palabras y devuelva un conjunto con las palabras que 
contienen una letra determinada."""

def palabras_con_letra(conjunto_palabras, letra):

    palabras_seleccionadas = set()  # Creamos un conjunto vacío para almacenar las palabras seleccionadas
    # Iteramos sobre cada palabra en el conjunto
    for palabra in conjunto_palabras:
        # Verificamos si la letra está presente en la palabra
        if letra in palabra:
            # Si la letra está presente, agregamos la palabra al conjunto de palabras seleccionadas
            palabras_seleccionadas.add(palabra)
    return palabras_seleccionadas

# Ejemplo de uso:
conjunto_palabras = {"gato", "perro", "elefante", "girafa", "león", "tigre", "mono"}
letra = "o"
palabras_seleccionadas = palabras_con_letra(conjunto_palabras, letra)
print("Palabras del conjunto que contienen la letra", letra, ":", palabras_seleccionadas)
