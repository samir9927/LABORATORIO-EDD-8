"""Implementa una función que concatene dos listas enlazadas simples."""

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

def concatenar_listas(lista1, lista2):
    if lista1.cabeza is None:  # Verifica si la primera lista está vacía
        return lista2  # Retorna la segunda lista si la primera está vacía
    if lista2.cabeza is None:  # Verifica si la segunda lista está vacía
        return lista1  # Retorna la primera lista si la segunda está vacía

    actual = lista1.cabeza  # Comienza desde la cabeza de la primera lista
    while actual.siguiente:  # Itera hasta llegar al último nodo de la primera lista
        actual = actual.siguiente  # Avanza al siguiente nodo
    actual.siguiente = lista2.cabeza  # Enlaza el último nodo de la primera lista al primer nodo de la segunda lista

    return lista1  # Retorna la primera lista, que ahora contiene los elementos de ambas listas concatenados

# Crear la primera lista enlazada
lista1 = ListaEnlazada()
lista1.insertar_al_principio(3)
lista1.insertar_al_principio(2)
lista1.insertar_al_principio(1)

# Crear la segunda lista enlazada
lista2 = ListaEnlazada()
lista2.insertar_al_principio(6)
lista2.insertar_al_principio(5)
lista2.insertar_al_principio(4)

# Concatenar las listas
concatenada = concatenar_listas(lista1, lista2)

# Mostrar la lista concatenada
print("Lista concatenada:", concatenada.mostrar())
