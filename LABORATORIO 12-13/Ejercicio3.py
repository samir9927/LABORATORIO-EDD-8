"""Desarrolla un programa que encuentre el camino más
 corto a través de un laberinto. Utiliza una cola 
para realizar un recorrido en anchura (BFS) desde 
el punto de inicio hasta el punto de destino"""

from collections import deque

def encontrar_camino_laberinto(laberinto, inicio, destino):
    """
    Encuentra el camino más corto a través de un laberinto utilizando BFS.
    """
    # Definir movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Inicializar cola para BFS
    cola = deque([inicio])
    
    # Inicializar conjunto para nodos visitados
    visitados = set([inicio])
    
    # Inicializar diccionario para registrar padres de cada nodo
    padres = {inicio: None}
    
    # Recorrido BFS
    while cola:
        actual = cola.popleft()
        
        if actual == destino:
            break
        
        fila, columna = actual
        
        for movimiento in movimientos:
            nueva_fila = fila + movimiento[0]
            nueva_columna = columna + movimiento[1]
            nuevo_nodo = (nueva_fila, nueva_columna)
            
            # Verificar si el nuevo nodo está dentro del laberinto y no ha sido visitado
            if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]) and laberinto[nueva_fila][nueva_columna] != '#' and nuevo_nodo not in visitados:
                cola.append(nuevo_nodo)
                visitados.add(nuevo_nodo)
                padres[nuevo_nodo] = actual
                
    # Reconstruir el camino más corto
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()
    
    return camino

# Ejemplo de uso
laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

inicio = (1, 1)
destino = (7, 7)

camino_mas_corto = encontrar_camino_laberinto(laberinto, inicio, destino)
if camino_mas_corto:
    print("Camino más corto encontrado:")
    for nodo in camino_mas_corto:
        print(nodo)
else:
    print("No hay camino válido para llegar al destino.")
