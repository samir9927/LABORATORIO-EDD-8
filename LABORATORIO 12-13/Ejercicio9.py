""" Implementar una función que calcule la 
profundidad de un nodo (la longitud del camino desde la raíz 
hasta el nodo)"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def calcular_profundidad(raiz, valor_nodo, profundidad_actual=0):

    if raiz is None:
        return -1
    
    # Si encontramos el nodo objetivo, retornamos la profundidad actual
    if raiz.valor == valor_nodo:
        return profundidad_actual
    
    # Buscamos el nodo en los subárboles izquierdo y derecho
    profundidad_izquierda = calcular_profundidad(raiz.izquierda, valor_nodo, profundidad_actual + 1)
    profundidad_derecha = calcular_profundidad(raiz.derecha, valor_nodo, profundidad_actual + 1)
    
    # Si el nodo no se encuentra en ninguno de los subárboles, retornamos -1
    if profundidad_izquierda == -1 and profundidad_derecha == -1:
        return -1
    
    # Si el nodo se encuentra en uno de los subárboles, retornamos su profundidad
    return max(profundidad_izquierda, profundidad_derecha)

# Ejemplo de uso
# Construimos un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Calculamos la profundidad de un nodo específico
valor_nodo = 5
profundidad_nodo = calcular_profundidad(raiz, valor_nodo)
if profundidad_nodo != -1:
    print(f"La profundidad del nodo con valor {valor_nodo} es {profundidad_nodo}")
else:
    print(f"No se encontró un nodo con valor {valor_nodo} en el árbol")
