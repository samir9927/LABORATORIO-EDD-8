""" Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
anagramas.
"""

def son_anagramas(palabra1, palabra2):

    # Ordenamos las letras de ambas palabras y comparamos si son iguales
    return sorted(palabra1.lower().replace(" ", "")) == sorted(palabra2.lower().replace(" ", ""))

def anagramas_en_conjunto(conjunto_palabras):

    anagramas = set()  # Creamos un conjunto vacío para almacenar los anagramas encontrados
    lista_palabras = list(conjunto_palabras)  # Convertimos el conjunto a una lista para poder acceder a las palabras por índice
    # Iteramos sobre cada par de palabras en el conjunto
    for i in range(len(lista_palabras)):
        for j in range(i + 1, len(lista_palabras)):
            palabra1 = lista_palabras[i]
            palabra2 = lista_palabras[j]
            # Si las palabras son anagramas, las agregamos al conjunto de anagramas
            if son_anagramas(palabra1, palabra2):
                anagramas.add(palabra1)
                anagramas.add(palabra2)
    return anagramas

# Ejemplo de uso:
conjunto_palabras = {"roma", "amor", "perro", "poder", "casa", "saca"}
# Llamamos a la función y almacenamos el resultado en una variable
anagramas = anagramas_en_conjunto(conjunto_palabras)
# Imprimimos el resultado
print("Palabras que son anagramas entre sí:", anagramas)


