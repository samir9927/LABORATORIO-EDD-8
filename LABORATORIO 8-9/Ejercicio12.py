"""Crea una función que devuelva la longitud de una lista enlazada simple."""

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

    def longitud(self):
        longitud = 0  # Inicializa la longitud en 0
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:  # Itera sobre la lista hasta que llegue al final
            longitud += 1  # Incrementa la longitud en 1 por cada nodo encontrado
            actual = actual.siguiente  # Avanza al siguiente nodo
        return longitud  # Retorna la longitud total de la lista

# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar elementos en la lista
lista.insertar_al_principio(3)
lista.insertar_al_principio(5)
lista.insertar_al_principio(7)
lista.insertar_al_principio(9)
lista.insertar_al_principio(10)
lista.insertar_al_principio(11)

# Obtener la longitud de la lista
longitud_lista = lista.longitud()
print("La longitud de la lista enlazada es:", longitud_lista)
