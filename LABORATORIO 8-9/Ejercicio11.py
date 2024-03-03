"""Implementa una función que sume todos los nodos de una lista enlazada simple."""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual is not None:
            suma += actual.dato
            actual = actual.siguiente
        return suma

# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar elementos en la lista
lista.insertar_al_principio(3)
lista.insertar_al_principio(5)
lista.insertar_al_principio(7)

# Calcular la suma de los nodos en la lista
suma_total = lista.sumar_nodos()
print("La suma de todos los nodos en la lista es:", suma_total)
