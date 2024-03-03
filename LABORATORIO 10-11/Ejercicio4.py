""" Crea una lista con nodos que contengan datos duplicados, 
elimina todos los nodos duplicados, dejando 
solo una instancia de cada dato e imprime la lista hacia 
adelante y hacia atrás."""

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

    def eliminar_duplicados(self):
        valores_vistos = set()  # Conjunto para almacenar los valores vistos
        actual = self.cabeza
        while actual:
            if actual.dato in valores_vistos:  # Si el dato ya ha sido visto, elimina el nodo
                siguiente_nodo = actual.siguiente
                self.eliminar_nodo(actual)
                actual = siguiente_nodo
            else:
                valores_vistos.add(actual.dato)
                actual = actual.siguiente

    def eliminar_nodo(self, nodo):
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.cola = nodo.anterior

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

# Crear una lista enlazada con nodos que contienen datos duplicados
lista = ListaEnlazada()
datos = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9]  # Lista con datos duplicados
for dato in datos:
    lista.insertar_al_final(dato)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:", lista.mostrar_adelante())
print("Lista hacia atrás:", lista.mostrar_atras())
