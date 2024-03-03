"""Crea una lista con al menos 6 nodos, invierte el orden de la 
lista (el último elemento se convierte en el 
primero y viceversa) e imprime la lista hacia adelante y hacia atrás."""

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato en el nodo
        self.siguiente = None  # Referencia al siguiente nodo, inicialmente establecido como None
        self.anterior = None  # Referencia al nodo anterior, inicialmente establecido como None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicialmente, la cabeza de la lista está vacía
        self.cola = None  # Inicialmente, la cola de la lista está vacía

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if self.cabeza is None:  # Si la lista está vacía, el nuevo nodo será tanto la cabeza como la cola
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:  # Si la lista no está vacía, agregamos el nuevo nodo al final y actualizamos la cola
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def invertir_lista(self):
        actual = self.cabeza
        while actual:
            temp = actual.siguiente  # Almacenamos el siguiente nodo en una variable temporal
            actual.siguiente = actual.anterior  # Invertimos las referencias al nodo siguiente y anterior
            actual.anterior = temp
            actual = temp  # Movemos al siguiente nodo
        temp = self.cabeza  # Intercambiamos la cabeza y la cola de la lista
        self.cabeza = self.cola
        self.cola = temp

    def mostrar_adelante(self):
        nodos = []  # Inicializa una lista para almacenar los datos de los nodos
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual:  # Itera sobre la lista hasta que llegue al final
            nodos.append(actual.dato)  # Agrega el dato del nodo actual a la lista
            actual = actual.siguiente  # Avanza al siguiente nodo
        return nodos  # Retorna la lista de datos de los nodos en orden

    def mostrar_atras(self):
        nodos = []  # Inicializa una lista para almacenar los datos de los nodos
        actual = self.cola  # Comienza desde la cola de la lista
        while actual:  # Itera sobre la lista hasta que llegue al inicio
            nodos.append(actual.dato)  # Agrega el dato del nodo actual a la lista
            actual = actual.anterior  # Retrocede al nodo anterior
        return nodos  # Retorna la lista de datos de los nodos en orden inverso

# Crear una lista enlazada con al menos 6 nodos
lista = ListaEnlazada()
for dato in range(1, 7):  # Inserta números del 1 al 6
    lista.insertar_al_final(dato)

# Invertir el orden de la lista
lista.invertir_lista()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:", lista.mostrar_adelante())
print("Lista hacia atrás:", lista.mostrar_atras())
