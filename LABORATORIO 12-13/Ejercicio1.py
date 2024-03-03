"""Implementa una función que determine si una palabra 
es palíndroma o no. Utiliza una cola para 
comparar los caracteres de la palabra en orden original 
y reverso.
"""

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        """
        return len(self.items) == 0

    def encolar(self, elemento):
        """
        Agrega un elemento al final de la cola.
        """
        self.items.append(elemento)

    def desencolar(self):
        """
        Elimina y devuelve el primer elemento de la cola.
        """
        if self.esta_vacia():
            return None
        return self.items.pop(0)


def es_palindromo(palabra):
    """
    Determina si una palabra es palíndromo o no.
    Utiliza una cola para comparar los caracteres en orden original y reverso.
    """
    cola = Cola()

    # Agregar caracteres de la palabra a la cola en orden original
    for caracter in palabra:
        cola.encolar(caracter)

    # Comparar los caracteres en orden original y reverso
    while not cola.esta_vacia():
        if cola.desencolar() != palabra[-1]:
            return False
        palabra = palabra[:-1]

    return True


# Ejemplo de uso
print(es_palindromo("radar"))   # Devuelve True
print(es_palindromo("oso"))     # Devuelve True
print(es_palindromo("python"))  # Devuelve False

