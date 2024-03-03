"""Ordena una lista de números ingresados por el usuario de menor a mayor"""

entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario a una lista de números
numeros = [float(x) for x in entrada_usuario.split()]

# Ordenar la lista de números de menor a mayor
numeros.sort()

# Mostrar el resultado
print("Lista de números ordenados de menor a mayor:")
print(numeros)
