"""Implementar una función que encuentre el nodo con el valor mínimo en el árbol"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_valor_minimo(raiz):

    if raiz is None:
        return None
    
    # Recorremos hacia la izquierda hasta encontrar el nodo más a la izquierda
    nodo_actual = raiz
    while nodo_actual.izquierda is not None:
        nodo_actual = nodo_actual.izquierda
    
    # El valor mínimo estará en el nodo más a la izquierda
    return nodo_actual.valor

# Ejemplo de uso
# Construimos un árbol binario de ejemplo
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)
raiz.derecha.izquierda = Nodo(12)
raiz.derecha.derecha = Nodo(20)

# Encontramos el valor mínimo en el árbol
valor_minimo = encontrar_valor_minimo(raiz)
print("Valor mínimo en el árbol:", valor_minimo)
