"""Escriba una función que reciba un conjunto de palabras y
devuelva un conjunto con las palabras que 
tienen una longitud determinada y están ordenadas de menor a mayor.
"""
def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    return sorted(palabras_seleccionadas)

# Ejemplo de uso:
conjunto_palabras = {"gato", "perro", "elefante", "girafa", "león", "tigre", "mono"}
longitud = 5
palabras_seleccionadas_ordenadas = palabras_con_longitud_ordenadas(conjunto_palabras, longitud)
print(f"Palabras del conjunto con longitud {longitud}, ordenadas de menor a mayor:", palabras_seleccionadas_ordenadas)
