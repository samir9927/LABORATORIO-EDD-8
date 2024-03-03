"""Ordenar los elementos de una pila de manera 
ascendente utilizando estructuras adicionales."""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def ordenar_pila_ascendente(pila):
    pila_temporal = Pila()  # Creamos una pila temporal para almacenar los elementos ordenados
    lista_temporal = []  # Creamos una lista temporal para almacenar los elementos de la pila

    # Desapilamos todos los elementos de la pila y los almacenamos en la lista temporal
    while not pila.esta_vacia():
        lista_temporal.append(pila.desapilar())

    # Ordenamos la lista temporal de manera ascendente
    lista_temporal.sort()

    # Apilamos los elementos ordenados de la lista temporal en la pila temporal
    for elemento in lista_temporal:
        pila_temporal.apilar(elemento)

    # Retornamos la pila temporal con los elementos ordenados de manera ascendente
    return pila_temporal


# Ejemplo de uso
pila = Pila()
pila.apilar(4)
pila.apilar(2)
pila.apilar(6)
pila.apilar(1)
pila.apilar(5)

pila_ordenada = ordenar_pila_ascendente(pila)

print("Pila original:")
while not pila.esta_vacia():
    print(pila.desapilar())

print("\nPila ordenada de manera ascendente:")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar())
