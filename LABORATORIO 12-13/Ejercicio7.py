"""Implementar una función que cuente la cantidad de 
nodos internos (que tienen al menos un hijo)"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_internos(arbol):
    if arbol is None:
        return 0
    
    # Si el nodo tiene al menos un hijo, es un nodo interno
    if arbol.izquierda is not None or arbol.derecha is not None:
        return 1 + contar_nodos_internos(arbol.izquierda) + contar_nodos_internos(arbol.derecha)
    
    # Si no tiene hijos, es una hoja y no se cuenta como nodo interno
    return 0

# Ejemplo de uso
# Construimos un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)
raiz.derecha.derecha.izquierda = Nodo(8)

# Contamos los nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print("Cantidad de nodos internos en el árbol:", cantidad_nodos_internos)
