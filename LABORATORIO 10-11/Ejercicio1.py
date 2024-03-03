"""Crea una lista con al menos 4 nodos, duplica cada nodo de 
la lista e imprime la lista original y la lista 
duplicada hacia adelante y hacia atrás."""

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato en el nodo
        self.anterior = None  # Referencia al nodo anterior, inicialmente establecido como None
        self.siguiente = None  # Referencia al siguiente nodo, inicialmente establecido como None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None  # Inicialmente, la cabeza de la lista está vacía
        self.cola = None  # Inicialmente, la cola de la lista está vacía

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)  # Crea un nuevo nodo con el dato proporcionado
        if self.cabeza is None:  # Si la lista está vacía, el nuevo nodo será tanto la cabeza como la cola
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:  # Si la lista no está vacía, agregamos el nuevo nodo al final y actualizamos la cola
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def duplicar_nodos(self):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual:  # Itera sobre la lista
            duplicado = NodoDoble(actual.dato)  # Crea un nuevo nodo duplicado con el mismo dato
            duplicado.siguiente = actual.siguiente  # Establece el siguiente del duplicado como el siguiente del nodo actual
            duplicado.anterior = actual  # Establece el anterior del duplicado como el nodo actual
            actual.siguiente = duplicado  # Establece el siguiente del nodo actual como el duplicado
            if duplicado.siguiente:  # Si hay un siguiente nodo después del duplicado, actualiza su referencia al anterior como el duplicado
                duplicado.siguiente.anterior = duplicado
            actual = duplicado.siguiente  # Avanza al siguiente nodo (que ahora es el duplicado del nodo original)

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
        while actual:  # Itera sobre la lista hasta que llegue al final
            nodos.append(actual.dato)  # Agrega el dato del nodo actual a la lista
            actual = actual.anterior  # Retrocede al nodo anterior
        return nodos  # Retorna la lista de datos de los nodos en orden inverso

# Crear una lista enlazada doble
lista_doble = ListaEnlazadaDoble()

# Insertar nodos en la lista
lista_doble.insertar_al_final(1)
lista_doble.insertar_al_final(2)
lista_doble.insertar_al_final(3)
lista_doble.insertar_al_final(4)


# Duplicar los nodos de la lista
lista_doble.duplicar_nodos()

# Mostrar la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:", lista_doble.mostrar_adelante())
print("Lista original hacia atrás:", lista_doble.mostrar_atras())

