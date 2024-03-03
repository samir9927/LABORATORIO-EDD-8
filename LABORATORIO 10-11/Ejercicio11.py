"""Eliminar los elementos duplicados de una pila."""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def devolver_sin_repetir(pila):
    if pila.esta_vacia():
        return []

    elementos_vistos = set()  # Conjunto para registrar elementos vistos
    elementos_sin_repetir = []  # Lista para almacenar elementos únicos

    while not pila.esta_vacia():
        elemento = pila.desapilar()

        # Si el elemento no ha sido visto antes, lo agregamos a la lista de elementos sin repetir
        if elemento not in elementos_vistos:
            elementos_sin_repetir.append(elemento)
            elementos_vistos.add(elemento)

    # Invertimos el orden de la lista para que coincida con el orden original de la pila
    elementos_sin_repetir.reverse()
    return elementos_sin_repetir


# Ejemplo de uso
pila = Pila()
pila.apilar(3)
pila.apilar(2)
pila.apilar(5)
pila.apilar(3)
pila.apilar(2)

print("Elementos de la pila sin repetir:")
print(devolver_sin_repetir(pila))
