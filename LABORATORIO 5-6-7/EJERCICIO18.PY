""" Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que 
contienen una letra determinada y están ordenadas de mayor a menor"""

def palabras_con_letra_ordenadas(conjunto_palabras, letra):

    # Creamos un conjunto con las palabras del conjunto que contienen la letra especificada
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if letra in palabra}
    # Ordenamos las palabras seleccionadas de mayor a menor y las devolvemos
    return sorted(palabras_seleccionadas, reverse=True)

# Ejemplo de uso:
conjunto_palabras = {"gato", "perro", "elefante", "girafa", "león", "tigre", "mono"}
letra = "o"
# Llamamos a la función y almacenamos el resultado en una variable
palabras_seleccionadas_ordenadas = palabras_con_letra_ordenadas(conjunto_palabras, letra)
# Imprimimos el resultado
print(f"Palabras del conjunto que contienen la letra '{letra}', ordenadas de mayor a menor:", palabras_seleccionadas_ordenadas)
