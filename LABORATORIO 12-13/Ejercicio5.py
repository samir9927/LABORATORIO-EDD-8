"""Implementar una función que cuente la cantidad de nodos en el árbol"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos(arbol):
    if arbol is None:
        return 0
    
    # Contamos el nodo actual y luego recursivamente contamos los nodos en los subárboles izquierdo y derecho
    return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)

# Ejemplo de uso
# Construimos un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Contamos los nodos en el árbol
cantidad_nodos = contar_nodos(raiz)
print("Cantidad de nodos en el árbol:", cantidad_nodos)
