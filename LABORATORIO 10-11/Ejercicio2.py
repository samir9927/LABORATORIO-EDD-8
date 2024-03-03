"""Crea una lista con al menos 9 nodos, cuenta cuántos nodos 
tienen un dato par y cuántos tienen un dato 
impar e imprime la lista hacia adelante y hacia atrás."""

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

    def contar_pares_impares(self):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        pares = 0  # Inicializa un contador para nodos con datos pares
        impares = 0  # Inicializa un contador para nodos con datos impares
        while actual:  # Itera sobre la lista
            if actual.dato % 2 == 0:  # Verifica si el dato del nodo actual es par
                pares += 1  # Incrementa el contador de nodos pares
            else:  # Si el dato es impar
                impares += 1  # Incrementa el contador de nodos impares
            actual = actual.siguiente  # Avanza al siguiente nodo
        return pares, impares  # Retorna la cantidad de nodos con datos pares e impares

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

# Crear una lista enlazada doble
lista_doble = ListaEnlazadaDoble()

# Insertar nodos en la lista
for dato in range(1, 10):  # Inserta números del 1 al 9
    lista_doble.insertar_al_final(dato)

# Contar nodos con datos pares e impares
pares, impares = lista_doble.contar_pares_impares()

# Mostrar la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:", lista_doble.mostrar_adelante())
print("Lista original hacia atrás:", lista_doble.mostrar_atras())

# Imprimir la cantidad de nodos con datos pares e impares
print("Nodos con datos pares:", pares)
print("Nodos con datos impares:", impares)
