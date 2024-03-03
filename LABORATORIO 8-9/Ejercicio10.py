"""Desarrollar el código de buscar nodo en la lista enlazada simple."""

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

    def buscar_nodo(self, valor):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:  # Itera sobre la lista hasta que llegue al final
            if actual.dato == valor:  # Si el dato del nodo actual coincide con el valor buscado
                return True  # Retorna True indicando que el valor se encontró en la lista
            actual = actual.siguiente  # Avanza al siguiente nodo
        return False  # Retorna False si el valor no se encuentra en la lista

# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar elementos en la lista
lista.insertar_al_principio(3)
lista.insertar_al_principio(5)
lista.insertar_al_principio(7)

# Buscar un nodo en la lista
valor_buscado = int (input("Que nodo desea buscar en la lista: "))
if lista.buscar_nodo(valor_buscado):
    print(f"El valor {valor_buscado} se encuentra en la lista.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la lista.")
