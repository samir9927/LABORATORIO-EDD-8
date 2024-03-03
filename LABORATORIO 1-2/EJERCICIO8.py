"""Crea una lista de los cuadrados de los primeros 10 números naturales."""

lista=[] #Creamos una lista vacia
for x in range(1, 11): #Variable "x" con valores desde el 1 hsata un valor antes del 11
    num_cuadrado=[ x**2 ] #Cada valor de x elevado al cuadrado estara en la lista "num:cuadrado"
    lista = lista + num_cuadrado #Se guardan en la Lista todos los valores cuadrados.
print(f"Lista de cuadrados de los primeros 10 números naturales: {lista}")
