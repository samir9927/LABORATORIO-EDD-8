"""Utilizar una pila para invertir el orden de los caracteres de una cadena."""

class Pila:
    def __init__(self):
        self.items = []  # Inicializa una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []  # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        return self.items.pop()  # Elimina y devuelve el elemento superior de la pila


def invertir_cadena(cadena):
    pila = Pila()  # Crea una instancia de la clase Pila para almacenar los caracteres de la cadena
    # Apila cada caracter de la cadena en la pila
    for caracter in cadena:
        pila.apilar(caracter)
    # Construye una nueva cadena desapilando caracteres de la pila
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida  # Retorna la cadena invertida


# Ejemplo de uso
cadena = "Hola Mundo!"  # Define una cadena
cadena_invertida = invertir_cadena(cadena)  # Invierte la cadena utilizando la función invertir_cadena
print("Cadena original:", cadena)  # Imprime la cadena original
print("Cadena invertida:", cadena_invertida)  # Imprime la cadena invertida
