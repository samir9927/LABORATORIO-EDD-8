""" Asegurar que una lista no esté vacía."""

def verificar_lista(lista):
    # Verificar si la longitud de la lista es mayor que cero
    if len(lista) > 0:
        print("La lista no está vacía.")  # Imprimir este mensaje si la lista no está vacía
    else:
        print("La lista está vacía.")  # Imprimir este mensaje si la lista está vacía

# Ejemplo de uso:
mi_lista = [1, 2, 3]

# Llamar a la función para verificar si la lista no está vacía
verificar_lista(mi_lista)
