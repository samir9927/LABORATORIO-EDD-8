"""Implementar una función que cuente la cantidad de nodos 
hoja (que no tienen hijos)."""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    
    # Si el nodo no tiene hijos, es una hoja
    if arbol.izquierda is None and arbol.derecha is None:
        return 1
    
    # Si tiene hijos, contamos las hojas en los subárboles izquierdo y derecho
    return contar_nodos_hoja(arbol.izquierda) + contar_nodos_hoja(arbol.derecha)

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

# Contamos los nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)
