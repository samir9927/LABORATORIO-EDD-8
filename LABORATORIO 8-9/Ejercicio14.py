"""Crea una función que elimine los nodos duplicados de una lista enlazada simple."""
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

    def mostrar(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.dato)
            actual = actual.siguiente
        return nodos

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        valores = set()  # Utilizamos un conjunto para almacenar valores únicos
        actual = self.cabeza
        valores.add(actual.dato)  # Agregamos el primer valor a nuestro conjunto
        while actual.siguiente:
            if actual.siguiente.dato in valores:
                actual.siguiente = actual.siguiente.siguiente  # Eliminamos el nodo duplicado
            else:
                valores.add(actual.siguiente.dato)  # Agregamos el valor a nuestro conjunto
                actual = actual.siguiente

# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar elementos en la lista
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)

# Mostrar la lista original
print("Lista original:", lista.mostrar())

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Mostrar la lista después de eliminar los duplicados
print("Lista después de eliminar duplicados:", lista.mostrar())
