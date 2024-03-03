"""Validar la igualdad de dos objetos"""

# Definir dos listas con los mismos valores
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

# Usar el operador == para verificar si las listas tienen los mismos valores
if lista1 == lista2:
    print("Las listas son iguales (según el operador ==)")

# Usar la función is para verificar si las listas son el mismo objeto en la memoria
if lista1 is lista2:
    print("Las listas son el mismo objeto (según la función is)")
else:
    print("Las listas no son el mismo objeto (según la función is)")
