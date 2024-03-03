""" Crea una lista con al menos 5 nodos, inserta un nuevo 
nodo con el dato 15 en la posición 3 e imprime la 
lista hacia adelante y hacia atrás."""

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

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if posicion == 0:  # Si la posición es 0, el nuevo nodo se convierte en la nueva cabeza de la lista
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:  # Si la lista no está vacía, actualiza la referencia al nodo anterior de la cabeza
                self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo  # El nuevo nodo se convierte en la nueva cabeza de la lista
        else:  # Si la posición no es 0, busca la posición e inserta el nuevo nodo en esa posición
            actual = self.cabeza
            for _ in range(posicion - 1):
                if actual is None:  # Si la posición está fuera de rango, imprime un mensaje y retorna
                    print("Posición fuera de rango")
                    return
                actual = actual.siguiente
            if actual is None:  # Si la posición está fuera de rango, imprime un mensaje y retorna
                print("Posición fuera de rango")
                return
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            if actual.siguiente:  # Si hay un nodo siguiente, actualiza la referencia al nodo anterior del siguiente nodo
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo  # Inserta el nuevo nodo después del nodo actual

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

# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar nodos en la lista
for dato in range(1, 6):  # Inserta números del 1 al 5
    lista.insertar_al_final(dato)

# Insertar un nuevo nodo con el dato 15 en la posición 3 (contando desde 0)
lista.insertar_en_posicion(15, 2)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:", lista.mostrar_adelante())
print("Lista hacia atrás:", lista.mostrar_atras())
