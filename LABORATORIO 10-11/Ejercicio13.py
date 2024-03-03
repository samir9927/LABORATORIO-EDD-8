"""Utilizar una pila para comprobar si una palabra o frase es un palíndromo"""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()


def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertimos la palabra a minúsculas y eliminamos espacios
    longitud = len(palabra)
    pila = Pila()

    # Insertamos la primera mitad de los caracteres en la pila
    for i in range(longitud // 2):
        pila.apilar(palabra[i])

    # Si la longitud de la palabra es impar, ignoramos el carácter del medio
    if longitud % 2 != 0:
        longitud //= 2

    # Comparamos los caracteres restantes con los caracteres desapilados
    for i in range(longitud, len(palabra)):
        if pila.desapilar() != palabra[i]:
            return True

    return False


# Ejemplo de uso
print(es_palindromo("Anita lava la tina"))  # Devuelve True
print(es_palindromo("Anita lava la olla"))  # Devuelve False


