"""Implementa una función que invierta el orden de una lista enlazada simple"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato en el nodo
        self.siguiente = None  # El siguiente nodo en la lista, inicialmente establecido como None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicialmente, la cabeza de la lista está vacía

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        nuevo_nodo.siguiente = self.cabeza  # El siguiente del nuevo nodo apunta a la cabeza actual
        self.cabeza = nuevo_nodo  # El nuevo nodo se convierte en la nueva cabeza de la lista

    def mostrar(self):
        nodos = []  # Inicializa una lista para almacenar los datos de los nodos
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual:  # Itera sobre la lista hasta que llegue al final
            nodos.append(actual.dato)  # Agrega el dato del nodo actual a la lista
            actual = actual.siguiente  # Avanza al siguiente nodo
        return nodos  # Retorna la lista de datos de los nodos

    def invertir(self):
        previo = None  # Inicializa un nodo previo
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual:  # Itera sobre la lista
            siguiente_temporal = actual.siguiente  # Almacena el siguiente nodo temporalmente
            actual.siguiente = previo  # Invierte la referencia del nodo actual para que apunte al nodo previo
            previo = actual  # Avanza al siguiente nodo
            actual = siguiente_temporal  # Avanza al siguiente nodo
        self.cabeza = previo  # Actualiza la cabeza de la lista a la nueva cabeza invertida

# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar elementos en la lista
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(1)

# Mostrar la lista original
print("Lista original:", lista.mostrar())

# Invertir la lista
lista.invertir()

# Mostrar la lista invertida
print("Lista invertida:", lista.mostrar())
