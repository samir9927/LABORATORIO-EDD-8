"""Implementar una función que encuentre el nodo con el valor máximo en el árbol"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_valor_maximo(raiz):

    if raiz is None:
        return None
    
    # Recorremos hacia la derecha hasta encontrar el nodo más a la derecha
    nodo_actual = raiz
    while nodo_actual.derecha is not None:
        nodo_actual = nodo_actual.derecha
    
    # El valor máximo estará en el nodo más a la derecha
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

# Encontramos el valor máximo en el árbol
valor_maximo = encontrar_valor_maximo(raiz)
print("Valor máximo en el árbol:", valor_maximo)
