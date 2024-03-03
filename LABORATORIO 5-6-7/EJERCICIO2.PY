""" Escriba una función que reciba un conjunto 
de palabras y devuelva un conjunto con las palabras que 
comienzan con una letra determinada."""

def palabras_comienzan_con_letra(conjunto_palabras, letra):

    palabras_seleccionadas = set()  # Creamos un conjunto vacío para almacenar las palabras seleccionadas
    for palabra in conjunto_palabras:
        # Verificamos si la palabra actual comienza con la letra especificada
        if palabra.startswith(letra):
            # Si la palabra comienza con la letra, la agregamos al conjunto de palabras seleccionadas
            palabras_seleccionadas.add(palabra)
    return palabras_seleccionadas

# Ejemplo de uso:
conjunto_palabras = {"gato", "perro", "elefante", "girafa", "león", "tigre", "mono"}
letra = "g"
palabras_seleccionadas = palabras_comienzan_con_letra(conjunto_palabras, letra)
print("Palabras que comienzan con la letra", letra + ":", palabras_seleccionadas)
