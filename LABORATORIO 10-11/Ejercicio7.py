"""Implementar un programa que convierta un número decimal
 a su representación en sistema binario 
utilizando una pila."""

class Pila:
    def __init__(self):
        self.items = []  # Inicializa una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []  # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        return self.items.pop()  # Elimina y devuelve el elemento superior de la pila


def decimal_a_binario(numero_decimal):
    pila = Pila()  # Crea una instancia de la clase Pila para almacenar los bits de la representación binaria

    # Si el número es 0, la representación binaria también es 0
    if numero_decimal == 0:
        return '0'

    # Calcula el binario usando el algoritmo de división sucesiva
    while numero_decimal > 0:
        residuo = numero_decimal % 2  # Calcula el residuo de la división entre el número decimal y 2
        pila.apilar(residuo)  # Apila el residuo en la pila
        numero_decimal //= 2  # Actualiza el número decimal dividiéndolo por 2

    # Construye la cadena binaria desapilando los elementos de la pila
    binario = ''
    while not pila.esta_vacia():
        binario += str(pila.desapilar())  # Desapila cada bit de la representación binaria y lo agrega a la cadena

    return binario  # Retorna la representación binaria como una cadena


# Solicita al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convierte el número decimal a binario llamando a la función decimal_a_binario
binario = decimal_a_binario(numero_decimal)

# Imprime el resultado
print(f"El número {numero_decimal} en binario es: {binario}")
