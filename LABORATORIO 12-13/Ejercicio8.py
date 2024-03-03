"""Implementar una función que calcule la altura 
del árbol (la longitud del camino más largo desde la raíz 
hasta una hoja)"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def calcular_altura(arbol):
    if arbol is None:
        return 0
    
    # Calculamos la altura de los subárboles izquierdo y derecho
    altura_izquierda = calcular_altura(arbol.izquierda)
    altura_derecha = calcular_altura(arbol.derecha)
    
    # La altura del árbol es el máximo entre las alturas de los subárboles izquierdo y derecho, más 1
    return 1 + max(altura_izquierda, altura_derecha)

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

# Calculamos la altura del árbol
altura_arbol = calcular_altura(raiz)
print("Altura del árbol:", altura_arbol)
